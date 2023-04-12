from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=100, validators=[
        MinLengthValidator(3, 'Title must be greater than 3 chars')])
    description = models.TextField(max_length=450)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:note_detail', kwargs={'pk': self.pk})
