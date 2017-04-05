from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Category, Post, Author, Contact
from .forms import ContactForm, ContactPhoneFormSet

def homepage(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories,
                                               'posts': posts})

def admin_post_detail(request):
    post = Post.objects.filter(author__main=True).order_by('-created_date').last()
    return redirect('post_detail', pk=post.pk)

def admin_author_detail(request):
    author = Author.objects.filter(main=True).order_by('pk').last()
    return redirect('author_detail', pk=author.pk)

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk,)
    posts = Post.objects.filter(author_id=author.id).order_by('-created_date')[:3]
    return render(request, 'blog/author.html', {'author': author,
                                              'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk,)
    categories = Category.objects.filter(post__author_id=post.author.id)
    return render(request, 'blog/post.html', {'categories': categories,
                                              'post': post})

def alt_homepage(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    categories = Category.objects.all()
    return render(request, 'blog/alt-home.html', {'categories': categories,
                                               'posts': posts})

def simplepage(request):
    return render(request, 'blog/page.html', {})

def favoritespage(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:4]
    categories = Category.objects.all()[:3]
    return render(request, 'blog/favorites.html', {'categories': categories,
                                               'posts': posts})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories.html', {'categories': categories})

def category_detail(request, pk):
    posts = Post.objects.filter(created_date__lte=timezone.now(), category_id=pk).order_by('-created_date')
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {'category': category,
                                                            'posts': posts})

def contactpage(request):
    contact_form = ContactForm(request.POST or None)
    phone_formset = ContactPhoneFormSet(instance=Contact())
    if contact_form.is_valid():
        contact = contact_form.save(commit=False)
        phone_formset = ContactPhoneFormSet(request.POST, instance=contact)
        if phone_formset.is_valid():
            contact.save()
            print(69)
            print(phone_formset)
            phone_formset.save()

    return render(request, 'blog/contact.html',
                  {'form': contact_form,
                   'phone_formset': phone_formset})

def post_sidebar(request):
    post = Post.objects.get(author__main=True)
    categories = Category.objects.all()[:3]
    posts = Post.objects.all()[:4]
    return render(request, 'blog/post-sidebar.html', {'post': post,
                                                      'categories': categories,
                                                      'posts': posts})
