def useless (lst):
    temp = lst [0]
    for k in (0,len(lst)-1):
        if temp < lst[k]:
            temp = lst[k]
    temp = temp / len(lst)
    return temp
print(useless([216775,795310,54389,1000,7]))