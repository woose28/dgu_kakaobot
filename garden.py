import re
import requests
from bs4 import BeautifulSoup

#가든쿡
def getMenu():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=9"
    res = requests.get(url)
    res.encoding = None
    html = res.text

    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")

    menu = "[가든쿡]\n"+"<"+tags_td[1].text+">\n"

    for i in range(3, len(tags_td), 2) :
        food = tags_td[i].text
        if len(food) == 0 :
            continue
        food = re.sub("(?P<won>\d+)[원]", " ￦\g<won>", food)
        menu = menu+food+"\n"
    return menu