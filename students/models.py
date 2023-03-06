from django.db import models


class Flow(models.Model):
    title = models.CharField(
        max_length=60,
        verbose_name='Заголовок'
    )

    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'

    def __str__(self):
        return self.title
        


class Direction(models.Model):
    title = models.CharField(
        max_length=60,
        verbose_name='Заголовок'
    )

    flow = models.ForeignKey(
        'Flow',
        on_delete=models.CASCADE,
        related_name='directions',
        verbose_name='Поток'
    )

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.title
    

class Student(models.Model):
    first_name = models.CharField(
        max_length=60,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=60,
        verbose_name='Фамилия'
    )

    age = models.PositiveIntegerField(
        verbose_name='Возраст'
    )

    direction = models.ForeignKey(
        'Direction',
        on_delete=models.CASCADE,
        related_name='directions',
        verbose_name='Направление'
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


