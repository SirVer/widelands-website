#!/usr/bin/env python -tt
# encoding: utf-8
#
# File: images/admin.py
#
# Created by Holger Rapp on 2009-03-01.
# Copyright (c) 2009 HolgerRapp@gmx.net. All rights reserved.
#
# Last Modified: $Date$
#

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from models import Image

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('content_object', 'content_type', 'object_id')
    list_display = ( '__unicode__', 'date_submitted', 'content_object', 'user')
    list_filter = ('date_submitted',)
    date_hierarchy = 'date_submitted'
    search_fields = ('image', 'user__username')
    fieldsets = (
        (None, {'fields': ( 'image', 'name', 'date_submitted','revision')}),
        (_('Upload data:'), { 'fields': ( 'user', 'editor_ip')}),
        (_('Content object:'), { 'fields': ( ('content_type', 'content_object'), 'object_id')}),
    )

admin.site.register(Image, ImageAdmin)
