from django.contrib import admin
from homepage.models import Slogan, HeroImage, OurWork, OurTeam


class SloganAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_date', 'updated_date')


admin.site.register(Slogan, SloganAdmin)


class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'image_source', 'created_date', 'updated_date')


admin.site.register(HeroImage, HeroImageAdmin)


class OurWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'website', 'image_url', 'image_source', 'created_date', 'updated_date')


admin.site.register(OurWork, OurWorkAdmin)


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'website', 'image_url', 'image_source', 'created_date', 'updated_date')


admin.site.register(OurTeam, OurTeamAdmin)
