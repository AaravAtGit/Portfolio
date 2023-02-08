from flask import Flask,render_template
import requests

app = Flask(__name__)






@app.route("/")
def home():
    r = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&format=txt&type=single")
    joke = r.text
    return render_template("index.html",joke=joke)




if __name__ == "__main__":
    app.run(debug=True)


