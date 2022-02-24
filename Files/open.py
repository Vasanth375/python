#File Open and print what ever in that

# after opening a file we have to do any operation to go next step. Performing read operation
# just printing the whole content
# print(H.read(),end="\n")
with open('python\Files\hello.txt','r') as fp:
    lines=fp.read()
for i in lines:
    if i == ' ':
        print(end="\n")
    else:
        print(i,end="")

'''
paste file path in open function and put mode of operation  in open()
read() - is to read the file just we are reading only 
(based on mode of operation specified in open() we can do read() and write())
is to close the file {mandatory step}
'''