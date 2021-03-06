# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-2-10'

from core.signals import heropanel_open_hero_signal

from core.activity import ActivityEntry
from core.attachment import is_empty_drop, merge_drop
from core.resource import Resource
from core.times_log import TimesLogGetHeroBySycee


def _open_hero(char_id, hero_oid, sycee, **kwargs):
    drop1 = ActivityEntry(char_id, 9001).get_additional_drop()
    drop2 = ActivityEntry(char_id, 13001).get_additional_drop()

    drop = merge_drop([drop1, drop2])
    if not is_empty_drop(drop):
        resource = Resource(char_id, "HeroPanel open")
        resource.add(**drop)

    if sycee:
        TimesLogGetHeroBySycee(char_id).inc()

heropanel_open_hero_signal.connect(
    _open_hero,
    dispatch_uid='callbacks.signals.heropanel._open_hero'
)
