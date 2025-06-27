from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    if settings.MACHINE_ENV == "local":
        image = models.ImageField(max_length=500, null=True, blank=True,upload_to="posts/images")
    else:
        image = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_published = models.BooleanField(default=False)

    @property
    def formatted_img_url(self):
        url = self.image if self.image.__str__().startswith(('http://','https://')) else self.image.url
        return url
    
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