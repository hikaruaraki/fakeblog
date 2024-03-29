from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.template import loader
from .models import Commentmodels
from .forms import CommentForm
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import CreateView,DeleteView

def commentbase(request):
    comment = Commentmodels.objects.all()
    context = {'comment':comment}
    template = loader.get_template('commentbase.html')
    return HttpResponse(template.render(context,request))

def comment(request):
    if request.method == "POST":
        forms = CommentForm(request.POST)
        if forms.is_valid():
            comment = Commentmodels()
            print(request)
            comment.users = request.POST['users']
            comment.comment = request.POST['comment']
            comment.publishe_date = timezone.now()
            comment.save()
            return redirect('/success', pk=comment.pk)
    else:
        forms = CommentForm()
    return render(request, 'comment.html', {'forms': forms})

def success(request):
    return render(request,'success.html')

class CommentView(CreateView):
    model = Commentmodels
    form_class = CommentForm
    def form_valid(self, form):
        form.instence.author = self.request.user
        # article_pk = self.kwargs.get('pk')
        comment = form.save(commit=False)
        comment.save()
        return redirect('comment:success')
    
