def lst_sort(lst):
    for i in range(len(lst)):
        for i in range (len(lst)-1):
            if lst[i]>lst[i+1]:
                lst [i],lst[i+1]=lst[i+1],lst[i]
    return lst

print(lst_sort([228,1488,-7,1000,100500]))