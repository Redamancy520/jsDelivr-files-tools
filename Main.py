import logging
import os
import re

import download


def findAllFile(file_path: str):
    """
    遍历目录及其子目录下文件
    :param file_path: 目录
    :return: str数组(文件详细路径)
    """
    file_list = []
    for root, dir, filename in os.walk(file_path):
        for file in filename:
            file_list.append(os.path.join(root, file))
    return file_list


def read_file(path: str):
    """
    读取文件内容 返回内容str
    :param path: 路径
    :return:
    """
    try:
        f = open(path, encoding='utf-8', errors='ignore')  # 'gb18030'
        return f.read()
    except:
        print("bug:" + path)
        return ""


def find_url(text: str):
    """
    正则表达式匹配一个str中的url 返回str url[]
    :param text: 一堆字符串文本
    :return: urls[]
    """
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
    return re.findall(url_pattern, text)


def clean_waste(str_: str):
    """
    正则表达式获取URL时 有的会出现部分多余字符,本方法对其进行处理删除
    :param str_: url
    :return: 处理后的url
    """
    char = "')"

    if str_.endswith("')"):
        # print("find:" + str_ + "|" + char)
        str_ = str_.replace("')", '')
    return str_


def import_url(base: str, cdn: str):
    """
    导出URL
    :param base: 目录
    :param cdn: 自己的cdn仓库
    """

    if os.path.exists("list.txt"):
        os.remove("list.txt")

    files = findAllFile(base)
    for f in files:
        file_str = read_file(f)
        urls = find_url(file_str)
        if urls.count != 0:
            for url in urls:
                if url.find("jsdelivr") != -1 and url != "" and url.find(cdn) == -1 and url.find("https://img1.imgtp.com/2023/08/12/z5s15lgH.png") == -1:  # 这段可以删,这个是针对我自己的库
                    url = clean_waste(url)  # 处理URL
                    if url.endswith(".css"):  # 指定文件类型 .css 也可以不指定 建议和下方保持一致
                        with open("list.txt", "a") as j:
                            print("list add:" + url)
                            j.write(url + "\r\n")  # 将url写入到list.txt中
                    else:
                        pass
    with open("list.txt", "a") as j:
        j.write(" \r\n")  # 将url写入到list.txt中


def replace_url(cdn_self, base):
    """
    替换URL
    :param cdn_self: 自己的CDN仓库
    :param base: 需要替换的文件目录
    :return:
    """
    files = findAllFile(base)
    for f in files:
        file_str = read_file(f)
        urls = find_url(file_str)
        if urls.count != 0:
            for url in urls:
                # 判断是否为cdn的url
                if url.find("jsdelivr") != -1 and url != "" and url.find(cdn_self) == -1 and url.find("https://img1.imgtp.com/2023/08/12/z5s15lgH.png") == -1:
                    url = clean_waste(url)  # 处理URL
                    #print(url)
                    if url.endswith(".css"):  # 指定文件类型 .css 也可以不指定 建议和上方保持一致
                        print(url)
                        file_str = file_str.replace(url,
                                                    url.replace("https://cdn.jsdelivr.net/", cdn_self))  # 替换为你自己的CDN仓库
                        with open(f, "w", encoding="utf-8") as j:
                            j.write(file_str)
                            logging.getLogger("replace.log").info("replace file:" + f)
                            #print("replace file:" + f)
                            j.close()


if __name__ == '__main__':
    all_base = r"D:\Desktop\我的东西\Blog"
    all_cdn = "https://cdn.jsdelivr.net/gh/redamancy520/CDN/"
    import_url(all_base, all_cdn)
    download.main()
    replace_url(all_cdn,  # 替换为自己的CDN仓库
                all_base)  # 加r表示不转义
