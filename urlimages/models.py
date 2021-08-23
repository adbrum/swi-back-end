from django.db import models


class Lead(models.Model):
    user_id = models.IntegerField()
    image_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
