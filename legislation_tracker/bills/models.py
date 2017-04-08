from django.db import models

# Create your models here.
BILL_PRIORITY_CHOICES = [
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low')
]
BILL_STATUS_CHOICES = [
    (1, 'Needs Review'),
    (2, 'Updated'),
    (3, 'Research Complete'),
    (4, 'Done')
]


class InterestCategory(models.Model):
    name = models.CharField(max_length=200)


class MemberOfCongress(models.Model):
    name = models.CharField(max_length=200)


class MemberOfCongressInterests(models.Model):
    interest = models.ForeignKey('InterestCategory')
    member_of_congress = models.ForeignKey('MemberOfCongress')


class BillCategories(models.Model):
    bill = models.ForeignKey('Bill')
    category = models.ForeignKey('InterestCategory')


class Bill(models.Model):
    bill_id = models.CharField(max_length=200)
    summary = models.TextField()
    status = models.IntegerField(choices=BILL_STATUS_CHOICES)
    priority = models.IntegerField(choices=BILL_PRIORITY_CHOICES)
