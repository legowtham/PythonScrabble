#Handle wildcard characters. "?" can represent any of the 26 characters.
def magic(str_1,str_2):
    strlen, lis_1, lis_2 = len(str_2), list(str_1), list(str_2)
    flag=1
    for letters in lis_1:
        if letters != '?':
            pos = lis_2.index(letters) if letters in lis_2 else -1
            if pos == -1:
                flag=0
                break
            del(lis_2[pos])
            strlen -=1

    qlen = str_1.count('?')
    strlen = strlen-qlen
    if strlen>0:
        flag=0
    if flag:
        return True
    else:
        return False