
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def user_only(user):
    return user.is_authenticated


@user_passes_test(user_only, login_url="/")
def index_view(request):
    user = request.user
    notesraw = Note.objects.filter(user=user)
    notes = notesraw.order_by('-timestamp')
    return render(request, 'core/index.html', {'notes': notes})


@user_passes_test(user_only, login_url="/")
def add_note(request):
    user = request.user
    id1 = request.GET.get('id', None)
    if id1 is not None:
        note = get_object_or_404(Note, id=id1, user=user)
    else:
        note = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Note Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            note.user = user
            note.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'core/addnote.html', {'form': form, 'note': note})

