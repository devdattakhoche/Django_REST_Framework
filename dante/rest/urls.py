from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'Hospitali', views.HospitalViewSet)
router.register(r'Hospitalj', views.HospitalViewSet1)


urlpatterns = [
    path('Hospitals/',views.Hospital_list,name = 'Hospitals'),
    path('Hospitals_list/',views.Hospital_list.as_view(),name = 'Hospitals_list'),
    path('Hospitals_list1/',views.HospList.as_view(),name = 'Hospitallist'),
    path('Hospitals_list12/',views.HospitalList12.as_view(),name = 'Hospitallist'),
    path('Hospitals_list1/<int:pk>/',views.Detailed_view.as_view(),name = 'Hospitals_list'),
    path('Hospitals_list12/<int:pk>/',views.HospitalDetail12.as_view(),name = 'Hospitals_list'),
    path('Hospitals/<int:Hospital_id>/', views.Hospital_detail),
    path('Hospitals_list/<int:Hospital_id>/',views.Hospital_detail1.as_view(),name = 'Hospitals_detail'),
    path('', include(router.urls)),
]
# urlpatterns = format_suffix_patterns(urlpatterns)F