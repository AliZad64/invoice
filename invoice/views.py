from django.views.generic import TemplateView
# Create your views here.

class InvoicePageView(TemplateView):
    template_name = "index.html"
