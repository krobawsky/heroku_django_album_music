from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Album, Track
from .serializers import AlbumSerializer, TrackSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def album_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return JSONResponse(serializer.data)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def track_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return JSONResponse(serializer.data)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def track_detail(request, pk):

    try:
        track = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return HttpResponse(status=404)
 
    if request.method == 'GET':
        serializer = TrackSerializer(track)
        return JSONResponse(serializer.data)
 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrackSerializer(track, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
 
    elif request.method == 'DELETE':
        track.delete()
        return HttpResponse(status=204)