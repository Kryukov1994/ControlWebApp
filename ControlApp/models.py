from django.db import models

class Post(models.Model):

    text = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class PostStr(models.Model):
    poststr = models.ForeignKey(Post,on_delete=models.CASCADE)
