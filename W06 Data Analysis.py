"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Professor: Sister Creer
Project: Data Analysis
Creativity Credit Explanation: I ran a loop analogous to selected_year for a selected_country analysis, addind trackers for the respective analysis.
"""

min_life = float('inf')
max_life = float('-inf')
min_country = ""
max_country = ""
min_year = 0
max_year = 0

selected_year = int(input("Enter the year of interest: "))
selected_country = input("Enter the country of interest: ")

# Trackers for selected year
year_total_life = 0
year_count = 0
selected_year_min_life = float('inf')
selected_year_max_life = float('-inf')
selected_year_min_country = ""
selected_year_max_country = ""

# Trackers for selected country
country_total_life = 0
country_count = 0
selected_country_min_life = float('inf')
selected_country_max_life = float('-inf')
selected_country_min_year = 0
selected_country_max_year = 0


with open("life-expectancy.csv") as file:
    next(file)  # Skip header

    for line in file:
        column = line.strip().split(',')

        # Get columns into variables
        country = column[0]
        code = column[1]
        year = int(column[2])
        life_exp = float(column[3])

        # Check for min and max
        if life_exp < min_life:
            min_life = life_exp
            min_country = country
            min_year = year

        if life_exp > max_life:
            max_life = life_exp
            max_country = country
            max_year = year

        #Selected year analysis
        if year == selected_year:
            # Calculate total life expectancy in selected year and count for average
            year_total_life += life_exp
            year_count += 1
            # Check for min and max for the selected year
            if life_exp < selected_year_min_life:
                selected_year_min_life = life_exp
                selected_year_min_country = country
            if life_exp > selected_year_max_life:
                selected_year_max_life = life_exp
                selected_year_max_country = country
        
        #Selected country analysis
        if country.lower() == selected_country.lower():
            # Calculate total life expectancy for the selected country
            country_total_life += life_exp
            country_count += 1
            # Check for min and max for the selected country
            if life_exp < selected_country_min_life:
                selected_country_min_life = life_exp
                selected_country_min_year = year
            if life_exp > selected_country_max_life:
                selected_country_max_life = life_exp
                selected_country_max_year = year

year_avg_life = year_total_life / year_count
country_avg_life = country_total_life / country_count

print(f"\nThe overall max life expectancy is: {max_life:.3f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}")

print(f"\nFor the year {selected_year}:")
print(f"The average life expectancy across all countries was {year_avg_life:.2f}")
print(f"The max life expectancy was in {selected_year_max_country} with {selected_year_max_life:.2f}")
print(f"The min life expectancy was in {selected_year_min_country} with {selected_year_min_life:.3f}")

print(f"\nFor the country of {selected_country}:")
if country_count > 0:
    print(f"The average life expectancy was {country_avg_life:.2f}")
    print(f"The max life expectancy was {selected_country_max_life:.2f} in {selected_country_max_year}")
    print(f"The min life expectancy was {selected_country_min_life:.2f} in {selected_country_min_year}")
else:
    print("No data available for that country.")