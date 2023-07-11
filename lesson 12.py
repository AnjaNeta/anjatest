class Passport:
    def __init__(self,name, surname,birthday, country,number):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.country = country
        self.number = number

    def passport_print(self):
            print("Name: ", self.name,
                 "Surname: ", self.surname,
                  "birthday: ", self.birthday,
                  "country: ",self.country,
                  "number: ", self.number)
detail = Passport ("Anna", "Dobrian", 11071994, "Russian Federation", 2345796858)
detail.passport_print()
class Foreignpassport(Passport):
    def  __init__(self, name, surname, birthday, country, number, visa):
        super().__init__(name, surname, birthday, country, number)
        self.visa = visa
    def visaprint(self):
        print("visa", self.visa)
details = Foreignpassport("Anna", "Dobrian", 11071994, "Russian Federation", 2345796858, "Germany")
details.visaprint()