name = input("Введите имя: ")
family = input("Введите фамилию: ")
userName = f"{name} {family}"
print(f"Привет {userName}")
userAge = int(input("Введите ваш возраст: "))
if userAge<=0 or userAge>120:
    print("Недопустимое значение")
else:
    user = f"name: {userName}  age: {userAge}"
    print(user)