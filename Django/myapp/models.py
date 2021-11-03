from django.db import models

# Create your models here.


class PileColor(models.Model):
    """Holds the Pile Color, like SALT & PEPPER, Cinnamon"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Myapp(models.Model):
    """ The Model to hold a list of myapp """
    name = models.CharField(max_length=250)
    pile_color = models.ForeignKey('PileColor', on_delete=models.CASCADE)
    stars = models.FloatField(default=1.0)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Stores Comments by users about the myapp """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    myapp = models.ForeignKey('Myapp', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)