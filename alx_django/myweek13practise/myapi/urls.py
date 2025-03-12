from django.urls import path,include
from .views import myfirstview, PlayerViewSet,CustomerViewSet
from rest_framework.routers import DefaultRouter 

router=DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'customers',CustomerViewSet)
urlpatterns = [
    path('mytrial/', view=myfirstview, name='trying'),
    path('', include(router.urls)),

]