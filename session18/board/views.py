from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Board
from .forms import BoardPost

def board(request):
    boards = Board.objects
    board_list = Board.objects.all()
    paginator = Paginator(board_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'board/board.html', {'boards':boards, 'posts':posts})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk = board_id)
    return render(request, 'board/detail.html', {'board':board_detail})

def new(request):
    return render(request, 'board/new.html')

def create(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/board/'+str(board.id))

def boardpost(request):
    if request.method =='POST':
        form = BoradPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('board')
    else:
        form = BoardPost()
        return render(request,'board/new.html',{'form':form})