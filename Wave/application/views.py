from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'application/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'application/show_album.html'

def showAlbum(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    context = {'album':album}
    return render(request, 'application/show_album.html', context)

def edit(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    context = {'song':song}
    return render(request, 'application/edit.html', context)

def deleteSong(request,album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    context = {'album':album}
    return render(request, 'application/show_album.html', context)

def deleteAlbum(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    albums1 = Album.objects.all
    context = {'albums': albums1}
    return render(request, 'application/index.html', context)

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AddNewSong(CreateView):
    model = Song
    fields = ['album','song_title', 'file']

class AlbumUpdate(UpdateView):
    model = Album
    template_name = 'application/album_form.html'
    fields = ['artist','album_title','genre','album_logo']

class SongUpdate(UpdateView):
    model = Song
    template_name = 'application/song_form.html'
    fields = ['album','song_title', 'file']

class UserFormView(View):
    form_class = UserForm
    template_name = 'application/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('application:index')

        return render(request, self.template_name, {'form': form})




































