def LetterChanges(str1): 

    # code goes here 
    vowels = ['a', 'e', 'i', 'o', 'u']
    str2 = ''
    for i in range(len(str1)):
        x = int(ord(str1[i]))
        if x < 97 or x > 122:
            str2 += chr(x)
        if x >= 97 and x <= 122:
            temp = chr(ord(str1[i]) + 1)
            if temp in vowels:
                temp = temp.upper()
            str2 += temp
    return str2
    
    
# keep this function call here  
print LetterChanges(raw_input())