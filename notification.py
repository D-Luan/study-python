from abc import ABC, abstractmethod

class Notifiable(ABC):
    @abstractmethod
    def notify(self):
        pass

class User(Notifiable):
    def __init__(self, name):
        self.name = name

    def notify(self):
        print(f"Notifying {self.name} by email")

class Admin(User):
    def notify(self):
        print(f"Notifying Admin {self.name} with priority")

def send_alert(obj):
    obj.notify()

u = User("John")
a = Admin("Mary")

send_alert(u)
send_alert(a)