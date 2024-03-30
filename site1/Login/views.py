
from django.contrib import messages
import re
from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class IndexClass(View):
    def get(self,request):
        return HttpResponse('<h1>Xin chao<h1>')
class RegisterClass(View):
    def get(self, request):
        return render(request, 'Login/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        # Kiểm tra xem các trường đã được điền đầy đủ hay không
        if not (username and password and confirm_password and email):
            error_message = 'Vui lòng điền đầy đủ thông tin.'
            return render(request, 'Login/register.html', {'error_message': error_message})
        # Kiểm tra độ dài tài khoản
        if len(username) < 6:
            error_message = 'Tài khoản phải chứa ít nhất 6 kí tự.'
            return render(request, 'Login/register.html', {'error_message': error_message})
        # Kiểm tra xem mật khẩu đủ dài và đáp ứng các yêu cầu
        if len(password) < 8:
            error_message = 'Mật khẩu phải chứa ít nhất 8 kí tự.'
            return render(request, 'Login/register.html', {'error_message': error_message})
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z]).+', password):
            error_message = 'Mật khẩu chứa kí tự chữ hoa và kí tự chữ thường.'
            return render(request, 'Login/register.html', {'error_message': error_message})

        # Kiểm tra xem mật khẩu và mật khẩu xác nhận có khớp nhau không
        if password != confirm_password:
            error_message = 'Mật khẩu và mật khẩu xác nhận không khớp.'
            return render(request, 'Login/register.html', {'error_message': error_message})
        # Kiểm tra xem email đã tồn tại trong hệ thống hay chưa
        if User.objects.filter(email=email).exists():
            error_message = 'Email đã được sử dụng.'
            return render(request, 'Login/register.html', {'error_message': error_message})

        # Kiểm tra xem tên người dùng đã tồn tại trong hệ thống hay chưa
        if User.objects.filter(username=username).exists():
            error_message = 'Tên người dùng đã được sử dụng.'
            return render(request, 'Login/register.html', {'error_message': error_message})

        # Tạo người dùng mới
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        context = {'success_message': f'Đăng ký thành công với tài khoản : {username}.'}
        return render(request, 'Login/register.html', context)

class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('nhapbn')  # Chuyển hướng đến trang chính sau khi đăng nhập thành công
        else:
            error_message= 'Tài khoản hoặc mật khẩu không chính xác.'
            return render(request, 'Login/login.html', {'error_message': error_message})

class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('Bạn vui lòng đăng nhập')
        else:
            return HttpResponse('Đây là trang có quyền mới xem được')