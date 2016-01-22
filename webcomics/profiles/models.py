from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import permalink

from django.core.files.base import ContentFile
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail

from posts.models import Post

class User(AbstractUser):  
    avatar = models.ImageField(upload_to='avatars/', default=None,blank=True, null=True)
    background = models.ImageField(upload_to='backgrounds/', default=None,blank=True, null=True)
    about = models.TextField(max_length=512, blank=True)
    website = models.CharField(max_length=64, blank=True)

    karma = models.IntegerField(default=0)
    # created = models.DateTimeField(auto_now_add=True, blank=True)

    subscribed = models.ManyToManyField('User', related_name="subscribers", blank=True)

    upvoted = models.ManyToManyField('posts.Post', related_name="upvoters", blank=True)

    # comments_upvoted = models.ManyToManyField('comments.Comment', related_name="upvoters", blank=True)
    # approved = models.BooleanField(default=False)
    
    # @permalink
    # def get_absolute_url(self):
    #     return ('view_post', None, {'slug': self.slug })        

    # def save(self, slug="", *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)  
    #     resized = get_thumbnail(self.avatar, "120x120", crop='center', quality=99)
    #     self.avatar.save(resized.name, ContentFile(resized.read()), True)            

    #     return super(User, self).save(*args, **kwargs)
    
