
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/aboutus.html'

