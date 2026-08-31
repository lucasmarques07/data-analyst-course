def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

print(factorial(10))

def totalSum(num):
    if num == 1:
        return 1
    else:
        return (num + totalSum(num - 1))
    
print(totalSum(10))