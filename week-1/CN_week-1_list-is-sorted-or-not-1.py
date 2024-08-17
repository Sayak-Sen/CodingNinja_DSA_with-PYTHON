# a list is sorted or not
#without using recurtion

def is_sortedList(lst):
    l=len(lst)
    for i in range(l-1):
        if lst[i]>lst[i+1]:
            return False
            break
    else:
        return True
    
myLst=list(map(eval,input("enter numbers :").split(",")))
print(is_sortedList(myLst))
    
    
    
