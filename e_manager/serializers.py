from rest_framework import serializers

from .models import ExpenseDetails

class ExpenseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseDetails
        fields = ['date','category','accounts','contents','amount']