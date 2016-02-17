from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class ActiveMixinManager(models.Manager):
    """Manager class for ActiveMixin.
    """
    def current(self):
        return self.filter(effective_to=None)

    def deleted(self):
        return self.filter(effective_to__isnull=False)


class ActiveMixin(models.Model):
    """Model mixin to allow objects to be saved as 'non-current' or 'inactive',
    instead of deleting those objects.
    The standard model delete() method is overridden.

    "effective_to" is used to flag 'deleted' objects (not null==deleted).
    """
    effective_to = models.DateTimeField(null=True, blank=True)
    objects = ActiveMixinManager()

    class Meta:
        abstract = True

    def is_active(self):
        return self.effective_to is None

    def is_deleted(self):
        return not self.is_active()

    def delete(self, *args, **kwargs):
        """Overide the standard delete method; sets effective_to the current
        date and time.
        """
        self.effective_to = timezone.now()
        super(ActiveMixin, self).save(*args, **kwargs)
