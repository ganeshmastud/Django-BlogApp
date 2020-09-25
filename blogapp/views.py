from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,EditForm, CommmentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})
def LikeView(request, pk):
    post= get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:

        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))



class HomeView(ListView):
    model= Post
    template_name= 'home.html'
    cats=Category.objects.all()
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context= super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context
def CategoryListView(request):
    catmenu_list=Category.objects.all()
    return render(request,'category_list.html',{'catmenu_list':catmenu_list})
def CategoryView(request,cats):
    category_post =Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_post':category_post})
class detailarticleview(DetailView):
    model=Post
    template_name = 'detailarticle.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context= super(detailarticleview,self).get_context_data(*args,**kwargs)

        post_likes=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=post_likes.total_likes()
        liked=False
        if post_likes.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCategorytView(CreateView):
    model =Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post

    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommmentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    # success_url = reverse_lazy('article-detail')