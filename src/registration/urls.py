# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import re_path

"""
URLconf for django-inspectional-registration
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'

from registration.views import RegistrationView
from registration.views import RegistrationClosedView
from registration.views import RegistrationCompleteView
from registration.views import ActivationView
from registration.views import ActivationCompleteView

urlpatterns = [
    re_path(r'^activate/complete/$', ActivationCompleteView.as_view(),
        name='registration_activation_complete'),
    re_path(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(),
        name='registration_activate'),
    re_path(r'^register/$', RegistrationView.as_view(),
        name='registration_register'),
    re_path(r'^register/closed/$', RegistrationClosedView.as_view(),
        name='registration_disallowed'),
    re_path(r'^register/complete/$', RegistrationCompleteView.as_view(),
        name='registration_complete'),
]

# django.contrib.auth
from registration.conf import settings
from django.contrib import auth
if settings.REGISTRATION_DJANGO_AUTH_URLS_ENABLE:
    prefix = settings.REGISTRATION_DJANGO_AUTH_URL_NAMES_PREFIX
    suffix = settings.REGISTRATION_DJANGO_AUTH_URL_NAMES_SUFFIX

    import django
    if django.VERSION >= (1, 6):
        uidb = r"(?P<uidb64>[0-9A-Za-z_\-]+)"
        token = r"(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})"
        password_reset_confirm_rule = (
            r"^password/reset/confirm/%s/%s/$" % (uidb, token)
        )
    else:
        uidb = r"(?P<uidb36>[0-9A-Za-z]+)"
        token = r"(?P<token>.+)"
        password_reset_confirm_rule = (
            r"^password/reset/confirm/%s-%s/$" % (uidb, token)
        )

    urlpatterns += [
        re_path(r'^login/$', auth.login,
            {'template_name': 'registration/login.html'},
            name=prefix+'login'+suffix),
        re_path(r'^logout/$', auth.logout,
            {'template_name': 'registration/logout.html'},
            name=prefix+'logout'+suffix),
        re_path(r'^password/change/$', PasswordChangeView.as_view(),
            name=prefix+'password_change'+suffix),
        re_path(r'^password/change/done/$', PasswordChangeDoneView.as_view(),
            name=prefix+'password_change_done'+suffix),
        re_path(r'^password/reset/$', PasswordResetView.as_view(),
            name=prefix+'password_reset'+suffix, kwargs=dict(
                post_reset_redirect=prefix+'password_reset_done'+suffix)),
        re_path(password_reset_confirm_rule,
            PasswordResetConfirmView.as_view(),
            name=prefix+'password_reset_confirm'+suffix),
        re_path(r'^password/reset/complete/$', PasswordResetCompleteView.as_view(),
            name=prefix+'password_reset_complete'+suffix),
        re_path(r'^password/reset/done/$', PasswordResetDoneView.as_view(),
            name=prefix+'password_reset_done'+suffix),
    ]

import django
if django.VERSION <= (1, 8):
    from registration.compat import patterns
    urlpatterns = patterns('', *urlpatterns)
