from flask import Flask, redirect, url_for, render_template, make_response, request, json
import QueryList as Query
import Happiness

app = Flask(__name__, template_folder="bd_project_frontend", static_folder="bd_project_frontend/assets")


@app.route("/homepage")
def home():
    return render_template("index.html")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/test_query")
def test_query():
    lista = Query.countryAlphabetica()
    happy = []
    for i in lista:
        happy.append((Happiness.Happiness(i)))

    return render_template("test_query.html", list_country=happy)


@app.route("/test_query/find_query", methods=['POST', 'GET'])
def find_query():
    if request.method == 'POST':
        name = request.form['demo-name']
        minhappy = request.form['demo-min-happy']
        maxhappy = request.form['demo-max-happy']
        minpil = request.form['demo-min-pil']
        maxpil = request.form['demo-max-pil']
        minlife = request.form['demo-min-life']
        maxlife = request.form['demo-max-life']
        region = request.form['demo-category']

        temp1 = 0
        temp2 = 0
        if name == "":
            name = {"$ne": None}
        if minhappy == "":
            if maxhappy == "":
                tothappy = {"$ne": None, "$ne": None}
            else:
                temp2 = float(maxhappy)
                tothappy = {"$ne": None, "$lt": temp2}
        else:
            temp1 = float(minhappy)
            if maxhappy == "":
                tothappy = {"$gt": temp1, "$ne": None}
            else:
                temp2 = float(maxhappy)
                tothappy = {"$gt": temp1, "$lt": temp2}
        if minpil == "":
            if maxpil == "":
                totpil = {"$ne": None, "$ne": None}
            else:
                temp2 = float(maxpil)
                totpil = {"$ne": None, "$lt": temp2}
        else:
            temp1 = float(minpil)
            if maxpil == "":
                totpil = {"$gt": temp1, "$ne": None}
            else:
                temp2 = float(maxpil)
                totpil = {"$gt": temp1, "$lt": temp2}
        if minlife == "":
            if maxlife == "":
                totlife = {"$ne": None, "$ne": None}
            else:
                temp2 = float(maxlife)
                totlife = {"$ne": None, "$lt": temp2}
        else:
            temp1 = float(minlife)
            if maxlife == "":
                totlife = {"$gt": temp1, "$ne": None}
            else:
                temp2 = float(maxlife)
                totlife = {"$gt": temp1, "$lt": temp2}
        if region == "":
            region = {"$ne": None}
        try:
            lista = Query.fiveParameter(name, region, tothappy, totpil, totlife)
            happy = []
            for i in lista:
                happy.append(Happiness.Happiness(i))
            return render_template("test_query.html", list_country=happy)
        except:
            return render_template("test_query.html", list_country="Nessun paese trovato")
    return render_template("test_query.html", list_country="problema a caso")


@app.route("/test_query/insert_country", methods=['POST', 'GET'])
def insert_country():
    name = request.form['demo-name']
    region = request.form['demo-category']
    score = request.form['demo-score']
    dev = request.form['demo-dev']
    upper = request.form['demo-upper']
    lower = request.form['demo-lower']
    pil = request.form['demo-pil']
    social = request.form['demo-social']
    life = request.form['demo-life']
    freedom = request.form['demo-freedom']
    generosity = request.form['demo-generosity']
    disto = request.form['demo-disto']
    corr = request.form['demo-corr']
    # mancano dei valori
    happy = Happiness.Happiness(name, region, score, dev, upper, lower, pil, social, life, freedom, generosity, disto,
                                corr)
    if Happiness.checkFormato(happy):
        Query.insertCountry(happy)
        return render_template("test_query.html", country_name="oggetto inserito correttamente")
    else:
        return render_template("test_query.html", country_name="valori mancanti")


@app.route("/test_query/update_country", methods=['POST', 'GET'])
def update_country():
    name = request.form['demo-name']
    new_name = request.form['demo-new-name']
    region = request.form['demo-category']
    score = request.form['demo-score']
    dev = request.form['demo-dev']
    upper = request.form['demo-upper']
    lower = request.form['demo-lower']
    pil = request.form['demo-pil']
    social = request.form['demo-social']
    life = request.form['demo-life']
    freedom = request.form['demo-freedom']
    generosity = request.form['demo-generosity']
    corr = request.form['demo-corr']
    disto = request.form['demo-disto']

    if name == "":
        return render_template("test_query.html", risposta="nessun paese inserito")
    else:
        result = Query.findCountry(name)
        value = None
        new = Happiness.Happiness(new_name, region, score, dev, upper, lower, pil, social, life,
                                  freedom, generosity, corr, disto)
        for i in result:
            value = result
        if value is not None:
            if new.country_name == "":
                new.country_name = value.country_name
                new_name = value.country_name
            if new.regional_indicator == "":
                new.regional_indicator = value.regional_indicator
            if new.ladder_score == "":
                new.ladder_score = value.ladder_score
            if new.standard_error == "":
                new.standard_error = value.ladder_score
            if new.upperwhisker == "":
                new.upperwhisker = value.upperwhisker
            if new.lowerwhisker == "":
                new.lowerwhisker = value.lowerwhisker
            if new.logged_gdp == "":
                new.logged_gdp = value.logged_gdp
            if new.social_suppport == "":
                new.logged_gdp = value.logged_gdp
            if new.healty_life_ex == "":
                new.healty_life_ex = value.healty_life_ex
            if new.freedom_choices == "":
                new.freedom_choices = value.freedom_choices
            if new.generosity == "":
                new.generosity = value.generosity
            if new.ladder_dystopia == "":
                new.ladder_dystopia = value.ladder_dystopia
            if new.percetions_corruption == "":
                new.percetions_corruption = value.percetions_corruption

            Query.updateCountry(new_name, new)
            return render_template("test_query.html", risposta="Aggiornamento effettuato")
        else:
            return render_template("test_query.html", risposta="Aggiornamento non effettuato")


@app.route("/test_query/delete_query", methods=['POST', 'GET'])
def delete_query():
    if request.method == 'POST':
        name = request.form['demo-name']
        if name == "":
            return render_template("test_query.html", risposta="nessun paese inserito")
        else:
            result = Query.findCountry(name)
            value = None
            for i in result:
                value = result
            if value is not None:
                Query.deleteCountry(name)
                return render_template("test_query.html", risposta="Eliminazione effettuata")
            else:
                return render_template("test_query.html", risposta="Eliminazione non effettuata")


if __name__ == "__main__":
    app.run(debug=True)
