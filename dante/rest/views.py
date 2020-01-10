from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from dante.models import Hospital,Dept
from .serializers import HospitalSerializer , DepartmentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
@csrf_exempt
@api_view(['GET','POST'])
def Hospital_list(request , format = None):
    """
    List all code Hospitals, or create a new Hospital.
    """
    if request.method == 'GET':
        Hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(Hospitals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HospitalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=400)
@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def Hospital_detail(request, Hospital_id):
    """
    Retrieve, update or delete a code Hospital.
    """
    try:
        x = Hospital.objects.get(Hospital_id = Hospital_id)
    except Hospital.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HospitalSerializer(x)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HospitalSerializer(x, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        x.delete()
        return HttpResponse(status=204)

class Hospital_list(APIView):
    def get(self , request , format = None):
        x = Hospital.objects.all()
        serializer = HospitalSerializer(x, many = True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self,request,format = None):
        serializer = HospitalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
class Hospital_detail1(APIView):
    def get_object(self , Hospital_id):
        try:
            return Hospital.objects.get(Hospital_id = Hospital_id)
        except Hospital.DoesNotExist:
            raise Http404
    def get(self,request,Hospital_id,format =None):
        x = self.get_object(Hospital_id)
        serializer = HospitalSerializer(x)
        return Response(serializer.data)
    
    def put(self,request,Hospital_id,format=None):
        x = self.get_object(Hospital_id)
        serializer = HospitalSerializer(x , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,Hospital_id,format=None):
        x = self.get_object(Hospital_id)
        x.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        pass
class Detailed_view(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class HospList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HospitalList12(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalDetail12(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class HospitalViewSet1(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer