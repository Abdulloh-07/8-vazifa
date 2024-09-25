from abc import ABC, abstractmethod
import math

class Shakl(ABC):
    @abstractmethod
    def maydon_hisobla(self):
        pass

    @abstractmethod
    def perimetr_hisobla(self):
        pass

class TogriTortburchak(Shakl):
    def __init__(self, uzunlik, kenglik):
        self.uzunlik = uzunlik
        self.kenglik = kenglik

    def maydon_hisobla(self):
        return self.uzunlik * self.kenglik

    def perimetr_hisobla(self):
        return 2 * (self.uzunlik + self.kenglik)

class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def maydon_hisobla(self):
        return math.pi * (self.radius ** 2)

    def perimetr_hisobla(self):
        return 2 * math.pi * self.radius

class Uchburchak(Shakl):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def maydon_hisobla(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetr_hisobla(self):
        return self.a + self.b + self.c

t_tortburchak = TogriTortburchak(5, 10)
doira = Doira(7)
uchburchak = Uchburchak(3, 4, 5)

print(t_tortburchak.maydon_hisobla())
print(t_tortburchak.perimetr_hisobla())

print(doira.maydon_hisobla())
print(doira.perimetr_hisobla())

print(uchburchak.maydon_hisobla())
print(uchburchak.perimetr_hisobla())