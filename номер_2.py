def first_last(letter,st):
    first = None
    last = None
    letter_place = []
    st = st.lower()
    for i in range (len(st)):
        if st[i] == letter:
            letter_place.append(i)
    if letter_place != []:
        first = letter_place[0]
        last = letter_place[-1]
    return first,last
print(first_last('a','AbCdEfGhI'))