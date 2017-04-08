from django.contrib import admin

from .models import Bill
from .models import BillCategories
# Register your models here.
from .models import InterestCategory
from .models import MemberOfCongress
from .models import MemberOfCongressInterests

admin.site.register(InterestCategory)
admin.site.register(MemberOfCongress)
admin.site.register(MemberOfCongressInterests)
admin.site.register(BillCategories)
admin.site.register(Bill)
