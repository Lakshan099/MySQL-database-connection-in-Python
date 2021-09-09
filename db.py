import pymysql

try:
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="python_test")
    myCursor = conn.cursor()

    ID = int(input("enter ID: "))
    LastName = (input("enter LastName: "))
    FristName = (input("enter FristName: "))
    Adress = (input("enter Adress: "))
    City = (input("enter City: "))
    


    myCursor.execute("INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES ('"+ID+"','"+LastName+"','"+FristName+"','"+Adress+"','"+City+"');")

    print("Data Insert ")



    conn.commit()
    conn.close()

except pymysql.connect.Error as error:
    print("Connection fail {}".format(error))


