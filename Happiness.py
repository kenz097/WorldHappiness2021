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
        self.exp_log_gdp = happiness["Explained_by_Log_GDP_per_capita"]
        self.exp_social_support = happiness["Explained_by_Social_support"]
        self.exp_healthy_life = happiness["Explained_by_Healthy_life_expectancy"]
        self.exp_freedom_choices = happiness["Explained_by_Freedom_to_make_life_choices"]
        self.exp_generosity = happiness["Explained_by_Generosity"]
        self.exp_percetion_corruption = happiness["Explained_by_Perceptions_of_corruption"]
        self.dystopia_plus_residual = happiness["Dystopia_plus_residual"]

    def dump(self):
        return {"Country_name": self.country_name,
                "Regional_indicator": self.regional_indicator,
                "Ladder_score": self.ladder_score,
                "Standard_error_of_ladder_score": self.standard_error, "upperwhisker": self.upperwhisker,
                "lowerwhisker": self.lowerwhisker, "Logged_GDP_per_capita": self.logged_gdp,
                "Social_support": self.social_suppport,
                "Healthy_life_expectancy": self.healty_life_ex, "Freedom_to_make_life_choices": self.freedom_choices,
                "Generosity": self.generosity, "Perceptions_of_corruption": self.percetions_corruption,
                "Ladder_score_in_Dystopia": self.ladder_dystopia, "Explained_by_Log_GDP_per_capita": self.exp_log_gdp,
                "Explained_by_Social_support": self.exp_social_support,
                "Explained_by_Healthy_life_expectancy": self.exp_healthy_life,
                "Explained_by_Freedom_to_make_life_choices": self.exp_freedom_choices,
                "Explained_by_Generosity": self.exp_generosity,
                "Explained_by_Perceptions_of_corruption": self.exp_percetion_corruption,
                "Dystopia_plus_residual": self.dystopia_plus_residual}
