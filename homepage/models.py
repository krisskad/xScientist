from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    slogan = models.TextField(null=True, blank=True)
    hero_image = models.TextField(null=True, blank=True)
    about = models.TextField()
    mission = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    geo_coordinates = models.TextField(null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)
    logo_source_url = models.ImageField(upload_to='homepage', null=True, blank=True)
    login_url = models.TextField(null=True, blank=True)
    seo_keyword = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Slogan(models.Model):
#     text = models.TextField()
#     type_effect = models.CharField(max_length=40, null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.text
#

class Technology(models.Model):
    name = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    svg = models.TextField(null=True, blank=True)
    heading = models.TextField(null=True, blank=True)
    elaborate = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class HeroImage(models.Model):
#     image_url = models.TextField(null=True)
#     image_source = models.ImageField(upload_to='homepage', null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.image_url
#

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
    website = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    image_source = models.ImageField(upload_to='homepage', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender_name = models.CharField(max_length=255, null=True, blank=True)
    sender_email = models.TextField(null=True, blank=True)
    sender_message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender_email


