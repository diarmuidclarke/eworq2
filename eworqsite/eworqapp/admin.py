from django.contrib import admin



from .models import eWORQ_Request, eWORQ_CopyFile

admin.site.register(eWORQ_Request)
admin.site.register(eWORQ_CopyFile)