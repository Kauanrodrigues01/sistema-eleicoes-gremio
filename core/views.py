from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_get_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    next_page = request.GET.get('next', '')

    if next_page:
        request.session['next_page'] = next_page

    login_form_data = request.session.get('login_form_data', {})
    errors_login_form = request.session.get('errors_login_form', [])

    if errors_login_form:
        del request.session['errors_login_form']

    form = AuthenticationForm(initial=login_form_data)

    return render(request, 'core/pages/login.html', {'form': form, 'errors': errors_login_form})


def login_post_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    next_page = request.session.get('next_page')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        request.session['login_form_data'] = request.POST

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.pop('next_page') if next_page else ...
            return redirect(next_page) if next_page else redirect('votes:home')
        else:
            request.session['errors_login_form'] = [
                "Credenciais incorretas."
            ]
            return redirect('core:login')


def logout_view(request):
    logout(request)
    return redirect('core:login')
