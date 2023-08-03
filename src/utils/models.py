from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(("date joined"), auto_now_add=True)
    update_at = models.DateTimeField(("update date"), auto_now=True)

    class Meta:
        abstract = True
