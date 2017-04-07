from django.db import models

# Create your models here.
PRIORITY_CHOICES = [ 'high', 'medium', 'low' ]
class Priority(model.Models):
    name = models.CharField(choices = PRIORITY_CHOICES)

class InterestCategory(model.Models):
    name = models.CharField(max_length=200)

class MemberOfCongress(model.Models):
    name = models.CharField(max_length=200)

class MemberOfCongressInterests:
    interest = models.ForeignKey('InterestCategory')
    member_of_congress = models.ForeignKey('MemberOfCongress')

class BillCategories:
    bill = models.ForeignKey('Bill')
    category = models.ForeignKey('InterestCategory')

class Bill(model.Model):
    bill_id = models.CharField(max_length=200)






