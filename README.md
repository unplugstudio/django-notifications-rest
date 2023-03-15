``django-notifications-rest`` Documentation
=======================================

[django-notifications-rest](https://github.com/yhdelgado/django-notifications-rest) provides rest endpoints for ``django-notifications-hq``.

Requirements
============

- Python 3.5, 3.6, 3.7, 3.8
- Django 2.2, 3.0, 3.1
- django-notifications-hq latest version
- djangorestframework latest version

Endpoints
============
- `GET /notifications/all/`
Returns a list of notifications (unread and read)

- `GET /notifications/unread/`
Returns a list of unread notifications

- `GET /notifications/add/`
Create a new notification via http 

- `PUT /notifications/mark-all-as-read/`
Sets `unread` to `true` in every notification

`GET /notifications/mark-as-read/${id}/`
`GET /notifications/mark-as-unread/${id}/`
`DELETE /notifications/${id}`
`GET /notifications/api/unread_count/`
`GET /notifications/api/all_count/`
`GET /notifications/api/unread_list/`

Installation
============

Installation using ``pip``. You need to manually install the required ``django-notifications-hq`` and ``djangorestframework`` packages.
    
    $ pip install django-notifications-rest

or get it from source

    $ git clone https://github.com/yhdelgado/django-notifications-rest.git
    $ cd django-notifications-rest
    $ python setup.py sdist
    $ pip install dist/django-notifications-rest*

Then to add the Django Notifications Rest to your project add the app ``notifications_rest`` to your ``INSTALLED_APPS`` and urlconf.

The app should go somewhere after all the apps that are going to be generating notifications like ``django.contrib.auth``

    INSTALLED_APPS = (
        'django.contrib.auth',
        'rest_framework',
        'notifications'.
        ...
        'notifications_rest',
        ...
    )

Add the notifications urls to your urlconf::

    urlpatterns = [
        ...
        url('^notifications/', include('notifications_rest.urls')),
        ...
    ]
If the installed version of django>=3.1, then::

    from django.urls import path, include
    urlpatterns = [
        ...
        path('^notifications/', include('notifications_rest.urls')),
        ...
    ]
 
To run schema migration, execute ``python manage.py migrate``.