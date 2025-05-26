from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    return JsonResponse({
        "message": "Welcome to the API",
        "status": "running",
        "endpoints": {
            "admin": "/admin/",
            "auth": "/api/auth/"
        }
    })

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
] 