from django.contrib import admin
from models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uri')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
