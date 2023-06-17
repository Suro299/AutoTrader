from django.db import models


class DetailType(models.Model):
    name = models.CharField("Detail", max_length = 50, default = "NoName")
    image = models.ImageField("Image")
    
    def __str__(self) -> str:
        return f"id - {self.id} |  {self.name}"



class Detail(models.Model):
    type = models.ForeignKey(DetailType, on_delete = models.CASCADE)
    level = models.PositiveIntegerField("Detail Level", default = 1)
    in_car = models.ForeignKey("Car", on_delete = models.DO_NOTHING, blank = True, null = True)
    def __str__(self) -> str:
        return f"id - {self.id} |  {self.type.name}  | Level - {self.level}"
    


class Car(models.Model):
    
    CAR_COLOR = (
        ('white', 'white'),
        ('black', 'black'),
        ('red', 'red'),
        ('blue', 'blue'),
    )
    
    name = models.CharField("Name", max_length = 255)
    price = models.PositiveBigIntegerField("Pirce", default = 0)
    image = models.ImageField("Image", default = None)
    color = models.CharField(max_length=7, choices= CAR_COLOR, default='white', blank = True)

    turbo = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_turbo", blank = True, null = True)
    engine = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_engine", blank = True, null = True)
    ecu = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_ecu", blank = True, null = True)
    clutch = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_clutch", blank = True, null = True)
    
    
    def __str__(self) -> str:
        return f"id - {self.id} |  {self.name}"