
from django.shortcuts import render
from django.views.generic import View, ListView, FormView, DetailView
from django.urls import reverse_lazy
from visit.models import Visit, Room
from visit.forms import 

def index(request):
    return render(
    reguest=request, 
    template_name= 'deposit/'input.html',
    context={},
      )

elif reguest.method == 'POST':
    return HttpResponse('Incoming request')

clas DepositView(View):
    
    def multiplier(request):

        num1 = request.POST['num1']
        num2 = request.POST['num2']
         num3 = request.POST['num3']

    if num1.isdigit() and num2.isdigit() and num3.isdigit():
        a = int(num1)
        b = int(num2)
        c = int(num3)
        res = (a * b * c) - a

        return render(request, "/deposit/result.html", {"result": res})
    else:
        res = "Only digits"
        return render(request, "/deposit/input.html", {"result": res})

