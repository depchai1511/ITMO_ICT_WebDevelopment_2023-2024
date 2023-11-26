from datetime import date
from project_first_app.models import Driver, Car, Ownership, DriverLicense
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project_truong.settings")
# Создание автовладельцев
driver1 = Driver.objects.create(username='username1', name='name1', birthday=date(1990, 1, 1))
driver2 = Driver.objects.create(username='username2', name='name2', birthday=date(1985, 5, 15))
driver3 = Driver.objects.create(username='username3', name='name3', birthday=date(1995, 8, 20))
driver4 = Driver.objects.create(username='username4', name='name4', birthday=date(1980, 3, 10))
driver5 = Driver.objects.create(username='username5', name='name5', birthday=date(1992, 11, 25))
driver6 = Driver.objects.create(username='username6', name='name6', birthday=date(1988, 7, 3))
driver7 = Driver.objects.create(username='username7', name='name7', birthday=date(1998, 4, 17))

# Создание автомобилей
car1 = Car.objects.create(id=1, model='Toyota', label='Camry', color='Blue')
car2 = Car.objects.create(id=2, model='Honda', label='Civic', color='Red')
car3 = Car.objects.create(id=3, model='Ford', label='Fusion', color='Silver')
car4 = Car.objects.create(id=4, model='Chevrolet', label='Malibu', color='Black')
car5 = Car.objects.create(id=5, model='Nissan', label='Altima', color='White')
car6 = Car.objects.create(id=6, model='Hyundai', label='Elantra', color='Green')

# Привязка автомобилей к владельцам
ownership1 = Ownership.objects.create(car=car1, driver=driver1, start_date=date(2022, 1, 1))
ownership2 = Ownership.objects.create(car=car2, driver=driver1, start_date=date(2022, 2, 1))
ownership3 = Ownership.objects.create(car=car3, driver=driver1, start_date=date(2022, 3, 1))

ownership4 = Ownership.objects.create(car=car4, driver=driver2, start_date=date(2022, 1, 1))
ownership5 = Ownership.objects.create(car=car5, driver=driver2, start_date=date(2022, 2, 1))

ownership6 = Ownership.objects.create(car=car6, driver=driver3, start_date=date(2022, 1, 1))

ownership7 = Ownership.objects.create(car=car1, driver=driver4, start_date=date(2022, 1, 1))
ownership8 = Ownership.objects.create(car=car3, driver=driver4, start_date=date(2022, 2, 1))

ownership9 = Ownership.objects.create(car=car2, driver=driver5, start_date=date(2022, 1, 1))
ownership10 = Ownership.objects.create(car=car4, driver=driver5, start_date=date(2022, 2, 1))
ownership11 = Ownership.objects.create(car=car6, driver=driver5, start_date=date(2022, 3, 1))

ownership12 = Ownership.objects.create(car=car5, driver=driver6, start_date=date(2022, 1, 1))
ownership13 = Ownership.objects.create(car=car1, driver=driver6, start_date=date(2022, 2, 1))

ownership14 = Ownership.objects.create(car=car3, driver=driver7, start_date=date(2022, 1, 1))
ownership15 = Ownership.objects.create(car=car6, driver=driver7, start_date=date(2022, 2, 1))

# Создание удостоверений владельцев
license1 = DriverLicense.objects.create(driver=driver1, type='A', creation_date=date(2022, 1, 1))
license2 = DriverLicense.objects.create(driver=driver2, type='B', creation_date=date(2022, 2, 1))
license3 = DriverLicense.objects.create(driver=driver3, type='C', creation_date=date(2022, 3, 1))
license4 = DriverLicense.objects.create(driver=driver4, type='A', creation_date=date(2022, 4, 1))
license5 = DriverLicense.objects.create(driver=driver5, type='B', creation_date=date(2022, 5, 1))
license6 = DriverLicense.objects.create(driver=driver6, type='C', creation_date=date(2022, 6, 1))
license7 = DriverLicense.objects.create(driver=driver7, type='A', creation_date=date(2022, 7, 1))
