#fernet (Symmetric encryption)
try:
    #importing the fernet class from 
    from cryptography.fernet import Fernet

    #plain text of secret message
    plainText=b"N Vasanth 19124-cm-068"
    print("Original secret message :",plainText)

    #generating the random key 
    key=Fernet.generate_key()
    with open("mykey.key",'wb') as mykey:
        mykey.write(key)

    print("Key is:",key)
    #creating instance for fernet class to encode and decode the plain text
    f=Fernet(key)

    #encrypting the plain text using Fernet instance
    cipherText=f.encrypt(plainText)

    #printing the cipher text
    print("Encrypted secret message:",cipherText)

    #decrypting the encrypted code
    DecryptText=f.decrypt(cipherText)

    #printing the original text
    print("Decrypted secret message:",DecryptText)

except Exception as E:
    print(E)
finally:
    pass

