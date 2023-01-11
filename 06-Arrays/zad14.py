arr = [[True,False],[True,True],[False,False]]
x = 0

for i in arr:
    arr[x] = [not elem for elem in i]
    x += 1

print(arr)