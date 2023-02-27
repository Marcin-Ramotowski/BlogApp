from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORY = (
    ('IT', 'informatyka'),
    ('G', 'geografia'),
    ('Z', 'zdrowie')
)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(choices=CATEGORY, max_length=30, default='Z')
    title = models.CharField(max_length=50, unique_for_date='created')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def get_details_url(self):
        return reverse('news:news_detail', args=[self.id])

    def get_update_url(self):
        return reverse('news:news_update', args=[self.id])

    def get_delete_url(self):
        return reverse('news:news_delete', args=[self.id])

    def __str__(self):
        return self.title
