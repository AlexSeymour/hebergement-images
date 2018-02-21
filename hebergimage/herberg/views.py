from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from herberg.forms import ImageForm
from django.contrib import messages
from herberg.models import Image
from django.core.paginator import Paginator, InvalidPage
from django.contrib.auth.decorators import login_required


def home(request, page="1"):
    image_list = Image.objects.all()
    pages = Paginator(image_list, 5)
    try:
        images = pages.page(page)
    except InvalidPage:
        images = pages.page(1)

    return render(request, 'home.html', {"images": images})

@login_required
def post_image(request):

    if request.method == "POST":

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():

            image = form.save(commit=False)
            image.user = request.user
            image.save()
            messages.add_message(request, messages.SUCCESS, "Vous avez déposé une image.")
            return redirect('/')

    else:
        form = ImageForm()

    return render(request, "herberg/post_image.html", {"form": form})

@login_required
def delete_image(request, pk):
    try:
        Image.objects.get(user=request.user, pk=pk).delete()
        messages.add_message(request, messages.SUCCESS, "Vous avez supprimé une image.")
    except:
        pass

    return redirect('/')

