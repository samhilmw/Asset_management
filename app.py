from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>/<string:passw>")
def login(name,passw):
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8099)
