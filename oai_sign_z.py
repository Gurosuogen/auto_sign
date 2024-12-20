"""
name: OAI_Z签到
cron: 22 0 * * *
"""
import asyncio
import httpx
import os
import json

body = """
    {"id":3262}
"""

async def fetch():
    cookie = json.loads(os.environ.get('OAI_COOKIE'))
    if cookie is None:
        print("Cookie not set  use getenv method")
        cookie = os.getenv('OAI_COOKIE')

    if cookie is None:
        print("cookie not set ")
        return

    client = httpx.AsyncClient()
    response = await client.request(
        method="POST",
        url="https://oai.furryapi.org/api/user/signing",
        headers={
            "accept":"application/json, text/plain, */*",
            "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
            "content-type":"application/json",
            "dnt":"1",
            "new-api-user":"3262",
            "origin":"https://oai.furryapi.org",
            "priority":"u=1, i",
            "referer":"https://oai.furryapi.org/pricing",
            "sec-ch-ua":"\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"\"Windows\"",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        },
        cookies=cookie,
        content=body,
    )
    # 解析 JSON 数据
    data = json.loads(response_text)
    # 构造通知消息
    if data['Success']:
        message = f"签到成功！{data['message']}"
    else:
        message = f"签到失败：{data['message']}"
    # 发送通知
    QLAPI.notify('Linux.do API', message)
    await client.aclose()

asyncio.run(fetch())