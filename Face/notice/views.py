from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from notice.models import *


class NoticesListView(ListView):
    model = Notices
    paginate_by = 3
    template_name = 'notice/notices_list.html'  # DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'notice_list'  # DEFAULT : <model_name>_list

    def get_queryset(self):
        notice_list = Notices.objects.order_by('-id')
        return notice_list


class NoticesDetailView(DetailView):
    model = Notices


