def camel(st):
    num = 0
    word = ''
    for letter in st:
        if  letter.isalpha():
            if num == 0:
                letter = letter.upper()
                word += letter
                num = 1
            elif num == 1:
                letter = letter.lower()
                word += letter
                num = 0
        else:
            word += letter
    return word
print(camel("cnwv.1 pu4vnwqr;c  23 l54qc3t53/weir"))