from django.contrib import admin
from footer.models import Footer_item, Footer_links

class FooterItemAdmin(admin.ModelAdmin):
    list_display = ('footer_title', 'footer_content')

class FooterLinksAdmin(admin.ModelAdmin):
    list_display = ('footer_link_title', 'links')

admin.site.register(Footer_item, FooterItemAdmin)
admin.site.register(Footer_links, FooterLinksAdmin)
