from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.TextField()
    preparation = models.TextField()
    preparation_time = models.TimeField()
    chief = models.ForeignKey("chief.Chief", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
