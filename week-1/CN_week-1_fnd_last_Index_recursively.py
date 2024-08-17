#Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array.
#Return -1 if it is not present in the array.

#Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.

#You should start traversing your array from 0, not from (N - 1).

#Do this recursively. Indexing in the array starts from 0.

arr=[str(x) for x in input("enter comma seperated list " ).split(',')]
targetValue=input("enter what element you are found : ")

def lastindex(arr,target):
    if target not in arr:
        return -1
    else:
        fi=arr.index(target)
        sub=arr[fi+1:]
        return fi+1+lastindex(sub,target)
         
print(lastindex(arr,targetValue) )   
        
        
