def silencer(st):
    word = ''
    m = ''
    m_found = False
    for k in range(len(st)-1, -1, -1):
        if st[k] == '!' and not m_found:
            m = '!'
            m_found = True
        elif st[k] == '?' and not m_found:
            m = '?'
            m_found = True
        elif st[k] != '!' and st[k] != '?':
            word += st[k]
    word = word[::-1] + m
    return word
print(silencer('Last Chtistmas!!!!!!!!'))