from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=False, upload_to='products/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'),blank=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)
    
    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class Category(models.Model):
    class Status(models.TextChoices):
        Draft = "DF","DRAFT"
        Publish = "PB","PUBLISH"
    
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(blank=False, upload_to='categories/')
    is_enable = models.CharField(max_length=2,choices=Status.choices, default=Status.Draft)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class File(models.Model):
    title = models.CharField(_('title'),max_length=50)
    product = models.ForeignKey('Product', verbose_name=_('product'),on_delete=models.CASCADE)
    file = models.FileField(_('File'),upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')