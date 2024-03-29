from django.contrib import admin
from pinapp.models import Category,Image,Follow,Board
from pinapp.models import Comments,ChatMessage
admin.site.register(Category),
admin.site.register(Image),
admin.site.register(Comments),
admin.site.register(Follow),
admin.site.register(Board),
admin.site.register(ChatMessage)

# Register your models here.
