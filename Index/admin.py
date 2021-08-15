from django.contrib import admin

from .models import about
from .models import slider
from .models import feature
from .models import service
from .models import client
from .models import team
from .models import category
from .models import product


admin.site.register(about)
admin.site.register(slider)
admin.site.register(feature)
admin.site.register(service)
admin.site.register(team)
admin.site.register(client)



@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat_nm']


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name', 'image', 'cat']
