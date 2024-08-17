from array import *
lst=list(map(int,input("enter elements : ").split(",")))
data=array('i',lst)
target=int(input("what is the target element to search : "))
#binary search function
def binary_search(data,target,low,high):
    '''return position if target is found else return -1'''
    while low<=high:
        mid=(high+low)//2
        if data[mid]==target:
            return mid
        elif target<data[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        return -1        
#call the function
print(binary_search(data,target,0,len(data)-1))            
