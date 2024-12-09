from .views import *
from django.urls import path

urlpatterns = [
    path('api/portfolio/',PortfolioCreateListView.as_view(),name='portfolio-create'),
    path('api/contact/',ContactCreateListView.as_view(),name='contact-create')
]