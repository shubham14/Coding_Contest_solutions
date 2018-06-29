def LetterCapitalize(str): 
    str1 = ''
    # code goes here 
    n = len(str)
    for i,ele in enumerate(str):
        if i==0:
            str1 += str[i].upper()
        if ele == ' ' and i != n-1:
            str1 += str[i+1].upper()
        elif ele != ' ' and i != n-1:
            str1 += str[i+1]    
    return str1

# keep this function call here  
print LetterCapitalize(raw_input())