class Passport:
    def __init__(self,name, surname,birthday, country,number):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.country = country
        self.number = number

    def passport_print(self):
            print("Name: ", self.name)
            print("Surname: ", self.surname)
            print("birthday: ", self.birthday)
            print("country: ",self.country)
            print("number: ", self.number)
detail = Passport ("Anna", "Dobrian", 11071994, "Russian Federation", 2345796858)
detail.passport_print()
class ForeignPassport(Passport):
    def  __init__(self, name, surname, birthday, country, number, visa):
        super().passport_print
        super().__init__(name, surname, birthday, country, number)
        self.visa = visa
    def visaprint(self):
        print("visa", self.visa)
details = ForeignPassport("Anna", "Dobrian", 11071994, "Russian Federation", 2345796858, "Germany")
details.passport_print()