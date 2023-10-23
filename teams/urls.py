from django.urls import path, include
from rest_framework import routers

from teams.views import TeamViewSet, MemberViewSet

router = routers.DefaultRouter()
router.register("teams", TeamViewSet)
router.register("members", MemberViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "teams"
