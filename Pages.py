from flask import Flask, redirect, url_for, render_template, make_response, request, json
import QueryList as Query
import Happiness

app = Flask(__name__, template_folder="bd_project_frontend", static_folder="bd_project_frontend/assets")

table = None


def changeResult(value):
    global table
    table = value
    return getResult()


def getResult():
    return table


def fullTable():
    lista = Query.countryAlphabetica()
    happy = []
    for i in lista:
        happy.append((Happiness.Happiness(i)))
    return happy


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/test_query")
def test_query():
    return render_template("test_query.html", list_country=changeResult(fullTable()))


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
            if len(happy) != 0:
                return render_template("test_query.html", list_country=changeResult(happy))
            else:
                return render_template("test_query.html", response="Non esistono paesi con queste caratteristiche",
                                       list_country=getResult())
        except:
            return render_template("test_query.html", response="Nessun paese trovato", list_country=getResult())
    return render_template("test_query.html", response="Errore rilevato", list_country=getResult())


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
    corr = request.form['demo-corr']

    object = {"_id": "", "Country_name": name, "Regional_indicator": region, "Ladder_score": score,
              "Standard_error_of_ladder_score": dev, "upperwhisker": upper, "lowerwhisker": lower,
              "Logged_GDP_per_capita": pil, "Social_support": social, "Healthy_life_expectancy": life,
              "Freedom_to_make_life_choices": freedom, "Generosity": generosity, "Perceptions_of_corruption": corr}

    happy = Happiness.Happiness(object)
    if Happiness.checkFormato(happy):
        Query.insertCountry(happy)
        return render_template("test_query.html", response="paese inserito correttamente",
                               list_country=fullTable())
    else:
        return render_template("test_query.html", response="valori mancanti", list_country=getResult())


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

    object = {"_id": "", "Country_name": name, "Regional_indicator": region, "Ladder_score": score,
              "Standard_error_of_ladder_score": dev, "upperwhisker": upper, "lowerwhisker": lower,
              "Logged_GDP_per_capita": pil, "Social_support": social, "Healthy_life_expectancy": life,
              "Freedom_to_make_life_choices": freedom, "Generosity": generosity, "Perceptions_of_corruption": corr}

    if name == "":
        return render_template("test_query.html", response="Errore. Nessun paese inserito", list_country=getResult())
    else:
        result = Query.findCountry(name)
        value = []
        new = Happiness.Happiness(object)
        for i in result:
            value.append(Happiness.Happiness(i))
        if len(value) != 0:
            if new_name == "":
                new_name = name
            if new.country_name == "":
                new.country_name = value.country_name
                new_name = value.country_name
            if new.regional_indicator == "":
                new.regional_indicator = value[0].regional_indicator
            if new.ladder_score == "":
                new.ladder_score = value[0].ladder_score
            if new.standard_error == "":
                new.standard_error = value[0].ladder_score
            if new.upperwhisker == "":
                new.upperwhisker = value[0].upperwhisker
            if new.lowerwhisker == "":
                new.lowerwhisker = value[0].lowerwhisker
            if new.logged_gdp == "":
                new.logged_gdp = value[0].logged_gdp
            if new.social_suppport == "":
                new.logged_gdp = value[0].logged_gdp
            if new.healty_life_ex == "":
                new.healty_life_ex = value[0].healty_life_ex
            if new.freedom_choices == "":
                new.freedom_choices = value[0].freedom_choices
            if new.generosity == "":
                new.generosity = value[0].generosity
            if new.percetions_corruption == "":
                new.percetions_corruption = value[0].percetions_corruption
            Query.updateCountry(new_name, new)
            return render_template("test_query.html", response="Aggiornamento effettuato", list_country=fullTable())
        else:
            return render_template("test_query.html", response="Aggiornamento non effettuato", list_country=getResult())


@app.route("/test_query/delete_query", methods=['POST', 'GET'])
def delete_query():
    if request.method == 'POST':
        name = request.form['demo-name']
        if name == "":
            return render_template("test_query.html", response="Nessun paese rilevato da eliminare",
                                   list_country=getResult())
        else:
            result = Query.findCountry(name)
            value = None
            for i in result:
                value = result
            if value is not None:
                Query.deleteCountry(name)
                return render_template("test_query.html", response="Eliminazione effettuata", list_country=fullTable())
            else:
                return render_template("test_query.html", response="Eliminazione non effettuata",
                                       list_country=getResult())


if __name__ == "__main__":
    app.run(debug=True)
