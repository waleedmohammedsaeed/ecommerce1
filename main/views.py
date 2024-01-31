from django.shortcuts import render

# Create your views here.
def main(request):
	return render(request, 'main.html')

def products(request):
	return render(request, 'products.html')

def activities(request):
	return render(request, 'activities.html')

def aboutus(request):
	return render(request, 'aboutus.html')

def clients(request):
	return render(request, 'clients.html')

def client(request):
	return render(request, 'client.html')

def energy(request):
	return render(request, 'services/energy.html')

def marketing(request):
	return render(request, 'services/marketing.html')

def catering(request):
	return render(request, 'services/catering.html')

def constructing(request):
	return render(request, 'services/constructing.html')