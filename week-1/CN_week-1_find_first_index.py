# find first index of a number using itteration
def first_Index(arr,target):
     length=len(arr)
     for i in range(length):
         if arr[i]==target:
             return i
     else:
         message="target is not found"
         return message
lst=input("enter elements : ").split(',')
print("your list is ",lst)
target=input("what is your target element ? ")
print(first_Index(lst,target))

               
    
    
    
