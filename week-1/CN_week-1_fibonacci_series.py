# Fibonacci series
# series starts from 1

def fibonacci_sequence(n):
    assert n>=1 and n==int(n) ,"enter correct input"
    if n==1 or n==2:
        return 1
    else:
        a=fibonacci_sequence(n-1)
        b=fibonacci_sequence(n-2)
        output=a+b
        return output
    
n=eval(input("enter positive integer : "))
print(f"{n} th fibonacci number is {fibonacci_sequence(n)}")
