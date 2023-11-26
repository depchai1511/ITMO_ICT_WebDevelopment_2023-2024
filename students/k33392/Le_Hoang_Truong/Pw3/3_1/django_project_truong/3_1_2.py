# queries.py

from datetime import date
import random
from project_first_app.models import Driver, Car, Ownership, DriverLicense


# 2. Query: Tìm tất cả các mô hình "Toyota"
toyota_cars = Car.objects.filter(model='Toyota')
for car in toyota_cars:
    print(car)

# 3. Query: Tìm tất cả các tài xế với tên "Олег"
oleg_drivers = Driver.objects.filter(name='Олег')
for driver in oleg_drivers:
    print(driver)

# 4. Query: Lấy một chủ xe ngẫu nhiên và hiển thị ID và bằng lái của chủ xe đó
random_owner = random.choice(Driver.objects.all())
print(f"Owner ID: {random_owner.id}")
driver_license = DriverLicense.objects.get(driver=random_owner)
print(driver_license.type)

# 5. Query: Tìm tất cả các chủ sở hữu xe màu đỏ
red_car_owners = Driver.objects.filter(cars__color='Red')
for owner in red_car_owners:
    print(owner)

# 6. Query: Tìm tất cả các chủ xe có năm bắt đầu sở hữu từ năm 2010
owners_2010 = Driver.objects.filter(cars__ownership__start_date__year=2010)
for owner in owners_2010:
    print(owner)
