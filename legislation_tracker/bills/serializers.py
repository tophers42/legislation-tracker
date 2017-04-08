from rest_framework import serializers

from legislation_tracker.bills import models


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bill
        fields = ('id', 'bill_id', 'summary', 'status', 'priority')
