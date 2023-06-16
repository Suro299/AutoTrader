from django.db import models


class DetailType(models.Model):
    name = models.CharField("Detail", max_length = 50, default = "NoName")
    
    def __str__(self) -> str:
        return f"{self.id} | {self.name}"



class Detail(models.Model):
    type = models.ForeignKey(DetailType, on_delete = models.CASCADE)
    level = models.PositiveIntegerField("Detail Level", default = 0)
    
    def __str__(self) -> str:
        return f"{self.id} | {self.type} | {self.level}"
    


class Car(models.Model):
    name = models.CharField("Name", max_length = 255)
    turbo = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_turbo", blank = True, null = True)
    engine = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_engine", blank = True, null = True)
    ecu = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_ecu", blank = True, null = True)
    clutch = models.ForeignKey(Detail, on_delete = models.DO_NOTHING, related_name = "car_clutch", blank = True, null = True)
    
    
    def __str__(self) -> str:
        return f"{self.id} | {self.name}"