from django.contrib import admin
from .  import models

# Register your models here.

# If we wanna change the order of specific models field then we should do ...
class StudentAdmin(admin.ModelAdmin):
    # it is our previous order of the fields
    #fields = ['name','department','semester','phone_number',]
    # I will customize that order
    fields = ['semester','department','name','phone_number']

    # we can also add search option using search_field
    search_fields = ['semester','department','name']

    # we can add filter method
    list_filter = ['semester','department','name','phone_number']

    # we can also show all the fields using list_display rather than the object.
    list_display = ['name','department','semester','phone_number']

    # we use editable list so that we can edit each and every attribute.
    list_editable = ['department','semester', 'phone_number']

# admin.site.register(Student)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Course)
