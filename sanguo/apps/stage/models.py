# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_delete, post_save

from utils import cache

class Battle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=32)
    level_limit = models.IntegerField("等级限制", default=1)

    @staticmethod
    def all():
        data = cache.get('battle', hours=None)
        if data:
            return data
        return _save_battle_cache()

    def __unicode__(self):
        return u'<Battle: %s>' % self.name

    class Meta:
        db_table = 'battle'
        ordering = ('id',)
        verbose_name = "战役"
        verbose_name_plural = "战役"


def _save_battle_cache(*args, **kwargs):
    battles = Battle.objects.all()
    data = {b.id: b for b in battles}
    cache.set('battle', data, hours=None)
    return data

post_save.connect(
    _save_battle_cache,
    sender=Battle,
    dispatch_uid='apps.stage.Battle.post_save'
)

post_delete.connect(
    _save_battle_cache,
    sender=Battle,
    dispatch_uid='apps.stage.Battle.post_delete'
)


class Stage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("名字", max_length=32)
    des = models.TextField("描述", blank=True)
    bg = models.CharField("背景图片", max_length=32, blank=True)
    level = models.IntegerField("关卡等级")

    battle = models.ForeignKey(Battle, verbose_name="所属战役", null=True, blank=True)
    times_limit = models.IntegerField("每日次数", null=True, blank=True,
                                      help_text="不填写表示无限制， 0 表示不能打， 其他大于0的数字表示确切的次数"
                                      )

    open_condition = models.IntegerField("前置关卡ID", null=True, blank=True,
                                         help_text="不填写表示没有前置关卡ID"
                                         )
    monsters = models.TextField("怪物ID")

    normal_exp = models.IntegerField("普通经验")
    normal_gold = models.IntegerField("普通金币")
    normal_drop = models.CharField("普通掉落", max_length=255)

    first_exp = models.IntegerField("首通经验")
    first_gold = models.IntegerField("首通金币")
    first_drop = models.CharField("首通掉落", max_length=255)

    star_exp = models.IntegerField("三星经验")
    star_gold = models.IntegerField("三星金币")
    star_drop = models.CharField("三星掉落", max_length=255)

    def __unicode__(self):
        return u'<Stage: %s>' % self.name

    @staticmethod
    def all():
        data = cache.get('stage', hours=None)
        if data:
            return data
        return _save_stage_cache()

    @property
    def decoded_monsters(self):
        return [int(i) for i in self.monsters.split(',')]


    class Meta:
        db_table = 'stage'
        ordering = ('id',)
        verbose_name = "关卡"
        verbose_name_plural = "关卡"


def _save_stage_cache(*args, **kwargs):
    stages = Stage.objects.all()
    data = {s.id: s for s in stages}
    for _id, s in data.items():
        open_condition = s.open_condition
        if not open_condition:
            continue

        data[open_condition].next = _id

    cache.set('stage', data, hours=None)
    return data


post_save.connect(
    _save_stage_cache,
    sender=Stage,
    dispatch_uid='apps.stage.Stage.post_save'
)

post_delete.connect(
    _save_stage_cache,
    sender=Stage,
    dispatch_uid='apps.stage.Stage.post_delete'
)
