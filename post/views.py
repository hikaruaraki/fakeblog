from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import PostForm
from .models import Postmodels
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin





def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Postmodels()
            print(request)
            post.title = request.POST['title']
            post.post = request.POST['post']
            post.media = request.FILES['media']
            post.published_date = timezone.now()
            post.save()
            return redirect('/comp', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def comp(request):
    return render(request,'comp.html')

def view(request):
    title = request.POST.get('title')
    post = Postmodels(title=title)
    post.save()
    return HttpResponseRedirect(reverse('post:view2'))

def view2(request):
    post = Postmodels.objects.all()
    context = {'post':post}
    template = loader.get_template('view.html')
    return HttpResponse(template.render(context,request))


def syousai(request, post_id):
    post = Postmodels.objects.get(id=post_id)
    context = {'post':post}
    template = loader.get_template('syousai.html')
    return HttpResponse(template.render(context,request))



    
