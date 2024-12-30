def pluser(st):
    for k in range(1,len(st)-1):
        if st[k] != '+' and st[k+1] == '+' and st[k+1] == '+':
            return True
        else:
            return False
print(pluser('+32+3+4+2+3+4+'))