from smartphone import Smatrphone

phone1 = Smatrphone('Apple', 'iphone_12', '+79644634896')
phone2 = Smatrphone('Apple', 'ipone_15', '+79143696519')

print(phone1.sayBrand (), phone1.sayModel(), phone1.sayNumber())
print(phone2.sayBrand(), phone2.sayModel(), phone2.sayNumber())

catalog = [phone1, phone2]