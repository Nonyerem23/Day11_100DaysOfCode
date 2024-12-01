print("How many seconds are in a year?")
print()
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_month = 31
months_in_year = 12
days_in_leap_year = 366
days_in_year = 365
# seconds in a year
seconds_in_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year
# seconds in a leap year
seconds_in_leap_year = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_leap_year
# ask user if it is a leap year
leap_year = input("Is it a leap year? ")
if leap_year == "yes" or leap_year == "Yes":
  print("There are", seconds_in_leap_year, "seconds in a leap year.")
else:
  print("There are", seconds_in_year, "seconds in a year.")

