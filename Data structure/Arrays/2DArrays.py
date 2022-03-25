
# 2 dimensional arrays
list=[[], []]

for i in range(len(list)): # 2
    for j in range(5): # 5
        list[i].append(j+1) # appends each value to row

print(list)