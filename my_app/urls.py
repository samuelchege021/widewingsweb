


from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("biodigester/",views.biodigester,name='biodigester'),
    path("solar/",views.solar,name="solar"),
    path("water/",views.water,name="water"),
    path("plumbing/",views.plumbing,name="plumbing"),
    
    
    path("contact/",views.contact,name="contact"),
    
    
]
