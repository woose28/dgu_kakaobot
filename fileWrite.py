from time import sleep
from requests_html import HTMLSession

url = "https://lib.dongguk.edu"
#session = HTMLSession()
#i = 1

while(True) :
    session = HTMLSession()

    r = session.get(url)
    r.html.render()
    sleep(8)
    html  = r.html
    session.close()

    seats = ""

    for tag in html.find("li.book"):
        seat = tag.find("h3")[0].text+":"+tag.find("span.num")[0].text+"/"+tag.find("span.total")[0].text
        seats = seats+seat+"\n"
    seats = seats[:len(seats) - 5]+seats[len(seats)-5:].replace("\n","")#+str(i)
    
    fhandle = open("./library_seats.txt", "w")
    fhandle.write(seats)
    
    #i = i + 1
    fhandle.close()
    
    sleep(1)