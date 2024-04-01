from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        form_lst = []
        for form in self.forms:
            dict_form = form.cleaned_data
            print(type(dict_form), dict_form)
            if dict_form['main'] == True:
                form_lst.append(dict_form['main'])
        if len(form_lst) >= 2:
            raise ValidationError('Основной раздел может быть только 1')
        else:
            return super().clean()

class ScopeRelationInline(admin.TabularInline):  # or admin.StackedInline
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0

class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeRelationInline]

admin.site.register(Tag)

