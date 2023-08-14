# jsDelivr-files-tools
help download jsDelivr file and change others' cdn url to own url (快速下载多个其他人jsDelivr的文件并且修改文件中的jsDelivr链接指向自己的cdn链接)

## 使用
1. 下载Release文件并且解压
2. 打开Main.py文件,根据需求修改all_cdn,all_base变量,和`import_url` 和 `replace_url` 中的 `指定文件类型` 保存
3. 在同目录下打开cmd,输入 `python Main.py`

## 功能
1. 获取指定目录中所有的jsDelivr cdn链接
2. 下载指定目录中所有的jsDelivr cdn链接
3. 替换指定目录中所有的jsDelivr cdn链接为自己cdn仓库链接
   
## 说明
> 该程序本来是我用来修改hexo博客文件中指向其他jsDelivr仓库的cdn链接改为我的，所以有地方需要你自己修改适配
> 
> 本人高中生,python新手 有bug请见谅 发issue反馈即可
