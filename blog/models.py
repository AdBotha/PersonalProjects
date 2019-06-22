from django.db import models

class Blogpost(models.Model):
    title = models.CharField(max_length=250)
    pubdate = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def shortpubdate(self):
        return self.pubdate.strftime('%e %b %Y')

    def __str__(self):
        return self.title

    def summary_body(self):
        return self.body[:100]
