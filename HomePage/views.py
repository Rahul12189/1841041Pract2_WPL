from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse(" Hello, This is Rahul Kadam From T3 Batch with PRN 1841041. Rahul Kadam GCOEJ")
