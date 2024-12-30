def sizer (data):
    full_size = []
    for k in data:
        size = 1
        for n in k:
            size *= n
        full_size.append(size)
    res = 0
    for k in full_size:
        res += k
    return res
print(sizer([[2,4,6],[1,3,5],[7,7,7]]))