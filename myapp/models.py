from django.db import models


class Emplyee(models.Model):
    eid = models.CharField(max_length=22)
    ename = models.CharField(max_length=100)
    emailid = models.EmailField()
    econtact = models.CharField(max_length=40)


