import pandas as pd
import csv


def delete_null_item():
    happiness = pd.read_csv("world_happiness_report_2021.csv")
    happiness.dropna(axis='index', how='any', inplace=True)

    with open('world_happiness_report_2021_not_null.csv', 'w', encoding="UTF-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Country_name", "Regional_indicator", "Ladder_score", "Standard_error_of_ladder_score",
                         "upperwhisker", "lowerwhisker", "Logged_GDP_per_capita", "Social_support",
                         "Healthy_life_expectancy", "Freedom_to_make_life_choices", "Generosity",
                         "Perceptions_of_corruption", "Ladder_score_in_Dystopia", "Explained_by_Log_GDP_per_capita",
                         "Explained_by_Social_support", "Explained_by_Healthy_life_expectancy",
                         "Explained_by_Freedom_to_make_life_choices",
                         "Explained_by_Generosity", "Explained_by_Perceptions_of_corruption", "Dystopia_plus_residual"])

        for i in range(0, len(happiness)):
            try:

                writer.writerow(
                    [happiness["Country_name"][i], happiness["Regional_indicator"][i],
                     happiness["Ladder_score"][i],
                     happiness["Standard_error_of_ladder_score"][i],
                     happiness["upperwhisker"][i],
                     happiness["lowerwhisker"][i], happiness["Logged_GDP_per_capita"][i],
                     happiness["Social_support"][i], happiness["Healthy_life_expectancy"][i],
                     happiness["Freedom_to_make_life_choices"][i],
                     happiness["Generosity"][i], happiness["Perceptions_of_corruption"][i],
                     happiness["Ladder_score_in_Dystopia"][i],
                     happiness["Explained_by_Log_GDP_per_capita"][i], happiness["Explained_by_Social_support"][i],
                     happiness["Explained_by_Healthy_life_expectancy"][i],
                     happiness["Explained_by_Freedom_to_make_life_choices"][i], happiness["Explained_by_Generosity"][i],
                     happiness["Explained_by_Perceptions_of_corruption"][i], happiness["Dystopia_plus_residual"][i]
                     ])
            except:
                print("Valore non inserito numero", i)


delete_null_item()
