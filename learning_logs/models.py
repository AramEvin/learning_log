from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=100) # Для заголовка тем 
    date_added = models.DateTimeField(auto_now_add=True) # Для показа даты и времени создания темы (Topic )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

"""
ForeignKey настраивает связь с главной сущностью. 
Первый параметр указывает, с какой моделью будет создаваться связь - в данном случае это модель Company. 
Второй параметр - on_delete задает опцию удаления 
объекта текущей модели при удалении связанного объекта главной модели
"""

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'


    def __str__(self):
        return f"{self.description[:50]}..."




