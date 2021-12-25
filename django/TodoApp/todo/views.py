from django.shortcuts import render
from .models import WorkTodo # Import our WorkTodo model
from .serializers import WorkSerializer # Import the serializer we just created

# Create your views here.


# Import django rest framework functions

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class WorkViewSet(viewsets.ModelViewSet): # Create a class based view
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = WorkTodo.objects.all() # Select all taks
    serializer_class = WorkSerializer # Serialize data