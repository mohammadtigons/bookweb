from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User
class post(models.Model):
    choise=(
        ("draft","Draft"),
        ("publish","Publish")
    )
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique_for_date="publish")
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    body=models.TextField()
    publish=models.DateTimeField(default= timezone.now)
    creat=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=15,choices=choise,default="draft")
    class Meta:
        ordering=("-publish",)
        def __str__(self) -> str:
            return self.title
