from django.db import models
from users.models import User
import os
from uuid import uuid4
from datetime import date

# change image name to uuid4
def rename_imagefile_to_uuid(instance, filename):
    now = date.today()
    upload_to = f'image/{now.year}/{now.month}/{now.day}/{instance}'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    
    if instance:
        filename = '{}_{}.{}'.format(uuid, instance, ext)
    else:
        filename = '{}.{}'.format(uuid, ext)
    return os.path.join(upload_to, filename)

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=100, verbose_name='할일')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(null=True, blank=True, upload_to=rename_imagefile_to_uuid, storage=None)
    is_complete = models.BooleanField(default=False, verbose_name='완료여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')
    completion_at = models.DateTimeField(null=True, blank=True, verbose_name='완료시간')
    
    def __str__(self):
        return str(self.title)
    
    
class Comment(models.Model):
    pass