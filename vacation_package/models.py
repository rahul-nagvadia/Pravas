from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class Photos(models.Model):
    image = models.ImageField(upload_to='static/package/images')

    def __str__(self):
        return f"{self.image}"


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ForeignKey(Photos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.place}"


class Inclusions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Activity(models.Model):
    name = models.CharField(max_length=100)
    inclusion = models.ForeignKey(Inclusions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class DaySchedule(models.Model):
    day_number = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    activities = models.ManyToManyField(Activity, related_name="activities")

    def __str__(self):
        return f"{self.day_number} - {self.name}"


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Things(models.Model):
    thing = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.thing}"


class Package(models.Model):
    name = models.CharField(max_length=100)
    overview = models.CharField(max_length=200, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    days = models.ManyToManyField(DaySchedule, related_name="days")
    price = models.IntegerField()
    images_folder = models.IntegerField(null=True)
    inclusions = models.ManyToManyField(Inclusions, related_name="inclusion")
    themes = models.ManyToManyField(Theme, related_name="themes")
    inclusions_things = models.ManyToManyField(
        Things, related_name="inclusions_things")
    exclusions_things = models.ManyToManyField(
        Things, related_name="exclusions_things")

    def __str__(self):
        return f"{self.name} - {self.place}"


class Month(models.Model):
    name = models.CharField(max_length=50)
    packages = models.ManyToManyField(
        Package, related_name="packages", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Package_Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    children = models.IntegerField()
    Adult = models.IntegerField()
    date_booked = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.package}"
