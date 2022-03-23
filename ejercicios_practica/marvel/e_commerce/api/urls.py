from django.urls import path
from e_commerce.api.hello_world_api import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('hello-world/', hello_world),
    path('request-data/', return_request_data),
    path('comics/', get_comics),
    path('purchased_item/', purchased_item),
    
    # 3 Vistas de Tarea:
    path('welcome/', welcome),
    path('grade_homework/', grade_homework),
    path('guess_number/', guess_number),
]
