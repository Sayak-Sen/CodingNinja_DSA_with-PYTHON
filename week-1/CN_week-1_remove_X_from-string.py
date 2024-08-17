#remove x from a string without recurtion
s=input("enter your string : ")
def removeX(string):
    lst=list(string)    #convert string to list
    flag='x' in lst
    if flag:
        noOf_Times=lst.count('x')
        for i in range(noOf_Times):
            lst.remove('x')
        newString=''.join(lst)
        print(newString)
    else:
        print(string)
              
#call the function       
removeX(s)    
    
