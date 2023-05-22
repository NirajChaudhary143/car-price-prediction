from django.contrib import admin
from contactus.models import ContactUs,contactList
# Register your models here.
class Contactus(admin.ModelAdmin):
    list_display=('name','email','message')
class ContactList(admin.ModelAdmin):
    list_display=('icon','title','address')
admin.site.register(ContactUs,Contactus)
admin.site.register(contactList,ContactList)

