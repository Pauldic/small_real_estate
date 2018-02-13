from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(_('name'), max_length=50)


class Feature(models.Model):
    name = models.CharField(_('name'), max_length=50)
    icon = models.ImageField(_('icon'))


class Image(models.Model):
    WIDE = 0; NARROW = 1;
    POSITION = [(WIDE, _('Wide')), (NARROW, _('Narrow'))]

    image_file = models.ImageField(_('path'), max_length=250)
    title = models.CharField(_('title'), max_length=250)
    comment = models.TextField(_('comment'))
    position = models.IntegerField(_('position'), choices=POSITION)
    weight = models.IntegerField(_('weight'), choices=POSITION)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, blank=True, default=None)


class Project(models.Model):
    OPTIONS = 0; ARCHIVED = 1; RENTED = 2; SOLD = 3; RENTING = 4; SALE = 5; FUTURE = 6
    STATUS = [(OPTIONS, _("OPTIONS")), (ARCHIVED, _("ARCHIVED")), (RENTED, _("RENTED")), (SOLD, _("SOLD")), (RENTING, _("RENTING")), (FUTURE, _("FUTURE"))]

    title = models.CharField(_('title'), max_length=250)
    general_desc = models.TextField(_('general description'))
    location_desc = models.TextField(_('location description'))
    interior_desc = models.TextField(_('interior description'))
    exterior_desc = models.TextField(_('exterior description'))
    features = models.ManyToManyField(Feature, verbose_name=_('features'))
    google_place_id = models.CharField(_('google location'), max_length=250)
    call2action = models.CharField(_('call to action'), max_length=250)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), related_name='categories')
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=10)
    surface = models.IntegerField(_('surface'))
    bedrooms = models.IntegerField(_('bedrooms'))
    bathrooms = models.IntegerField(_('bathrooms'))
    comment = models.TextField(_('comment'))
    status = models.IntegerField(_('status'), choices=STATUS)
    promoted = models.BooleanField(_('promoted'), default=False)
    promote_weight = models.IntegerField(_('promote weight'))
    slider = models.BooleanField(_('slider'), default=False)
    slider_weight = models.IntegerField(_('slider weight'))