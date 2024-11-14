from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from tasks.setializer import TaskSerializer
from .models import Task


class TasksPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000
@method_decorator(cache_page(30), name='dispatch')
class GetAndCreateTask(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = TasksPagination
    def get_queryset(self):
        queryset = Task.objects.all()
        filter_by = self.request.query_params.get('filter_by')
        filter_value = self.request.query_params.get('filter_value')
        sort_by = self.request.query_params.get('sort_by')

        if filter_by and filter_value:
            if filter_by == 'status':
                queryset = queryset.filter(status=filter_value)
            elif filter_by == 'priority':
                queryset = queryset.filter(priority=filter_value)
            elif filter_by == 'time_create':
                queryset = queryset.filter(time_create=filter_value)
        if sort_by:
            queryset = queryset.order_by(sort_by)
        else:
            queryset = queryset.order_by("id")
        return queryset

class GetUpdateDeleteTaskById(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
