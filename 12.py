def doubler (st):
    for k in range(len(st)-1):
        if st[k] == st [k+1]:
            return True
    return False
print(doubler('successful'))
print(doubler('pen'))