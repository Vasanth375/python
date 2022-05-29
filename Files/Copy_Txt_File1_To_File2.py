#Method 1
# with open('Files\Hello.txt','r') as fp, open('Files\File2txt','w') as fp2:
#     for i in fp:
#         fp2.write(i)

# method 2
file1 = open('Files\Hello.txt','r') 
file2 = open('Files\File2txt', 'w')
for i in file1:
    file2.write(i)