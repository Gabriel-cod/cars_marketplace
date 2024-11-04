from .models import Car
from .forms import CarForm
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CarsListView(ListView):
    model = Car
    template_name = 'cars/listed_cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        filtered_cars = super().get_queryset().order_by('-value')
        search = self.request.GET.get('search')
        
        if search:
            filtered_cars = filtered_cars.filter(model__contains=search)

        models = super().get_queryset().order_by('model')
        cars = {
            'filtered_cars': filtered_cars,
            'models': models
        }
        return cars

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SellCreateView(CreateView):
    model = Car
    template_name = 'cars/sell.html'
    form_class = CarForm
    success_url = '/cars/'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    template_name = 'cars/update_car.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy('car_detail_view', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/confirm_delete.html'
    success_url = '/cars/'
