from flask import Flask

app = Flask(__name__)

@app.route('/')

def hell():
    return "<h1>hello Flask    hohohoho <h1>"


@app.route("/test")

def test():
    return"<h1>test<h1>"

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)

