
from .serializers import UserSerializer
from django.http import JsonResponse
from ..models import User

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

'''
{
    url: '',
    method: 'GET'/'POST'/...
    data:{},
    headers: {}
}

POST :      CreateAPIView
GET:        ListAPIView, RetrieveAPIView
PUT/PATCH:  UpdateAPIView
DELETE:     DeleteAPIView


1. ListCreateAPIView
2. RetrieveUpdateDeleteAPIView

Country
    countryName = ..

State
    stateName = ..

City
    my_State = .. ForeignKey
    cityName = ..


'''

class user_List(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class user_Detail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

def user_list(request):
    if request.method == 'GET':
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

