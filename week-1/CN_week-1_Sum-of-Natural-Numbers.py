# sum of 'n' natural numbers
def sumOf_N_Natural(n):
    assert n>0  ,"write correct input i.e. n>0"
    if n==1:
        return 1
    else:
        return n+sumOf_N_Natural(n-1)
n=int(input("How many natural numbers ? : "))
result=sumOf_N_Natural(n)
print("sum of %i natural numbers is %d"%(n,result))    
