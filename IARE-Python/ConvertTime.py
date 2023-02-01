import datetime

# Get the current datetime
now = datetime.datetime.now()

# Get the number of seconds since the epoch
seconds_since_epoch = (now - datetime.datetime(2003,11,28)).total_seconds()

# Calculate the number of days since the epoch
days_since_epoch = int(seconds_since_epoch / (60 * 60 * 24))

# Get the time of day in hours, minutes, and seconds
hours = now.hour
minutes = now.minute
seconds = now.second

# Print the results
print(seconds_since_epoch)
print("Number of days since the epoch:", days_since_epoch)
print("Current time of day:", hours, "hours,", minutes, "minutes,", seconds, "seconds")
