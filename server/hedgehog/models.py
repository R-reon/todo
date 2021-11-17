from django.db import models
from django.utils import timezone

# Create your models here.


class PileColor(models.Model):
    """Holds the Pile Color, like SALT & PEPPER, Cinnamon"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class HedgeHog(models.Model):
    """ The Model to hold a list of Hedgehogs """
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='myapp', null=True)
    pile_color = models.ForeignKey('PileColor', on_delete=models.CASCADE)
    stars = models.FloatField(default=1.0)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Stores Comments by users about the HedgeHog """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    hedgehog = models.ForeignKey('HedgeHog', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


class TodoModel(models.Model):
    class Meta:
        verbose_name = "Todoリスト"
        verbose_name_plural = 'Todoリスト'

    title = models.CharField(
        verbose_name="タイトル",
        max_length=50,
    )
    content = models.TextField(
        verbose_name="内容"
    )
    deadline = models.DateTimeField(
        verbose_name="期日",
        default=timezone.now
    )

    def __str__(self):
        return self.title