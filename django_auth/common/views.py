from django.shortcuts import redirect, render
from django.views.generic import FormView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from common.forms import ProfileCreationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from common.models import UserProfile
from django.forms.models import model_to_dict

from allauth.socialaccount.models import SocialAccount

def profile(request):
    try:
        user_profile = model_to_dict(UserProfile.objects.get(user = request.user))
        user_profile['username'] = request.user.username
        return render(
            request,
            'view_user_profile.html',user_profile
        )
    except:
        return redirect('/profile-create/')


class RegisterView(FormView):

    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        login(self.request, authenticate(username=username, password=raw_password))
        return super(RegisterView, self).form_valid(form)

class CreateUserProfile(FormView):

    form_class = ProfileCreationForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('common:index')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('common:login'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        try:
            user_profile = UserProfile.objects.get(user = self.request.user)
            user_profile.age=instance.age
        except:
            user_profile = form.save(commit=False)
        user_profile.user = self.request.user


        try:
            user_profile.extra_data = SocialAccount.objects.get(provider='github', user=self.request.user).extra_data
        except:
            user_profile.extra_data = ''

        user_profile.save()

        return super(CreateUserProfile, self).form_valid(form)

def index(request):
    context = {}
    if request.user.is_authenticated:

        context['username'] = request.user.username
        try:
            context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
        except:
            context['github_url'] =''

    return render(request, 'index.html', context)