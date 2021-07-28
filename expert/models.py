from django.db import models
from accounts.models import CustomerUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Expert(models.Model):
    title = models.CharField(max_length=200, verbose_name="글제목",null=True)
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name="글작성일",null=True)
    writer = models.ForeignKey(CustomerUser, related_name="expert_user", on_delete=models.CASCADE,db_column="user",verbose_name="작성자",null=True)
    body = models.TextField(verbose_name="글내용",null=True,blank=False)
    image = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFit(width=250, height=250, upscale=False)],
        format='JPEG'
    )

    def __str__(self):
        return self.title



# class Image(models.Model):
#     post = models.ForeignKey(Expert, on_delete=models.CASCADE)
#     file = models.ImageField(upload_to='images/', blank=False)
    