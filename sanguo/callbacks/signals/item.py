from core.signals import (
    equip_changed_signal,
    socket_changed_signal,
    stuff_add_signal,
    stuff_remove_signal,
    )

from core.formation import Formation
from core.activity import ActivityStatic, ActivityEntry


def _equip_changed(char_id, equip_obj, **kwargs):
    equip_id = equip_obj.equip_id

    f = Formation(char_id)
    socket = f.find_socket_by_equip(equip_id)

    if socket:
        socket_changed_signal.send(
            sender=None,
            socket_obj=socket
        )


def _stuff_add(char_id, stuff_id, add_amount, new_amount, **kwargs):
    ae = ActivityEntry(char_id, 7001)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(7001)

    ae = ActivityEntry(char_id, 18009)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(18009)

    ae = ActivityEntry(char_id, 40005)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(40005)

    ae = ActivityEntry(char_id, 50003)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(50003)

    ae = ActivityEntry(char_id, 60000)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(60000)


def _stuff_remove(char_id, stuff_id, rm_amount, new_amount, **kwargs):
    ae = ActivityEntry(char_id, 7001)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(7001)

    ae = ActivityEntry(char_id, 18009)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(18009)

    ae = ActivityEntry(char_id, 40005)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(40005)

    ae = ActivityEntry(char_id, 50003)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(50003)

    ae = ActivityEntry(char_id, 60000)
    if ae and stuff_id == ae.STUFF_ID:
        ActivityStatic(char_id).trig(60000)

equip_changed_signal.connect(
    _equip_changed,
    dispatch_uid='core.callbacks.item._equip_changed'
)

stuff_add_signal.connect(
    _stuff_add,
    dispatch_uid='callbacks.signal.item._stuff_add'
)

stuff_remove_signal.connect(
    _stuff_remove,
    dispatch_uid='callbacks.signal.item._stuff_remove'
)
