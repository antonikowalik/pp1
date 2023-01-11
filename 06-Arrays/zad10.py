import random

arr = [random.randint(0,150) for j in range(0,10)]
even = 0
odd = 0
i = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print(arr)
print(f"even: {even}")
print(f"odd: {odd}")