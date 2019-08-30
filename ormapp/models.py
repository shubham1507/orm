from django.db import models


class dept(models.Model):

    dname = models.CharField(max_length=200, default="", editable=False)
    deptno = models.IntegerField(primary_key=True, default="", editable=False)
    loc = models.CharField(max_length=200, default="", editable=False)


class emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    mgr = models.IntegerField()
    hiredate = models.DateTimeField(auto_now_add=True, blank=True)
    sal = models.IntegerField()
    comm = models.IntegerField()
    deptno = models.ForeignKey(dept, on_delete=models.CASCADE, null=True)


class salgrade(models.Model):
    grade = models.IntegerField()
    losal = models.IntegerField()
    hisal = models.IntegerField()
