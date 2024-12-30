def blackjack (cards):
    sum = 0
    a_count = 0
    for card in cards:
        if type(card) == int:
            sum += int(card)
        elif card != 'a':
            sum += 10
        elif card == 'a':
            a_count += 1
    if sum + (a_count * 11) > 21:
        sum = sum + (a_count * 11)
    else:
        sum = sum + (a_count * 1)
    if sum > 21:
        return True
    else:
        return False