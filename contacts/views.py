from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contactform
from .models import people


def index(request):
    people_list = people.objects.all()
    context = {'people_list': people_list}
    return render(request, 'contacts/index.html', context)


def detail(request, id=None):
    instance = get_object_or_404(people, id=id)
    context = {"name": instance.name,
               "instance": instance}
    return render(request, 'contacts/detail.html', context)


def update(request, id=None):
    instance = get_object_or_404(people, id=id)
    form = contactform(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
        messages.success(request, "Saved")
    context = {
        "name": instance.name,
        "instance": instance,
        "form": form,
    }
    return render(request, "contacts/people_form.html", context)


def create(request):
    form = contactform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.success(request, "Not Successfully Created")
    context = {
        "form": form,
    }
    return render(request, "contacts/people_form.html", context)


def delete(request, id=None):
    instance = get_object_or_404(people, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("contacts:index")
