from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls.base import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView

from Credit.models import CreditCard


# @login_required(login_url='/accounts/login')


class CardListView(LoginRequiredMixin, ListView):
    model = CreditCard
    login_url = 'login'

    def get_queryset(self):
        # ret = CreditCard.objects.all()
        ret = CreditCard.objects.filter(owner=self.request.user)
        return ret


class CardDetailView(DetailView, LoginRequiredMixin):
    model = CreditCard
    login_url = 'login'

    def get_queryset(self):
        ret = CreditCard.objects.filter(owner=self.request.user).filter(id=self.kwargs['pk'])
        return ret



class CardUpdateView(UpdateView, LoginRequiredMixin):
    login_url = 'login'
    model = CreditCard
    fields = ['first_name', 'last_name', 'name_on_card', 'number', 'type', 'expiry_date']

    def get_success_url(self):
        return reverse('card-list')

    def get_queryset(self):
        ret = CreditCard.objects.filter(owner=self.request.user).filter(id=self.kwargs['pk'])
        return ret


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CardUpdateView, self).form_valid(form)


class CardCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = CreditCard
    fields = ['first_name', 'last_name', 'name_on_card', 'number', 'type', 'expiry_date']

    def get_success_url(self):
        return reverse('card-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CardCreateView, self).form_valid(form)


class CardDeleteView(DeleteView, LoginRequiredMixin):
    login_url = 'login'
    model = CreditCard

    def get_queryset(self):
        ret = CreditCard.objects.filter(owner=self.request.user).filter(id=self.kwargs['pk'])
        return ret

    def get_success_url(self):
        return reverse('card-list')




# def user_login(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect(reverse('card-list'))
#
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         if request.POST.get('next') != 'None':
#             return HttpResponseRedirect(request.POST.get('next'))
#
#         return render(request, 'Credit/creditcard_list.html')
#
#     return render(request, 'registration/login.html')
#
#
# def user_logout(request):
#     logout(request)