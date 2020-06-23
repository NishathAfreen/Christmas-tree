x=int(input())
#first part
for i in range(0,x+1):
     for j in range(x-i,0,-1):
            print(" ",end=" ")
     for j in range(0,(i*2)+1):
            print("*",end=" ")
     for j in range(x-i,0,-1):
                    print(" ",end=" ")
     print()
#second part
for i in range(0,x-1):
     for j in range(x1-i,0,-1):
            print(" ",end=" ")
     for j in range(0,(i*2)+3):
            print("*",end=" ")
     for j in range(x1-i,0,-1):
                    print(" ",end=" ")
     print()
#third part
for i in range(0,x-2):
     for j in range(x1-i,0,-1):
            print(" ",end=" ")
     for j in range(0,(i*2)+3):
            print("*",end=" ")
     for j in range(x1-i,0,-1):
                    print(" ",end=" ")
     print()
#fourth part
for i in range(0,x-1):
     for j in range(0,x):
            print(" ",end=" ")
     for j in range(1):
            print("*",end=" ")
     for j in range(0,x):
                    print(" ",end=" ")
     print()

