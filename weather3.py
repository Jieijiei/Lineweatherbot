#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup

import requests
line_notify_token = 'N1ErpTvFtbgdviHjUa7aua8F7y4nGrboeNKS0UUcY53'
line_notify_api = 'https://notify-api.line.me/api/notify'

# Get Weather Information (Default:Mito, Ibaraki, Japan)
rssurl = "http://weather.livedoor.com/forecast/rss/area/130010.xml"

tenki = []
with urllib.request.urlopen(rssurl) as res:
    xml = res.read()
    soup = BeautifulSoup(xml, "html.parser")
    for item in soup.find_all("item"):
        title = item.find("title").string
        if title.find("[ PR ]") == -1:
            tenki.append(title)

for i in range(0,2):
    message = tenki[i]
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # Token
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
