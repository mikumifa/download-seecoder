import requests
import json
import os

url = "https://p.seec.seecoder.cn/api/courseWare/getCourseWaresByCourseId?courseId=15"

r = requests.get(url)
j = json.loads(r.text)
fileUrls = list(map(lambda x: x["courseWareVO"]["fileUrl"], j["data"]))
fileNames = list(map(lambda x: x["courseWareVO"]["name"], j["data"]))


# 遍历文件URL和文件名列表并下载文件
for fileUrl, fileName in zip(fileUrls, fileNames):
    if not os.path.exists(fileName):
        response = requests.get(fileUrl)
        if response.status_code == 200:
            with open(fileName, 'wb') as file:
                file.write(response.content)
            print(f"下载文件 {fileName} 成功")
        else:
            print(f"无法下载文件 {fileName}，状态码: {response.status_code}")
    else:
        print(f"文件 {fileName} 已存在，跳过下载")
