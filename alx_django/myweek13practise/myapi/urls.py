from django.urls import path,include
from .views import myfirstview, PlayerViewSet
from rest_framework.routers import DefaultRouter 

router=DefaultRouter()
router.register(r'players', PlayerViewSet)
urlpatterns = [
    path('mytrial/', view=myfirstview, name='trying'),
    path('', include(router.urls)),

]