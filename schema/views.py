from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic

from schema.forms import CSVForm
from schema.models import Schema


class SchemasListView(mixins.LoginRequiredMixin, generic.ListView):
    model = Schema
    context_object_name = 'schema'
    login_url = reverse_lazy("account:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Schemas"
        return context


class SchemaCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Schema
    form_class = CSVForm
    login_url = reverse_lazy("account:login")
    template_name = "schema/schema_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Schemas"
        return context

    def post(self, request, *args, **kwargs):
        # form = self.get_form()
        # if form.is_valid():
        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)
        pass
