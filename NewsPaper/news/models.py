from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):
    name_author = models.OneToOneField(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name_author.username

class Category(models.Model):
    name_category = models.CharField(max_length=64, unique=True, )

    def __str__(self):
        return self.name_category.title()

class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AR'
    TYPE_CHOICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    ]
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    post_type = models.CharField(choices=TYPE_CHOICES, max_length=64,)
    post_datetime = models.DateTimeField(auto_now_add=True,)
    post_category = models.ManyToManyField(Category, through='PostCategory',)
    post_title = models.CharField(max_length=64)
    post_text = models.TextField()

    def __str__(self):
        return f'{self.post_author.name_author.username}: {self.get_post_type_display()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment_text = models.TextField()
    comment_datetime = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.comment_user
