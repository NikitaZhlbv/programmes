def reverser(x, y = []):
    length = len(x)
    for k in range(length - 1, -1, -1):
        y.append(x[k])
    return y
print(reverser([1, 2, 3, 4, 5]))