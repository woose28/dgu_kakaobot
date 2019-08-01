import re
import requests
from bs4 import BeautifulSoup

#상록원 2층
def getMenu():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=1"
    res = requests.get(url)
    res.encoding = None
    html = res.text

    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")

    menu = "[상록원2층]\n"+"<"+tags_td[1].text+">\n"

    for i in [0,1] :
        for j in range(4+i, len(tags_td), 3) :
            if(i == 1 and j == 5) :
                menu = menu+"\n<"+tags_td[2].text+">\n"
            text = tags_td[j].text
            if(len(text) == 0) :
                continue
            if(text.find("￦") >= 0) :
                #￦가 있는 경우
                text = text.replace("￦ ", " ￦")
            else :
                #￦가 없는 경우
                text = text.replace(" ", " ￦").replace("원", "")
            menu = menu+text+"\n"
    return menu