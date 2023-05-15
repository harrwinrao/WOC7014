from django.shortcuts import render
from .models import Model, Brand
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    models = Model.objects.all()
    brands = Brand.objects.all()
    context = {
        'brands': list(brands),
        'models': list(models)
    }
    logger.info("Context: ", context)
    return render(request, "gamereview.html", context)
