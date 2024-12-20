import requests
import json
import os

try:
    # 获取环境变量并解析为字典
    follow_cookie_env = os.environ.get("FOLLOW_COOKIE")
    if not follow_cookie_env:
        raise ValueError("环境变量 FOLLOW_COOKIE 未设置或为空")
    cookie_data = json.loads(follow_cookie_env)
    
    # 验证是否包含所需字段
    if not all(key in cookie_data for key in ("cookie", "csrfToken")):
        raise ValueError("FOLLOW_COOKIE 缺少必要字段 'cookie' 或 'csrfToken'")
    
    # 提取 cookie 和 csrfToken
    cookie = cookie_data["cookie"]
    csrfToken = cookie_data["csrfToken"]

except json.JSONDecodeError:
    raise ValueError("FOLLOW_COOKIE 不是有效的 JSON 格式")
except ValueError as e:
    raise e

def sign_in():
    url = "https://api.follow.is/wallets/transactions/claim_daily"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.38(0x1800262c) NetType/4G Language/zh_CN',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Cookie': cookie
    }
    
    payload = {
        "csrfToken": csrfToken
    }
    
    try:
        # 发送 POST 请求
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        message = f"请求失败: {e}"
        QLAPI.notify('follow', message)
        return
    
    # 解析返回结果
    result = response.json()
    code = result.get('code')
    message = result.get('message', 'No message')
    
    if code == 0:
        message = "签到成功"
    elif "Already claimed" in message:
        message = "今日已签到"
    else:
        message = f"签到失败: {message}"
    # 发送通知
    QLAPI.notify('follow', message)

if __name__ == "__main__":
    sign_in()