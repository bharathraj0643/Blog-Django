from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=500, null=True, blank=True)
    # image = CloudinaryField("image")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_published = models.BooleanField(default=False)

    @property
    def formatted_img_url(self):
        fallback = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png'
        return self.image if self.image else fallback
    
    def save(self, *args, **kwargs):
        fallback = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png'
        if not self.image:
            self.image = fallback
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    content = models.TextField()