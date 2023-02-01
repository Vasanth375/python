# Initialize the birthday string
birthday = "22-01-1997"

# Use split method to separate the string into a list of elements
birthday_list = birthday.split("-")

# Use the join method to concatenate the list into a string
birthday_str = "/".join(birthday_list)

# Create a dictionary to store the birthday information
birthday_dict = {
    "day": birthday_list[0],
    "month": birthday_list[1],
    "year": birthday_list[2]
}

# Access the birthday information from the dictionary
day = birthday_dict["day"]
month = birthday_dict["month"]
year = birthday_dict["year"]

# Print the birthday information
print("Birthday:", birthday_str)
print("Day:", day)
print("Month:", month)
print("Year:", year)
