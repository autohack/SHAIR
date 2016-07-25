from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import ProfileImageForm
from .models import ProfileImage

class ProfileImageView(FormView):
    template_name = 'profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs={'pk': self.id})

class ProfileDetailView(DetailView):
    model = ProfileImage
    template_name = 'profile_image.html'
    context_object_name = 'image'


class ProfileImageIndexView(ListView):
    model = ProfileImage
    template_name = 'profile_image_view.html'
    context_object_name = 'images'
    queryset = ProfileImage.objects.all()