array = [39,458,3891,4920,4821,59999]
user_number = float(input("Enter a number: "))
greater = 0

for i in array:
    if i > user_number:
        greater += 1

print(greater)