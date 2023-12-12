from math import inf


atk_up_table_normal = {
    "small": {1: 1.0, 10: 10.0, 15: 12.0, 20: 13.0},
    "medium": {1: 3.0, 10: 12.0, 15: 14.5, 20: 16.0},
    "big": {1: 6.0, 10: 15.0, 15: 18.0, 20: 20.0},
    "big II": {1: 7.0, 10: 16.0, 15: 20.0, 20: 22.0},
    "massive": {1: 8.0, 10: 17.0, 15: 22.0, 20: 25.5},
}


def get_normal_atk_up_percent_by_level(boost: str, level: int) -> float:
    if boost not in atk_up_table_normal:
        raise ValueError(
            "boost must be one of 'small', 'medium', 'big', 'big II', 'massive'"
        )

    if level not in atk_up_table_normal[boost]:
        raise ValueError(
            f"level must be {', '.join(list(atk_up_table_normal[boost].keys()))}"
        )
    return atk_up_table_normal[boost][level]


atk_up_table_omega = {
    "medium": {1: 3.0, 10: 12.0, 15: 14.5, 20: 16.0},
    "big": {1: 6.0, 10: 15.0, 15: 18.0, 20: 20.0},
}


def get_omega_atk_up_percent_by_level(boost: str, level: int) -> float:
    if boost not in atk_up_table_omega:
        raise ValueError("boost must be one of 'medium', 'big'")

    if level not in atk_up_table_omega[boost]:
        raise ValueError(
            f"level must be {', '.join(list(atk_up_table_omega[boost].keys()))}"
        )
    return atk_up_table_omega[boost][level]


atk_up_table_ex = {
    "small": {1: 1.0, 10: 10.0, 15: 12.0},
    "medium": {1: 3.0, 10: 12.0, 15: 14.5},
    "big": {1: 6.0, 10: 15.0, 15: 18.0, 20: 21.0},
    "massive": {1: 9.0, 10: 18.0, 15: 23.0, 20: 25.5},
    "unworldly": {1: 12.0, 10: 25.0, 15: 33.0, 20: 37.0},
}


def get_ex_atk_up_percent_by_level(boost: str, level: int) -> float:
    if boost not in atk_up_table_ex:
        raise ValueError(
            "boost must be one of 'small', 'medium', 'big', 'massive', 'unworldly'"
        )

    if level not in atk_up_table_ex[boost]:
        raise ValueError(
            f"level must be {', '.join(list(atk_up_table_ex[boost].keys()))}"
        )
    return atk_up_table_ex[boost][level]


hp_up_table_normal = {
    "small": {1: 3.0, 10: 12.0, 15: 14.0, 20: 16.0},
    "medium": {1: 6.0, 10: 15.0, 15: 17.0},
    "big": {1: 9.0, 10: 18.0, 15: 21.0},
    "big II": {1: 10.0, 10: 19.0, 15: 24.0},
}

hp_up_table_omega = {
    "small": {1: 1.0, 10: 10.0, 15: 12.0, 20: 13.0},
    "medium": {1: 3.0, 10: 12.0, 15: 14.5},
    "big": {1: 6.0, 10: 15.0, 15: 18.0, 20: 20.0},
}


UNKNOWN_PERCENT = -inf

hp_up_table_ex = {
    "small": {1: 1.0, 10: 10.0, 15: UNKNOWN_PERCENT},
    "medium": {1: 3.0, 10: 12.0, 15: 14.5},
    "big": {1: 6.0, 10: 15.0, 15: UNKNOWN_PERCENT},
}


hp_up_debuff_resistance_table_normal = {
    "small": {
        "debuff_resistance": {1: 1.2, 10: 3.0, 15: 4.0},
        "hp_up": {1: 3.0, 10: 12.0, 15: 14.0},
    },
    "medium": {
        "debuff_resistance": {1: 2.3, 10: 5.0, 15: 6.5},
        "hp_up": {1: 6.0, 10: 15.0, 15: 17.0},
    },
}

hp_up_double_attack_rate_table_omega = {
    "medium": {
        "double_attack_rate": {1: 0.8, 10: 3.5, 15: 5.0},
        "hp_up": {1: 3.0, 10: 12.0, 15: 14.0},
    }
}

critical_hit_rate_table_normal_omega = {
    "small": {1: 1.1, 10: 2.0, 15: 3.0, 20: 4.0},
    "medium": {1: 3.2, 10: 5.0, 15: 6.5, 20: 7.5},
    "big": {1: 4.4, 10: 8.0, 15: 10.0, 20: 11.0},
    "big II": {1: 5.5, 10: 10.0, 15: 12.0},
    "massive": {1: 7.9, 10: 16.0, 15: 20.0},
    "massive (Sephira)": {1: 2.0, 10: 20.0, 15: 30.0},
}


atk_up_hp_up_table_normal_omega = {
    "small": {
        "atk_up": {1: 1.0, 10: 10.0, 15: 12.0, 20: 12.5},
        "hp_up": {1: 1.0, 10: 10.0, 15: 12.0, 20: 12.5},
    },
    "medium": {
        "atk_up": {1: 3.0, 10: 12.0, 15: 14.5, 20: 15.5},
        "hp_up": {1: 3.0, 10: 12.0, 15: 14.5, 20: 15.5},
    },
    "big": {
        "atk_up": {1: 6.0, 10: 15.0, 15: 18.0, 20: 20.0},
        "hp_up": {1: 6.0, 10: 15.0, 15: 18.0, 20: 20.0},
    },
}


atk_up_hp_up_table_ex = {
    "atk_up": {1: 9.0, 10: 18.0, 15: 23.0, 20: 25.5},
    "hp_up": {1: 3.0, 10: 12.0, 15: 14.5, 20: 16.0},
}

atk_up_hp_down_table_normal = {
    "big": {
        "atk_up": {1: 6.0, 10: 15.0, 15: 18.0},
        "hp_down": {1: 6.0, 10: 15.0, 15: 18.0},
    },
    "massive": {
        "atk_up": {1: 9.0, 10: 18.0, 15: 23.0, 20: 25.5},
        "hp_down": {1: 9.0, 10: 18.0, 15: 23.0, 20: 25.5},
    },
}

multi_attack_rate_up_table_normal_omega = {
    "small": {
        "fandango": {1: 0.18, 10: 1.35, 15: 2.0},
        "devastation": {1: 0.4, 10: 1.75, 15: 2.5},
        "normal": {1: 0.4, 10: 2.2, 15: 3.5},
    },
    "medium": {
        "fandango": {1: 0.8, 10: 2.15, 15: 2.9, 20: 3.65},
        "normal": {1: 0.8, 10: 3.5, 15: 5.0, 20: 6.0},
    },
    "big": {
        "fandango": {1: UNKNOWN_PERCENT, 10: UNKNOWN_PERCENT, 15: 4.2},
        "normal": {1: 1.2, 10: 5.0, 15: 7.0},
    },
    "big II": {1: UNKNOWN_PERCENT, 10: 7.0, 15: 9.0},
    "animus parity": {1: UNKNOWN_PERCENT, 10: 5.0, 15: 8.0, 20: 11.0},
}

atk_up_double_attack_rate_table = {
    "medium": {
        "atk_up": atk_up_table_normal["medium"],
        "double_attack_rate": multi_attack_rate_up_table_normal_omega["medium"],
    },
}

double_attack_up_critical_hit_rate_up_table = {
    "medium": {
        "double_attack_rate": multi_attack_rate_up_table_normal_omega["medium"],
        "critical_hit_rate": critical_hit_rate_table_normal_omega["medium"],
    },
}

atk_up_critical_hit_rate_up_table_normal = {
    "small": {
        "atk_up": atk_up_table_normal["small"],
        "critical_hit_rate": critical_hit_rate_table_normal_omega["small"],
    },
    "medium": {
        "atk_up": atk_up_table_normal["medium"],
        "critical_hit_rate": critical_hit_rate_table_normal_omega["medium"],
    },
}

atk_up_critical_hit_rate_up_table_omega = {
    "medium": {
        "atk_up": atk_up_table_omega["medium"],
        "critical_hit_rate": critical_hit_rate_table_normal_omega["medium"],
    },
}


dodge_counter_table_normal_omega = {
    "small": {1: UNKNOWN_PERCENT, 10: UNKNOWN_PERCENT, 15: 20.0},
    "medium": {1: 3.2, 10: 16.0, 15: 23.5},
    "big": {1: UNKNOWN_PERCENT, 10: UNKNOWN_PERCENT, 15: UNKNOWN_PERCENT},
}

healing_cap_up_table = {
    "small": {1: 1.0, 10: 5.0, 15: 7.5},
    "medium": {1: 3.0, 10: 7.5, 15: 10.0},
    "big": {1: 5.0, 10: 10.0, 15: 15.0, 20: 17.5},
}

charge_atk_damage_up_table_normal_omega = {
    "mystery": {
        "small": {1: 0.5, 10: 5.0, 15: 7.5},
        "medium": {1: 2.5, 10: 7.0, 15: 9.5},
        "big": {1: 5.5, 10: 10.0, 15: 12.5},
        "massive": {1: 11.0, 10: 20.0, 15: 25.0},
    },
    "sentence": {
        "small": {1: 0.5, 10: 5.0, 15: 7.5},
        "medium": {1: 2.5, 10: 7.0, 15: 9.5},
        "big": {1: 5.5, 10: 10.0, 15: 12.5},
    },
    "glory": {
        "big": {1: 5.5, 10: 10.0, 15: 12.5, 20: 14.5},
    },
}

charge_atk_damage_cap_up_table_normal_omega = {
    "excelsior": {1: 5.5, 10: 10.0, 15: 15.0},
    "sentence": {
        "omega": {
            "medium": {1: 2.5, 10: 7.0, 15: 9.5},
        },
        "normal": {
            "small": {1: 0.2, 10: 2.0, 15: 3.0},
            "medium": {1: 0.8, 10: 3.5, 15: 5.0},
            "big": {1: 1.2, 10: 4.8, 15: 6.8},
        },
    },
    "glory": {
        "big": {1: 1.2, 10: 4.8, 15: 6.8, 20: 7.8},
    },
}


stamina_table = {
    "normal": {"medium": 65, "big": 56.4, "big II": 53.7, "ancestral": 50.4},
    "omega": {
        "medium": 60.4,
        "big": 56.4,
    },
}


def get_percent_by_level(table: dict[int, float], level: int):
    if level in table:
        return table[level]
    else:
        return UNKNOWN_PERCENT


def get_stamina_strength_for_hp_percent(
    modifier: float, level: int, hp_percent: float
) -> float:
    if hp_percent > 100 or hp_percent < 1:
        raise ValueError("hp percent must be between 1 and 100")
    if level < 1 or level > 20:
        raise ValueError("level must be between 1 and 20")

    if hp_percent < 25:
        return 0.00
    if level <= 15:
        return (hp_percent / (modifier - level)) ** 2.9 + 2.1
    return (hp_percent / (modifier - (15 + (0.4 * (level - 15))))) ** 2.9 + 2.1


# Enmity


def get_enmity_strengh_for_hp_percent(
    boost: str, level: int, hp_percent: float
) -> float:
    if hp_percent > 100 or hp_percent < 1:
        raise ValueError("hp percent must be between 1 and 100")

    enmity_table = {
        "small": {
            1: 0.5,
            2: 1.1,
            3: 1.7,
            4: 2.3,
            5: 2.9,
            6: 3.5,
            7: 4.09,
            8: 4.7,
            9: 5.3,
            10: 6.0,
            11: 6.2,
            12: 6.4,
            13: 6.6,
            14: 6.8,
            15: 7.0,
            20: 7.5,
        },
        "medium": {
            1: 0.66,
            2: 1.83,
            3: 2.26,
            4: 3.06,
            5: 3.86,
            6: 4.66,
            7: 5.46,
            8: 6.26,
            9: 7.06,
            10: 8.0,
            11: 8.4,
            12: 8.79,
            13: 9.2,
            14: 9.6,
            15: 10.0,
        },
        "big": {
            1: 0.83,
            2: 1.83,
            3: 2.83,
            4: 3.83,
            5: 4.83,
            6: 5.83,
            7: 6.83,
            8: 7.83,
            9: 8.83,
            10: 10.0,
            11: 10.5,
            12: 11.0,
            13: 11.5,
            14: 12.0,
            15: 12.5,
            20: 13.5,
        },
    }

    if boost not in enmity_table:
        raise ValueError("boost must be one of 'small', 'medium', 'big'")

    if level not in enmity_table[boost]:
        raise ValueError(f"level must be {', '.join(list(enmity_table[boost].keys()))}")

    modifier_percent = enmity_table[boost][level]

    hp_ratio = 1 - (hp_percent / 100)
    return modifier_percent * ((1 + 2 * hp_ratio) * hp_ratio)
