from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from tagging.fields import TagField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, db_index=True)
    text = RichTextUploadingField()
    material = models.FileField(upload_to='material/%Y/%m/%d',blank=True)
    tag = TagField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)