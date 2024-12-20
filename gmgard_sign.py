"""
name: gmgard签到
cron: 7 0 * * *
"""
import asyncio
import httpx
import json
import os

async def fetch():
    cookie = json.loads(os.environ.get("GM_COOKIE"))
    if cookie is None:
        print("Cookie not set  use getenv method")
        cookie = os.getenv('GM_COOKIE')

    if cookie is None:
        print("cookie not set")
        return

    client = httpx.AsyncClient()
    response = await client.request(
        method="POST",
        url="https://gmgard.com/api/PunchIn/Do",
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept":"*/*",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Content-Type":"application/json",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://gmgard.com",
            "DNT":"1",
            "Sec-GPC":"1",
            "Connection":"keep-alive",
            "Referer":"https://gmgard.com/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin",
            "Priority":"u=0",
            "TE":"trailers",
        },
        cookies= cookie,
        content = """
                {}
            """
    )

    # response.encoding = "utf-8"
    # print(response.text)
    # QLAPI.notify('绅士之庭', '签到成功')
    # data = json.loads(response.text)
    # QLAPI.notify('绅士之庭', f'签到成功: {data}')
    # 解析 JSON 数据
    data = json.loads(response_text)
    # 构造通知消息
    if data['Success']:
        message = f"签到成功！连续签到天数: {data['ConsecutiveDays']}，奖励经验: {data['ExpBonus']}，当前积分: {data['Points']}"
    else:
        message = f"签到失败：{data['ErrorMessage']}"
    # 发送通知
    QLAPI.notify('绅士之庭', message)

    await client.aclose()
asyncio.run(fetch())