# find first index of a number using recurtion
def first_Index(arr,target):
     length=len(arr)
     if length==0:
         return -1
     if arr[0]==target:
         return 0
     else:
         sub=arr[1:]
         output=first_Index(sub,target)
         if output==-1:
             return -1
         else:
             return 1+output
lst=input("enter elements : ").split(',')
print("your list is ",lst)
target=input("what is your target element ? ")
print(first_Index(lst,target))

