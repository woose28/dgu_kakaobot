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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    