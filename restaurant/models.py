from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.CharField(max_length=12)
    working_hours_start= models.TimeField(null=True)
    working_hours_end= models.TimeField(null=True)
    adress = models.CharField(max_length=450, blank=False)
    category = models.CharField(max_length=200, blank=False)
    causin = models.CharField(max_length=200, blank=False)
    description = models.TextField()

    raiting = models.IntegerField(blank=False, default=0)
    menu = models.TextField()
    event = models.TextField()
    # что за end_point
    end_point = models.CharField(max_length=120, blank=False)


#Booking - заявка
class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    person = models.CharField(max_length=120, blank=False, default=1) #TODO: choice field
    time = models.DateTimeField(blank=False) #TODO: определить как назначить время
    comment = models.TextField()
    status = models.TextField() #TODO: choice field


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    score = models.IntegerField(blank=False, default=0)
    description = models.TextField()

    #TODO
    def rating_count () :
        #models.ForeignKey — ссылка на другую модель.
        ...
