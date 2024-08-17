#sum of list element
def sumArray(arr):
    if len(arr)==0:
        return 0
    else:
        x=arr.pop()
        output=x+sumArray(arr)
        return output
print(sumArray([1,2,3,4,4,3,2,1]))    
