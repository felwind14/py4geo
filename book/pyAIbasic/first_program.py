import datetime

# Print "Hello, World!" to the console
print("Hello, World!")

# Get the current year and create a datetime object for Christmas
christmas = datetime.date(datetime.date.today().year, 12, 25)

# Get the current year and create a datetime object for April 18th
april_18 = datetime.date(datetime.date.today().year, 4, 18)

# Calculate the number of days between Christmas and April 18th
days_between = (april_18 - christmas).days

# Print the number of days between Christmas and April 18th
print("Number of days between Christmas and April 18:", days_between)
