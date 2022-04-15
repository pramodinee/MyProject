from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class post (models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args = [self.id,self.slug])

    def total_likes(self):
        return self.likes.count()

@receiver (pre_save,sender=post)
def pre_save_slug(sender,**kwargs):
    slug1 = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug1


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateTimeField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return 'Profile of user {}'.format(self.user.username)

class Images(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.post.title + 'images'

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)


