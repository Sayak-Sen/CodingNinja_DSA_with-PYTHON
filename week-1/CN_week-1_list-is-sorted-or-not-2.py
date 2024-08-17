#list is sorted or not
# using recurtion
#method-1

def is_sorted(lst):
    l=len(lst)
    if l==1:
        return True
    else:
        if lst[0]>lst[1]:
            return False
        else:
            smallerList=lst[1:]
            return is_sorted(smallerList)
        
MyLst=list(map(eval,input("enter numbers : ").split(",")))
print(is_sorted(MyLst))
    
