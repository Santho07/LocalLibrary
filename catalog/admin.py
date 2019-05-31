from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance
# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BookInline(admin.TabularInline):
    model = Book
    extra = 0
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
class BookInstancesAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')

    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Book, BookAdmin)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstancesAdmin)
admin.site.register(Author, AuthorAdmin)
