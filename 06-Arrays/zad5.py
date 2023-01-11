import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]

print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"arr3: {arr3}")
print(f"arr4: {arr4}")
print(f"arr5: {arr5}")
print(f"arr6: {arr6}")
print(f"arr7: {arr7}")
print(f"arr8: {arr8}")
print(f"arr9: {arr9}")

# j. an array with values: 4,0,3
print(f"j. {[4,0,3]}")

# k. 50-element array filled with zeros
print(f"k. {[0 for i in range(0,50)]}")

# l. an array with integer values in the range of <1,30>
print(f"l. {[int(i) for i in range(1,31)]}")

# m. 20-element array filled with 0 or 1 randomly
print(f"m. {[random.randint(0,1) for i in range(0,20)]}")

# n. two dimensional array with five rows and two columns filled with False
twodarr = [[False, False],[False, False],[False, False],[False, False],[False, False]]
for row in twodarr:
    print(row)