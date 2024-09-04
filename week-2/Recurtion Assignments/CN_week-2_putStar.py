def star(string):
    if len(string)==1:
        return string
    if string[0]==string[1]:
        string=list(string)
        string.insert(1,"*")
        string="".join(string)
        new=string[2:]
        return string[0]+string[1]+star(new)
    else:
        sub=string[1:]
        result=string[0]+star(sub)
        return result
        
string=input("enter your string : ")
print(star(string))