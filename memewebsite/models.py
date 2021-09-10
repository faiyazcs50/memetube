from django.db import models

# Create your models here.
class meme(models.Model):
    meme = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "meme":self.meme.url
        }

class shittypost(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    adult = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title