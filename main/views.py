from django.shortcuts import render,HttpResponse,redirect
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import *
from .forms import *
from .filters import CattleFilter
from .tables import CattleTable
# Create your views here.
class CattleListView(SingleTableMixin,FilterView):
    model = Cattle
    table_class = CattleTable
    template_name = "index.html"
    filterset_class = CattleFilter
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CattleListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = AddCattle
        return context
def send(request):
    if request.method == "POST":
        Cattle.objects.create(buyer=request.POST.get("buyer"),salesorder=request.POST.get("salesorder"),cattleid=request.POST.get("cattleid"),slaughterorder=request.POST.get("slaughterorder"))
        return redirect("/")
    return HttpResponse("")
def delete(request,pk):
    item = Cattle.objects.get(id=pk)
    item.delete()
    return redirect("/")
    return HttpResponse("")
def update(request,pk):
    item = Cattle.objects.get(id=pk)
    form = AddCattle(instance=item)
    if request.method == "POST":
        form = AddCattle(request.POST,instance=item)
        if form.is_valid:
            form.save()
            return redirect("/")
        
    
    return render(request,"update.html",{"form":form})