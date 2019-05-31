from django.shortcuts import render
from catalog.models import BookInstance, Book, Author, Genre
from django.contrib.auth.decorators import login_required



# Create your views here
@login_required
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
        'num_genre' : num_genre,
        'num_visits': num_visits
    }
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    def get_queryset(self):
        return Book.objects.filter(title__icontains='a') # Get 5 books containing the title war

    paginate_by = 3
    #def get_queryset(self):
        #return Book.objects.filter(genre__icontains='self') */
class BookDetailedView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView):
    model = Author
class AuthorDetailedView(generic.DetailView):
    model = Author

