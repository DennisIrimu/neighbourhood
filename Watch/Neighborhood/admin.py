from django.contrib import admin
from .models import Neighborhood,UserProfile,Business,Post,Services
# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Services)
