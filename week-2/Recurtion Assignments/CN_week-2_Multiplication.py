#program for multiplication
def multiplication(m,n):
    if n==1:
        return m
    else:
        return m+multiplication(m,n-1)
    
n=int(input("enter one operand :"))
m=int(input("enter another operand :"))
print(multiplication(m,n))