from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, FormView

from qna.models import QnA, Comment


class QnAListView(ListView):
    model = QnA
    paginate_by = 5
    template_name = 'qna/list.html'  # DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'qna_list'  # DEFAULT : <model_name>_list

    def get_queryset(self):
        qna_list = QnA.objects.order_by('-id')
        return qna_list


class QnADetailView(DetailView):
    model = QnA


def create(request):
    c = QnA()
    c.member = request.user
    c.q_title = request.POST['title']
    c.q_data = request.POST['q_data']
    c.q_date = timezone.datetime.now()
    c.save()
    return render(request, 'qna/qna_create.html')


def new(request):
    if request.user.is_authenticated:
        return render(request, 'qna/qna_create.html')
    else:
        a = QnA.objects
    return render(request, 'qna/write_error.html', {'a': a, 'error': 'You have to login to make newpost'})


class QnADeleteView(DeleteView):
    model = QnA
    success_url = reverse_lazy('qna:List')


class QnAUpdateView(UpdateView):
    model = QnA
    fields = ['q_title', 'q_data', 'q_password']
    success_url = reverse_lazy('qna:List')
    template_name_suffix = '_update'

# def QnACreateView(request):
#    if not request.user.is_authenticated:
#        return redirect('/account/login')
#
#    if request.method == "GET":
#        form = BoardForm()
#
#    elif request.method == "POST":
#        form = BoardForm(request.POST)
#        if form.is_valid():
#            user_id = request.user.is_authenticated
#            user = User.objects.get(pk = user_id)
#            new_board = QnA(
#                q_title = form.cleaned_data['q_title'],
#                q_data = form.cleaned_data['q_data'],
#                member = user
#            )
#            new_board.save()
#            return redirect('qna/qna_list.html')
#
#    return render(request, 'qna/qna_create.html', {'form':form})



