"""
Class: CSE110 Section: A7 Student Name: Alejandro Garcia Trujillo
Project Windchill Calculator
"""

def calculate_wind_chill(temp_f, wind_speed):
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(temp_c):
    return temp_c * (9 / 5) + 32

def main():
    temp = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if scale == 'C':
        temp_f = celsius_to_fahrenheit(temp)
    else:
        temp_f = temp

    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temp_f, wind_speed)
        print(f"At temperature {temp_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

main()
