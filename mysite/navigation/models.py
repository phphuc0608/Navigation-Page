from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=10000)
    link = models.URLField()
    
    class Meta:
        db_table = 'pages'
        
    def __str__(self):
        return self.title
     
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username
