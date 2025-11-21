# A dictionary storing the number of days in each month
days_in_month = { 
    1: 31,
    2:28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for the name of a month
month = int(input("Enter the number of the month (1-12): "))
# Check if the month is on the dictionary
if month in days_in_month:
    print(f"this month has {days_in_month[month]} days") 
else:
    print("invalid month number")






