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
        region = request.form['demo-category']  # non funziona

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
            j = 0
            for i in lista:
                happy.append(Happiness.Happiness(i))
                print(happy[j].country_name)
                j += 1
            return render_template("test_query.html", country_name=happy)
        except:
            return render_template("test_query.html", country_name="Nessun paese trovato")
    return render_template("test_query.html", country_name="problema a caso")


'''
QUERY DA COMPLETARE
@app.route("/test_query/insert_country", methods=['POST', 'GET'])
def insert_country():
    name = request.form['demo-name']
    region = request.form['demo-category']
    score = request.form['demo-score']
    dev = request.form['demo-dev']
    upper = request.form['demo-upper']
    lower = request.form['demo-lower']
    pil = request.form['demo-pil']
    social= request.form['demo-social']
    life= request.form['demo-life']
    freedom=request.form['demo-freedom']

    return render_template("test_query.html", country_name="nessun valore inserito")
'''


@app.route("/test_query/delete_query", methods=['POST', 'GET'])
def delete_query():
    if request.method == 'POST':
        name = request.form['demo-name']
        if name == "":
            return render_template("test_query.html", risposta="nessun paese inserito")
        else:
            elim = Query.deleteCountry(name)
            if elim:
                return render_template("test_query.html", risposta="Eliminazione effettuata")
            else:
                return render_template("test_query.html", risposta="Eliminazione non effettuata")


if __name__ == "__main__":
    app.run(debug=True)
