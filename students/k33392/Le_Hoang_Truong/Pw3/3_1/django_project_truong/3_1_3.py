from project_first_app.models import Driver, Car, Ownership, DriverLicense
from django.db.models import Max, Count

# 1. Вывод даты выдачи самого старшего водительского удостоверения
oldest_license_date = DriverLicense.objects.all().aggregate(oldest_date=Max('creation_date'))
print(f"Дата выдачи самого старшего водительского удостоверения: {oldest_license_date['oldest_date']}")

# 2. Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей
latest_ownership_date = Ownership.objects.filter(car__model__isnull=False).aggregate(latest_date=Max('start_date'))
print(f"Самая поздняя дата владения машиной: {latest_ownership_date['latest_date']}")

# 3. Выведите количество машин для каждого водителя
drivers_with_car_count = Driver.objects.annotate(car_count=Count('cars')).values('name', 'car_count')
for driver in drivers_with_car_count:
    print(f"{driver['name']} - Количество машин: {driver['car_count']}")

# 4. Подсчитайте количество машин каждой марки
car_brand_count = Car.objects.values('model').annotate(car_count=Count('model'))
for brand in car_brand_count:
    print(f"{brand['model']} - Количество машин: {brand['car_count']}")

# 5. Отсортируйте всех автовладельцев по дате выдачи удостоверения
sorted_drivers = DriverLicense.objects.distinct().order_by('creation_date')
for driver in sorted_drivers:
    print(f"{driver.driver.name} - Дата выдачи удостоверения: {driver.creation_date}")
