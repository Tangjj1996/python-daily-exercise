numbers = [1, 2, 2, 3, 4]
newNumbers = []
for number in numbers:
    if number in newNumbers:
        continue
    newNumbers.append(number)
print(newNumbers)
