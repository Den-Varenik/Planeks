from django.contrib.auth import logout, decorators, views
from django.shortcuts import redirect
from django.urls import reverse_lazy

from account.forms import LoginUserForm


class UserLoginView(views.LoginView):
    form_class = LoginUserForm
    template_name = 'account/user_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy("home:index")


@decorators.login_required
def logout_user(request):
    logout(request)
    return redirect("account:login")
