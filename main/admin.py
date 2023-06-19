from django.contrib import admin
from .models import DetailType, Detail, Car, DealerCar, DealerDetail


admin.site.register(DetailType)
admin.site.register(Detail)
admin.site.register(Car)

admin.site.register(DealerCar)
admin.site.register(DealerDetail)