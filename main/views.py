from django.shortcuts import render


def garage(request):
    return render(request, "main/garage.html")


def detail_tuning(request):
    return render(request, "main/detail_tuning.html")


def car_tuning(request):
    return render(request, "main/car_tuning.html")
