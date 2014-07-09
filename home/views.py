# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def contact(request):
    data = {}
#
#    form = ContactForm(request.POST or None)
#    data['form'] = form
#    if request.method == "POST":
#        if form.is_valid():
#            form.save()
#            data['sent'] = True
#            data['form'] = ContactForm()
#        else:
#            data['invalid'] = True

    return render_to_response('contact/index.html', data, context_instance=RequestContext(request))

def home(request):
    data = {}

    return render_to_response('home/index.html', data, context_instance=RequestContext(request))

def about(request):
    data = {}

    return render_to_response('about/index.html', data, context_instance=RequestContext(request))

def work(request):
    data = {}

    return render_to_response('work/index.html', data, context_instance=RequestContext(request))