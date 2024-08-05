## IOT Web Bypass

### 简介

IOT Web Bypass 是一个用于检测潜在未授权访问的 Python 脚本。它通过遍历指定目录中的文件，构建 URL，并检查响应内容以识别可能存在的安全漏洞。

### 功能

遍历指定目录，列出文件。
发送 HTTP 请求并检查响应状态。
过滤掉已知的无效文件扩展名。
根据自定义模式识别潜在的未授权访问页面。

### 依赖


可以通过以下命令安装依赖：

```
pip3 install -r requirements
```

### 使用方法

##### 准备工作：

修改排除扩展名的文件 dic/extensions。
修改包含检测模式的文件 dic/login。//默认为login

##### 运行脚本：

```
python3 unauth_bypass.py
```

##### 输入参数：

输入要列出的文件目录。
输入目标主机地址（例如 http://example.com）。

##### 查看结果：

脚本将输出潜在未授权访问的 URL。

##### 示例


![image](https://github.com/user-attachments/assets/55ed45ab-ad3a-4c55-9771-1f73dd4fea0e)


##### 输出示例：


![image](https://github.com/user-attachments/assets/a21c8d93-281f-43b2-9c4b-e18c332ed3b8)


##### 注意事项

请确保在合法授权的情况下使用此工具。
该脚本仅供教育和安全测试目的使用。

##### 作者

GroundCTL2MajorTom - IOTSec-Zone


