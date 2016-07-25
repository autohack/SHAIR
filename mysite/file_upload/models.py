# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    user_name = models.CharField(max_length=100, default='PUBLIC')
    #password = models.CharField(max_length=100, default='NULL')
    is_deleted= models.IntegerField(default=0)
