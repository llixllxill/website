from django.db import models
from django.utils import timezone

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
    status_choices = [
        ('STATUS_AVAILABLE', 'Доступно'),
        ('STATUS_IN_USE', 'В использовании'),
        ('STATUS_MAINTENANCE', 'На обслуживании'),
        ('STATUS_BROKEN', 'Сломан'),
        ('STATUS_RESERVED', 'Зарезервировано'),
    ]
    weapon_name = models.CharField(max_length=100, verbose_name="Название оружия")
    weapon_type = models.CharField(max_length=50, verbose_name="Тип оружия")
    caliber = models.CharField(max_length=20, verbose_name="Калибр")
    status = models.CharField(max_length=50, verbose_name="Статус", choices=status_choices)
    
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
    
    # Выбор калибров
    CALIBER_CHOICES = [
        ('9x19', '9x19 мм (пистолетный)'),
        ('7.62x39', '7.62x39 мм (автоматный)'),
        ('5.45x39', '5.45x39 мм (автоматный)'),
        ('223REM', '.223 Remington (винтовочный)'),
        ('308WIN', '.308 Winchester (винтовочный)'),
        ('12GA', '12 калибр (дробовой)'),
        ('762x54', '7.62x54 мм (винтовочный)'),
        ('9x18', '9x18 мм (пистолетный)'),
        ('45ACP', '.45 ACP (пистолетный)'),
    ]
    
    # Выбор типов патронов
    TYPE_CHOICES = [
        ('PISTOL', 'Пистолетные патроны'),
        ('RIFLE', 'Винтовочные патроны'),
        ('SHOTGUN', 'Дробовые патроны'),
        ('SPORT', 'Спортивные патроны'),
        ('HUNTING', 'Охотничьи патроны'),
    ]
    
    # Основная информация
    name = models.CharField(
        max_length=200, 
        verbose_name="Тип патронов",
        choices=TYPE_CHOICES,
        default='PISTOL'
    )
    
    caliber = models.CharField(
        max_length=20, 
        verbose_name="Калибр",
        choices=CALIBER_CHOICES,
        default='9x19'
    )
    
    # Производитель
    manufacturer = models.CharField(
        max_length=100,
        verbose_name="Производитель",
        default='Тульский патронный завод'
    )
    
    # Цена
    price = models.IntegerField(
        verbose_name="Цена (руб)", 
        default=1500
    )
    
    # Количество в упаковке
    quantity = models.IntegerField(
        verbose_name="Количество в упаковке", 
        default=20
    )
    
    # Описание
    description = models.TextField(
        verbose_name="Описание", 
        blank=True,
        default='Качественные патроны для стрельбы'
    )
    
    # Дата добавления
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    
    class Meta:
        verbose_name = "Патрон"
        verbose_name_plural = "Патроны"
        ordering = ['caliber', 'price']
    
    def price_per_round(self):
        """Цена за один патрон"""
        if self.quantity > 0:
            return round(self.price / self.quantity, 2)
        return 0
    
    def get_caliber_display_name(self):
        """Красивое отображение калибра"""
        for code, name in self.CALIBER_CHOICES:
            if code == self.caliber:
                return name
        return self.caliber
    
    def get_name_display_name(self):
        """Красивое отображение типа патронов"""
        for code, name in self.TYPE_CHOICES:
            if code == self.name:
                return name
        return self.name
    
    def __str__(self):
        return f"{self.get_name_display_name()} - {self.get_caliber_display_name()}"