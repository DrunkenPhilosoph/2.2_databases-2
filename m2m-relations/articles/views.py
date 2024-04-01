from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    queryset = Article.objects.all()
    context = {'object_list': queryset}
    for i in queryset:
        print(f"DD: {i.tags.all()}")

    return render(request, template, context)
