from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models


class Post(models.Model):

    """Model for blog post."""

    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='blog_images/',
                                       default='blog_images/default.jpeg')
    content = tinymce_models.HTMLField()
    date_added = models.DateTimeField(auto_now_add=True)
    data_published = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
