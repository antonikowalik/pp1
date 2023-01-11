arr = [12, 6, 4, 9, 10]

def star(n):
    y = ""
    for i in range(n):
        y = y + "*"
    return y

for i in arr:
    print(f"{i}: {star(i)}")
