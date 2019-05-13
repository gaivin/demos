from django.db import models


# Create your models here.
class User(models.Model):
    MALE = "M"
    FEMALE = "W"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    followed_by = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __unicode__(self):
        return "%s.%s" % (self.first_name, self.last_name)

    __str__ = __unicode__


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.author, self.title)

    def __str__(self):
        return "%s - %s" % (self.author, self.title)
