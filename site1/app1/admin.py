from django.contrib import admin
from .models import Question,Choice,BenhNhan,PhongKham
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(BenhNhan)
admin.site.register(PhongKham)