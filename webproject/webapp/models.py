from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    """Модель клиента"""
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Email")
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Target(models.Model):
    """Модель цели"""
    name = models.CharField(max_length=100, verbose_name="Название цели")
    target_type = models.CharField(max_length=50, verbose_name="Тип цели")
    difficulty_level = models.IntegerField(verbose_name="Уровень сложности")
    
    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"
    
    def __str__(self):
        return self.name


class Service(models.Model):
    """Модель услуги"""
    service_name = models.CharField(max_length=100, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    duration_minute = models.IntegerField(verbose_name="Продолжительность (минуты)")
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
    def __str__(self):
        return self.service_name


class Weapon(models.Model):
    """Модель оружия"""
    weapon_name = models.CharField(max_length=100, verbose_name="Название оружия")
    weapon_type = models.CharField(max_length=50, verbose_name="Тип оружия")
    caliber = models.CharField(max_length=20, verbose_name="Калибр")
    status = models.CharField(max_length=50, verbose_name="Статус")
    
    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"
    
    def __str__(self):
        return self.weapon_name


class Staff(models.Model):
    """Модель сотрудника"""
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    hire_date = models.DateField(verbose_name="Дата найма")
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    """Модель бронирования"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Сотрудник")
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, verbose_name="Оружие")
    target = models.ForeignKey(Target, on_delete=models.CASCADE, verbose_name="Цель")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    booking_date = models.DateField(verbose_name="Дата бронирования")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
    
    def __str__(self):
        return f"Бронирование {self.client} - {self.booking_date}"


class AmmoSales(models.Model):
    """Модель продаж боеприпасов"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name="Бронирование")
    caliber = models.CharField(max_length=20, verbose_name="Калибр")
    quantity = models.IntegerField(verbose_name="Количество")
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена за единицу")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая сумма")
    sale_date = models.DateField(verbose_name="Дата продажи")
    
    class Meta:
        verbose_name = "Продажа боеприпасов"
        verbose_name_plural = "Продажи боеприпасов"
    
    def __str__(self):
        return f"Боеприпасы {self.caliber} - {self.sale_date}"