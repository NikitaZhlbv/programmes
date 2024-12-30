def coiner(coins):
    if (len(coins)) % 3 == 0:
        return True
    else:
        return False
print(coiner([23, 23, 23, 23, 22]))