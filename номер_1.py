def search_substr(subst,st):
    subst = subst.lower()
    st = st.lower()
    if subst in st:
        return ('Есть контакт!')
    else:
        return ('Мимо!')

search_substr('12345','AbCdEfGhI')
search_substr('bebebe','12345')