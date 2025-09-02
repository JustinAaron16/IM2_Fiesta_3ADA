
while True:
    row=int(input("Enter number of rows: "))
    col=int(input("Enter number of col: "))
    num=int(input("Enter number to find: "))
    if(row==0 or col==0):
        break;
    for x in range(1,row+1):
        for y in range(1,col+1):
            res=x*y
            if(num==res):
                print(f"[{res}]", end=" ")
            else:
                print(f"{res}", end=" ")
        print()
    