from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from faker import Faker


def create_users():

    fake = Faker()
    
    # Fake data for student user
    code = str(fake.random_int(100000, 200000)) #username
    password = str(fake.random_int(40000000, 50000000)) #dni is the student password in this case

    # Fake data for Administrator User
    administrator_name = fake.name().replace(" ", "_") #username
    administrator_password = fake.word() #password

    #Data for Both
    email = fake.email()

    #print(f"Administrador: Nombre => {administrator_name} | Contraseña => {administrator_password}") See the data created

    for i in range(5):
        User.objects.create_user(code, email, password)
        code = str(fake.random_int(100000, 200000))
        password = str(fake.random_int(40000000, 50000000))
        email = fake.email()

    for j in range(5):
        User.objects.create_user(administrator_name, email, administrator_password)
        administrator_password = fake.word()
        administrator_name = fake.name().replace(" ", "_")
        email = fake.email()


#Assume we have a dictionary as session value
def validate_url(request, session_key, key_value, compare_to, redirect_to=""):
    if request.user.is_authenticated:
        if session_key in request.session:
            if request.session[session_key][key_value] == compare_to:
                return True
    return False

def get_random_number(initial, end):
    return str(Faker().random_int(initial, end))

def get_random_email():
    return Faker().email()