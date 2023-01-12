def median(array):
    x = len(array)
    if x % 2 == 0:
        a = array[x//2-1]
        b = array[x//2]
        result = (a + b) / 2
        return result
    else:
        return array[x//2]

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))