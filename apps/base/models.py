import uuid
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

# Create your models here.


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(object):
        abstract = True
