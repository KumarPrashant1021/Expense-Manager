from django.shortcuts import render
from django.shortcuts import redirect
import json
from django.contrib.auth.models import User, auth
from rest_framework.parsers import JSONParser
from .serializers import ExpenseDetailsSerializer
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from .models import ExpenseDetails,Customer
from .filters import ExpenseDetailsFilter
from django.db.models import Count,Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import UserForm
from datetime import datetime, timedelta
from django.contrib import messages
# Create your views here.
ALLOWED_HOSTS=settings.ALLOWED_HOSTS

def home(request):
    if request.user.is_authenticated:
        queryset = Customer.objects.all().filter(user=request.user)
        monthly_income=0
        for q in queryset:
           monthly_income=q.monthlyIncome
        context = {'monthly_income':monthly_income}
        return render(request,'home.html',context)
    else:
        return redirect('register')


def addExpense(request, *args,**kwargs):
    #return redirect('home')
    if request.method == 'GET':
        customer = Customer.objects.get(user=request.user)
        expensedetails = ExpenseDetails.objects.filter(customer = customer)
        serializer = ExpenseDetailsSerializer(expensedetails, many=True)
        return JsonResponse(serializer.data, status=201,safe=False)

    if request.method=="POST":
        customer = Customer.objects.get(user=request.user)
        serializer = ExpenseDetailsSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(customer=customer)
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    
def showExpenseDetail(request, *args,**kwargs):
    if request.method == 'GET':
        last_month = datetime.today() - timedelta(days=30)
        print(last_month)
        customer = Customer.objects.get(user=request.user)
        expensedetails = ExpenseDetails.objects.all().filter(customer = customer ,date__gte=last_month).order_by('-id')
        context = {'sum':sum}
        serializer = ExpenseDetailsSerializer(expensedetails, many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    return JsonResponse({},status=400)

def filter(request, *args,**kwargs):
   if request.method=="POST":
        date = ''
        category = ''
        accounts = ''
        print(request.POST)
        date = request.POST['date']
        category = request.POST['category']
        accounts = request.POST['accounts']
        customer = Customer.objects.get(user=request.user)
        if not date  == '' and category == '' and accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,date=date)

        elif date  == '' and not category == '' and accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,category=category)

        elif date  == '' and category == '' and not accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,accounts=accounts)

        elif not date  == '' and not category == '' and accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,date=date,category=category)

        elif not date  == '' and  category == '' and  not accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,date=date,accounts=accounts)

        elif  date  == '' and not category == '' and  not accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,category=category,accounts=accounts)

        elif not date == '' and not category =='' and not accounts == '':
            expensedetails = ExpenseDetails.objects.all().filter(customer = customer,date=date,category=category,accounts=accounts)

        else:
            expensedetails = False

        if expensedetails == False:
            return JsonResponse({},status=201,safe=False)
        else:
            serializer = ExpenseDetailsSerializer(expensedetails, many=True)
            return JsonResponse(serializer.data,status=201,safe=False)



def pie_chart(request):
    if request.user.is_authenticated:
        user =  User.objects.get( id = request.user.id )
        customer = Customer.objects.get(user = user )
        monthlyIncome = customer.monthlyIncome
        if monthlyIncome == 0:
            messages.info(request,"Please update monthly income or else it will show 0 by defualt")
        no_of_item = ExpenseDetails.objects.annotate(count = Count('id'))
        context = {'user':user,'customer':customer}
        return render(request,'charts.html',context)
    else:
        return redirect('register')

class ChartData(APIView):
    def get(self, request , format=None):
        customer = Customer.objects.get(user=request.user)
        queryset = ExpenseDetails.objects.filter(customer = customer).values('category').annotate(sum=Sum('amount'))
        return Response(queryset)
            
def register(request , *args , **kwargs ):
    form = UserForm()
    context = {'form':form}
    return render(request, 'register.html',context)

def addMonthlyIncome(request):
    if request.method == 'POST':
        monthly_income = request.POST['monthly_income']
        user = User.objects.get(id  = request.user.id)
        customer = Customer.objects.get(user = user)
        customer.monthlyIncome = monthly_income
        customer.save()
    return redirect('pie_chart')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password =  password)
        if user is not None:
            auth.login(request , user)
            return redirect('home')
        else:
            messages.info(request,"User is not found please check username or password")
            return redirect('register')

def logout(request):
    auth.logout(request)
    print("logout")
    return redirect('home')