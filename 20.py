def stonks(numbers):
    a = numbers[0]
    for k in range(1, len(numbers)):
        if a > numbers[k]:
            return 'Не возраставет'
        else:
            a = numbers[k]
    return 'Возрастает'
print(stonks([1, 2, 3, 4, 5]))
print(stonks([2, 3, 4, 5, 1]))
print(stonks([5, 2, 3, 4, 1]))
print(stonks([-10,53,5800,61311]))