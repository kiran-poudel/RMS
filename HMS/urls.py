"""
URL configuration for HMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import MenuCategoryApiView,MenuItemApiView,MenuItemDetailApiView,OrderApiView,OrderDetailApiView,WaiterApiView,WaiterDetailApiView,ReceptionApiView,ReceptionDetailApiView,register_employee,login,register_management,BillListCreateView,BillRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    # MenuCategory URLS
    path('menu-category/', MenuCategoryApiView.as_view({'get':'list','post':'create'})),
    path('menu-category/<int:pk>/', MenuCategoryApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),

    #MenuItems URLS

    path('menu-item/',MenuItemApiView.as_view()),
    path('menu-item/<int:pk>/',MenuItemDetailApiView.as_view()),

    #Order URlS

    path('order/',OrderApiView.as_view()),
    path('order/<int:pk>/',OrderDetailApiView.as_view()),

    #Waiter URLS
    path('waiter/',WaiterApiView.as_view()),
    path('waiter/<int:pk>/',WaiterDetailApiView.as_view()),
    
    #Reception URLS
    path('reception/',ReceptionApiView.as_view()),
    path('reception/<int:pk>/',ReceptionDetailApiView.as_view()),

    #register,login URLS
    path('register-employee/',register_employee),
    path('register-management/',register_management),
    path('login/',login),

    #Bills urls
   path('bills/', BillListCreateView.as_view(), name='bill-list-create'),
   path('bills/<int:pk>/', BillRetrieveUpdateDestroyView.as_view(), name='bill-detail'),
    
    
]
