from rest_framework import viewsets

from legislation_tracker.bills import models
from legislation_tracker.bills import serializers


class BillViewSet(viewsets.ModelViewSet):
    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer
