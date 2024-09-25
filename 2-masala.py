from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def harakatlanish(self):
        pass

class Mashina(Transport):
    def harakatlanish(self):
        return "Mashina g'ildiraklar yordamida harakatlanadi."

class Velosiped(Transport):
    def harakatlanish(self):
        return "Velosiped pedallar yordamida harakatlanadi."

class Samolyot(Transport):
    def harakatlanish(self):
        return "Samolyot uchib harakatlanadi."

mashina = Mashina()
velosiped = Velosiped()
samolyot = Samolyot()

print(mashina.harakatlanish())
print(velosiped.harakatlanish())
print(samolyot.harakatlanish())