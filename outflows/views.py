from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from config.metrics import get_sales_metrics
from outflows.forms import OutflowForm
from outflows.models import Outflow
from outflows.serializers import OutflowSerializer


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = "outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 10
    permission_required = "outflows.view_outflow"

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sales_metrics"] = get_sales_metrics()

        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = "outflow_create.html"
    form_class = OutflowForm
    success_url = reverse_lazy("outflow_list")
    permission_required = "outflows.add_outflow"


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = "outflow_detail.html"
    permission_required = "outflow_view_outflow"


class OutflowCreateListAPIView(ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer


class OutflowRetrieveAPIView(RetrieveAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
