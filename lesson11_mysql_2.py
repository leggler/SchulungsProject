import mysql.connector



######################## OPEN DB ##################################
mydb = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n",
    database="sql11404167"
)


print(mydb) #wenn was ausgegeben wird, können wir uns zur DB verbinden

mycursor = mydb.cursor()


#löscht den table "leg" (wenn er existiert, um fehler zu vermeiden)
sql = "DROP TABLE IF EXISTS leg"
mycursor.execute(sql)

#"name" = variablenname, VARCHAR(255) = 255 zeichen lange zeichenfolge
#CREATE muss/kann nur einmal ausgeführt werden
mycursor.execute("CREATE TABLE leg(name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES") #SQL Code
#for tables in mycursor:
#    print(tables)

#selbst erhöhende ID hinzufügen und als primary key setzen
sql = "ALTER TABLE leg ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
mycursor.execute(sql)

sql = "INSERT INTO leg (name, address) VALUES (%s, %s)"
#VARIANTE WENN NUR EIN DATENSATZ HINZUFÜGEN
 #values = ("Markus", "Straße 332")
 #mycursor.execute(sql, values)
#VARIANTE MIT EINER LISTE VON DATEN ÜBERGEBEN
values = [("Markus", "Straße 332"), ("peter", "gasse2")]
mycursor.executemany(sql, values) #für listen
#muss nach der transaktion ausgeführt werden, damit die änderung auch gespeichert wird
mydb.commit()

print(mycursor.rowcount, "...anzahl an datensätzen")
print("ID: ", mycursor.lastrowid)

sql = "SELECT * FROM leg"
myresults = mycursor.execute(sql)
for result in myresults:
    print(result.address)



############################### CLOSE DB ##########################
mydb.close()
