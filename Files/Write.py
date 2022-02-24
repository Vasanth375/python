# Before going to write anything just open the file
try:
    with open('python\Files\Hello.txt','r+') as fp:
        print(fp.read())
        fp.write('Vasanth\n')
        fp.write('19124-cm-068\n')
except Exception as exp:
    print(exp)
