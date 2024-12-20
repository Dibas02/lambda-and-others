num1 = [1, 2, 3,]
num2 = [4, 5, 6]

result = map(lambda x, y: x+y, num1, num2)
print(list(result))



def square(n):
    return n**2

l1 = (2, 3, 4, 5, 6)

squared = map(square, l1)

print(list(squared))