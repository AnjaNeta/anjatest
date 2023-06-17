"""Два списка: автомобили и имена
Подобрать автомобиль владельцу на основании алфавитного порядка
 В случае, если списки отличаются по длине, выдать сообщение, что кому-то не достанется автомобиль"""

from itertools import zip_longest
car_brands = ["Audi", "Kia", "Volkswagen", "Hyundai", "Mercedez", "Tesla", "Toyota", "Nissan", "BMW", "Mitsubishi"]
customers = sorted(["Peter Krause", "Akira Takashi", "Kim Won Shik", "Alexander Schulz", "Martin Eden","Jeon Jungkook", "Aishariya Ray", "James Filz", "Maurice Ernst", "Lee Felix", "Min Yoongi"])
# dictionary = {i[0]:i[1] for i in zipped_list}
zipped_list = zip_longest(customers,car_brands,fillvalue="Got no car")
print(list(zipped_list))
