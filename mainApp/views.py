from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['If you have questions, ask by phone number', '+77004521571', 'cheto@gmail.com']})