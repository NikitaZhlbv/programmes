def encoder (st):
    st.lower()
    word = ''
    for k in st:
        print(k)
        if k == "е":
            word += "3"
        elif k == "а":
            word += "4"
        else:
            word += k
    return word
print(encoder('С наступающим Новым Годом!'))