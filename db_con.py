import pymysql

try:
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="python_test")
    myCursor = conn.cursor()

    myCursor.execute(" CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));")
    myCursor.execute("INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (002,'Sandanayaka','Lakshan','Bandaragama','Wevita');")
    print("Data Insert ")

    myCursor.execute("SELECT * FROM persons;")
    print(myCursor.fetchall(), end="\n")


    conn.commit()
    conn.close()

except pymysql.connect.Error as error:
    print("Connection fail {}".format(error))


