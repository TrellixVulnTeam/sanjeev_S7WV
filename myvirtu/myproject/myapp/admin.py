from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Functions_Master)
admin.site.register(Employee)
admin.site.register(CourtSeat_Master)
admin.site.register(CourtType_Master)
admin.site.register(WorkBench1_Master)
admin.site.register(WorkBench2_Master)
admin.site.register(WorkBench3_Master)
admin.site.register(WorkBench4_Master)
admin.site.register(WorkFlowStatus_Master)
admin.site.register(SiteStatus_Master)
admin.site.register(PositionWeight_Master)
admin.site.register(Gender_Master)
admin.site.register(Country_Master)
admin.site.register(TABLE_AUDIT)

