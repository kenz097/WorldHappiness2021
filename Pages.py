from flask import Flask, redirect, url_for, render_template, make_response, request, json
import QueryList as Query
import Happiness

app = Flask(__name__)


@app.route("/")
def main():
    lista = Query.country()
    happy = []
    for i in lista:
        happy.append(Happiness.Happiness(i))
    resp = make_response(render_template('Homepage.html', list_country=happy))
    return resp


if __name__ == "__main__":
    app.run(debug=True)
