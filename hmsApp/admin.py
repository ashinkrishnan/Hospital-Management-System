from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)

admin.site.register(CardioDoc)
admin.site.register(OrthoDoc)
admin.site.register(UroDoc)
admin.site.register(PulmonoDoc)

admin.site.register(Appointment)


