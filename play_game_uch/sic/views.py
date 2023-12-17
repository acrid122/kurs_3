from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Stat
from .serializers import StatSerializer

# class StatListPagination(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'page_size'
#     max_page_size = 100

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
class StatView(APIView):
    serializer_class = StatSerializer
    # pagination_class = StatListPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        queryset = Stat.objects.all()


        serializer = self.serializer_class(queryset, many=True)
        return render(request, 'sic/index.html', {'stats': serializer.data})


class UserStatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user_stat = Stat.objects.filter(user_id=user_id).first()
        if user_stat:
            serializer = StatSerializer(user_stat)
            return render(request, 'sic/one_user.html', {'stats': serializer.data})
        else:
            return Response({'error': 'Твоя статистика не была найдена'}, status=404)
