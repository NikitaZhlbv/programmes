def time24_to_12 (time):
    hours = ''
    minutes = ''
    for k in range (0,2):
        hours += time[k]
    for k in range(3, 5):
        minutes += time[k]
    hours = int(hours)
    if hours > 12:
        hours = hours - 12
    else:
        hours = hours
    res = str(hours) + ':' + str(minutes)
    return res
def time12_to_24 (time, pm):
    hours = ''
    minutes = ''
    for k in range (0,2):
        hours += time[k]
    for k in range(3, 5):
        minutes += time[k]
    if pm:
        hours = int(hours) +12
    res = str(hours) + ':' + str(minutes)
    return res
def timer (st, type, pm = None):
    if type == '12':
        res = time12_to_24(st, pm)
    elif type == '24':
        res = time24_to_12(st)
    return res
print(timer('13:43', '24', pm = False))