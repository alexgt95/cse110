my_list = [3,65,23,4,5,6,7,8,9,10,11,12,13,14,15]
largest = 0

for value in my_list:

    if value > largest:

        largest = value

print(f"The largest is {largest}")

print("------------------------------------------------------")

smallest = 13

for value in my_list:

    if value < smallest:

        smallest = value

print(f"The smallest is {smallest}")