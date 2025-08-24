# demographic_data_analyzer.py
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Carregar o dataset
    df = pd.read_csv("adult.data.csv")

    # 1. Contagem de cada raça
    race_count = df["race"].value_counts()

    # 2. Média de idade dos homens
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentual de pessoas com bacharelado
    percentage_bachelors = round(
        (df["education"].eq("Bachelors").mean() * 100), 1
    )

    # 4. Educação avançada (Bachelors, Masters, Doctorate)
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education = ~higher_education

    # Percentuais de ricos (>50K)
    higher_education_rich = round(
        df[higher_education]["salary"].eq(">50K").mean() * 100, 1
    )
    lower_education_rich = round(
        df[lower_education]["salary"].eq(">50K").mean() * 100, 1
    )

    # 5. Mínimo de horas trabalhadas por semana
    min_work_hours = int(df["hours-per-week"].min())

    # Percentual de ricos entre quem trabalha o mínimo
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(min_workers["salary"].eq(">50K").mean() * 100, 1)

    # 6. País com maior percentual de pessoas >50K
    country_salary = (
        df.groupby("native-country")["salary"]
          .value_counts(normalize=True)
          .unstack(fill_value=0)
    )
    country_salary[">50K%"] = country_salary[">50K"] * 100
    highest_earning_country = country_salary[">50K%"].idxmax()
    highest_earning_country_percentage = round(country_salary[">50K%"].max(), 1)

    # 7. Ocupação mais comum na Índia para pessoas >50K
    india_top_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        ["occupation"].mode()[0]
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print("Min work time:", min_work_hours, "hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", india_top_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "india_top_occupation": india_top_occupation,
    }

if __name__ == "__main__":
    calculate_demographic_data(print_data=True)
