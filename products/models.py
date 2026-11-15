from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    pass


class Category(models.Model):
    class Status:
        Draft = "DF","DRAFT"
        Publish = "PB","PUBLISH"
    
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(blank=False, upload_to='categories')
    is_enable = models.BooleanField(choices=Status)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class File(models.Model):
    pass