from __future__ import unicode_literals

from django.db import models
import django.contrib.auth.models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    """Person model."""
    GENDER_CHOICES = ((1, 'Female'), (2, 'Male'),)
    first_name = models.CharField('First name', blank=True, max_length=100)
    middle_name = models.CharField('Middle name', blank=True,
                                   max_length=100)
    nickname = models.CharField('Middle name', blank=True, max_length=100)
    last_name = models.CharField('Last name', blank=True, max_length=100)
    title = models.CharField('Title', blank=True, max_length=100)
    slug = models.SlugField('Slug', unique=True)
    user = models.ForeignKey(django.contrib.auth.models.User, blank=True,
                             null=True,
                             help_text=("""If the person is an existing
                             user of your site."""))
    gender = models.PositiveSmallIntegerField('Gender',
                                              choices=GENDER_CHOICES,
                                              blank=True, null=True)
    member = models.BooleanField('Member', default=True,
                                 help_text=("""Is this person a member of
                                 the organization?"""))
    phone = PhoneNumberField('Phone', blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    bio = models.TextField('Biography', blank=True, null=True)

    class Meta:
        verbose_name = ('person')
        verbose_name_plural = ('people')
        ordering = ('last_name', 'first_name',)

    def __unicode__(self):
        return u'%s' % self.full_name

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('cm-person-detail', None, {'slug': self.slug})
