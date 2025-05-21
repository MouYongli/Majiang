from enum import IntEnum
from typing import List, Optional

class TileType(IntEnum):
    """麻将牌类型"""
    # 万子 (Characters)
    MAN_1 = 0
    MAN_2 = 1
    MAN_3 = 2
    MAN_4 = 3
    MAN_5 = 4
    MAN_6 = 5
    MAN_7 = 6
    MAN_8 = 7
    MAN_9 = 8
    
    # 筒子 (Dots)
    PIN_1 = 9
    PIN_2 = 10
    PIN_3 = 11
    PIN_4 = 12
    PIN_5 = 13
    PIN_6 = 14
    PIN_7 = 15
    PIN_8 = 16
    PIN_9 = 17
    
    # 条子 (Bamboo)
    SOU_1 = 18
    SOU_2 = 19
    SOU_3 = 20
    SOU_4 = 21
    SOU_5 = 22
    SOU_6 = 23
    SOU_7 = 24
    SOU_8 = 25
    SOU_9 = 26
    
    # 字牌 (Honor tiles)
    # 东南西北
    WIND_EAST = 27
    WIND_SOUTH = 28
    WIND_WEST = 29
    WIND_NORTH = 30
    # 中发白
    DRAGON_RED = 31
    DRAGON_GREEN = 32
    DRAGON_WHITE = 33

    # 花牌 （flower tiles）
    # 春夏秋冬梅兰竹菊
    SPRING = 34
    SUMMER = 35
    AUTUMN = 36
    WINTER = 37
    PLUM = 38
    ORCHID = 39
    BAMBOO = 40
    CHRYSANTHEMUM = 41

class ActionType(IntEnum):
    """特殊动作"""
    DISCARD = 101 # 打牌
    CHI = 102    # 吃
    PON = 103    # 碰
    KAN = 104    # 杠
    RON = 105    # 胡
    TSUMO = 106  # 自摸

class MahjongType(IntEnum):
    """麻将类型"""
    INTERNATIONAL = 200
    JAPAN = 201
    SICHUAN = 202