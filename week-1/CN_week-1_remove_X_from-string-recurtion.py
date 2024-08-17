#remove x from a string with recurtion
s=input("enter your string : ")
def removeX(string):
    lst=list(string)    #convert string to list
    if 'x' not in lst:
        return string
    else:
        lst.remove('x')
        newString=''.join(lst)
        return removeX(newString)

#call the function
    
print(removeX(s))
