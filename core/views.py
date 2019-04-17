from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request,"index.html")
def cadastro(request):
	return render(request,"cadastro.html")
def login(request):
	return render(request,"login.html")
def notas(request):
	return render(request,"Notas.html")
def RA(request):
	return render(request,"RA.html")
def nomes(request):
	return render(request,"Nomes.html")