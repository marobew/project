from django.db import models

class Board(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateField('date published')
    body = models.TextField()
    
    def __str__(self):
        return self.title 
    
    def summary(self):
        return self.body[:300]