def bubblesort(array):
    print(f"array: {array}")
    print("bubblesorting...")
    n = len(array)
    while n > 1:
        for i in range(n - 1):
            if array[i] > array[i+1]:
                t = array[i]
                array[i] = array[i+1]
                array[i+1] = t
                del t
        n -= 1
    print(f"sorted: {array}")

bubblesort([5, 3, 9, 4, 8, 7, 500, 2, 4912, 59, 201, 58, 0, 5, 6])
bubblesort([6, 0, 402, 582, 592, 502, 1285, 30726, 5, 4, 3, 2, 1])
bubblesort([947, 56783209, 482010, 582018, 6830183740127, 698302])