array = [4,2,5,8,4,7,9,5]
result_even = []
result_odd = []
result = []

for i in array:
    if i % 2 == 0:
        result_even.append(i)
    else:
        result_odd.append(i)

for i in result_even:
    result.append(i)

for i in result_odd:
    result.append(i)

print(result)

