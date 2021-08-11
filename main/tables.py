import django_tables2 as tables
from .models import Cattle

class CattleTable(tables.Table):
    class Meta:
        model = Cattle
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("buyer","salesorder","cattleid","slaughterorder","phonenumber")
    Sil = tables.TemplateColumn(template_name="links.html",)
    #phonenumber = tables.TemplateColumn(template_name="phonenum.html")

