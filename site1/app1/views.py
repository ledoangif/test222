from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Question,BenhNhan,PhongKham
from collections import deque
from .form import MyForm,NhapBN
import time
# Create your views here.

dq= deque()
dq1 = deque()
dq2 = deque()
dq3 = deque()
def nhapbn(request):
    a= NhapBN()
    return render(request,"app1/nhapbn.html",{"form":a})

def savebn(request):
    if request.method == "POST":
        g = NhapBN(request.POST)
        if g.is_valid():
            saveg=BenhNhan(NameBN= g.cleaned_data['NameBN'],
                           Date= g.cleaned_data['Date'],
                           DateK= g.cleaned_data['DateK'],
                           CCCD= g.cleaned_data['CCCD'])
            saveg.save()
            
            UT=g.cleaned_data['UT']
            if(UT==False):
              dq.append(saveg)
            else:
                dq.appendleft(saveg)

            return redirect('hienbn')
        else:
            return HttpResponse("sai")
    else:
        return HttpResponse("ko phải post")      
def hien(request):
    listPK = PhongKham.objects.all()
    context={"dq":dq , "listPK":listPK}
    return render(request,"app1/hienbn.html",context)
def chuyendenpk(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ request.POST cho các dữ liệu gửi dưới dạng POST
        data = request.POST.get('selected_option', None)
        if data is not None:
            if data=="1":
                g=dq.popleft()
                dq1.append(g)
                return redirect('PK')
            elif data=="2":
                g=dq.popleft()
                dq2.append(g)
                return redirect('PK')
            elif data=="3":
                g=dq.popleft()
                dq3.append(g)
                return redirect('PK')
        else:
            return HttpResponse('Không tìm thấy dữ liệu')
    else:
        return HttpResponse('Yêu cầu không hợp lệ')
def hienPK(request):
    dsPK= PhongKham.objects.all()
    return render(request,"app1/hienPK.html",{"dsPK":dsPK})
def deltailView(request,PK_id):
    if PK_id==1:
        q=PhongKham.objects.get(id=PK_id)
        return render(request,"app1/hienbnpk.html",{"dq": dq1,"q":q})
    elif PK_id==2:
        q=PhongKham.objects.get(id=PK_id)
        return render(request,"app1/hienbnpk.html",{"dq": dq2,"q":q})
    elif PK_id==3:
        q=PhongKham.objects.get(id=PK_id)
        return render(request,"app1/hienbnpk.html",{"dq": dq1,"q":q})


