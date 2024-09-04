#a numeric string is converted into integer number
def string_To_integer(str):
    length=len(str)
    if length==0:
        return 0
    else:
        start=str[0]
        start=int(start)
        num=start*10**(length-1)
        sub=str[1:]
        return num+string_To_integer(sub)
        
string=input("enter your string : ")
print(string_To_integer(string))    