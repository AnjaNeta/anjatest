"""сделать класс User с параметрами login, password, mode: user / admin """
class User:
    def __init__(self,login,password, mode = 'user'):
        self.login = login
        self.password = password
        self.mode = mode
    def __str__(self):
        return f"login: {self.login}, password: {self.password}, mode :{self.mode}"

list_of_users = []

user_1 = User("anjadobrian", 1234567, "user")
user_2 = User("yongimin", 5678904,"admin")
user_3 = User("taehyungkim",9768427,"user")
list_of_users.append(user_1)
list_of_users.append(user_2)
list_of_users.append(user_3)
print(list_of_users[0])
print(list_of_users[1])
print(list_of_users[2])
