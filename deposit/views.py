
from django.shortcuts import render

def index(request):
    return render(request, "input.html")

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

