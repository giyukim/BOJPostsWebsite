from django.db import models

class Post(models.Model):
    title = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    plink = models.TextField()
    code = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title