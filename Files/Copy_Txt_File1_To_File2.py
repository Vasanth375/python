with open('python\Files\Hello.txt','r+') as fp, open('python\Files\File2.txt','r+') as fp2:
    for i in fp:
        fp2.write(i)
    print(fp.read())
    print(fp2.read())