class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

preson = Person("Anass", 21)

print(f"My name is {preson.name} and I am {preson.age} years old.")
