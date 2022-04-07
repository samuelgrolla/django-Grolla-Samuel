from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import  ListView

# Create your views here.
def home(request):
    articoli= Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB(DetailView):
    model = Articolo
    template_name = "articolo_detail.html"

class ArticoloListView(ListView):
    model = Articolo
    template_name = "Lista_articoli.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context



