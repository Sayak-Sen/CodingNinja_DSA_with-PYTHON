def merge(s1,s2,lst):
    #new=[]
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


def mergesort(lst):
    l=len(lst)
    if l<2:
        return 
    else:
        mid=l//2
        sub1=lst[0:mid]
        sub2=lst[mid:]
        mergesort(sub1)
        mergesort(sub2)
        return merge(sub1,sub2,lst)
        

print("enter element by comma seperated one by one : ",end='')  
custList=[eval(x) for x in input().split(",")]  
#call function
print(mergesort(custList))      



