# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '2/19/14'

import json

from _base import Logger
from core.attachment import get_drop
from core.character import Char
from core.mail import Mail
from core.arena import REDIS_ARENA_KEY
from core.drives import redis_client
from core.achievement import Achievement
from core.activity import ActivityStatic
from preset.data import ARENA_WEEK_REWARD_TUPLE
from preset.settings import MAIL_ARENA_WEEK_REWARD_CONTENT, MAIL_ARENA_WEEK_REWARD_TITLE


def _get_reward_by_rank(score, rank):
    data = None

    for _rank, _reward in ARENA_WEEK_REWARD_TUPLE:
        if rank >= _rank and _reward.packages:
            drop_ids = [int(i) for i in _reward.packages.split(',')]
            data = get_drop(drop_ids)
            break

    if data:
        return json.dumps(data)
    return None


def reset():
    amount = redis_client.zcard(REDIS_ARENA_KEY)

    logger = Logger("reset_arena_week.log")
    logger.write("Reset Arena Week: Start. chars amount: {0}".format(amount))

    score_data = redis_client.zrevrange(REDIS_ARENA_KEY, 0, -1, withscores=True)

    data = []
    for char_id, score in score_data:
        data.append( (int(char_id), score, Char(int(char_id)).power) )

    data.sort(key=lambda item: (-item[1], -item[2]))


    # 发送奖励
    for index, data in enumerate(data):
        rank = index + 1
        char_id = data[0]

        achievement = Achievement(char_id)
        achievement.trig(10, rank)

        attachment = _get_reward_by_rank(data[1], rank)
        if not attachment:
            continue

        mail = Mail(char_id)
        mail.add(MAIL_ARENA_WEEK_REWARD_TITLE, MAIL_ARENA_WEEK_REWARD_CONTENT, attachment=attachment)

        ActivityStatic(char_id).send_mail()

    logger.write("Reset Arena Week: Complete")
    logger.close()


if __name__ == '__main__':
    reset()
