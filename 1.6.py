def all_eq(lst): 
    max_len = 0
    temp = []
    for string in lst:
        if len(string) > max_len:
            max_len = len(string)
    for string in lst:
        add = 0
        if len(string) < max_len:
            add = max_len - len(string)
        string = string + ('_' * add)
        temp.append (string)
    return temp
print (all_eq(['1','987654321' ,'123456789','2']))