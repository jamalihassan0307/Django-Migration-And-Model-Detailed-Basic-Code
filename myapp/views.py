from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Artist

def create_artist(request):

    artist = Artist(first_name = "Atif", last_name = "Aslam", bio = "A pakistanin pop singer")
    artist.save()
    return HttpResponse(f"A singer is created with an ID of {artist.id}")


def fetch_artists(request):
    artists = Artist.objects.all()
    context = {'singers':artists}

    return render(request, 'artists.html', context)


def delete_artist(request, pk):
    artist = get_object_or_404(Artist, id = pk) 
    artist.delete()
    return redirect('artists')


def edit_artist(request, pk):
     artist = get_object_or_404(Artist, id = pk)

     artist.first_name = "Rahat"
     artist.last_name = "Khan"

     artist.save()

     return redirect('artists')   



    




# Create your views here.
def message(request):
	return HttpResponse("<h1 style = 'color:red'>Welcome to my website</h1>")


def greeting(request):
	return HttpResponse("Good Noon...")


def home(request):
	return render(request, 'home.html')

def contact(request):
	return render(request, 'contact.html')

def a(request):
	return render(request, 'a.html')

def b(request):
	return render(request, 'b.html')

def c(request):
	return render(request, 'c.html')


def response(request):

	context = {'uname': 'john doe', 'email': 'john@gmail.com', 'age':50, 'intersts':['coding','reading', 'swimming', 'sleeping']}



	return render(request, 'response.html', context)

# def submit_form(request):
# 	if request.method == 'POST':
# 		#data recieved
# 		uname = request.POST.get('name') # request.POST['name']
# 		uemail = request.POST.get('email')
# 		password = request.POST.get('pass')

# 		return HttpResponse(f" username : {uname}, email : {uemail}, password : { password}")


# 	return render(request, 'form.html')


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        age = request.POST.get("age")
        dob = request.POST.get("dob")
        time = request.POST.get("time")
        interests = request.POST.getlist("interests")  # Multiple checkboxes
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        message = request.POST.get("message")
        file = request.FILES.get("file")

        # Process the data (For now, just returning a response)
        return HttpResponse(f"Received Data: {name}, {email}, {password}, {age}, {dob}, {time}, {interests}, {gender}, {country}, {message}, {file}")

    return render(request, "form.html")


def url_data(request, email):
    return HttpResponse(f"email : {email}")


