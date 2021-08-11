from django.urls import path
from . import views

urlpatterns = [
    path("",views.CattleListView.as_view(),name="index"),
    path("send/",views.send),
    path("delete/<int:pk>/",views.delete,name="delete"),
    path("update/<int:pk>",views.update,name="update"),
    path("excel/",views.excel,name="excel"),
    

]