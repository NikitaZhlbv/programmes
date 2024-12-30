def top3(st):
    st = st.lower()
    letters = {}
    for letter in st:
        if letter == ' ':
            letter = ''
    for letter in st:
        letters[letter] = 0
    for letter in st:
        letters[letter] += 1
    temp = {}
    for i in range(3):
        max_num = -1
        big_key = None
        for number in letters:
            if int(letters[number]) > int(max_num):
                max_num = letters[number]
                big_key = number
        temp[big_key] = max_num
        letters[big_key] = 0
    top = ''
    for key,value in temp.items():
        top += f"{key} - {value}\n"
    text = "Топ 3 символа в данной строке:\n" + top
    return text
print(top3('jnzvj;aeitnjlvfsfjs24897mdsbawjodensdb15awer81cw25'))