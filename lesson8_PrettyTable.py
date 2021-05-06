from prettytable import PrettyTable



table = PrettyTable(["name","ps"])
table.add_row(["audi",500])
table.add_row(["nissan",100])

print(table)