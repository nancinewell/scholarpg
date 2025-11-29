from django.contrib import admin

# Register your models here.
from .models import Student, Behaviors, Skills, RandomEvents, Miracles

admin.site.register(Student)
admin.site.register(Behaviors)
admin.site.register(Skills)
admin.site.register(RandomEvents)
admin.site.register(Miracles)