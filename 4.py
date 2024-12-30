def sum (st):
    word = ''
    number = ''
    sum = 0
    for k in range(0,len(st)):
        if not st[k].isdigit() and not st[k+1].isdigit():
            word += ''
        else:
            word += st[k]
    for k in word:
        if k.isdigit():
            number += k
        else:
            number += '_'
    num = ''
    numbers = []
    for k in number:
        if k != '_':
            num += k
        else:
            numbers.append(num)
            num = ''
    numbers.append(num)
    for k in numbers:
        sum += int(k)
    return sum
print(sum('bwer1y68b16rtu61myto61ceyr61n7rn6bev1r6u4'))