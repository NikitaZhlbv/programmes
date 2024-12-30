def mid (numbers):
    if len(numbers)%2 == 0:
        return 'Требуется нечетное количество чисел'
    for k in range(0, len(numbers)):
        for n in range(0, len(numbers)-1):
            if numbers[n] > numbers[n+1]:
                numbers[n],numbers[n+1] = numbers[n+1],numbers[n]
    return numbers[len(numbers)//2]
print(mid([1817,3833,5409,7796,9964]))