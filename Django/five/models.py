from django.db import models

# Create your models here.
class Tempcategory(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Template(models.Model):
    template_name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Tempcategory, on_delete=models.CASCADE, related_name="tempcategory")
    def __str__(self):
        return self.template_name