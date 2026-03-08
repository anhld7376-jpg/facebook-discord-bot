import requests
from bs4 import BeautifulSoup

WEBHOOK = "https://discord.com/api/webhooks/1480184925172011108/VHK2TDc3BYsvlqco-fKpCLYmcd0yqI9QVd_aOtwcxhVLP27ewgoKZmnaYFfCYWQPHP3u"
URL = "https://mbasic.facebook.com/nghichthuyhanofficial"

headers = {
 "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.text,"html.parser")

post = soup.find("a", string="Full Story")

if post:
 link = "https://facebook.com"+post["href"]

 requests.post(WEBHOOK,json={
  "content":f"📢 Bài mới từ fanpage\n{link}"
 })
