from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Курс')
    preview = models.ImageField(upload_to='image/', **NULLABLE, verbose_name='Превью')
    description = models.TextField(verbose_name='Содержание курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Урок')
    crss = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True, verbose_name='Урок курса')
    description = models.TextField(verbose_name='Содержание урока')
    preview = models.ImageField(upload_to='image/', **NULLABLE, verbose_name='Превью')
    video = models.URLField(**NULLABLE, verbose_name='Видео')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


# Добавил модель платежа. Мигировал, с консоли заполнил БД.
class Payment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    course_link = models.ForeignKey('courses.Course', on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    lesson_link = models.ForeignKey('courses.Lesson', on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')
    summa = models.SmallIntegerField(verbose_name='Сумма')
    payment_form = models.CharField(max_length=50, verbose_name='Форма оплаты')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'

    def __str__(self):
        return f'{self.user} {self.course_link if self.course_link else self.lesson_link}'

