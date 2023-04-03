from django.urls import path
from . import views

urlpatterns = [
    path('json-to-xml/', views.json_to_xml, name='json_to_xml'),
    path('xml-to-json/', views.xml_to_json, name='xml_to_json'),
]
