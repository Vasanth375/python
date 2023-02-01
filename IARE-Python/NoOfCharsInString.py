string = "aaaaaaaaaabbbbbbbbbbbbbbcccccccccccccc"
count = 0
dictCount = {}

for i in string:
    dictCount[i] = string.count(i)
print(dictCount)