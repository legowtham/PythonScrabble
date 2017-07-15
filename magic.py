#Determine if a word can be formed using the letters given to you.

def magic(str_1,str_2):
    lis_1, lis_2 = list(str_1), list(str_2)
    flag=1
    for letter in lis_2:
        loc = lis_1.index(letter) if letter in lis_1 else -1
        if loc == -1 :
            flag=0
            break
        else:
            del(lis_1[loc])
    if flag:
        return True
    else:
        return False