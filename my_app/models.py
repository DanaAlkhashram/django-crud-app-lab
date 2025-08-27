from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    CATEGORY_CHOICES = [
        ('EL', 'Electronics'),
        ('CL', 'Clothing'),
        ('FD', 'Food'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='EL'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='items',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
