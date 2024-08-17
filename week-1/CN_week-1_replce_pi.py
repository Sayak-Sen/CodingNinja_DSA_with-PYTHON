s=input('enter your string : ')
def replace_PI(s):
    if len(s)==1 or len(s)==0:
        return s
    else:
        #assuming first two elements are 'p' and 'i'
        if s[0]=='p' and s[1]=='i':
            return '3.14'+replace_PI(s[2:])
        else:
            return s[0]+replace_PI(s[1:])
        
#call the function
print(replace_PI(s))