from django.db import models
from django.contrib.auth.models import AbstractUser

class MainUser(AbstractUser):

    def __str__(self):
        return '%s %s' %(self.last_name, self.first_name)
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = '1. Barcha foydalanuvchilar'


class Fanlar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = '2. Barcha Fanlar'


class Kategoriya(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = '3. Kategoriyalar'
    


class DocumentFile(models.Model):
    file = models.FileField(upload_to='files/')
    category = models.ForeignKey(to='Kategoriya', on_delete=models.CASCADE)
    fan = models.ForeignKey(to='Fanlar', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name = 'Fayl'
        verbose_name_plural = '4. Barcha fayllar'