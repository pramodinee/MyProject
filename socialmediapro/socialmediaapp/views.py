
from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms import modelformset_factory
from django.contrib import messages


def post_list(request):
    post_list = post.objects.all().order_by('-id')
    query = request.GET.get('query')
    if query:
        post_list  = post.objects.filter(
            Q(title__contains = query) |
            Q(body__contains = query) |
            Q(author__username = query)
        )
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render (request,'post_list.html',{'posts': posts })

def post_detail(request,id,slug):
    post1 = get_object_or_404(post,id=id,slug=slug)
    is_liked = False
    comments = Comment.objects.filter(post=post1).order_by('-id')
    if post1.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method =='POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment = Comment.objects.create(post = post1 , user = request.user, content=content)

            comment.save()
            return redirect('/')
    else:
        comment_form = CommentForm

    return render (request,'post_detail.html',
                   {'post':post1,'is_liked':is_liked,
                    'total_likes':post1.total_likes(),
                    'comments':comments,
                    'comment_form':comment_form})

def like_post(request):
    pid = request.POST.get('post_id')
    posts = get_object_or_404(post,id = pid)
    if posts.likes.filter(id=request.user.id).exists():
        posts.likes.remove(request.user)
        is_liked = False
    else:
        posts.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(posts.get_absolute_url())

def post_create(request):
    ImageFormSet = modelformset_factory(Images,fields=('image',),extra = 4)

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()


            for f in formset:
                photo = Images(post=post, image=f.cleaned_data['image'])
                photo.save()
            messages.success(request,'Your Post Created Successfully')
            return redirect ('post_list')
    else:

        form = PostCreateForm()
        formset = ImageFormSet(queryset = Images.objects.none())
        return render (request,'post_create.html',{'form':form, 'formset':formset})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    messages.success(request, 'User Login Successfully')
                    return redirect(post_list)
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User Non')
        else:
            return HttpResponse('User is Not Valid')
    else:
        form = UserLoginForm
        return render (request,'login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'User Logout Successfully')
    return redirect(post_list)

def user_register(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('post_list')
        else:
            return HttpResponse('Invalid Data')

    else:
        form = UserRegistationForm()
        return render(request,'registation.html',{'form':form})

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data = request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data = request.POST or None, instance=request.user.profile,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('post_list')
        else:
            return HttpResponse('Invalid Forms')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm( instance=request.user.profile)
        context = {'user_form':user_form,'profile_form': profile_form}
        return render(request,'profile.html',context)

def post_edit(request,id):
    posts = get_object_or_404(post,id=id)
    if request.method=='POST':
        form = PostEditForm(request.POST or None,instance=posts)
        if form.is_valid():
            form.save()
            messages.success(request,'Post Edit Successfuly')
            return redirect ('post_list')
    else:
        form = PostEditForm(instance=posts)
    context = {
            'post':posts,
            'form': form
        }
    return render(request,'post_edit.html',context)

def post_delete(request,id):
    post1 = get_object_or_404(post,id=id)
    post1.delete()
    messages.warning(request,'Post Delete Successfully')
    return redirect('post_list')




