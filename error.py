mbers = [10, 20, 30, 40, 50]
total = 0
for i in range(len(numbers) + 1):   # Bug: should be range(len(numbers))
    total += numbers[i]
print("Sum:", total)
print("Average:", total / len(numbers))