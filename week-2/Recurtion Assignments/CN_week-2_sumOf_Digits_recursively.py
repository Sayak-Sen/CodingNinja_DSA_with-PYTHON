def sum_of_digits(number):
    if number==0:
        return 0
    else:
        q=number//10
        r=number%10
        return r+sum_of_digits(q)
n=int(input("enter the number : "))    
print("sum of digits = ",sum_of_digits(n))    