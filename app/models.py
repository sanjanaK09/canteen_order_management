from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=20)
    time_slot = models.CharField(max_length=50, null=True, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.item}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.item}"