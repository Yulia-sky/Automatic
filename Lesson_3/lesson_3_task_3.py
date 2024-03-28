from adress import Address
from mailing import Mailing

my_mailing = Mailing('Chita', 'Moscow', '1234', '1111')
my_address = Address('123456', 'Chita', 'Chaikovskogo', '39')

my_mailing.sayTrack()
my_mailing.sayTo_address()
my_mailing.sayFrom_address()
my_mailing.sayCost()

my_address.sayIndex()
my_address.sayCity()
my_address.sayHouse()
my_address.sayApartment()