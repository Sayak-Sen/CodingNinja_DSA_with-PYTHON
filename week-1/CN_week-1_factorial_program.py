# factorial
def fact(n):
    assert n>=0 and n==int(n),"sorry ! you are enter wrong input\n kindly pass the positive integer "
    #base case
    if n==0:
        return 1
    else:
        factorial_n=n*fact(n-1)
        return factorial_n
n=eval(input("enter a positive integer : "))
print(f"value of {n}! is {fact(n)}")
