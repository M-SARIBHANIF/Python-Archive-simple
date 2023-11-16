row1 = ["11","12","13"]
row2 = ["21","22","23"]
row3 = ["31","32","33"]
map = [ row1,row2,row3 ]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure: ")
row = int(position[0])
colum = int(position[1])
map[colum-1][row-1] = "x"
print(f"{row1}\n{row2}\n{row3}")