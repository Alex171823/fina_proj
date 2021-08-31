from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    pages = models.IntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(blank=True)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    pubdate = models.DateField(blank=True)

    def __str__(self):
        return f"{self.name} {self.pages} {self.price} {self.rating} {self.author} {self.publisher} {self.pubdate}"
