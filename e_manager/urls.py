from django.urls import path
from . import views
from .views import ChartData

urlpatterns = [
    path('',views.home,name='home'),
    path('addExpense',views.addExpense,name='addExpense'),
    path('show',views.showExpenseDetail,name='showExpenseDetail'),
    path('filter',views.filter,name='filter'),
    path('user/',views.pie_chart,name='pie_chart'),
    path('user/api/chart/data',ChartData.as_view()),
    path('register',views.register,name='register'),
    path('user/addmi',views.addMonthlyIncome,name='addMonthlyIncome'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
    ]