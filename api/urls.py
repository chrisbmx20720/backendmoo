from django.urls import path
from . import views

'''
from .views import LeerArchivoPdf


urlpatterns=[
    path('procesar-pdf/', LeerArchivoPdf.as_view(), name='procesar_pdf')
]
'''
urlpatterns = [
    path('', views.LeerArchivoPdf, name='procesar_pdf'),
]