from django.shortcuts import render
from .models import chai
# Create your views here.
def app_by_ankesh(request):
    chais = chai.objects.all()
    return render(request,'ankesh/ankesh_and_html.html',{'chais':chais})

def chai_detail(request,chai_id):
    chaiDetail = chai.objects.get(pk = chai_id)
    return render(request,'ankesh/chai_detail.html',{'chai':chaiDetail})

