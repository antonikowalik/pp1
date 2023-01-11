arr = [[0,0,0],[0,0,0],[0,0,0]]
x = 0
y = 0

for i in arr:
    arr[x][y] = 1
    x += 1
    y += 1
    for j in i:
        print(j, end = " ")
    print()