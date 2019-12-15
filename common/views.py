from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin)

from django.views.generic import ListView, DetailView


class AuthenticatedListView(LoginRequiredMixin, ListView):
    login_url = 'account_login'


class AuthenticatedDetailView(LoginRequiredMixin, DetailView):
    login_url = 'account_login'


class AuthorizedListView(PermissionRequiredMixin, AuthenticatedListView):
    pass


class AuthorizedDetailView(PermissionRequiredMixin, AuthenticatedDetailView):
    pass
