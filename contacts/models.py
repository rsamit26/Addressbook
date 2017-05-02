# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class people(models.Model):
	"""docstring for peple"""
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("detail", kwargs = {"id": self.id})