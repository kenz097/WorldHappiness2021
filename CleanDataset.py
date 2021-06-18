import pandas as pd
import csv


# delete all tuples having at least one null attribute and create a new csv file containing the tuples
def delete_null_item():
    happiness = pd.read_csv("world_happiness_report_2021.csv")
    happiness.dropna(axis='index', how='any', inplace=True)

    with open('world_happiness_report_2021_cleaned.csv', 'w', encoding="UTF-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Country_name", "Regional_indicator", "Ladder_score", "Standard_error_of_ladder_score",
                         "upperwhisker", "lowerwhisker", "Logged_GDP_per_capita", "Social_support",
                         "Healthy_life_expectancy", "Freedom_to_make_life_choices", "Generosity",
                         "Perceptions_of_corruption", "Ladder_score_in_Dystopia"])

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
                     happiness["Ladder_score_in_Dystopia"][i]
                     ])
            except:
                print("Valore non inserito numero", i)


delete_null_item()
