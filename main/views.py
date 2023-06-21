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
                if car.count > 0:
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
                
        elif buy_detail:
            detail = DealerDetail.objects.get(id = buy_detail)     
            
            if request.user.money >= detail.product.price:
                if detail.count > 0:
                    user = CustomUser.objects.get(id = request.user.id)
                        
                    new_detail = Detail.objects.create(
                        type =  detail.product.type,
                        level = detail.product.level,
                        in_car = None,
                        price = detail.product.price,
                        added_max_speed = 0,
                        added_power = 0,
                        added_acceleration = 0,
                        added_controllability = 0,
                    )
                    
                    user.details.add(new_detail)
                    detail.count -= 1
                    user.money -= detail.product.price
                    
                    if detail.count == 0:
                        detail.delete()
                    else:
                        detail.save()
                        
                    user.save()
                    return redirect("bfd")
            
    return render(request, "main/buy_from_dealer.html", {
        "page": "bfd",
        "dealer_cars": dealer_cars,
        "dealer_details": dealer_details,
    })


def detail_tuning(request):
    return render(request, "main/detail_tuning.html")




def insert_detail(car, detail):
    if detail.type.name == "Clutch":
        coefficients = {
            1: (0.03, 0.05, 0.02, 0.01),
            2: (0.06, 0.1, 0.04, 0.02),
            3: (0.09, 0.15, 0.06, 0.03),
            4: (0.12, 0.2, 0.08, 0.04)
        }
    elif detail.type.name == "Turbo":
        coefficients = {
            1: (0.05, 0.08, 0.03, 0.01),
            2: (0.08, 0.12, 0.05, 0.02),
            3: (0.11, 0.16, 0.07, 0.03),
            4: (0.14, 0.2, 0.1, 0.04)
        }
    elif detail.type.name == "Engine":
        coefficients = {
            1: (0.08, 0.15, 0.05, 0.02),
            2: (0.15, 0.25, 0.1, 0.04),
            3: (0.22, 0.35, 0.15, 0.06),
            4: (0.3, 0.45, 0.2, 0.08)
        }
    elif detail.type.name == "Ecu":
        coefficients = {
            1: (0.05, 0.1, 0.03, 0.01),
            2: (0.08, 0.15, 0.05, 0.02),
            3: (0.12, 0.2, 0.08, 0.03),
            4: (0.15, 0.25, 0.1, 0.04)
        }
    else:
        return

    coeffs = coefficients[detail.level]
    detail.added_max_speed = car.max_speed * coeffs[0]
    detail.added_power = car.power * coeffs[1]
    detail.added_acceleration = car.acceleration * coeffs[2]
    detail.added_controllability = car.controllability * coeffs[3]
        
    car.max_speed += detail.added_max_speed
    car.power += detail.added_power
    car.acceleration += detail.added_acceleration
    car.controllability += detail.added_controllability
       
    car.max_speed = round(car.max_speed, 1)
    car.power = round(car.power, 1)
    car.acceleration = round(car.acceleration, 1)
    car.controllability = round(car.controllability, 1)
            
    car.save()
    detail.save()

def take_off_detail(car, detail):
    car.max_speed -= detail.added_max_speed
    car.power -= detail.added_power
    car.acceleration -= detail.added_acceleration
    car.controllability -= detail.added_controllability
    
    detail.added_max_speed = 0
    detail.added_power = 0
    detail.added_acceleration = 0
    detail.added_controllability = 0
    
    car.save()
    detail.save()

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
                take_off_detail(car, ecu)
                ecu.in_car = None
                car.ecu = None
                ecu.save()
                
            ecu = Detail.objects.get(id = car_ecu)
            
            if ecu in request.user.details.all():
                insert_detail(car, ecu)

                car.ecu = ecu
                ecu.in_car = car
                ecu.save()
            
        else:
            if car.ecu:
                ecu = car.ecu
                take_off_detail(car, ecu)
                ecu.in_car = None
                car.ecu = None
                ecu.save()
        
        # Engine Swap/Delete
        if car_engine:
            if car.engine:
                engine = car.engine
                take_off_detail(car, engine)
                engine.in_car = None
                car.engine = None
                engine.save()

            engine = Detail.objects.get(id = car_engine)
            if engine in request.user.details.all():
                insert_detail(car, engine)
                car.engine = engine
                engine.in_car = car
                engine.save()
            
  
            
        else:
            if car.engine:
                engine = car.engine
                take_off_detail(car, engine)
                engine.in_car = None
                car.engine = None
                engine.save()
                
        # turbo Swap/Delete
        if car_turbo:
            if car.turbo:
                turbo = car.turbo
                take_off_detail(car, turbo)
                turbo.in_car = None
                car.turbo = None
                turbo.save()
            
            turbo = Detail.objects.get(id = car_turbo)
            
            if turbo in request.user.details.all():  
                insert_detail(car, turbo)
                car.turbo = turbo
                turbo.in_car = car
                turbo.save()
            
        else:
            if car.turbo:
                turbo = car.turbo
                take_off_detail(car, turbo)
                turbo.in_car = None
                car.turbo = None
                turbo.save()
                
        if car_clutch:
            if car.clutch:
                clutch = car.clutch
                take_off_detail(car, clutch)
                clutch.in_car = None
                car.clutch = None
                clutch.save()
            
            clutch = Detail.objects.get(id = car_clutch)
            if clutch in request.user.details.all():
                insert_detail(car, clutch)
                car.clutch = clutch
                clutch.in_car = car
                clutch.save()
            
        else:
            if car.clutch:
                clutch = car.clutch
                take_off_detail(car, clutch)
                clutch.in_car = None
                car.clutch = None
                clutch.save()
        
        
        car.save()
    
    return render(request, "main/car_tuning.html", {
        "car": car,
        "details": details
    })
