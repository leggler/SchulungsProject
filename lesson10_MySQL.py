import mysql.connector



######################## OPEN DB ##################################
#freemysqlhosting = gratis anbieter für mysql dbs
mydb = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n"
)
# mit https://www.phpmyadmin.co/ kann man sich auch mit der db
# verbinden, und sieht was dort los ist


####################### WORK WITH DB ##############################
print(mydb) #wenn was ausgegeben wird, können wir uns zur DB verbinden

#mit dem cursor habe ich die möglichkeit SQL-code direkt an die DB zu schicken
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE dbnamen")
mycursor.execute("SHOW DATABASES") #SQL Code

for x in mycursor:
    print(x)

############################### CLOSE DB ##########################
mydb.close()


############################### DANACH NORMALER PY CODE ###########




