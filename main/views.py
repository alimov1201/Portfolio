from django.shortcuts import render, get_object_or_404
from main.models import Work, Teacher, Article
from django.core.paginator import Paginator
from main.forms import CommentForm, ContactForm, EmailForm

def main(request):
    teachers = Teacher.objects.all()[::6]
    articles = Article.objects.all()
    work = Work.objects.all()
    paginator = Paginator(work, 4)
    page_num = request.GET.get('page')
    if not page_num:
        page_num = 1  
    pages = paginator.num_pages
    if int(page_num) > pages or int(page_num) < 1:
        page_num = 1
    page_obj = paginator.get_page(page_num)

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'articles': articles,
        'page_obj': page_obj,
        'page_number': page_num,
        'teachers': teachers,
        'form': form,
    }
    return render(request, 'index.html', context=context)

def single(request, id):
    article = get_object_or_404(Article, id=id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            print(form.errors)
    mail = EmailForm()
    if request.method == 'POST':
        mail = EmailForm(request.POST)
        if mail.is_valid():
            mail.save()

    comments = article.comments.all()
    context = {
        "article": article,
        'form': form,
        'comments': comments,
        'mail': mail
    }
    return render(request, 'blog-single.html', context=context)
