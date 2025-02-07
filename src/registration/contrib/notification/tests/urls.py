# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import re_path

from registration.compat import include
from registration.compat import patterns

admin.autodiscover()

# default template used in template
# require admin site
urlpatterns = patterns('',
    re_path(r'^admin/', include(admin.site.urls)),
)
