from django.db import models

# Create your models here.

class Footer_item(models.Model):
    footer_title=models.TextField(max_length=50)
    footer_content=models.TextField(max_length=1000)

class Footer_links(models.Model):
    footer_link_title=models.TextField(max_length=50)
    links=models.TextField(max_length=30)
