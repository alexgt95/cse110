from collections import defaultdict

data_by_year = {}

with open("life-expectancy.csv") as file:
    next(file)
    for line in file:
        country, _, year, life_exp = line.strip().split(",")
        year = int(year)
        life_exp = float(life_exp)

        record = {"country": country, "life_exp": life_exp}
        if year not in data_by_year:
            data_by_year[year] = []
        data_by_year[year].append(record)

min_record = {"life_exp": float('inf')}
max_record = {"life_exp": float('-inf')}

for records in data_by_year.values():
    for record in records:
        life_exp = record["life_exp"]
        if life_exp < min_record["life_exp"]:
            min_record = record
        if life_exp > max_record["life_exp"]:
            max_record = record

print(f"Max life expectancy: {max_record['life_exp']} in {max_record['country']} ({max_record['year']})")
print(f"Min life expectancy: {min_record['life_exp']} in {min_record['country']} ({min_record['year']})")

year_input = int(input("\nEnter the year of interest: "))
records = data_by_year.get(year_input)

if records:
    avg = sum(r["life_exp"] for r in records) / len(records)
    min_y = min(records, key=lambda x: x["life_exp"])
    max_y = max(records, key=lambda x: x["life_exp"])
    print(f"\nAverage life expectancy in {year_input}: {avg:.2f}")
    print(f"Min: {min_y['life_exp']} in {min_y['country']}")
    print(f"Max: {max_y['life_exp']} in {max_y['country']}")
else:
    print("No data for that year.")
