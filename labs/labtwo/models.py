from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    manufacturing_since = models.DateField()

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    model = models.ManyToManyField(Model, through='ReviewModel')

    def __str__(self):
        return self.title


class ReviewModel(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.review.title} - {self.model.name}"
