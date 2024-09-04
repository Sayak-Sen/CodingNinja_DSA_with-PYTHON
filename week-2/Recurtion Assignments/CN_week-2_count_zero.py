def count_zeros(number):
    r=number%10  
    q=number//10 
    if q==0 and r!=0:
        return 0
    if q==0 and r==0:
        return 1
    else:
        result=count_zeros(q)
        if r==0:
            count=1
        else:
            count=0    
        return count+result
n=int(input("enter the number : "))    
print("total zeros in the number is = ",count_zeros(n))    
        
