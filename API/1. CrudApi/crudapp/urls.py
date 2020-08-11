from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('friend', views.FriendViewset)
router.register('belonging', views.BelongingViewset)
router.register('borrowed', views.BorrowedViewset)

urlpatterns = [
    path('api/', include(router.urls))
]