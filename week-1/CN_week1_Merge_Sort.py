def merge(s1,s2,lst):
    i=j=0
    k=i+j
    while k<len(lst)  :
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            lst[k]=s1[i]
            i+=1
        else:
            lst[k]=s2[j]
            j+=1 
        k=i+j             
    return lst    
  
def mergeSort(arr,l,r):
    r=len(arr)
    if r<2:
        return
    else:
        r=r//2
        sub1=arr[l:r]
        sub2=arr[r:]
        mergeSort(sub1,l,r)
        mergeSort(sub2,l,r)
        return merge(sub1,sub2,arr)
print("enter element by comma seperated one by one : ",end='')  
custList=[eval(x) for x in input().split(",")]
start=0
end=0  
#call function
print(mergeSort(custList,start,end))      
