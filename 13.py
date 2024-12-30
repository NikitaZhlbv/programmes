def unspacer (st):
    word = ''
    for k in st:
        if k != ' ':
            word += ''
        else:
           break
    for k in range(len(st)-1):
        if st[k] == st [k+1] and st[k] == ' ':
            word += ''
        else:
            word += st[k]
    for k in range(len(st)-1, -1, -1 ):
        if st[k] != ' ':
            break
        else:
            word += ''
    return word
print(f"#{unspacer('   Happy   New Year  !')}#")