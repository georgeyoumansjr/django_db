from django.shortcuts import render, redirect
from .models import MockData
from .forms import MockDataForm

def add_mock_data(request):
    if request.method == 'POST':
        form = MockDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_mock_data')
    else:
        form = MockDataForm()
    return render(request, 'add_mock_data.html', {'form': form})

def display_mock_data(request):
    mock_data = MockData.objects.all()
    return render(request, 'display_mock_data.html', {'mock_data': mock_data})
