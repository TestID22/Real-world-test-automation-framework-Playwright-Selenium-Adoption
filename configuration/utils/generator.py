import random

from configuration.data import Person
from faker import Faker

faker_en = Faker("en_US")
Faker.seed()

def generated_person():
    yield Person(
        first_name = faker_en.first_name(),
        last_name=faker_en.last_name(),
        email = faker_en.email(),
        age = random.randint(10, 89),
        salary= random.randint(8_500, 39_000),
        mobile_number = faker_en.numerify(text='##########'), #text = creates number with digits only
        department= faker_en.job()[:20],  #WebTables: Department field has restricted length
        current_address = faker_en.address(),
        permanent_address = faker_en.address()
    )
