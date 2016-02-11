from django.db import models


class REST(models.Model):
    owner = models.ForeignKey('auth.User', related_name='details')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    designation = models.TextField()
    alive = models.BooleanField(default=False)
    data = models.FileField(default="", upload_to='uploads/')

    class Meta:
        ordering = ('created',)

