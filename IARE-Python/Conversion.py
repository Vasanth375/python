import datetime

# Create a date object for today's date
today = datetime.date.today()

# Print today's date in different formats
print("Today's date in iso format:", today.isoformat())
print("Today's date in strftime format:", today.strftime("%A, %B %d, %Y"))

# Create a time object for the current time
now = datetime.datetime.now().time()

# Print the current time in different formats
print("Current time in strftime format:", now.strftime("%H:%M:%S"))
print("Current time in iso format:", now.isoformat())

# Convert a string representation of a date to a datetime object
date_str = "2020-05-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
print("Date from string:", date_obj)

# Convert a datetime object to a string representation of a date
date_obj = datetime.date(2020, 5, 1)
date_str = date_obj.strftime("%Y-%m-%d")
print("String representation of date:", date_str)

# Format a datetime object to a string
datetime_obj = datetime.datetime(2020, 5, 1, 12, 30, 45)
datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime string:", datetime_str)

# Parse a string representation of a datetime
datetime_str = "2020-05-01 12:30:45"
datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print("Datetime object from string:", datetime_obj)
