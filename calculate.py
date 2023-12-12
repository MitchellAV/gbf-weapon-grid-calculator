from math import inf
from typing import TypedDict


character_atk_stat = 1000
elemental_boost = 0.15

weapon_modifiers = 1.0
summons_modifiers = 1.0

omega_boost = 1 + (weapon_modifiers * summons_modifiers)

total_ex_modifiers = 0.0

ex_boost = 1 + total_ex_modifiers


normal_boost = 1 + (weapon_modifiers * summons_modifiers)
other_boosts = 1.0

total_boost = elemental_boost * omega_boost * ex_boost * normal_boost * other_boosts

character_base_damage = character_atk_stat * total_boost

innate_defense = 10
modifiers = 1.0

per_hit_damage = character_base_damage / (innate_defense * modifiers)


class WeaponSkill(TypedDict):
    damage_cap: int
    damage_cap_special: int
    normal_atk_damage_cap: int
    arcarum_damage_cap: int
    charge_atk_damage: int
    charge_atk_damage_cap: int
    special_charge_atk_damage_cap: int
    charge_atk_supplemental_damage: int
    chain_burst_damage: int
    chain_burst_damage_cap: int
    skill_damage_cap: int
    skill_damage_supplemental: int
    damage_supplemental: int
    charge_gain: int
    normal_atk_amplification: int
    charge_atk_amplification_arcarum: int
    normal_atk_amplification_arcarum: int
    skill_damage_amplification_arcarum: int
    normal_might: float
    omega_might: float
    ex_might: float
    normal_stamina: float
    omega_stamina: float
    normal_enmity: int
    omega_enmity: int
    ex_enmity: int
    ex_might_special: int
    elemental_atk_progession: int
    double_atk_rate: int
    triple_atk_rate: int
    critical: int
    counter_rate: int
    elemental_optimus: int
    elemental_atk: int
    hp: int
    hp_cut: int
    hp_damage: int
    heal_cap: int
    defense: int
    debuff_resistance: int
    fire_resistance: int
    water_resistance: int
    earth_resistance: int
    wind_resistance: int
    light_resistance: int
    dark_resistance: int
    exp_gain: int
    rupie_gain: int


WEAPON_SKILL_CAPS: WeaponSkill = {
    "damage_cap": 20,
    "damage_cap_special": 20,
    "normal_atk_damage_cap": 20,
    "arcarum_damage_cap": 20,
    "charge_atk_damage": 120,
    "charge_atk_damage_cap": 75,
    "special_charge_atk_damage_cap": 30,
    "charge_atk_supplemental_damage": 1_000_000,
    "chain_burst_damage": 120,
    "chain_burst_damage_cap": 100,
    "skill_damage_cap": 100,
    "skill_damage_supplemental": 200_000,
    "damage_supplemental": 100_000,
    "charge_gain": 50,
    "normal_atk_amplification": 30,
    "charge_atk_amplification_arcarum": 20,
    "normal_atk_amplification_arcarum": 15,
    "skill_damage_amplification_arcarum": 10,
    "normal_might": inf,
    "omega_might": inf,
    "ex_might": inf,
    "normal_stamina": inf,
    "omega_stamina": inf,
    "normal_enmity": 800,
    "omega_enmity": 800,
    "ex_enmity": 800,
    "ex_might_special": 80,
    "elemental_atk_progession": 75,
    "double_atk_rate": 75,
    "triple_atk_rate": 75,
    "critical": 100,
    "counter_rate": 20,
    "elemental_optimus": 90,
    "elemental_atk": 40,
    "hp": 400,
    "hp_cut": 70,
    "hp_damage": 40,
    "heal_cap": 100,
    "defense": 400,
    "debuff_resistance": 30,
    "fire_resistance": 30,
    "water_resistance": 30,
    "earth_resistance": 30,
    "wind_resistance": 30,
    "light_resistance": 30,
    "dark_resistance": 30,
    "exp_gain": 30,
    "rupie_gain": 50,
}


class WeaponInfo(TypedDict):
    attack: int
    hp: int
    skills: WeaponSkill


class WeaponGrid(TypedDict):
    attack: int
    hp: int
    skills: WeaponSkill


# def calculate_weapon_grid(weapon_grid: list[WeaponInfo]) -> WeaponGrid:
#     total_weapon_grid: WeaponGrid = {
#         "attack": 0,
#         "hp": 0,
#         "skills": default_weapon_skills.copy(),
#     }

#     for weapon_skill in weapon_grid["skills"]:
#         for key, value in weapon_skill.items():
#             total_weapon_grid["skills"][key] += value

#     for key, value in total_weapon_grid["skills"].items():
#         if key in WEAPON_SKILL_CAPS:
#             total_weapon_grid["skills"][key] = min(value, WEAPON_SKILL_CAPS[key])

#     return total_weapon_grid


# weapons_in_grid = []
