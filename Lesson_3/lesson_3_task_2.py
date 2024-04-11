from smartphone import Smartphone

phone1 = Smartphone('Apple', 'iphone_12', '+79644634896')
phone2 = Smartphone('Apple', 'iphone_15', '+79143696519')

print(phone1.say_brand (), phone1.say_model(), phone1.say_number())
print(phone2.say_brand(), phone2.say_model(), phone2.say_number())

catalog = [phone1, phone2]
for phone in catalog:
    print(phone.brand_phone, phone.model_phone, phone.brand_phone)