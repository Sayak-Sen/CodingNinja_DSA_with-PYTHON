def checkAB(s):
    if len(s)==0:
        return True
    if s[0]=="a":
        if len(s[1:])>1 and s[1:3]=="bb":
            return checkAB(s[3:])
        else:
            return checkAB(s[1:])
    else:
        return False

string=input("enter your string :")
if checkAB(string)==True:
    print("true")
else:
    print("false")