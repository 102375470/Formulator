from base.skill import PhysicalDamage, PhysicalDotDamage

SKILLS = {
    32823: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.875 - 1),
            1048576 * (0.1375 - 1),
            1048576 * (0.275 - 1),
            1048576 * (0.504 - 1)
        ]
    },
    16419: {
        "skill_class": PhysicalDamage,
        "skill_name": "霜风刀法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    16820: {
        "skill_class": PhysicalDamage,
        "skill_name": "霜风刀法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    16822: {
        "skill_class": PhysicalDamage,
        "skill_name": "霜风刀法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    16631: {
        "skill_class": PhysicalDamage,
        "skill_name": "雷走风切",
        "damage_base": [35, 45, 55, 70, 85, 100, 115, 130, 145, 175],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15],
        "attack_power_cof": [45 * 0.8 * 0.7] +
                            [(16 + (i - 1) * 17) * 0.8 * 0.7 for i in range(2, 10)] +
                            [224 * 0.8 * 0.7],
    },
    16599: {
        "skill_class": PhysicalDamage,
        "skill_name": "雷走风切",
        "damage_base": [35, 45, 55, 70, 85, 100, 115, 130, 145, 175],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15],
        "attack_power_cof": [45 * 0.8 * 0.7] +
                            [(16 + (i - 1) * 17) * 0.8 * 0.7 for i in range(2, 10)] +
                            [224 * 0.8 * 0.7],
    },
    11447: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "闹须弥(DOT)",
        "damage_base": [25, 28, 31, 34, 37, 40, 43, 46, 49, 52],
        "attack_power_cof": [50] +
                            [50 + (i - 1) * 25 for i in range(2, 10)] +
                            [280],
        "interval": 48
    },
    16933: {
        "skill_class": PhysicalDamage,
        "skill_name": "惊燕式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [64 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16934: {
        "skill_class": PhysicalDamage,
        "skill_name": "惊燕式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [80 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16935: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐鹰式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [64 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16936: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐鹰式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [96 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16937: {
        "skill_class": PhysicalDamage,
        "skill_name": "控鹤式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [80 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16938: {
        "skill_class": PhysicalDamage,
        "skill_name": "控鹤式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [104 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16787: {
        "skill_class": PhysicalDamage,
        "skill_name": "坚壁清野",
        "damage_base": [150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": [60 * 1.2 * 0.7 * 1.1] +
                            [(60 + (i - 1) * 16) * 1.2 * 0.7 * 1.1 for i in range(2, 15)] +
                            [288 * 1.2 * 0.7 * 1.1],
    },
    16794: {
        "skill_class": PhysicalDamage,
        "skill_name": "坚壁清野",
        "damage_base": [55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 240, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": [32 * 1.1] +
                            [32 + (i - 1) * 9 * 1.1 for i in range(2, 15)] +
                            [160 * 1.1],
    },
    16610: {
        "skill_class": PhysicalDamage,
        "skill_name": "刀啸风吟",
        "damage_base": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 205, 220, 235, 240, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": [50 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05 * 1.1] +
                            [(50 + (i - 1) * 14) * 1.2 * 1.05 * 1.1 * 1.1 * 1.05 * 1.1 for i in range(2, 15)] +
                            [256 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05 * 1.1],
    },
    16760: {
        "skill_class": PhysicalDamage,
        "skill_name": "项王击鼎",
        "damage_base": [35, 45, 55, 70, 85, 100, 115, 130, 145, 175, 190, 205, 220, 235, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": [40 * 1.2 * 0.9 * 1.1 * 1.1] +
                            [(40 + (i - 1) * 11) * 1.2 * 0.9 * 1.1 * 1.1 for i in range(2, 15)] +
                            [200 * 1.2 * 0.9 * 1.1 * 1.1],
        "weapon_damage_cof": 1024
    },
    16382: {
        "skill_class": PhysicalDamage,
        "skill_name": "项王击鼎",
        "damage_base": [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": [16 * 0.9 * 1.1] +
                            [(16 + (i - 1) * 7) * 0.9 * 1.1 for i in range(2, 15)] +
                            [128 * 0.9 * 1.1],
        "weapon_damage_cof": 1024
    },
    20991: {
        "skill_class": PhysicalDamage,
        "skill_name": "破釜沉舟",
        "damage_base": [90, 86, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20],
        "attack_power_cof": [80 * 0.9 * 0.95 * 1.1 * 1.15 * 1.1] +
                            [(80 + (i - 1) * 22) * 0.9 * 0.95 * 1.1 * 1.15 * 1.1 for i in range(2, 15)] +
                            [400 * 0.9 * 0.95 * 1.1 * 1.15 * 1.1],
        "weapon_damage_cof": 2048
    },
    16803: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [100, 140, 160, 180, 200, 220, 240, 260, 280, 300],
        "damage_rand": [10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
        "attack_power_cof": [60 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024
    },
    16802: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [int(e * 1.15) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.15) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.15 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 1.15 * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 1.15 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024 * 1.15
    },
    16801: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [int(e * 1.3) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.3) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.3 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 1.3 * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 1.3 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024 * 1.3
    },
    16800: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [int(e * 1.45) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.45) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.45 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 1.45 * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 1.45 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024 * 1.45
    },
    17043: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [int(e * 1.6) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.6) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.6 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 1.6 * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 1.6 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024 * 1.6
    },
    19423: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [int(e * 1.75) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.75) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.75 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 1.75 * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 1.75 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024 * 1.6
    },
    19424: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印",
        "damage_base": [int(e * 1.9) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.9) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.9 * 0.9 * 1.1 * 1.05] +
                            [(60 + (i - 1) * 10) * 1.9 * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                            [160 * 1.9 * 0.9 * 1.1 * 1.05],
        "weapon_damage_cof": 1024 * 1.6
    },
    36486: {
        "skill_class": PhysicalDamage,
        "skill_name": "楚歌",
        "damage_base": [55, 70],
        "damage_rand": 5,
        "attack_power_cof": [240 * 0.8 * 1.5, 1200 * 0.8 * 1.5],
    },
    30645: {
        "skill_class": PhysicalDamage,
        "skill_name": "降麒",
        "damage_base": [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": 60 * 2,
        "weapon_damage_cof": 1024
    },
    34585: {
        "skill_class": PhysicalDamage,
        "skill_name": "绝期",
        "damage_base": [55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 240, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": 120,
    },
    32859: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印·见尘",
        "damage_base": [int(e * 1.45 * 0.5) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.45 * 0.5) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.45 * 1.1 * 0.7] +
                            [(60 + (i - 1) * 10) * 1.45 * 1.1 * 0.7 for i in range(2, 10)] +
                            [160 * 1.45 * 0.9 * 1.1 * 0.7],
        "weapon_damage_cof": 1024 * 1.45 * 0.25
    },
    37458: {
        "skill_class": PhysicalDamage,
        "skill_name": "掠关",
        "damage_base": [80, 88, 96, 106, 112, 118, 124, 132, 138, 142, 150, 158, 166, 172, 180],
        "damage_rand": [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 48, 50],
        "attack_power_cof": 230 * 1.3
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id, detail.pop('skill_name'))
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)
