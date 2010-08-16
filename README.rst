
Django geoChile
===============

django-geoChile is a Django application to provide geographic information of
Chile. It is an app with fixed information to be used in your models.

Basically, it provides information about regions, provinces and municipalities.
Municipalities also have their location coordinates, to be located with a
geolocalization tool, to calculate distances between them, and so on.

All of them are related to their parent administrative level, so a municipality
is member of a province, and a province is member of a region.


Requirements
*************

The only requirement is to have GeoDjango installed, and your database to be a
spatial database.  More information about it at `GeoDjango Install page
<http://docs.djangoproject.com/en/dev/ref/contrib/gis/install/>`_


Installation
*************

You can get django-geoChile from github with: ::
    
    git clone git://github.com/spectresearch/django-geoChile.git

You must add django-geoChile to your ``INSTALLED_APPS`` in ``settings.py``: ::

    INSTALLED_APPS = ( 
        ...
        'geoChile',
        ...
    )

Then synchronize the database: ::

    python manage.py syncdb

If you have no problems with the syncronization, the installation was
successful.

Usage
******

It's an example how to use this app in your models::
    
    from geoChile.models import Comuna

    class Example(models.Model):
        ...
        comuna = models.ForeignKey(Comuna)
        ...




