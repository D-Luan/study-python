class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self.age = age

    def greet(self):
        print(f"Hello, {self._name}")

p = Person("Smith", 30)

p.greet()