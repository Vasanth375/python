try:
    import mysql.connector

    mydb=mysql.connector.connect(
        host="localhost",
        user="Vasanth",
        password="vasanth68"
    )
    mycursor=mydb.cursor()
    mycursor.execute("Show databases;")
    for i in mycursor:
        print(i)
    
except Exception as e :
    print(e)
