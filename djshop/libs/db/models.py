from django.conf import settings
from django.db import models


class AuditableModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.SET_NULL, null=True, related_name='created')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.SET_NULL, null=True, related_name='modified')
    modified_at = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        abstract = True