from decorator import my_decorator, uppercaseDecorator, splitString

@my_decorator 
def my_function():
    print("Dentro da função!")

my_function()

@uppercaseDecorator
def text():
    return "Hello World"

print(text())

@splitString
def example():
    return "Aprendendo python e criando decorators"

print(example())