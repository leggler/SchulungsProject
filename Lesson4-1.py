#csvs lesen (wie eine text datei, und manuell splitten) und in advanced data types speichern


with open("text4.csv", 'r') as csv_file:
    csv_data = csv_file.read().splitlines()


    for row in csv_data:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[2]} and {row_data[1]} years old") #Index für eine Liste: Immer in [eckiger Klammer]!

        