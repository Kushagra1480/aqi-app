from django.shortcuts import render

# Create your views here.
# A view is a function that takes a web request and returns a response
from rest_framework import generics # pre-built model to create views 
from .models import Location
from .serializers import LocationSerializer

# ListAPIView is a GET request
# CreateAPIView is a POST request
class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all() # defines what table to use for queries
    serializer_class = LocationSerializer # defines what serializer to use
    
    def get(self, request, pk):
        # Returns a single Location object
        return self.retrieve(request, pk)
    def put(self, request, pk):
        # Updates a Location object
        return self.update(request, pk)
    def patch(self, request, pk):
        # Partially updates a Location object
        return self.partial_update(request, pk)

class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all() 
    serializer_class = LocationSerializer