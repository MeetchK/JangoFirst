from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Регистрируем нового пользователя"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Обработка заполненной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {"form": form}
    return render(request, 'users/register.html', context)
# Create your views here.
