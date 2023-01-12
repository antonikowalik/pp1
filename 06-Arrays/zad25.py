def occurs(number, array):
    if array.__contains__(number):
        return True
    else:
        return False
    
number = int(input("Enter a number: "))
array = [15, 38, 7, 23, 14]

if occurs(number, array) == True:
    print(f"Number: {number}\nArray: {array}\nResult: number {number} appears to be in the array")
else:
    print(f"Number: {number}\nArray: {array}\nResult: number {number} does not appear to be in the array")