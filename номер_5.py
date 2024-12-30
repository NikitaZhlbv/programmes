def shortener(st):
    deleter = False
    word = ''
    for k in st:
        if k == '(':
            deleter = True
        elif k == ')':
            deleter = False
        elif not deleter:
            word += k
    return word.strip()
print(shortener('важная информация(не очень)'))