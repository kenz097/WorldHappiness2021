import BDConnectionPool as Cp
import Happiness


# list of all querys
# insert country inside database
def insertCountry(country):
    col = Cp.connection_pool()
    col.insert_one({"Country_name": country.country_name,
                    "Regional_indicator": country.regional_indicator,
                    "Ladder_score": country.ladder_score,
                    "Standard_error_of_ladder_score": country.standard_error,
                    "upperwhisker": country.upperwhisker,
                    "lowerwhisker": country.lowerwhisker, "Logged_GDP_per_capita": country.logged_gdp,
                    "Social_support": country.social_suppport,
                    "Healthy_life_expectancy": country.healty_life_ex,
                    "Freedom_to_make_life_choices": country.freedom_choices,
                    "Generosity": country.generosity,
                    "Perceptions_of_corruption": country.percetions_corruption,
                    "Ladder_score_in_Dystopia": country.ladder_dystopia})


# update one country by name
def updateCountry(name, country2):
    col = Cp.connection_pool()
    myquery = {"Country_name": name}
    newvalues = {
        "$set": {"Country_name": country2.country_name, "Regional_indicator": country2.regional_indicator,
                 "Ladder_score": country2.ladder_score,
                 "Standard_error_of_ladder_score": country2.standard_error,
                 "upperwhisker": country2.upperwhisker,
                 "lowerwhisker": country2.lowerwhisker, "Logged_GDP_per_capita": country2.logged_gdp,
                 "Social_support": country2.social_suppport,
                 "Healthy_life_expectancy": country2.healty_life_ex,
                 "Freedom_to_make_life_choices": country2.freedom_choices,
                 "Generosity": country2.generosity,
                 "Perceptions_of_corruption": country2.percetions_corruption,
                 "Ladder_score_in_Dystopia": country2.ladder_dystopia}}
    col.update(myquery, newvalues)


# delete country by name
def deleteCountry(name):
    col = Cp.connection_pool()
    col.delete_one({"Country_name": name})


# find countries by name
def findCountry(name):
    col = Cp.connection_pool()
    query = col.find({"Country_name": name})
    return query


# find countries by Regional indicator
def findRegionalIndicator(name):
    col = Cp.connection_pool()
    query = col.find({"Regional_indicator": name})
    return query


# finds all ladder score values between min and max
def findLadderScore(min, max):
    col = Cp.connection_pool()
    query = col.find({"Ladder_score": {"$gt": min, "$lt": max}})
    return query


# finds all Logged_GDP_per_capita values between min and max
def findGDPCapita(min, max):
    col = Cp.connection_pool()
    query = col.find({"Logged_GDP_per_capita": {"$gt": min, "$lt": max}})
    return query


# finds all Healthy_life_expectancy values between min and max
def findHealthyLife(min, max):
    col = Cp.connection_pool()
    query = col.find({"Healthy_life_expectancy": {"$gt": min, "$lt": max}})
    return query


# finds all countries in ascending order of name
def countryAlphabetica():
    col = Cp.connection_pool()
    query = col.find().sort("Country_name", 1)
    return query


# find all countries in ascending order of the ladder score
def ladderAscending():
    col = Cp.connection_pool()
    query = col.find().sort("Ladder_score", 1)
    return query


# find all countries in descending order of the ladder score
def ladderDescending():
    col = Cp.connection_pool()
    query = col.find().sort("Ladder_score", -1)
    return query


def fiveParameter(country, region, ladder, gdp, life):
    col = Cp.connection_pool()
    query = col.find({"$and": [
        {"Country_name": country, "Regional_indicator": region, "Ladder_score": ladder,
         "Logged_GDP_per_capita": gdp, "Healthy_life_expectancy": life}]})
    return query
