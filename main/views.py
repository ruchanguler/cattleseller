import io
from django.http import response
from django.shortcuts import render,HttpResponse,redirect
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import *
from .forms import *
from .filters import CattleFilter
from .tables import CattleTable
import xlsxwriter
from io import StringIO,BytesIO
import xlwt
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
        form = AddCattle(request.POST)
        if form.is_valid():
            if Cattle.objects.filter(buyer=request.POST.get('buyer')).exists():
                return redirect('/')
                

            else:
                form.save()
                return redirect('/')
                
             
            
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
def excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="sira.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data')

   
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ["İsim","Satış Sırası","Hayvan Numarası","Kesim Sırası","Tel" ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

   
    font_style = xlwt.XFStyle()

    rows = Cattle.objects.all().values_list("buyer","salesorder","cattleid","slaughterorder","phonenumber")
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
   