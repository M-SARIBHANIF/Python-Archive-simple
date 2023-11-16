from prettytable import PrettyTable
new_table = PrettyTable()
new_table.add_column("Pokimon name",["pikachu","Squirtal","CharMander"])
new_table.add_column("Pokimon Type",["Electric","Water","Flame"])
new_table.align = "l"
print(new_table)

