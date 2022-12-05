from django.db import models


class ChooseUs(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='baseapp/why_choose_us')

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='baseapp/team')

    def __str__(self):
        return self.name
