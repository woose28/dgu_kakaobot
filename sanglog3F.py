import re
import requests
from bs4 import BeautifulSoup

#상록원 3층

def getMenu():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=5"
    res = requests.get(url)
    res.encoding = None
    html = res.text

    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")

    menu = "[상록원3층]\n<"+tags_td[1].text+">\n"
    for i in [0,1] :
        for j in range(4+i, len(tags_td)-2, 3) :
            if(i == 1 and j == 5) :
                menu = menu+"\n<"+tags_td[2].text+">\n"
            text = tags_td[j].text
            if(len(text) == 0) :
                continue
            text = text.replace("￦ ", " ￦")
            
            menu = menu+text+"\n"

    menu = menu+"\n<"+tags_td[9].text+">\n"+tags_td[10].text.replace("-", " ￦").replace("원￦ ", "\n￦")
    return menu