from django.urls import path
from  . import views

urlpatterns = [
    path('ShowProducts', views.Show_products, name='showProducts'),
    path('pdfReports',views.pdf_report_create,name='PdfReport')
    
]

