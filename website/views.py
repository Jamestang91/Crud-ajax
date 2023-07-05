from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, AddRecordForm, RecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
    form = AddRecordForm()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records, 'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You Must be logged in that page")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Records Deleted Success")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be logged In...")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


# AJAX POST
@csrf_exempt
def save_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RecordForm(request.POST)
            if form.is_valid():
                rid = request.POST.get('recordid')
                created_at = request.POST.get('created_at_id')
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                phone = request.POST['phone']
                address = request.POST['address']
                city = request.POST['city']
                state = request.POST['state']
                zipcode = request.POST['zipcode']
                print('record id', rid)

                if not rid:
                    r = Record(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address,
                               city=city, state=state, zipcode=zipcode, created_at=created_at)
                else:
                    r = Record.objects.get(pk=rid)  # Retrieve the existing record
                    r.first_name = first_name
                    r.last_name = last_name
                    r.email = email
                    r.phone = phone
                    r.address = address
                    r.city = city
                    r.state = state
                    r.zipcode = zipcode

                r.save()

                rec = Record.objects.values()
                record_data = list(rec)
                return JsonResponse({'status': 'Data Saved', 'record_data': record_data})
            else:
                return JsonResponse({'status': 'Not Saved'})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


@csrf_exempt
def delete_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST.get('rid')
            r = Record.objects.get(pk=id)
            r.delete()
            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 0})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


@csrf_exempt
def edit_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST.get('rid')
            record = Record.objects.get(pk=id)
            record_data = {'id': record.id, 'created_at': record.created_at, 'first_name': record.first_name,
                           'last_name': record.last_name, 'email': record.email, 'phone': record.phone,
                           'address': record.address, 'city': record.city, 'state': record.state, 'zipcode': record.zipcode}
            return JsonResponse(record_data)
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')

