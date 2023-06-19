from django.shortcuts import render, redirect
from .models import Car, Detail, DealerCar, DealerDetail
from django.db.models import Subquery, OuterRef
from users.models import CustomUser
def garage(request):
    if not (request.user.is_authenticated):
        return redirect("login") 
    
    return render(request, "main/garage.html", {
        "page": "garage"
    })
    
    
    
def but_from_dealer(request):
    
    dealer_cars = DealerCar.objects.all()
    dealer_details =  DealerDetail.objects.all()
    
    if request.method == "POST":
        buy_detail = request.POST.get("buy_detail")
        buy_car = request.POST.get("buy_car")
        
        if buy_car:
            car = DealerCar.objects.get(id = buy_car)
            
            if request.user.money >= car.product.price:
                if car.count != 0:
                    user = CustomUser.objects.get(id = request.user.id)
                    new_car = Car.objects.create(
                        name = car.product.name,
                        image = car.product.image,
                        color = car.product.color,
                        price = car.product.price,
                        max_speed = car.product.max_speed,
                        power = car.product.power,
                        acceleration = car.product.acceleration,
                        controllability = car.product.controllability,
                        turbo = car.product.turbo,
                        engine = car.product.engine,
                        ecu = car.product.ecu,
                        clutch = car.product.clutch
                    )

                    user.cars.add(new_car)
                    car.count -= 1
                    user.money -= car.product.price
                    
                    if car.count == 0:
                        car.delete()
                    else:
                        car.save()
                        
                    user.save()
                    return redirect("bfd")
                              
            
    return render(request, "main/buy_from_dealer.html", {
        "page": "bfd",
        "dealer_cars": dealer_cars,
        "dealer_details": dealer_details,
    })


def detail_tuning(request):
    return render(request, "main/detail_tuning.html")


def car_tuning(request, id):
    car = Car.objects.get(id = id)
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
                
        if car_clutch:
            if car.clutch:
                clutch = car.clutch
                clutch.in_car = None
                car.clutch = None
                clutch.save()
            
            clutch = Detail.objects.get(id = car_clutch)
            car.clutch = clutch
            clutch.in_car = car
            clutch.save()
            
        else:
            if car.clutch:
                clutch = car.clutch
                clutch.in_car = None
                car.clutch = None
                clutch.save()
        
        
        car.save()
    
    return render(request, "main/car_tuning.html", {
        "car": car,
        "details": details
    })



