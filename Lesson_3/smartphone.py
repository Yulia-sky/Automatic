class Smartphone:

      def __init__(self, brand_phone, model_phone, number_phone):
            self.brand_phone = brand_phone
            self.model_phone = model_phone
            self.number_phone = number_phone

      def say_brand(self):
            print(self.brand_phone)

      def say_model(self):
            print(self.model_phone)

      def say_number(self):
            print(self.number_phone)