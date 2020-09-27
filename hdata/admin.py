from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from hdata.models import File


admin.site.register(File, DraggableMPTTAdmin)