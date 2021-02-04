from django.contrib import admin
from .models import Theme, Cours, Question, Td, Qcm

# Register your models here.

admin.site.register(Theme)
admin.site.register(Cours)
admin.site.register(Question)
admin.site.register(Td)
admin.site.register(Qcm)