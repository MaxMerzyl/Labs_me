class UserAccount():
    def __init__(self, password, username, email):
        self.__password = password
        self.username = username
        self.email = email
    @property
    def password(self):
        pass

    @password.setter
    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


P1=UserAccount("asdqwe", "Babldoom", "goll@mail.ru")

print(P1.check_password('asdqwe167'))
P1.set_password = '12345'
print(P1.check_password('12345'))