def toSum(num):
     return sum(j ** i for i, j in enumerate(num, 1))

numbers = [2, 5, 11, 1, 3]
print(toSum(numbers))