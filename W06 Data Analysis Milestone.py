min_life = float('inf')
max_life = float('-inf')

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

        if life_exp > max_life:
            max_life = life_exp

print(f"The minimum life expectancy in the dataset is: {min_life}")
print(f"The maximum life expectancy in the dataset is: {max_life}")
