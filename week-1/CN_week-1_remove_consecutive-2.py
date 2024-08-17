# remove consecutive duplicate from a string with recurtion
s=input("enter your string : ")
def consecutive_remover(string):
    lst=list(string)
    if len(string)==0:
        return 
    else:
        lst[0]==lst[1]:
        lst.remove(lst[0])
        newString=''.join(lst)
        return consecutive_remover(newString)
    
        
    print(lst)
    print(smallerList)
consecutive_remover(s)
