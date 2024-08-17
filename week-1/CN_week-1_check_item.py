#check the item is in the list or not
def check(arr,item):
    length=len(arr)
    if length==0:
        return False
    if arr[0]==item:
        return True
    else:
        sub=arr[1:]
        return check(sub,item)
lst=input("enter elements : ").split(',')
print("your list is ",lst)
target=input("what is your target element ? ")
print(check(lst,target))    
