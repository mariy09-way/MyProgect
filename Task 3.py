class Person:
 
    def __init__(self, name, age):
        self.name = name    
        self.age = age       

pers = Person(input("Введите имя: "),int(input("Введите возраст: ")))