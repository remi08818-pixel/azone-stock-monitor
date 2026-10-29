import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# 淘宝店铺短链接
SHOP_URL = "https://m.tb.cn/h.j4N6x5jLyPNb9Kf"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": message},
        timeout=20
    )
    response.raise_for_status()
    result = response.json()
    if not result.get("ok"):
        raise RuntimeError(f"Telegram error: {result}")

def main():
    # 当前版本先验证云端运行和 Telegram 通知是否正常。
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    send_telegram(
        "Azone 监控程序已启动测试。\n"
        f"运行时间：{now}\n"
        f"目标店铺：{SHOP_URL}\n"
        "注意：淘宝商品抓取尚未接入，当前还不能自动发现新品。"
    )

if __name__ == "__main__":
    main()
