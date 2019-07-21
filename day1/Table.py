number = int(input("enter the number"))
value = range(11)
print("table of {} : ".format(number))
for i in value:
    print("{} X {} = {}".format(number,i,number*i))
