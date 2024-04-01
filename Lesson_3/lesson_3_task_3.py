from adress import Address
from mailing import Mailing

my_mailing = Mailing('Chita', 'Moscow', '1234', '1111')
my_address = Address('123456', 'Chita', 'Chaikovskogo', '39')

my_mailing.say_track()
my_mailing.say_to_address()
my_mailing.say_from_address()
my_mailing.say_cost()

my_address.say_index()
my_address.say_city()
my_address.say_house()
my_address.say_apartment()