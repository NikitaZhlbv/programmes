def passer(st):
    sum = 0
    special_symbol = False
    capital_symbol = False
    digit = False
    lower_symbol = False
    length = False
    for k in st:
        if not k.isalpha() and not k.isdigit():
            special_symbol = True
        if k.isupper():
            capital_symbol = True
        if k.islower():
            lower_symbol = True
        if k.isdigit():
            digit = True
    if len(st) >= 16:
        length = True
    sum = special_symbol + capital_symbol + digit + lower_symbol + length
    return f"Ваш пароль получает оценку: {sum}/5"
print(passer('p4(b2He7N67&&C%O'))