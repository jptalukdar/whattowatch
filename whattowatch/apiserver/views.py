import imp
from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def getMovie(request):
  response = {
    "Movie" : "The silent voice",
    "Category" : "Anime",
    "Year" : 2016
  }
  return JsonResponse(response)
