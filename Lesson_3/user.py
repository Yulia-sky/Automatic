class User:

    def _init_(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name


    def sayName(self):
        print("меня зовут ", self.first_name)

    def saySurname(self):
        print("моя фамилия ", self.last_name)

    def sayFullname(self):
        print(f'мое имя: {self.first_name} {self.last_name}')