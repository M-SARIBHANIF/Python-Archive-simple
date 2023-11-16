#without "len" function
string = input("Enter A Sample String: ")
count = 0;
for i in string:
    count+=1
print(count)

#with len function
string = input("Enter A Sample String: ")
print(len(string))
#or
print(len(input("Enter String: ")))
