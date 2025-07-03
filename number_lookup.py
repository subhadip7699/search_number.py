number = (1, 4, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = int(input("Enter your number: "))
while i < len(number):
    if number[i] == x:
        print("Found number at index", i)
        break  
    i += 1
else:
    print("Number not found")
