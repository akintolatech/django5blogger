from django.db import models
from django.utils import timezone
from django.db.models.functions import Now
from django.conf import settings

from django.urls import reverse


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    post_img = models.ImageField(upload_to="blog_img/", null=True)
    title = models.CharField(max_length=33)

    slug = models.SlugField(
        max_length=250,
        unique_for_date="publish",
    )

    body = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )

    # publish = models.DateTimeField(default=timezone.now)
    # database generated values
    publish = models.DateTimeField(db_default=Now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    # If you declare any managers for
    # your model but, you want to keep the objects manager as well,
    # you have to add it explicitly to your model.

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.slug,
                self.publish.year,
                self.publish.month,
                self.publish.day

            ]
        )

    def __str__(self):
        return self.title
