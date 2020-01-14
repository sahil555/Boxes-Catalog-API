from django.shortcuts import render

# Create your views here.

from .models import Box, Author


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_boxes = Box.objects.all().count()
    

    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_boxes': num_boxes, 
                 'num_authors': num_authors,
                 'num_visits': num_visits},
    )


from django.views import generic


class BoxListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Box
    paginate_by = 10

class BoxDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Box


class AuthorListView(generic.ListView):
    """Generic class-based list view for a list of authors."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author


from django.contrib.auth.mixins import LoginRequiredMixin


class createdboxesByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing boxes on loan to current user."""
    model = Box
    template_name = 'catalog/boxlistbyuser.html'
    paginate_by = 10

    def get_queryset(self):
        return Box.objects.filter(borrower=self.request.user).filter(status__exact='o')


# Added as part of challenge!
from django.contrib.auth.mixins import PermissionRequiredMixin


class createdboxesAllListView(PermissionRequiredMixin, generic.ListView):
    model = Box
    permission_required = 1
    template_name = 'catalog/box_list_all.html'
    paginate_by = 10

    def get_queryset(self):
        return Box.objects.filter(status__exact='o')


from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required




@permission_required(1)
def renew_box_librarian(request, pk):
    box = get_object_or_404(Box, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBoxForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            box_instance.due_back = form.cleaned_data['renewal_date']
            box_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBoxForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'box_instance': box_instance,
    }

    return render(request, 'catalog/box_renew.html', context)


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_birth': '05/01/1998'}
    permission_required = 1


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth']
    permission_required = 1


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 1


# Classes created for the forms challenge
class BoxCreate(PermissionRequiredMixin, CreateView):
    model = Box
    fields = '__all__'
    permission_required = 1

class BoxUpdate(PermissionRequiredMixin, UpdateView):
    model = Box
    fields = '__all__'
    permission_required = 1


class BoxDelete(PermissionRequiredMixin, DeleteView):
    model = Box
    success_url = reverse_lazy('boxes')
    permission_required = 1