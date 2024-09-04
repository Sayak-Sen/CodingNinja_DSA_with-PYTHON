#check a string is polyndrome or not recursevely
def isPolindrome(strvalue):
    length=len(strvalue)
    if length<2:
        return True 
    elif strvalue[0]==strvalue[-1]:
        substr=strvalue[1:length-1]
        return isPolindrome(substr)
    else:
        return False
        
           
given_value=input("enter your string : ")   
print(isPolindrome(given_value))

    
