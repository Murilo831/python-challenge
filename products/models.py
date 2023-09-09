from django.db import models

class Product(models.Model):
    code = models.BigIntegerField(unique=True)
    status = models.CharField(max_length=20)
    imported_t = models.DateTimeField(null=True, blank=True)
    url = models.URLField()
    creator = models.CharField(max_length=100)
    created_t = models.IntegerField()
    last_modified_t = models.IntegerField()
    product_name = models.CharField(max_length=500)
    quantity = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    categories = models.CharField(max_length=500)
    labels = models.CharField(max_length=500)
    cities = models.CharField(max_length=500)
    purchase_places = models.CharField(max_length=500)
    stores = models.CharField(max_length=500)
    ingredients_text = models.TextField()
    traces = models.CharField(max_length=500)
    serving_size = models.CharField(max_length=100)
    serving_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    nutriscore_score = models.BigIntegerField()
    nutriscore_grade = models.CharField(max_length=1)
    main_category = models.CharField(max_length=500)
    image_url = models.URLField()

    def str(self):
        return self.product_name