def first_Index(arr,target):
     length=len(arr)
     idx=-1
     for i in range(length):
         if arr[i]==target:
             idx=i
     return idx
lst=input("enter elements : ").split(',')
print("your list is ",lst)
target=input("what is your target element ? ")
print(first_Index(lst,target))
