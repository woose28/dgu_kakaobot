from flask import Flask, jsonify

app = Flask("__name__")

@app.route("/test", methods=["POST"])
def test():
    res = {
        "version" : "2.0",
        "template" : {
            "outputs" : [
                {
                    "simpleText" : {
                        "text" : "Hello~!"
                    }
                }
            ]
        }
    }
    return jsonify(res)

@app.route("/library", methods=["POST"])
def library():
    fhandle = open("../library/library_seats.txt", "r")
    seats = ""
    for line in fhandle:
        if len(line) == 0:
            continue
        seats = seats + line
        #seats = seats.rstrip()
        
    res = {
        "version" : "2.0",
        "template" : {
            "outputs" : [
                {
                    "simpleText" :{
                        "text" : seats
                    }
                }
            ]
        }
    }
    return jsonify(res)

@app.route("/restaurant", methods=["POST"])
def restaurant():
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "상록원 1층",
                                "description": "운영시간 \n (분식) \n 평일: 09:00 ~ 18:00 \n 주말: 휴무 \n \n (솥앤누들) \n 평일: 10:30 ~ 19:00 \n 주말: 10:30 ~ 18:00",
                                "thumbnail": {
                                    "imageUrl": ""
                                },
                                "buttons": [
                                    {
                                        "action": "weblink",
                                        "label": "메뉴 확인하기",
                                        "webLinkUrl": "http://dgucoop.dongguk.edu/mobile/menu.html?code=7"
                                    }
                                ]
                            },
                            {
                                "title": "상록원 2층 & 3층",
                                "description": "운영시간 \n (2층) \n 평일: 10:30 ~ 18:00 \n 주말: 휴무 \n \n (3층) \n 평일: 11:00 ~ 18:00 \n 주말: 11:30 ~ 14:00 (일 휴무)",
                                "thumbnail": {
                                    "imageUrl": ""
                                },
                                "buttons": [
                                    {
                                        "action": "weblink",
                                        "label": "메뉴 확인하기(2층)",
                                        "webLinkUrl": "http://dgucoop.dongguk.edu/mobile/menu.html?code=1"
                                    },
                                    {
                                        "action": "weblink",
                                        "label": "메뉴 확인하기(3층)",
                                        "webLinkUrl": "http://dgucoop.dongguk.edu/mobile/menu.html?code=5"
                                    }
                                ]
                            },
                            {
                                "title": "남산학사",
                                "description": "운영시간 \n 평일: 08:00 ~ 19:00 \n 주말: 휴무",
                                "thumbnail": {
                                    "imageUrl": ""
                                },
                                "buttons": [
                                    {
                                        "action": "weblink",
                                        "label": "메뉴 확인하기",
                                        "webLinkUrl": "http://dgucoop.dongguk.edu/mobile/menu.html?code=8"
                                    }
                                ]
                            },
                            {
                                "title": "그루터기",
                                "description": "운영시간 \n 방학 중 운영중단",
                                "thumbnail": {
                                    "imageUrl": ""
                                },
                                "buttons": [
                                    {
                                        "action": "weblink",
                                        "label": "메뉴 확인하기",
                                        "webLinkUrl": "http://dgucoop.dongguk.edu/mobile/menu.html?code=2"
                                    }
                                ]
                            },
                            {
                                "title": "가든쿡",
                                "description": "운영시간 \n 평일: 11:00 ~ 18:00 \n 주말: 11:00 ~ 18:00 (일 휴무)",
                                "thumbnail": {
                                    "imageUrl": ""
                                },
                                "buttons": [
                                    {
                                        "action": "weblink",
                                        "label": "메뉴 확인하기",
                                        "webLinkUrl": "http://dgucoop.dongguk.edu/mobile/menu.html?code=9"
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
