from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
MAX_LENGTH = 30


class Follow(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Подписчик',
                             on_delete=models.CASCADE,
                             related_name='subscriber')
    following = models.ForeignKey(User,
                                  verbose_name='Автор',
                                  on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        unique_together = ('user', 'following')
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Group(models.Model):
    title = models.CharField(max_length=MAX_LENGTH,
                             verbose_name="Название группы")
    slug = models.SlugField(unique=True,
                            verbose_name="Слаг группы")
    description = models.TextField(verbose_name="Описание группы")

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата публикации")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="posts",
                               verbose_name="Автор поста")
    image = models.ImageField(upload_to="posts/",
                              null=True,
                              blank=True,
                              verbose_name="Изображение")
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              null=True, blank=True,
                              related_name="posts",
                              verbose_name="Группа")

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="comments",
                               verbose_name="Автор комментария")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments",
                             verbose_name="Пост")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
