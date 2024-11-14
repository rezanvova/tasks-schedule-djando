from django.db import models

class Task(models.Model):
    class StatusForms(models.IntegerChoices):
        NEW = 0, 'Новая'
        IN_PROGRESS = 1, 'В процессе'
        COMPLETED = 2, 'Завершена'

    class PriorityForms(models.IntegerChoices):
        LOW = 0, 'Низкий'
        MEDIUM = 1, 'Средний'
        HIGH = 2, 'Высокий'

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.CharField(max_length=255, verbose_name="Описание")
    status = models.IntegerField(choices=StatusForms.choices, default=StatusForms.NEW, verbose_name="Статус")
    priority = models.IntegerField(choices=PriorityForms.choices, verbose_name="Приоритет")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.title