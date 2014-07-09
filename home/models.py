# -*- coding: utf-8 -*-
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    mail = models.EmailField(max_length=50, verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')
    info = models.TextField(max_length=200, verbose_name='Mensaje')

    def __unicode__(self):
        return '%s [%s]' % (self.name, self.mail)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contacto'