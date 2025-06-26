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
    image = models.ImageField(max_length=255,null=True,upload_to="posts/images")
    # image = CloudinaryField("image")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_published = models.BooleanField(default=False)

    @property
    def formatted_img_url(self):
        fallback = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png'
        try:
            if self.image and hasattr(self.image, 'url') and self.image.url:
                return self.image.url
        except Exception:
            pass
        return fallback
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    content = models.TextField()