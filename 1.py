def rsp(player1,player2):
    player1.lower()
    player2.lower()
    r = 'камень'
    s = 'ножницы'
    p = 'бумага'
    w1 = 'Выйграл первый'
    w2 = 'Выйграл второй'
    if player1 == player2:
        return 'Ничья'
    if player1 == s and player2 == p:
        return w1
    if player1 == p and player2 == r:
        return w1
    if player1 == r and player2 == s:
        return w1
    if player2 == r and player1 == s:
        return w2
    if player2 == p and player1 == r:
        return w2
    if player2 == s and player1 == p:
        return w2
while True:
    a = str(input('Первый игрок: '))
    b = str(input('Второй игрок: '))
    print(rsp(a,b))