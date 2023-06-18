from django.shortcuts import render, redirect
from .models import Car, Detail

def garage(request):
    if not (request.user.is_authenticated):
        return redirect("login") 
    
    return render(request, "main/garage.html", {
        "page": "garage"
    })
    
    
    
def but_from_dealer(request):
    return render(request, "main/buy_from_dealer.html", {
        "page": "bfd"
    })


def detail_tuning(request):
    return render(request, "main/detail_tuning.html")


def car_tuning(request):
    car = Car.objects.all()[0]
    details = Detail.objects.all()
    
    if request.method == "POST":
        car_ecu = request.POST.get("car_ecu")
        car_engine = request.POST.get("car_engine")
        car_turbo = request.POST.get("car_turbo")
        car_clutch = request.POST.get("car_clutch")
        
        # Ecu Swap/Delete
        if car_ecu:
            if car.ecu:
                ecu = car.ecu
                ecu.in_car = None
                car.ecu = None
                ecu.save()
                
            ecu = Detail.objects.get(id = car_ecu)
            car.ecu = ecu
            ecu.in_car = car
            ecu.save()
            
            
        else:
            if car.ecu:
                ecu = car.ecu
                ecu.in_car = None
                car.ecu = None
                ecu.save()
        
        # Engine Swap/Delete
        if car_engine:
            if car.engine:
                engine = car.engine
                engine.in_car = None
                car.engine = None
                engine.save()

            engine = Detail.objects.get(id = car_engine)
            car.engine = engine
            engine.in_car = car
            engine.save()
            
  
            
        else:
            if car.engine:
                engine = car.engine
                engine.in_car = None
                car.engine = None
                engine.save()
                
        # turbo Swap/Delete
        if car_turbo:
            
            if car.turbo:
                turbo = car.turbo
                turbo.in_car = None
                car.turbo = None
                turbo.save()
            
            turbo = Detail.objects.get(id = car_turbo)
            car.turbo = turbo
            turbo.in_car = car
            turbo.save()
            
        else:
            if car.turbo:
                turbo = car.turbo
                turbo.in_car = None
                car.turbo = None
                turbo.save()
        
        car.save()
    
    return render(request, "main/car_tuning.html", {
        "car": car,
        "details": details
    })
