from statistics import mode
from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length= 500, default=" ")
    c_head0 = models.CharField(max_length= 5000, default=" ")

    head1 = models.CharField(max_length= 500, default=" ")
    c_head1 = models.CharField(max_length= 5000, default=" ")

    head2 = models.CharField(max_length= 500, default=" ")
    c_head2 = models.CharField(max_length= 5000, default=" ")

    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to = "blog/Images", default=" ")

    def __str__(self):
        return self.title
