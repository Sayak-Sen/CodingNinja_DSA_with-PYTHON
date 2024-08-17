# list is sorted or not
# using recurtion
# method--2
#start from any index method

def is_sorted(arr,si):
    l=len(arr)
    if si==l-1:
        return True
    if arr[si]>arr[si+1]:
        return False
    else:
        si+=1
        return is_sorted(arr,si)
    
lst=list(map(eval,input("enter numbers : ").split(",")))
startIndex=int(input("enter index value :"))
print(is_sorted(lst,startIndex))
        
        
    
