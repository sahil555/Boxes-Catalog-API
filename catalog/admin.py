from django.contrib import admin

# Register your models here.

from .models import Author,Box



class BoxesInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Box


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ('name','date_of_birth')
    fields = ['name', ('date_of_birth')]
    inlines = [BoxesInline]


class BoxesInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = Box


class BoxAdmin(admin.ModelAdmin):
   
    list_display = ('length','width','height', 'author',)
    inlines = [BoxesInstanceInline]


@admin.register(Box)
class BoxInstanceAdmin(admin.ModelAdmin):
   
    list_display = ('length','width','height', 'author',)

   
