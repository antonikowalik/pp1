def f(array2D):
    result = []
    for i in range(len(array2D[0])):
        col_sum = 0
        for row in array2D:
            col_sum += row[i]
        result.append(col_sum)
    print(result)

        



f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ])