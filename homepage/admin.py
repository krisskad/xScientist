from django.contrib import admin
from homepage.models import OurWork, OurTeam, Company, Technology, Message


# class SloganAdmin(admin.ModelAdmin):
#     list_display = ('text', 'created_date', 'updated_date')
#
#
# admin.site.register(Slogan, SloganAdmin)


# class HeroImageAdmin(admin.ModelAdmin):
#     list_display = ('image_url', 'image_source', 'created_date', 'updated_date')
#
#
# admin.site.register(HeroImage, HeroImageAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'updated_date')


admin.site.register(Company, CompanyAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'updated_date')


admin.site.register(Technology, TechnologyAdmin)


class OurWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'website', 'image_url', 'image_source', 'created_date', 'updated_date')


admin.site.register(OurWork, OurWorkAdmin)


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'website', 'image_url', 'image_source', 'created_date', 'updated_date')


admin.site.register(OurTeam, OurTeamAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'created_date', 'updated_date')


admin.site.register(Message, MessageAdmin)
