def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a/b 

if __name__ =="__main__":
    print("Простой колькулятор")
    print("Сложение 50 + 23", add(50,23))
    print("Вычитание 100 - 38", subtract(100,38))
    print("Умножение 34 * 45 =", multiply (34, 45) )  
    print("Деление 15 / 3", (15, 3))
