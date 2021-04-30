from flask import Flask, render_template, request
from spotify import spotify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    q = request.args.get("query")
    type_ = request.args.get("type")
    results = spotify.search(q, type=type_)[f"{type_}s"]["items"]

    return render_template("search.html", results=results, q=q, type=type_)

if __name__ == "__main__":
    app.run(debug=True)