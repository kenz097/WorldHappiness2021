import BDConnectionPool as Cp
import Happiness


# list of all querys
# insert country inside database
def insertCountry(country):
    col = Cp.connection_pool()
    col.insert_one({"Country_name": country[0].country_name,
                    "Regional_indicator": country[0].regional_indicator,
                    "Ladder_score": country[0].ladder_score,
                    "Standard_error_of_ladder_score": country[0].standard_error,
                    "upperwhisker": country[0].upperwhisker,
                    "lowerwhisker": country[0].lowerwhisker, "Logged_GDP_per_capita": country[0].logged_gdp,
                    "Social_support": country[0].social_suppport,
                    "Healthy_life_expectancy": country[0].healty_life_ex,
                    "Freedom_to_make_life_choices": country[0].freedom_choices,
                    "Generosity": country[0].generosity,
                    "Perceptions_of_corruption": country[0].percetions_corruption,
                    "Ladder_score_in_Dystopia": country[0].ladder_dystopia,
                    "Explained_by_Log_GDP_per_capita": country[0].exp_log_gdp,
                    "Explained_by_Social_support": country[0].exp_social_support,
                    "Explained_by_Healthy_life_expectancy": country[0].exp_healthy_life,
                    "Explained_by_Freedom_to_make_life_choices": country[0].exp_freedom_choices,
                    "Explained_by_Generosity": country[0].exp_generosity,
                    "Explained_by_Perceptions_of_corruption": country[0].exp_percetion_corruption,
                    "Dystopia_plus_residual": country[0].dystopia_plus_residual})
    return True


# update one country by name
def updateCountry(name, country2):
    col = Cp.connection_pool()
    myquery = {"Country_name": name}
    newvalues = {
        "$set": {"Country_name": country2[0].country_name, "Regional_indicator": country2[0].regional_indicator,
                 "Ladder_score": country2[0].ladder_score,
                 "Standard_error_of_ladder_score": country2[0].standard_error,
                 "upperwhisker": country2[0].upperwhisker,
                 "lowerwhisker": country2[0].lowerwhisker, "Logged_GDP_per_capita": country2[0].logged_gdp,
                 "Social_support": country2[0].social_suppport,
                 "Healthy_life_expectancy": country2[0].healty_life_ex,
                 "Freedom_to_make_life_choices": country2[0].freedom_choices,
                 "Generosity": country2[0].generosity,
                 "Perceptions_of_corruption": country2[0].percetions_corruption,
                 "Ladder_score_in_Dystopia": country2[0].ladder_dystopia,
                 "Explained_by_Log_GDP_per_capita": country2[0].exp_log_gdp,
                 "Explained_by_Social_support": country2[0].exp_social_support,
                 "Explained_by_Healthy_life_expectancy": country2[0].exp_healthy_life,
                 "Explained_by_Freedom_to_make_life_choices": country2[0].exp_freedom_choices,
                 "Explained_by_Generosity": country2[0].exp_generosity,
                 "Explained_by_Perceptions_of_corruption": country2[0].exp_percetion_corruption,
                 "Dystopia_plus_residual": country2[0].dystopia_plus_residual}}
    col.update_one(myquery, newvalues)


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
