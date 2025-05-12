from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.app_by_ankesh,name='ankesh_home'),
    path('<int:chai_id>/',views.chai_detail,name='chai_details')
]