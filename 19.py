def masser(*args):
    res = []
    temp = 0
    for num in args:
        for k in range(0, len(res)):
            temp += res[k]
        temp += num
        res.append(temp)
        temp = 0
    return res
print(masser(30,56,60,41))