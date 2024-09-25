import random
import string


class KodGenerator:
    def __init__(self):
        self.__kod = None

    def kod_yaratish(self, uzunlik):
        if uzunlik <= 0:
            return "Uzunlik musbat son bo'lsin!"

        belgi_toplami = string.ascii_letters + string.digits
        self.__kod = ''.join(random.choice(belgi_toplami) for _ in range(uzunlik))

    def kod_olish(self, uzunlik):
        if self.__kod is None:
            return "Kod hali yaratilmagan."

        if len(self.__kod) == uzunlik:
            return self.__kod
        else:
            return "Access Denied"


generator = KodGenerator()
generator.kod_yaratish(8)
print(generator.kod_olish(8))
print(generator.kod_olish(6))