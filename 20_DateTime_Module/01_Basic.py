import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Current date only
today = datetime.date.today()
print("Today:", today)

# Formatting date
print("Formatted Date:", today.strftime("%d-%m-%Y"))

# Create a specific date
d = datetime.date(2025, 8, 20)
print("Custom Date:", d)

# Difference between dates
future = datetime.date(2025, 12, 31)
diff = future - today
print("Days left in 2025:", diff.days)
