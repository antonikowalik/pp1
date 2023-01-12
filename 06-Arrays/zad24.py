def unique(array):
    uni = []
    for i in array:
        if array.count(i) == 1:
            uni.append(i)
    print(uni)

unique([2,3,2,5,8,1,9,8])