names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:])
print(names)

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2Dlists

matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#matrix[0] [1] = 20
#print(matrix[0] [1])

for row in matrix:
    for item in row:
        print(item)


numbers = [3, 6, 2, 8, 4, 10]
numbers.append(20)
print(numbers)
numbers.insert(0, 20)
print(numbers)
numbers.remove(8)
print(numbers)
numbers.clear()
print(numbers)
numbers = [3, 6, 2, 8, 4, 10]
numbers.pop()
print(numbers)
print(numbers.index(3))
print(50 in numbers)
print(numbers.count(3))
numbers.sort()
numbers.reverse()
print(numbers)
#copy

number = [2, 2, 5, 7, 5, 9]
uniques = []
for number in number:
    if number not in uniques:
        uniques.append(number)
print(uniques)