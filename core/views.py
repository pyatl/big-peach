from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from events.models import Event


class IndexView(TemplateView):
    ''' Index Page '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(
            published=True)[:3] # 3 upcoming events
        return context
