# from django.db import models
# __all__ = (
#     'Toppings',
#     'Pizza',
# )
# class Toppings(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
# class Pizza(models.Model):
#     name = models.CharField(max_length=50)
#     toppings = models.ManyToManyField(
#         Toppings,
#         related_name='pizzas'
#     )
#
#     def __str__(self):
#         return self.name

from django.db import models

__all__ = (
    'Toppings',
    'Pizza',
)

class Toppings(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(
        Toppings,
        related_name='Pizzas'
    )

    def __str__(self):
        return self.name