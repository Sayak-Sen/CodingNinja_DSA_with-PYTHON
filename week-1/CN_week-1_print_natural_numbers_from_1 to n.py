# print natural numbers from 1 to n
def numberGenerator(n):
    assert n>=0 and n==int(n) ,"enter correct input"
    if n==0:
        return
    else:
        numberGenerator(n-1)
        print(n)

#call the function
n=eval(input("enter a positive number : " ))
numberGenerator(n)
