height=int(input("enter the height of the triangle"))
range_value=range(height)
for i in range(height,-1,-1):
    for j in range(height):
        if(i<=j):
            print("*",end=" ")
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print(" ")
