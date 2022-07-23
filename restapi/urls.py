from rest_framework import routers

from .views import UserInfoViewSet


router = routers.DefaultRouter()
router.register('users', UserInfoViewSet)