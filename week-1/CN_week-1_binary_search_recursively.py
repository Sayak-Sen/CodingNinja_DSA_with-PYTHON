from array import *
lst=list(map(int,input("enter elements : ").split(",")))
data=array('i',lst)
target=int(input("what is the target element to search : "))
#binary search function
def binary_search(data,target,low,high):
    '''return position if target is found else return -1'''
    if low>high:
        return -1
    else:
        mid=(high+low)//2
        if data[mid]==target:
            return mid
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)
#call the function
print(binary_search(data,target,0,len(data)-1))         