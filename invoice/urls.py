


from django.urls import path
from .views import InvoicePageView
urlpatterns = [
path("", InvoicePageView.as_view(), name="invoice"),
]
