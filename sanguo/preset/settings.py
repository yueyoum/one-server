# -*- coding: utf-8 -*-
#
#########################
#       初始化           #
#########################
#  角色
CHARACTER_INIT = {
    'gold': 0,          # 银两
    'sycee': 0,         # 元宝
    'hero_in_formation': {      # 在阵法中武将及其装备
        48: (8, 64, 0),        # 武将ID: (武器ID， 防具ID， 饰品ID). 装备一定要填满3个，没有的用0代替
        51: (22, 71, 0),
        74: (1, 71, 0),
    },
    'hero': [],          # [id,id...]   不在阵法中的武将
    'equipment': [],     # [(id,amount), (id,amount)...]
    'gem':[],            # [(id,amount), (id,amount)...]
    'stuff': [],         # [(id,amount), (id,amount)...]
    'souls': [],         # [(id,amount), (id,amount)...]
}

# 阵法  上面 `在阵法中武将的` 位置.
# 这两处的武将ID必须一一对应
FORMATION_INIT_TABLE = [
    0, 48, 0,            # 第一军
    0, 51, 0,            # 第二军
    0, 74, 0,            # 第三军
]

# 初始开启的阵法插槽
FORMATION_INIT_OPENED_SOCKETS = 4


#########################
#      奖励倍数          #
#########################
REWARD_GOLD_MULTIPLE = 1              # 得银两倍数
REWARD_SYCEE_MULTIPLE = 1             # 得元宝倍数
REWARD_EXP_MULTIPLE = 1               # 得经验倍数
REWARD_OFFICAL_EXP_MULTIPLE = 1       # 得官职经验倍数
REWARD_DROP_PROB_MULTIPLE = 1         # 掉率倍数



#########################
#      次数限制          #
#########################
# 每天可以做多少次
# 值为0的，是根据其他条件（比如VIP）具有不同值的。否则就是固定值
COUNTER = {
    'arena': 5,                         # 比武次数 免费
    'arena_buy': 0,                     # 比武次数 购买 VIP

    'gethero': 1,                       # 抽将次数
    'official_reward': 1,               # 官职每日登录领取奖励次数

    'stage_elite': 10,                  # 精英关卡总次数
    'stage_elite_buy_total': 0,         # 精英关卡总重置次数 VIP

    'levy': 0,                          # 征收次数 VIP
    'horse_strength_free': 0            # 免费培养马的次数
}
# 挂机时间是特殊处理的，所以不写在COUNTER里
# 其他一些和VIP相关的功能不是次数限制，所以也不在这里
# 活动关卡的总次数是用的 core.counter.ActivityStageCounter 来特殊处理的
# 是为了兼容以后再加新的活动关卡类型

# 精英关卡单个副本的重置次数是按照每个关卡单独计算的
# 所以将其放在 MongoStage 中记录

# 掠夺次数不再每日清零，所以也不在这里

#########################
#      角色              #
#########################
# 角色最大等级，0为不限制
CHARACTER_MAX_LEVEL = 80



#########################
#      征收              #
#########################


#########################
#      关卡             #
#########################
# 关卡掉落概率基数
DROP_PROB_BASE = 100000
#########################
#    活动关卡            #
#########################
ACTIVITY_STAGE_MAX_TIMES = 3
############################################### 国庆期间调整为 6次 2014/10/1 - 2014/10/7##################################################


#########################
#      武将             #
#########################
# 武将最高阶数
HERO_MAX_STEP = 5
# 武将初始阶数
HERO_START_STEP = 0
# 武将升阶有几个孔
HERO_STEP_UP_SOCKET_AMOUNT = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}


#########################
#      抽将             #
#########################
# 抽奖，甲品质武将池
# 完整池 [1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,37,38,39,4,43,44,5,56,6,7,8,83,9]
# 取出貂蝉、吕布
GET_HERO_QUALITY_ONE_POOL = [1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,36,37,38,39,4,43,44,5,56,6,7,8,83,9, 91]
# 抽奖，乙品质武将池
GET_HERO_QUALITY_TWO_POOL = [40,41,42,45,46,47,49,50,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75, 48, 51, 74, 78]
#新手 48,51,74,78
# 抽奖，丙品质武将池
GET_HERO_QUALITY_THREE_POOL = [100,76,77,79,80,81,82,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99]
# 抽奖多少几率产生两个甲品质卡 (基数为100)
GET_HERO_TWO_QUALITY_ONE_HEROS = 4

# 抽卡花费元宝
GET_HERO_COST = 300
# 抽卡强制刷新花费元宝 （刷新间隔还在冷却中）
GET_HERO_FORCE_REFRESH_COST = 100
# 抽卡得甲卡概率概率
# 抽的次数： 得甲卡概率
GET_HERO_QUALITY_ONE_PROB = {
    1: 2,
    2: 5,
    3: 10,
    4: 20,
    5: 40,
    6: 100,
}



#########################
#      装备             #
#########################
# 装备最高等级
EQUIP_MAX_LEVEL = 99
# 装备最高阶数 (初始第0阶)
EQUIP_MAX_STEP= 6
# 售卖品阶基础值
EQUIP_SELL_QUALITY_BASE = {
    0: 1000,
    1: 2400,
    2: 10000,
    3: 24000,
    4: 50000,
    5: 100000,
    6: 500000,
}


#########################
#      挂机             #
#########################
# 挂机比例与收益加成
HANG_REWARD_ADDITIONAL = (
    (100, 1.4), (75, 1.3), (50, 1.2), (25, 1.1)
)


#########################
#      掠夺             #
#########################
### NEW ###
# 掠夺日志
PLUNDER_LOG_TEMPLATE = {
    1: u"{0} {1}偷袭了你的粮仓，银两-{2}. {3}",  # 掠夺防守失败
    2: u"{0} 你击退了 {1}",                  # 掠夺防守成功
    3: u"{0} 粮仓装满了",                    # 粮仓满了
}

# 掠夺日志最大条数
PLUNDER_LOG_MAX_AMOUNT = 20
# 掠夺应两计算参数
PLUNDER_GOT_GOLD_PARAM_BASE_ADJUST = 0.25

# 得战俘概率 %
PLUNDER_GET_PRISONER_PROB = 15
# 得物品按照多少分钟计算
PLUNDER_GET_DROPS_MINUTES = 15
PLUNDER_GET_DROPS_TIMES = 4 * PLUNDER_GET_DROPS_MINUTES * 60 / 15
PLUNDER_DROP_DECREASE_FACTOR = 0.05
PLUNDER_DROP_MIN_FACTOR = 0.2

#########################
#      战俘             #
#########################
# 俘虏武将池
PRISONER_POOL = [
1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,36,37,38,39,4,43,44,5,56,6,7,8,83,9,
40,41,42,45,46,47,49,50,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,91,48,51,74,
100,76,77,78,79,80,81,82,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99]

# 战俘初始劝降几率
PRISONER_START_PROB = 10
# 释放获得宝物 key: quality, value: 宝物ID列表
PRISONER_RELEASE_GOT_TREASURE = {3: [24], 2: [25], 1: [25]}



#########################
#      比武             #
#########################
# 比武超过免费次数后每次比武消耗元宝
ARENA_COST_SYCEE = 20
# 比武同一个人被打CD， 秒
ARENA_CD = 60

# 比武初始积分
ARENA_INITIAL_SCORE = 1500
# 新用户最低积分
ARENA_LOWEST_SCORE = 1200
# 参与排名的积分线
ARENA_RANK_LINE = 1400

#########################
#      精英关卡         #
#########################
# 重置小关卡花费  (第几次重置， 花费)
STAGE_ELITE_RESET_COST = [
    (1, 20), (2, 50), (3, 50), (4, 100), (5, 100),
    (6, 100), (7, 200), (8, 200), (9, 300), (10, 300),
]
# 重置总次数花费   (第几次重置， 花费)
STAGE_ELITE_TOTAL_RESET_COST = [
    (1, 50), (2, 100), (3, 100), (4, 200), (5, 200), (6, 400)
]



#########################
#      好友             #
#########################
FRIEND_CANDIDATE_LIST_AMOUNT = 5        # 好友候选人列表人数数量
FRIEND_CANDIDATE_LEVEL_DIFF = 10        # 好友候选人等级差


#########################
#      邮件             #
#########################
# 邮件可以保存多少天
MAIL_KEEP_DAYS = 7
# 激活码
ACTIVATECODE_MAIL_TITLE = u'激活码领取成功'
ACTIVATECODE_MAIL_CONTENT = u'激活码领取成功，请从附件领取奖励。'
# 比武日奖励
MAIL_ARENA_DAY_REWARD_TITLE = u'比武每日奖励'
MAIL_ARENA_DAY_REWARD_CONTENT = u'比武每日奖励'
# 比武周奖励
MAIL_ARENA_WEEK_REWARD_TITLE = u'比武每周奖励'
MAIL_ARENA_WEEK_REWARD_CONTENT = u'比武每周奖励'
# 比武被打
MAIL_ARENA_BEATEN_TITLE = u'比武挑战记录'
MAIl_ARENA_BEATEN_WIN_TEMPLATE = u'报～{0}在比武擂台中挑战我军，已被我军击退'
MAIl_ARENA_BEATEN_LOST_TEMPLATE = u'报～{0}在比武擂台中挑战我军，我军暂时落败'
# 月卡
MAIL_YUEKA_TITLE = u'月卡奖励'
MAIL_YUEKA_CONTENT_TEMPLATE = u'您获得了今日奖励的{0}元宝，月卡奖励还有{1}天可以领取哦。'
# 首充
MAIL_PURCHASE_FIRST_TITLE = u'首充大礼包'
MAIL_PURCHASE_FIRST_CONTENT = u'为了感谢您的充值，特为您送首充大礼包！礼品包括：玄武将印x1，方正红宝石x1，方正黄晶石x1，方正玉石x1，都在附件中哦，请主公查收。'
# 好友系统
# 好友申请被拒绝后的邮件
MAIL_FRIEND_REFUSE_TITLE = u'好友系统'
MAIL_FRIEND_REFUSE_CONTENT = u'{0} 拒绝了您的好友申请'

# 工会站每周奖励
MAIL_UNION_BATTLE_REWARD_TITLE = u'工会战周奖励'
MAIL_UNION_BATTLE_REWARD_CONTENT = u'工会战周奖励'
# VIP
MAIL_VIP_CHANGED_TITLE = u'VIP变更通知'
MAIL_VIP_CHANGED_CONTENT = u'恭喜您获得VIP{0}特权，快去VIP界面领取奖励吧'


#########################
#      激活码           #
#########################



#########################
#      聊天             #
#########################
CHAT_MESSAGE_MAX_LENGTH = 50            # 发送消息长度。多少个字



#########################
#      操作间隔时间 秒   #
#########################
OPERATE_INTERVAL_PVE = 5                # 普通关卡战斗间隔
OPERATE_INTERVAL_PVE_ELITE = 5          # 精英关卡战斗间隔
OPERATE_INTERVAL_PVE_ACTIVITY = 5       # 活动关卡间隔

OPERATE_INTERVAL_ARENA_PANEL = 2        # 比武擂台刷新面板间隔
OPERATE_INTERVAL_CHAT_SEND = 2         # 聊天发送间隔

OPERATE_INTERVAL_FRIEND_CANDIDATE_LIST = 2 # 添加好友的候选列表刷新间隔
OPERATE_INTERVAL_FRIEND_REFRESH = 2        # 刷新自己好友状态间隔

OPERATE_INTERVAL_PLUNDER_REFRESH = 2          # 掠夺刷新间隔
OPERATE_INTERVAL_PLUNDER_BATTLE = 2        # 掠夺战斗间隔


#########################
#      其他             #
#########################

# 在线用户生存期
# 因为http协议不能记录登录用户，所以在用户最后一次操作后的生存期时间内，都认为此用户在线
# 应用场景：
#   1 发送聊天。只给在线用户发送
#   2 统计服务器压力
PLAYER_ON_LINE_TIME_TO_ALIVE = 60 * 10  # 10分钟
# 过期强制登录
PLAYER_SESSION_EXPIRE = 3600


#########################
#      充值             #
#########################
# 首充奖励物品包
PURCHASE_FIRST_REWARD_PACKAGE_IDS = [6000,]



#########################
#      工会             #
#########################
UNION_NAME_MAX_LENGTH = 8
UNION_DES_MAX_LENGTH = 50
UNION_DEFAULT_DES = u'欢迎加入工会。客服邮箱：support@mztimes.com'
UNION_CREATE_NEEDS_SYCEE = 500

# 工会战初始积分
UNION_BATTLE_INITIAL_SCORE = ARENA_INITIAL_SCORE
# 工会战最低积分
UNION_BATTLE_LOWEST_SCORE = ARENA_LOWEST_SCORE
