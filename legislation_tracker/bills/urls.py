from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from legislation_tracker.bills import viewsets

router = DefaultRouter()
router.register(r'bills', viewsets.BillViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
