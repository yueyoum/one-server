# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '4/9/14'


from utils.decorate import message_response, function_check
from core.item import Item
from libs import pack_msg

from protomsg import StrengthEquipResponse, StuffUseResponse, MergeGemResponse


@message_response("StrengthEquipResponse")
@function_check(1)
def strengthen_equip(request):
    req = request._proto

    item = Item(request._char_id)
    equip_msgs = item.equip_level_up(req.id, req.quick)

    response = StrengthEquipResponse()
    response.ret = 0
    for m in equip_msgs:
        equip_msg = response.equips.add()
        equip_msg.MergeFrom(m)
    return pack_msg(response)


@message_response("StepUpEquipResponse")
@function_check(2)
def step_up_equip(request):
    req = request._proto

    item = Item(request._char_id)
    item.equip_step_up(req.id)
    return None




@message_response("EmbedGemResponse")
@function_check(4)
def embed(request):
    req = request._proto
    item = Item(request._char_id)
    item.equip_embed(req.equip_id, req.hole_id, req.gem_id)
    return None


@message_response("UnEmbedGemResponse")
def unembed(request):
    req = request._proto
    item = Item(request._char_id)
    item.equip_embed(req.equip_id, req.hole_id, 0)

    return None


@message_response("MergeGemResponse")
def merge(request):
    req = request._proto
    item = Item(request._char_id)
    new_id, new_amount = item.gem_merge(req.id, req.method)

    response = MergeGemResponse()
    response.ret = 0
    response.new_id = new_id
    response.amount = new_amount
    return pack_msg(response)


@message_response("StuffUseResponse")
def stuff_use(request):
    req = request._proto
    item = Item(request._char_id)

    res = item.stuff_use(req.id, req.amount)
    response = StuffUseResponse()
    response.ret = 0
    if res:
        response.attachment.MergeFrom(res)

    return pack_msg(response)
