from django.contrib import admin
from .models import Library
from embed_video.admin import AdminVideoMixin

# Register your models here.

class LibraryAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('exercise_Title', 'exercise_Body',)
    list_filter = ('exercise_Title',)
    search_fields = ('exercise_Title',)

admin.site.register(Library, LibraryAdmin)



