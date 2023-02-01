def combine_lists(list1, list2):
    # Initialize an empty dictionary
    combined_dict = {}

    # Loop through both lists and add the elements as key-value pairs in the dictionary
    for i in range(len(list1)):
        combined_dict[list1[i]] = list2[i]
    
    return combined_dict

# Example usage:
keys = ["name", "age", "gender"]
values = ["John", 30, "Male"]
combined = combine_lists(keys, values)
print(combined)