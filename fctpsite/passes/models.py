from django.db import models

# Create your models here.

class Users(models.Model):
    fam = models.CharField(max_length = 100,
                            verbose_name = "Фамилия")
    name = models.CharField(max_length = 50,
                            verbose_name = "Имя")
    otc = models.CharField(max_length = 100,
                            verbose_name = "Отчество")
    phone = models.IntegerField(unique = True,
                                verbose_name = "Телефон")
    email = models.EmailField (max_length = 50,
                             unique = True,
                             verbose_name = "email")

class Pereval_added(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'

    STATUS = [
        (NEW, 'Новое'),
        (PENDING, 'В работе'),
        (ACCEPTED, 'Принято'),
        (REJECTED, 'Не принято'),
    ]
    status = models.CharField(max_length=2,
                              choices=STATUS,
                              default=NEW)
    beautyTitle = models.TextField(help_text = "Введите название перевала",
                                   verbose_name = "Название перевала")
    title = models.TextField(help_text = "Введите описание перевала",
                             verbose_name = "Описание",
                             blank=True)
    other_titles = models.TextField(help_text = "Введите другое название перевала",
                             verbose_name = "Другое название перевала",
                             blank=True)
    connect = models.TextField(help_text = "Введите что соединяет перевал",
                             verbose_name = "Что соединяет перевал",
                             blank=True)
    add_time = models.DateTimeField(auto_now_add = True)
    level = models.CharField(max_length=10,
                            help_text = "Введите категорию сложности перевала",
                             verbose_name = "Категория сложности перевала")
    coords = models.OneToOneField('Coords', on_delete=models.CASCADE)
    users = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.beautyTitle

class Coords(models.Model):
    latitude = models.FloatField(help_text = "Введите широту перевала",
                             verbose_name = "Широта перевала")
    longitude = models.FloatField(help_text = "Введите долготу перевала",
                             verbose_name = "Долгота перевала")
    height = models.IntegerField(help_text = "Введите высоту перевала",
                             verbose_name = "Высота перевала")

class Pereval_images(models.Model):
    img = models.ImageField(upload_to = "photos/%Y/%m/%d/",
                            default = None,
                            blank = True,
                            null = True,
                            verbose_name = "Фото перевала")
    pereval = models.ForeignKey('Pereval_added', on_delete=models.CASCADE)





