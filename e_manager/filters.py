import django_filters

from .models import ExpenseDetails

class ExpenseDetailsFilter(django_filters.FilterSet):
    class Meta:
        model = ExpenseDetails
        fields = ['date','category','accounts']