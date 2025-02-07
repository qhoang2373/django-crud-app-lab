from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('parks/', views.park_index, name='park-index'),
    path('parks/<int:park_id>', views.park_detail, name='park-detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='park-create'),
    path('parks/<int:pk>/update/', views.ParkUpdate.as_view(), name='park-update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='park-delete'),
    path('parks/<int:park_id>/add-trail/', views.add_trail, name='add-trail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('trails/<int:pk>/update/', views.TrailUpdate.as_view(), name='trail-update'),
    path('trails/<int:pk>/delete/', views.TrailDelete.as_view(), name='trail-delete'),
    
    path('trails/', views.TrailList.as_view(), name='trail-index')

    # path('trails/<int:pk>/', views.TrailDetail.as_view(), name='trail-detail'),
 
]


