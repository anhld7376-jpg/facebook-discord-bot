import requests
from bs4 import BeautifulSoup
import time

WEBHOOK = "https://discord.com/api/webhooks/1480184925172011108/VHK2TDc3BYsvlqco-fKpCLYmcd0yqI9QVd_aOtwcxhVLP27ewgoKZmnaYFfCYWQPHP3u"
PAGE = "https://mbasic.facebook.com/nghichthuyhanofficial"

last_post = None

def send_discord(text, link):
    data = {
        "content": f"📢 Bài đăng Facebook mới\n{text}\n{link}"
    }
    requests.post(WEBHOOK, json=data)

while True:
    r = requests.get(PAGE)
    soup = BeautifulSoup(r.text, "html.parser")

    post = soup.find("a", href=True)

    if post:
        link = "https://facebook.com" + post["href"]
        text = post.text

        global last_post

        if link != last_post:
            send_discord(text, link)
            last_post = link

    time.sleep(120)
