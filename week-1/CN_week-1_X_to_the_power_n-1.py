# program for x to the power n where x may be integer or floating point number
def power(x,n):
    assert n>=0 ,"enter correct inputs"
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
    
x,n=list(map(eval,input("enter x,n : ").split(",")))
    
print(power(x,n))


