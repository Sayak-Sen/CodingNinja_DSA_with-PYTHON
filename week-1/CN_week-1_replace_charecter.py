#replace the charecter 'c' by the another charecter 'x'
#using recurtion
s=input("enter your string : ")
target=input("terget string : ")
replace=input("replacing charecter : ")
#replace charecter function
def replace_string(s,a,b): #where a is replaced by b
    if len(s)==0:
        return ''
    else:
        if s[0]==a:
            return b+replace_string(s[1:],a,b)
        else:
            return s[0]+replace_string(s[1:],a,b)
#call the function
print(replace_string(s,target,replace))        
