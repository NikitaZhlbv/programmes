def mult (st):
    number = ''
    numbers = []
    multiple = 1
    for k in range(len(st)):
        if st[k]!=',':
            number += st[k]
        elif st[k] == ' ':
            number += 0
        else:
            numbers.append(int(number))
            number = ''
    for k in numbers:
        multiple *= k
    return multiple
print(mult('15, 66, 25'))