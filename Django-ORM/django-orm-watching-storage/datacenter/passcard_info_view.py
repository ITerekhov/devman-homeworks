from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    passcard_visits = Visit.objects.filter(passcard=passcard)
    for visit in passcard_visits:
        duration = visit.format_duration()
        visit_data = {
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': visit.is_visit_long()}
        this_passcard_visits.append(visit_data)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
