"""
任务名称
name: OAI签到
定时规则
cron: 5 0 * * *
"""
import requests
import os

url = "https://oai.itsfurry.com/api/user/signing"

def sendNotify(title,desc):
    print(title,desc)
    ## 青龙脚本通知
    QLAPI.notify(title, desc)

def reqSign():
    cookie = os.environ.get('OAI_COOKIE')
    if cookie is None:
        print("Cookie not set  use getenv method")
        cookie = os.getenv('OAI_COOKIE')

    if cookie is None:
        print("cookie not set ")
        return

    headers = {
        # "authority": "oai.itsfurry.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        # "accept-encoding": "gzip, deflate, br, zstd",
        "content-type": "application/json",
        "cookie": cookie,
        "new-api-user": "3262",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        # "origin": "https://oai.itsfurry.com",
        "Referer": "https://oai.itsfurry.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    data = {
        "id": 3262
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        print("状态码:", response.status_code)
        if response.status_code == 200:
            QLAPI.notify("签到成功", "")
        else:
            QLAPI.notify("签到失败", response.text)
        print("响应内容:", response.text)

    except requests.exceptions.RequestException as e:
        print("请求失败:", e)
        QLAPI.notify("oai签到失败", str(e))


if __name__ == '__main__':
    reqSign()
else:
    print("模块注入。")