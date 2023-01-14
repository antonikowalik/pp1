def f(dictionary,x,y):
    result = 0
    for array in dictionary.values():
        for value in array:
            if x <= value and y >= value:
                result += value
    return result

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))