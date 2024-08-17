# find last index of an element in iterative way

arr=[str(x) for x in input("enter comma seperated list " ).split(',')]
targetValue=input("enter what element you are found : ")
def lastindex(arr,target):
    length=len(arr)
    count=-1
    for i in range(length):
        if arr[i]==target:
            count=i
    return count    
        
            
print(lastindex(arr,targetValue) )   
        
