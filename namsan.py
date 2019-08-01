import re
import requests
from bs4 import BeautifulSoup

def getMenu():
    url = "http://dgucoop.dongguk.edu/mobile/menu.html?code=8"
    res = requests.get(url)
    res.encoding = None

    html = res.text
    bs = BeautifulSoup(html, "html.parser")

    tags_td = bs.findAll("td")


    menu = "[남산학사]\n"

    breakfast = "<"+tags_td[1].text+">\n"
    lunch = "<"+tags_td[2].text+">\n"
    dinner = "<"+tags_td[3].text+">\n"

    #조식
    for i in range(5, len(tags_td), 5) :
        food = tags_td[i].text
        if(len(food) == 0) :
            continue
        breakfast = breakfast + food.replace("￦ ", " ￦") + "\n"
    #중식
    for i in range(6, len(tags_td), 5) :
        food = tags_td[i].text
        if(len(food) == 0) :
            continue
        if food.find("￦") != -1 :
            food = food.replace("￦ ", " ￦")
        elif re.search("[\r\n](?P<won>\d+)[원]", food) :
            food = food.replace("\r\n", "\n")
            food = re.sub("[\n](?P<won>\d+)[원]", " ￦\g<won>", food)
        elif food.startswith("*") :
            food = re.sub("\s{2}(?P<won>\d+)[원]", "  ￦\g<won>", food)
        lunch = lunch + food + "\n"
    #석식
    for i in range(7, len(tags_td), 5) :
        food = tags_td[i].text
        if(len(food) == 0) :
            continue
        
        dinner = dinner + food.replace("￦ ", " ￦") + "\n"

    menu = menu+breakfast+"\n"+lunch+"\n"+dinner
    return menu