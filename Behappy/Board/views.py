from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *

from .form import BoardWriteForm, MemberForm, signupForm, studentBoardWriteForm, graduateBoardWriteForm, loveBoardWriteForm
from Board import form
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
#새내기
def nonMemberMain(request):
    boardList = Board.objects.all()
    return render(request, 'nonMemberMain.html', {'boardList' : boardList})

def nonMemberDetail(request, boardid):
    board = get_object_or_404(Board,pk=boardid)
    
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'nonMemberDetail.html',context)

    except KeyError:
        return redirect('nonMemberMain')


def main(request):

    boardList = Board.objects.all()

    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        member = Member.objects.get(ID=ID,password=password)
        if member is not None:
            request.session['memberid'] = member.ID
            return render(request, 'main.html', {'boardList' : boardList})

        else:
            return redirect('login')
    
    return render(request, 'main.html',{'boardList' : boardList})


def write(request):
    if request.method =='POST':
        form = BoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    member_id = request.session['memberid']
    member = get_object_or_404(Member, pk=member_id)
    form = BoardWriteForm(initial={'member':member})
    return render(request, 'write.html', {'form':form, 'member':member})

def detail(request, boardid):
    board = get_object_or_404(Board,pk=boardid)
    
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'detail.html',context)

    except KeyError:
        return redirect('main')

@csrf_exempt
def update(request, boardid):
    if request.method =='POST':
        board = Board.objects.get(pk=boardid)
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.POST.get('user')
        if title is not None and board is not None:
            board.title = title
            board.content = content
            board.user = user
            board.save()
            return render(request, 'detail.html', {'board': board})
        else:
            return render(request, 'detail.html', {'board': board})


def delete(request, boardid):
    boardList = Board.objects.all()
    board = Board.objects.get(id=boardid)
    board.delete()
    boards = {'boards': Board.objects.all()}
    return render(request, 'main.html', {'boardList' : boardList})


def login(request):
    form = MemberForm()
    return render(request,'login.html',{'form': form})

def logout(request):
    boardList = Board.objects.all()
    if request.session.get('user'):
        del(request.session['user'])
    form = MemberForm()
    return render(request,'nonMemberMain.html',{'boardList' : boardList})

def signUp(request):
    if request.method =='POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = signupForm()
    return render(request,'signup.html',{'form': form})





#재학생
def studentnonMemberMain(request):
    boardList = studentBoard.objects.all()
    return render(request, 'studentnonMemberMain.html', {'boardList' : boardList})


def studentnonMemberDetail(request, boardid):
    board = get_object_or_404(studentBoard,pk=boardid)
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'studentnonMemberDetail.html',context)

    except KeyError:
        return redirect('studentnonMemberMain')


def studentmain(request):

    boardList = studentBoard.objects.all()

    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        member = Member.objects.get(ID=ID,password=password)
        if member is not None:
            request.session['memberid'] = member.ID
            return render(request, 'studentmain.html', {'boardList' : boardList})

        else:
            return redirect('studentlogin')
    
    return render(request, 'studentmain.html',{'boardList' : boardList})


def studentwrite(request):
    if request.method =='POST':
        form = studentBoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentmain')

    member_id = request.session['memberid']
    member = get_object_or_404(Member, pk=member_id)
    form = studentBoardWriteForm(initial={'member':member})
    return render(request, 'studentwrite.html', {'form':form, 'member':member})


def studentdetail(request, boardid):
    board = get_object_or_404(studentBoard,pk=boardid)    
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'studentdetail.html',context)

    except KeyError:
        return redirect('studentmain')

@csrf_exempt
def studentupdate(request, boardid):
    if request.method =='POST':
        board = studentBoard.objects.get(pk=boardid)
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.POST.get('user')
        if title is not None and board is not None:
            board.title = title
            board.content = content
            board.user = user
            board.save()
            return render(request, 'studentdetail.html', {'board': board})
        else:
            return render(request, 'studentdetail.html', {'board': board})


def studentdelete(request, boardid):
    boardList = studentBoard.objects.all()
    board = studentBoard.objects.get(id=boardid)
    board.delete()
    boards = {'boards': studentBoard.objects.all()}
    return render(request, 'studentmain.html', {'boardList' : boardList})


def studentlogin(request):
    form = MemberForm()
    return render(request,'studentlogin.html',{'form': form})


def studentlogout(request):
    boardList = studentBoard.objects.all()
    if request.session.get('user'):
        del(request.session['user'])
    form = MemberForm()
    return render(request,'studentnonMemberMain.html',{'boardList' : boardList})


def studentsignUp(request):
    if request.method =='POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlogin')
    form = signupForm()
    return render(request,'studentsignup.html',{'form': form})




#졸업생

def graduatenonMemberMain(request):
    boardList = graduateBoard.objects.all()
    return render(request, 'graduatenonMemberMain.html', {'boardList' : boardList})


def graduatenonMemberDetail(request, boardid):
    board = get_object_or_404(graduateBoard,pk=boardid)
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'graduatenonMemberDetail.html',context)

    except KeyError:
        return redirect('graduatenonMemberMain')


def graduatemain(request):

    boardList = graduateBoard.objects.all()

    if request.method == 'POST':
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        member = Member.objects.get(ID=ID,password=password)
        if member is not None:
            request.session['memberid'] = member.ID
            return render(request, 'graduatemain.html', {'boardList' : boardList})

        else:
            return redirect('graduatelogin')
    
    return render(request, 'graduatemain.html',{'boardList' : boardList})


def graduatewrite(request):
    if request.method =='POST':
        form = graduateBoardWriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('graduatemain')
    member_id = request.session['memberid']
    member = get_object_or_404(Member, pk=member_id)
    form = graduateBoardWriteForm(initial={'member':member})
    return render(request, 'graduatewrite.html', {'form':form, 'member':member})


def graduatedetail(request, boardid):
    board = get_object_or_404(graduateBoard,pk=boardid)    
    try:
        session = request.session['memberid']
        context = {
            'board': board,
            'session': session,
        }
        return render(request,'graduatedetail.html',context)

    except KeyError:
        return redirect('graduatemain')

@csrf_exempt
def graduateupdate(request, boardid):
    if request.method =='POST':
        board = graduateBoard.objects.get(pk=boardid)
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.POST.get('user')
        if title is not None and board is not None:
            board.title = title
            board.content = content
            board.user = user
            board.save()
            return render(request, 'graduatedetail.html', {'board': board})
        else:
            return render(request, 'graduatedetail.html', {'board': board})


def graduatedelete(request, boardid):
    boardList = graduateBoard.objects.all()
    board = graduateBoard.objects.get(id=boardid)
    board.delete()
    boards = {'boards': graduateBoard.objects.all()}
    return render(request, 'graduatemain.html', {'boardList' : boardList})


def graduatelogin(request):
    form = MemberForm()
    return render(request,'graduatelogin.html',{'form': form})


def graduatelogout(request):
    boardList = graduateBoard.objects.all()
    if request.session.get('user'):
        del(request.session['user'])
    form = MemberForm()
    return render(request,'graduatenonMemberMain.html',{'boardList' : boardList})


def graduatesignUp(request):
    if request.method =='POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('graduatelogin')
    form = signupForm()
    return render(request,'graduatesignup.html',{'form': form})


