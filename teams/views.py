from rest_framework import viewsets

from teams.models import Team, Member
from teams.serializers import TeamSerializer, MemberSerializer, MemberListSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return MemberListSerializer

        return MemberSerializer
