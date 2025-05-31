min_life = float('inf')
max_life = float('-inf')
min_country = ""
max_country = ""
min_year = 0
max_year = 0

data = []

# Read and parse data
with open("life-expectancy.csv") as file:
    next(file)
    for line in file:
        country, _, year, life_exp = line.strip().split(",")
        year = int(year)
        life_exp = float(life_exp)

        data.append((country, year, life_exp)) #appends a tuple to the data list

        # Track global min/max
        if life_exp < min_life:
            min_life = life_exp
            min_country = country
            min_year = year

        if life_exp > max_life:
            max_life = life_exp
            max_country = country
            max_year = year

# Display global results
print(f"\nThe overall max life expectancy is: {max_life} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

# Year-based analysis
year_input = int(input("\nEnter the year of interest: "))

year_life_exps = [entry for entry in data if entry[1] == year_input]

if year_life_exps:
    avg_life = sum([entry[2] for entry in year_life_exps]) / len(year_life_exps)
    max_entry = max(year_life_exps, key=lambda x: x[2])
    min_entry = min(year_life_exps, key=lambda x: x[2])

    print(f"\nFor the year {year_input}:")
    print(f"The average life expectancy across all countries was {avg_life:.2f}")
    print(f"The max life expectancy was in {max_entry[0]} with {max_entry[2]}")
    print(f"The min life expectancy was in {min_entry[0]} with {min_entry[2]}")
else:
    print("No data for that year.")
