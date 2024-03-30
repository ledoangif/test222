from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    time_pub = models.DateTimeField()
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    vote = models.IntegerField(default=0)
class BenhNhan(models.Model):
    NameBN = models.CharField(max_length = 200,blank=False, null=False)
    Date = models.DateField()
    DateK = models.DateTimeField(default=timezone.datetime.now())
    CCCD = models.CharField(max_length=20,blank=False, null=False)
class PhongKham(models.Model):
    NamePK = models.CharField(max_length = 200,blank=False, null=False)
    SoPhong = models.IntegerField(blank=False, null=False)