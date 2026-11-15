class User:
    #зададим пустые значения для универсальности использования класса
    #как при регистрации, так и при логине
    def __init__(self, name="", lastname="", email="",
                 password=""):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

