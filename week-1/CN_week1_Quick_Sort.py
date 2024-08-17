#pivot function
def pivot(lst,low,high):
    high=len(lst)
    pvt=lst[low]
    pvt_index=low
    swap_index=low
    i=low+1
    while i<high:
        if lst[i]<pvt:
            swap_index=swap_index+1
            lst[i],lst[swap_index]=lst[swap_index],lst[i]
        i=i+1
     
    lst[pvt_index],lst[swap_index]=lst[swap_index],lst[pvt_index]
    return swap_index

#quick sort with index that is help to sort 
def quicksort_helper(lst,left,right):
    if left>right:
        return 
    else:
        idx=pivot(lst,left,right)
        quicksort_helper(lst,left,idx-1)
        quicksort_helper(lst,idx+1,right)
    return lst

#quick sort where passing only lists
def quicksort(lst):
    left=0
    right=len(lst)-1
    return quicksort_helper(lst,left,right)


print("enter element by comma seperated one by one : ",end='')  
custList=[eval(x) for x in input().split(",")]  
#call function    
print(quicksort(custList))  