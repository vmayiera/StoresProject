"""StoresProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from materials import views
from materials.views import MaterialDetailView, MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="materials-home"),
    path('material/', views.material, name="materials-material"),
    path('list/', MaterialListView.as_view(), name="materials-list"),
    path('details/<int:pk>/', MaterialDetailView.as_view(), name="materials-detail"),
    path('material/new/', MaterialCreateView.as_view(), name="materials-create"),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name="materials-update"),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name="materials-update"),
]
