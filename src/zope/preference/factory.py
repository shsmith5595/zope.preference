#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import zope

from zope.annotation import IAnnotations

from zope.preference.interfaces import IPreferenceAnnotationFactory

from zope.security.management import getInteraction

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)


USER_PREFERENCE_ANNOTATION_KEY = 'zope.app.user.UserPreferences'


@zope.interface.implementer(IPreferenceAnnotationFactory)
class UserPreferenceAnnotationFactory(object):

    __annotation_key__ = USER_PREFERENCE_ANNOTATION_KEY

    @property
    def annotations(self):
        principal = getInteraction().participations[0].principal
        ann = zope.component.getMultiAdapter((principal, self), IAnnotations)
        return ann
