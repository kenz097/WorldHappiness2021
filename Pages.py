from flask import Flask, redirect, url_for, render_template, make_response, request, json
import QueryList as Query
import Happiness

app = Flask(__name__, template_folder="bd_project_frontend", static_folder="bd_project_frontend/assets")


@app.route("/homepage")
def main():
    return render_template("index.html")


@app.route("/test_query")
def test_query():
    lista = Query.countryAlphabetica()
    happy = []
    for i in lista:
        happy.append((Happiness.Happiness(i)))

    return render_template("test_query.html", list_country=happy)


if __name__ == "__main__":
    app.run(debug=True)
