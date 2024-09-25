class Kitob:
    def __init__(self, nom, muallif, janr, narx):
        self.__nom = nom
        self.__muallif = muallif
        self.__janr = janr
        self.__narx = narx

    @property
    def nom(self):
        return self.__nom

    @property
    def muallif(self):
        return self.__muallif

    @property
    def janr(self):
        return self.__janr

    @property
    def narx(self):
        return self.__narx

    def __str__(self):
        return f"{self.__nom} - {self.__muallif} ({self.__janr}) - {self.__narx} so'm"


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def kitob_ochirish(self, nom):
        self.kitoblar = [kitob for kitob in self.kitoblar if kitob.nom != nom]

    def kitob_qidirish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nom.lower() == nom.lower():
                return kitob
        return None

    def barcha_kitoblar(self):
        return self.kitoblar


class Foydalanuvchi:
    def __init__(self, ism, parol):
        self.ism = ism
        self.parol = parol

    def __str__(self):
        return self.ism


class KutubxonaBoshqaruvTizimi:
    def __init__(self):
        self.kutubxona = Kutubxona()
        self.foydalanuvchilar = []

    def foydalanuvchi_royxatdan_otish(self, ism, parol):
        yangi_foydalanuvchi = Foydalanuvchi(ism, parol)
        self.foydalanuvchilar.append(yangi_foydalanuvchi)

    def foydalanuvchi_tizimga_kirish(self, ism, parol):
        for foydalanuvchi in self.foydalanuvchilar:
            if foydalanuvchi.ism == ism and foydalanuvchi.parol == parol:
                return foydalanuvchi
        return None

    def kitoblar_bilan_ishlash(self):
        while True:
            print("\n1. Kitob qo'shish")
            print("2. Kitob o'chirish")
            print("3. Kitob qidirish")
            print("4. Barcha kitoblarni ko'rish")
            print("5. Chiqish")
            tanlov = input("Tanlovingizni kiriting: ")

            if tanlov == '1':
                nom = input("Kitob nomi: ")
                muallif = input("Muallif: ")
                janr = input("Janr: ")
                narx = float(input("Narxi: "))
                yangi_kitob = Kitob(nom, muallif, janr, narx)
                self.kutubxona.kitob_qoshish(yangi_kitob)
                print(f"{nom} kutubxonaga qo'shildi.")

            elif tanlov == '2':
                nom = input("O'chirish uchun kitob nomini kiriting: ")
                self.kutubxona.kitob_ochirish(nom)
                print(f"{nom} kutubxonadan o'chirildi.")

            elif tanlov == '3':
                nom = input("Qidirilayotgan kitob nomini kiriting: ")
                kitob = self.kutubxona.kitob_qidirish(nom)
                if kitob:
                    print(kitob)
                else:
                    print("Kitob topilmadi.")

            elif tanlov == '4':
                for kitob in self.kutubxona.barcha_kitoblar():
                    print(kitob)

            elif tanlov == '5':
                break
            else:
                print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")


tizim = KutubxonaBoshqaruvTizimi()

while True:
    print("\n1. Ro'yxatdan o'tish")
    print("2. Tizimga kirish")
    print("3. Chiqish")
    tanlov = input("Tanlovingizni kiriting: ")

    if tanlov == '1':
        ism = input("Ism: ")
        parol = input("Parol: ")
        tizim.foydalanuvchi_royxatdan_otish(ism, parol)
        print(f"{ism} ro'yxatdan o'tdi.")

    elif tanlov == '2':
        ism = input("Ism: ")
        parol = input("Parol: ")
        foydalanuvchi = tizim.foydalanuvchi_tizimga_kirish(ism, parol)
        if foydalanuvchi:
            print(f"{ism} tizimga kirdi.")
            tizim.kitoblar_bilan_ishlash()
        else:
            print("Noto'g'ri ism yoki parol.")

    elif tanlov == '3':
        break
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")