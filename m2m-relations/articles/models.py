from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tag', through='Scope')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        # ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='Название')

class Scope(models.Model):
    main = models.BooleanField(default=False, verbose_name='Основной')
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Tag_id')
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article_id')




