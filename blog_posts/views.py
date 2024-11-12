from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import BlogForm
from django.http import JsonResponse

from .models import Blog

# Create your views here.
def blogHomePage(request):
    blog = Blog.objects.all()

    # if 'category' in request.GET:
    #     q=request.GET['category']
    #     blog = Blog.objects.filter(categories__categories__icontains=q)
    # else:
    #     blog = Blog.objects.all()
        
    response_data = {'blog': list(blog.values())}
    return JsonResponse(response_data)
    # return render(request, 'blog_posts/index.html', response_data)


def blogPost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your Post has been updated")
            return redirect('home')
    else:
        form = BlogForm()
        
    return render(request, 'blog_posts/blog.html', {'form':form})


def editBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)  
    return render(request, 'blog_posts/blog.html', {'form':form})


def DetailBlog(request, pk):
    blog = Blog.objects.get(id=pk)

    return render(request, 'blog_posts/details.html', {'blog':blog})

def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    
    if request.method == 'POST':
        blog.delete()
        messages.success (request, 'Blog was deleted Sucessfully')
        return redirect('home')
    
    return render(request, 'blog_posts/delete-blog.html', {'blog':blog})
        
    