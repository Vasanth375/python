'''
According to the truth table any or all inputs 
off output will be off

100 - 4
110 - 6
100 - 4
'''
# print(4&6)
a=4
b=6
print(a&b)
bin_a, bin_b=bin(a), bin(b)
bin_a, bin_b=list(bin_a), list(bin_b)
for i in range(9):
    pass