# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthorTimeStampedModel(models.Model):
    created_by = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)
    modified_by = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
