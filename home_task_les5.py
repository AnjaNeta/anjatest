"""Два списка: автомобили и имена
Подобрать автомобиль владельцу на основании алфавитного порядка
 В случае, если списки отличаются по длине, выдать сообщение, что кому-то не достанется автомобиль"""

# from itertools import zip_longest
car_brands = ["Audi", "Kia", "Volkswagen", "Hyundai", "Mercedez", "Tesla", "Toyota", "Nissan", "BMW", "Mitsubishi"]
customers = sorted(["Wolfgang Mozart", "Peter Krause", "Akira Takashi", "Kim Won Shik", "Alexander Schulz", "Martin Eden","Jeon Jungkook", "Aishariya Ray", "James Filz", "Maurice Ernst", "Lee Felix", "Min Yoongi"])
no_car =[]
zipped_list = zip(car_brands,customers)
dictionary = {i[1]:i[0] for i in zipped_list}
# dictionary = {i[1]:i[0] for i in zipped_list if len(customers) != len(car_brands)}
for item in zipped_list:
    if len(customers) != len(car_brands):
        str(no_car.append(item))
print("A person who gets no car: ", no_car)
print("Customers who are getting a car: ", dictionary)


# zipped_list = zip_longest(customers,car_brands,fillvalue="Got no car")
# print(list(zipped_list))
