from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    real_first_name = models.CharField(max_length=200, null=True)
    real_last_name = models.CharField(max_length=200, null=True)
    
    email = models.EmailField(unique=True, null=True)
    
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    
    Self_Intro = models.TextField(max_length=300, null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    CL_Subject = 0
    EL_Subject = 1
    FR_Subject = 2
    IPLA_Subject = 3
    MA_Subject = 4
    PH_Subject = 5
    CM_Subject = 6
    OS_Subject = 7
    JS_Subject = 8
    CI_Subject = 9
    ME_Subject = 10
    CH_Subject = 11
    EI_Subject = 12
    BA_Subject = 13
    MIS_Subject = 14
    FM_Subject = 15
    EC_Subject = 16
    EE_Subject = 17
    CE_Subject = 18
    CO_Subject = 19
    IPEECS_Subject = 20
    AP_Subject = 21
    GP_Subject = 22
    SS_Subject = 23
    GA_Subject = 24
    HK_Subject = 25
    LS_Subject = 26
    BM_Subject = 27
    SUBJECT_CHOICES = [(CL_Subject, '中國文學系'), (EL_Subject, '英美語文學系'), 
                       (FR_Subject, '法國語文學系'), (IPLA_Subject, '文學院學士班'),
                       (CM_Subject, '化學系'), (OS_Subject, '光電科學與工程學系'),
                       (JS_Subject, '理學院學士班'), (CI_Subject, '土木工程學系'), 
                       (ME_Subject, '機械工程學系'), (CH_Subject, '化學工程與材料工程學系'), 
                       (EI_Subject, '工學院學士班'), (BA_Subject, '企業管理學系'), 
                       (MIS_Subject, '資訊管理學系'), (FM_Subject, '財務金融學系'),
                       (EC_Subject, '經濟學系'), (EE_Subject, '電機工程學系'),
                       (CE_Subject, '資訊工程學系'), (CO_Subject, '通訊工程學系'),
                       (IPEECS_Subject, '資訊電機學院學士班'), (AP_Subject, '大氣科學學系'),
                       (GP_Subject, '地球科學學系'), (SS_Subject, '太空工程與科學學系'),
                       (GA_Subject, '地科院學士班'), (HK_Subject, '客家語文暨社會科學學系'), 
                       (LS_Subject, '生命科學系'), (BM_Subject, '生醫工程與科學學系')]
    Subject = models.IntegerField(choices=SUBJECT_CHOICES, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

class Report(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    value1 = 'Yes'
    value2 = 'No'
    choices = (
        (value1, 'display1'),
        (value2, 'display2'),
    )
    name = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return self.name
        
class Image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images", null=True, blank=True)
    