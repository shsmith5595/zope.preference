##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""This module handles the 'preference' namespace directives.

"""
from zope.configuration.config import defineSimpleDirective

__docformat__ = 'restructuredtext'

from zope.component.zcml import utility
from zope.preference.interfaces import IPreferenceGroup
from zope.preference.interfaces import IPreferenceAnnotationFactory
from zope.preference.preference import PreferenceGroup


def preferenceGroup(_context, id=None, schema=None,
                    title=u'', description=u'', category=False):
    if id is None:
        id = ''
    group = PreferenceGroup(id, schema, title, description, category)
    utility(_context, IPreferenceGroup, group, name=id)


def registerPreferenceGroupDirective(_context, annotation_factory, directive_name, group_id):

    utility(_context, IPreferenceAnnotationFactory, annotation_factory, name=group_id)

    def customPreferenceGroup(_context, id=None, schema=None,
                              title=u'', description=u'', category=False):

        dotted_id = '%s.%s' % (group_id, id)
        id = dotted_id if id else id
        group = PreferenceGroup(id, annotation_factory, schema, title, description, category)
        utility(_context, IPreferenceGroup, group, name=id)

    defineSimpleDirective(_context,
                          name=directive_name,
                          schema=IPreferenceGroup,
                          handler=customPreferenceGroup)
