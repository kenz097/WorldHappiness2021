# class Happiness for our database
from typing import Type, Any


class Happiness:
    def __init__(self, happiness):
        self.id_dataset = happiness["_id"]
        self.country_name = happiness["Country_name"]
        self.regional_indicator = happiness["Regional_indicator"]
        self.ladder_score = happiness["Ladder_score"]
        self.standard_error = happiness["Standard_error_of_ladder_score"]
        self.upperwhisker = happiness["upperwhisker"]
        self.lowerwhisker = happiness["lowerwhisker"]
        self.logged_gdp = happiness["Logged_GDP_per_capita"]
        self.social_suppport = happiness["Social_support"]
        self.healty_life_ex = happiness["Healthy_life_expectancy"]
        self.freedom_choices = happiness["Freedom_to_make_life_choices"]
        self.generosity = happiness["Generosity"]
        self.percetions_corruption = happiness["Perceptions_of_corruption"]
        self.ladder_dystopia = happiness["Ladder_score_in_Dystopia"]


    def dump(self):
        return {"Country_name": self.country_name,
                "Regional_indicator": self.regional_indicator,
                "Ladder_score": self.ladder_score,
                "Standard_error_of_ladder_score": self.standard_error, "upperwhisker": self.upperwhisker,
                "lowerwhisker": self.lowerwhisker, "Logged_GDP_per_capita": self.logged_gdp,
                "Social_support": self.social_suppport,
                "Healthy_life_expectancy": self.healty_life_ex, "Freedom_to_make_life_choices": self.freedom_choices,
                "Generosity": self.generosity, "Perceptions_of_corruption": self.percetions_corruption,
                "Ladder_score_in_Dystopia": self.ladder_dystopia}


# check if all attribute aren't Null
def checkFormato(test):
    if test.country_name == "" and test.regional_indicator == "" and test.ladder_score == "" \
            and test.standard_error == "" and test.upperwhisker == "" and test.lowerwhisker == "" \
            and test.logged_gdp == "" and test.social_suppport == "" and test.healty_life_ex == "" \
            and test.freedom_choices == "" and test.generosity == "" and test.percetions_corruption == "" \
            and test.ladder_dystopia == "":
        return False
    return True
