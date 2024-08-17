#The tower of hanoi puzzel
n=int(input("number of disk : "))
def move(n,a,b,c):   #a,b,c are poles
    if n==0:
        pass
    elif n==1:
        print("move disk %i from %s to %s"%(n,a,c))
    else:
        move(n-1,a,c,b)
        print("move disk %i from %s to %s"%(n,a,c))
        move(n-1,b,a,c)
        #print("move disk %i from %s to %s"%(n,a,c))
            
#call the function
move(n,'A','B','C')
