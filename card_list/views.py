from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
	if request.method == 'POST':
		form = CardForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = Card.objects.all
			messages.success(request, ('Item Has Been Added To List!'))
			return render(request, 'home.html', {'all_items': all_items})
	else:
		all_items = Card.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def about(request):
	my_name = 'Tom Nowak'	
	return render(request, 'about.html', {'name': my_name})	

def delete(request, card_id):
	item = Card.objects.get(pk=card_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect('home')	

def received(request, card_id):	
	item = Card.objects.get(pk=card_id)
	item.completed = True
	item.save()
	return redirect('home')	

def not_received(request, card_id):	
	item = Card.objects.get(pk=card_id)
	item.completed = False
	item.save()
	return redirect('home')	

def edit(request, card_id):
	if request.method == 'POST':
		item = Card.objects.get(pk=card_id)
		form = CardForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item Has Been Edited!'))
			return redirect('home')
	else:
		item = Card.objects.get(pk=card_id)
		return render(request, 'edit.html', {'item': item})		
