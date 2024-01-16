#Item 1
"""
def lowercase_first (string1):
    lowerCase = ""
    for var in string1:
        if var.islower():
            lowerCase = string1
            print(lowerCase)
        else:
            print (lowerCase+string1)
        
print(lowercase_first('PyNaTive'))
"""
"""
string1 = "PyNaTive"
lc_list= [] 
uc_list= []
for var in string1:
    if var.islower():
        lc_list.append (var)
    else:
        uc_list.append (var)
ans = "".join(lc_list+uc_list)
print (ans)
"""
def lowercase_first (string1):
    lc_char = []
    uc_char = []
    for var in string1:
        if var.islower():
            lc_char.append (var)
        else:
            uc_char.append (var)
        
    print ("".join (lc_char+uc_char))
    
print(lowercase_first("PyNaTive"))


#Item 2


