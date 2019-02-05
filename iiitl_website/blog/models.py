from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models


class Post(models.Model):

    """Model for blog post."""

    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    date_added = models.DateTimeField(default=timezone.now())
    data_published = models.DateTimeField(blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
