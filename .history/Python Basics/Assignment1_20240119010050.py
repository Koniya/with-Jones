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

def string_counter(string):
    letters = 0 #container for letters. Initialized to 0.
    numbers = 0
    symbols = 0

    for counter in string: #traverse through the given string by passing it to counter
        if counter.isalpha(): #filtering which are the letters using the isalpha method
            letters += 1 #placing the found letters in the container "letters"
        if counter.isdigit():
            numbers +=1
        else:
            symbols += 1
    return letters, numbers, symbols # remember that tab space is important in Python

string = "P@#yn26at^&i5ve"
letters, numbers, symbols = string_counter(string)
print(f"The string {string} has {letters} letters, {numbers} numbers, and {symbols} symbols")
#the result has 12 symbols so this reads all of the characters as symbols
#The string P@#yn26at^&i5ve has 8 letters, 3 numbers, and 12 symbols

       
def string_counter(string):
    letters = 0 #container for letters. Initialized to 0.
    numbers = 0
    symbols = 0

    for counter in string: #traverse through the given string by passing it to counter
        if counter.isalpha(): #filtering which are the letters using the isalpha method
            letters += 1 #placing the found letters in the container "letters"
        if counter.isdigit():
            numbers +=1
        else:
            if letters == 0 or numbers == 0:
                symbols += 1
    return letters, numbers, symbols # remember that tab space is important in Python

string = "P@#yn26at^&i5ve"
letters, numbers, symbols = string_counter(string)
print(f"The string {string} has {letters} letters, {numbers} numbers, and {symbols} symbols")
    
#The string P@#yn26at^&i5ve has 8 letters, 3 numbers, and 5 symbols
    


