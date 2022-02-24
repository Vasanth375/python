# importing required modules
from flask import Flask, request, render_template
import mysql.connector

# flask constructor takes name of current module 
app=Flask(__name__)

#Making a mysql connection
database1 = mysql.connector.connect(host = 'Vasanth68.mysql.pythonanywhere-services.com', user = 'Vasanth68', password = '#nimmala9876', database = 'Vasanth68$sample')
#creating cursor to execute sql statements
mycursor = database1.cursor()

@app.route("/", methods=['POST', 'GET'])
def mainpage():
    return render_template("main_page.html")

@app.route("/getresult", methods=['GET'])
def getresult():
    if request.method == "GET":
        name=request.form['names']
        mycursor.execute("select * from Names")
        result=mycursor.fetchall()
        return result
        # print(result)
 
@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        name=request.form['Name']
        mycursor.execute("insert into Names(name) values(%s)",(name,))
        database1.commit()

    return render_template("main_page.html")