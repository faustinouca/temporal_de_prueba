import datetime

from django.template import Template, Context
from django.http import HttpResponse


def fecha_actual(request):
    ahora = datetime.datetime.now()
    fp = open('/home/djangouser/templates/miplantilla.html')
    t = Template(fp.read()) 
    fp.close() 
    html = t.render(Context({'fecha_actual': ahora})) 
    return HttpResponse(html)
