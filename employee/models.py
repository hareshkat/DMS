from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class Department(models.Model):
    dept_no = models.CharField('code', primary_key=True, max_length=4)
    dept_name = models.CharField('name', unique=True, max_length=40)

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'
        ordering = ['dept_no']

    def __str__(self):
        return self.dept_name

    def employees(self):
        return self.dmsuser_set.count()

    def reviewers(self):
        data = Group.objects.filter(name='reviewer').values().first()
        reviewer_users = DmsUser.objects.filter(department = self, groups = data['id']).values('username')
        return ", ".join([str(p['username']) for p in reviewer_users])

    def approver(self):
        data = Group.objects.filter(name='approver').values().first()
        approver_users = DmsUser.objects.filter(department = self, groups = data['id']).values('username')
        data =  DmsUser.objects.filter(department = self, approver=True).values('username')
        return ", ".join([str(p['username']) for p in approver_users])


class DmsUser(AbstractUser):
    department = models.ManyToManyField(Department, blank=True)
    reviewer = models.BooleanField(default=False)
    approver = models.BooleanField(default=False)
