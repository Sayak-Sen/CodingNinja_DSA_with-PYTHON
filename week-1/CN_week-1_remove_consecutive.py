#Python program to remove consecutive strings without recurtion.
#aabcaa
s=input("enter your string : ")
def remove_consecutive(string):
    lst=list(s)
    l=len(lst)
    empt=[]
    j=0
    while j<l-1 :
        if lst[j]!=lst[j+1]:
            empt.append(lst[j])
        j+=1    
    empt.append(lst[l-1])
    new_String=''.join(empt)
    print(new_String)
#call the function
remove_consecutive(s)
