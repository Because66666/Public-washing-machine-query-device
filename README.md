# Public-washing-machine-query-device
对于U净公共洗衣机的查询器。基于flask搭建的服务器文件。前端建议使用fusion app将部署的网址进行打包。

## 使用说明-必要修改
**请求头**：将项目`git clone`本地或者下载zip压缩包后解压。在`app.py`中修改`headers`变量，建议使用U净APP端以及reqable进行抓包处理。<br>
**二维码**：对于洗衣机的二维码处理：使用在线的二维码解码器[草料二维码](https://cli.im/deqr)解码后，填入到`app.py`中的
```
        json_data = {
            'qrCode': 'https://q.ujing.com.cn/ucqrc/index.html?cd=755501240412324394',
        }
```
中即可。<br>
**网页布局**：在`tempates\main.html`中进行修改。
