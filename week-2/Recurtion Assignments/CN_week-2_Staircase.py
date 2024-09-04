def step(n):

    if n==1:

        return 1

    elif n==2:

        return 2

    elif n==3:

        return 4

    else:

        way=step(n-1)+step(n-2)+step(n-3)

        

        return way
        
steps=int(input("total number of steps :"))
print(step(steps))    