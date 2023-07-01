from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('addProduct/', add_product, name='addProduct'),
    path('addModule/', add_module, name='addModule'),
    path('addChoiceImage/', add_choice_image, name='addChoiceImage'),
]
