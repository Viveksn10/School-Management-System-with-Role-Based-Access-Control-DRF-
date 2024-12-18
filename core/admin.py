from django.contrib import admin
from .models import CustomUser, Student, LibraryHistory, FeesHistory

#groups in django admin panel
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(LibraryHistory)
admin.site.register(FeesHistory)
