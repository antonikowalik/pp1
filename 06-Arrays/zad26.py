def secondLargest(array):
    array.remove(max(array))
    print(max(array))

secondLargest([5,91,1,9,6,1,99])