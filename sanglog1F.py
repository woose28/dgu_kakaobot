import re
import requests
from bs4 import BeautifulSoup
#tr : 행
#td : 칸

#상록원 1층
def getMenu():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=7"
    res = requests.get(url)
    res.encoding=None
    html = res.text

    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")
    menu = "[상록원1층]\n<"+tags_td[1].text+">\n"

    for i in range(3, len(tags_td), 2) :
        text = tags_td[i].text
        if len(text) == 0 :
            continue
        won = re.findall("￦\s[0-9]*,[0-9]*",text)[0]
        foods = text.replace(won, "").split("\r\n")
        for food in foods :
            menu = menu + food + " " + won.replace(" ", "") + "\n"
    return menu