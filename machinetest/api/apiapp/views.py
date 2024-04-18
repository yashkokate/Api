from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .serializers import *

class ClientView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Client.objects.all() 
    def get(self, request,format=None):
        client_obj = Client.objects.all()
        serializer = ClientSerializer(client_obj, many=True)
        return Response({'data': serializer.data})
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Client Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        client_obj = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        client_obj = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        client_obj = Client.objects.get(pk=pk)
        client_obj.delete()
        return Response({'msg': 'Client deleted'}, status=status.HTTP_204_NO_CONTENT)


class ProjectView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        project_obj = Project.objects.all()
        serializer = ProjectSerializer(project_obj, many=True)  # Use ProjectSerializer instead of ClProientSerializer
        return Response({'data': serializer.data})
    
    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Project Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        project_obj = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Project updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        project_obj = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(project_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Project updated partially'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        project_obj = Project.objects.get(pk=pk)
        project_obj.delete()
        return Response({'msg': 'Project deleted'}, status=status.HTTP_204_NO_CONTENT)
