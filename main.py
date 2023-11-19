from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_api = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_api)
    data = response.json()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
