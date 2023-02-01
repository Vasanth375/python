def shortest_list(d):
    # Find the key with the shortest value list
    shortest_key = min(d, key=lambda x: len(d[x]))
    
    # Return the shortest value list
    return d[shortest_key]

# Example usage:
d = {
    "list1": [1, 2, 3],
    "list2": [1, 2, 3, 4, 5],
    "list3": [1,2],
    "list4": [1,2,3,4,4,5,6,7,8,9]
}
result = shortest_list(d)
print(result)
