from django.views.generic import TemplateView


class BasePageView(TemplateView):
    template_name = 'index.html'
