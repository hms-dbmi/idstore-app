from django.db import models
import uuid

class IdPair(models.Model):
    """
    Pairing of a UDN ID with an ID for uploading to external sites.
    """
    external_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    udn_id = models.CharField(max_length=36, blank=True, null=True, unique=True)

    def __unicode__(self):
        return "%s" % (self.external_id, self.udn_id)
