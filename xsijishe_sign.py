import asyncio
import httpx


async def fetch():
    cookie = os.environ.get('SJS_COOKIE')
    if cookie is None:
        print("Cookie not set  use getenv method")
        cookie = os.getenv('SJS_COOKIE')

    if cookie is None:
        print("cookie not set ")
        return
    client = httpx.AsyncClient()
    response = await client.request(
        method="GET",
        url="https://xsijishe.com/k_misign-sign.html",
        params={
        "btwaf":"38363360"
    },
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Referer":"https://xsijishe.com/k_misign-sign.html?btwaf=24243759",
            "DNT":"1",
            "Sec-GPC":"1",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Fetch-Dest":"document",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin",
            "Sec-Fetch-User":"?1",
            "Priority":"u=0, i",
            "TE":"trailers"
        },
        cookies=cookie,
    )
    
    response.encoding = "utf-8"
    print(response.text)
    await client.aclose()

asyncio.run(fetch())
