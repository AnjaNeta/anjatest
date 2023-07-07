"""сделать класс User с параметрами login, password, mode: user / admin """
class User:
    def __init__(self,login,password, mode = 'user'):
        self.login = login
        self.password = password
        self.mode = mode
    def login_1(self):
        print("login:", self.login, "password:", self.password, "mode:", self.mode)
log = User("anjadobrian", 1234567, "user")
log.login_1()