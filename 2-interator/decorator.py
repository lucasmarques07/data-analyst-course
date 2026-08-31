def my_decorator(function):
    def wrapper():
        print("Antes da execução!")
        function()
        print("Depois da execução!")
    return wrapper

def uppercaseDecorator(function):
    def wrapper():
        func = function()
        makeUppercase = func.upper()
        return makeUppercase
    return wrapper

def splitString(function):
    def wrapper():
        func = function()
        splitedString = func.split()
        return splitedString
    return wrapper