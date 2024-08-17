# print natural numbers from n to 1
def numberGenerator(n):
    assert n>=0 and n==int(n) ,"enter correct input"
    if n==0:
        return
    else:
        print(n)
        numberGenerator(n-1)

#call the function
n=eval(input("enter a positive number : " ))
numberGenerator(n)
