from django.db import models


class Slogan(models.Model):
    text = models.TextField()
    type_effect = models.CharField(max_length=40, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Feature(models.Model):
    title = models.TextField()
    desc = models.TextField()
    svg = models.TextField()
    heading = models.TextField()
    elaborate = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HeroImage(models.Model):
    image_url = models.TextField(null=True)
    image_source = models.ImageField(upload_to='homepage', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_url


class OurWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    website = models.TextField(null=True)
    image_url = models.TextField(null=True)
    image_source = models.ImageField(upload_to='homepage', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    designation = models.TextField(null=True)
    website = models.TextField(null=True)
    image_url = models.TextField(null=True)
    image_source = models.ImageField(upload_to='homepage', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


