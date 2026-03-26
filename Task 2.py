while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(f'Сумма чисел: {a+b}')
    print(f"Разность чисел: {a-b}")
    print(f"Произведение чисел: {a*b}")
    n = input("Нажмите Y или y для завершения программы: ")
    if n=='Y' or n=='y':
        break

try:
    number = int(input("Введите число: "))
    if number > 5:
        raise Exception("Результат будет меньше 1")
    print("Введенное число:", 5/number)
except ZeroDivisionError as ex:
    print("Деление на ноль: ", ex)
except BaseException as ex:
    print("Преобразование прошло неудачно: ", ex)
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")