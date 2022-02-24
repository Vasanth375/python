# from cryptography.fernet import Fernet

# # reading key from mykey.key file
# with open("mykey.key","rb") as mykey:
#     key=mykey.read()

# # creating fernet object
# f=Fernet(key)

# print("Key",key)

# # Reading encrypted data to decrypt
# with open("C:\\Users\\VASANTH\\enc_download.jpg","rb") as decryp:
#     decrypttext=decryp.read()

# cipher=f.decrypt(decrypttext)

# with open("C:\\Users\\VASANTH\\dec_download.jpg","wb") as ciphe:
#     ciphe.write(cipher)

# print("Decryption Process completed...")

from flask import Flask, render_template

app=Flask(__name__)
@app.route("/",methods=["GET"])
def main():
    return "Hello CMD"