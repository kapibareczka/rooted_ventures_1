from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    main_text = models.TextField()
    publish_date = models.DateTimeField()

    def __str__(self):
     return f"{self.title} - {self.publish_date}"