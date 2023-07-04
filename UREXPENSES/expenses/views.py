from django.shortcuts import render,redirect
from .models import Expense
from .forms import ExpenseModelForm
from django.db.models import Q

def index(request):
    expenses = Expense.objects.all()
    form = ExpenseModelForm()
    if request.user.is_authenticated:
        context = {
            'username':request.user.username,
            'expenses': expenses,
            'form': form,
        }
    return render(request, 'expenses/home.html', context)

def update(request, pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseModelForm(instance=expense)
    if request.method == 'POST':
        form = ExpenseModelForm(request.POST,request.FILES,instance=expense)
        if form.is_valid():
            form.save()
        return redirect('/expenses')
    context = {
        'form': form
    }
    return render(request, 'expenses/update.html', context)

def delete(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect('/expenses')
    context = {
        'expense': expense
    }
    return render(request, 'expenses/delete.html', context)

def add(request):
    form = ExpenseModelForm()
    if request.method == "POST":
        form = ExpenseModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/expenses')
    context = {
        'form' : form
    }
    return render(request,'expenses/add.html',context)

def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        expenses = Expense.objects.filter(Q(name__contains=search_query)|Q(price__contains=search_query))
        return render(request, 'expenses/search.html', {'query':search_query, 'expenses':expenses})
    else:
        return render(request, 'expenses/search.html',{})