from django.contrib import admin
from django import forms
from .models import Post, Author, Category, Contact

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'summary',
                  'text', 'minute_read', 'created_date')

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('author', 'category', 'title',
                    'minute_read', 'created_date')


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'main',
                  'about', 'image')

class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm
    list_display = ('name', 'surname','about')


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'image')

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('title',)


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company',
                  'phone', 'message')

class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ('name', 'email', 'phone')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)