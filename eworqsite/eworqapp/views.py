from django.http import HttpResponse
from django.template import loader

from .models import eWORQ_Request


def index(request):
    
    active_eworq_list = eWORQ_Request.objects.order_by('-eWORQ_raised_date')[:5]
    template = loader.get_template('eworqapp/index.html')
    context = {
        'active_eworq_list': active_eworq_list,
    }
    return HttpResponse(template.render(context, request))
