def zestringuj(array):
    result = ""
    c = 0
    for i in array:
        c += 1
        result += str(i)
        if c < len(array):
            result += ","
    return result

print(zestringuj([5,4,3,2,6,5]))
