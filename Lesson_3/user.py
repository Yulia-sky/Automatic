class User:

    def _init_(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name


    def say_name(self):
        print("Меня зовут ", self.first_name)

    def say_surname(self):
        print("Моя фамилия ", self.last_name)

    def say_fullname(self):
        print('Мое имя: {self.first_name} {self.last_name}')