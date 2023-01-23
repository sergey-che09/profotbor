from django.shortcuts import render
from django.http import HttpResponse
from .models import Position, Branch, Control, Subdivision, Access, Materials, Specialist, Visibility, Candidate, ViewStatus

from django.core.paginator import Paginator


def index(request):
    # candidates = Candidate.objects.all()
    viewcandidates = ViewStatus.objects.all()
    # paginator = Paginator(candidates, 10)
    paginator = Paginator(viewcandidates, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {"viewcandidates": page_obj},)


