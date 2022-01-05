from task.models import *
from django.http import JsonResponse
# Create your views here.

def collection_frequency(request):
    bin_operation = list(BinOperation.objects.all().values('bin__latitude', 'bin__longitude', 'operation__name',
                                                           'collection_frequency', 'last_collection'))
    return JsonResponse(bin_operation, safe=False)


def navigation_record(request):
    import datetime
    response = dict()
    before_two_days = datetime.datetime.now() - datetime.timedelta(days=2)
    records = list(NavigationRecord.objects.filter(datetime__gte=before_two_days).
                   values('latitude', 'longitude', 'datetime','vehicle__plate').distinct('vehicle__plate').order_by('vehicle__plate', '-datetime' ))
    response['last_points'] = records
    return JsonResponse(response, safe=False)