from email.policy import default
from math import inf
from pprint import pprint
from typing import TypedDict
import pandas as pd
from weapon_skills import skill_mapping

fire_weapon_list = pd.read_csv("results/Fire.csv")
water_weapon_list = pd.read_csv("results/Water.csv")
earth_weapon_list = pd.read_csv("results/Earth.csv")
wind_weapon_list = pd.read_csv("results/Wind.csv")
dark_weapon_list = pd.read_csv("results/Dark.csv")
light_weapon_list = pd.read_csv("results/Light.csv")

weapons_df = pd.concat(
    [
        fire_weapon_list,
        water_weapon_list,
        earth_weapon_list,
        wind_weapon_list,
        dark_weapon_list,
        light_weapon_list,
    ]
).sort_values(by=["Name"], ascending=True, ignore_index=True)


class WeaponInfo(TypedDict):
    atk: int
    element: str
    hp: int
    id: str
    max_evo_level: int
    name: str
    rarity: int
    skills: list[str]
    type: str
    url: str


raw_weapons_dict = weapons_df.to_dict("records")
weapons_dict: dict[str, WeaponInfo] = {
    weapon["Name"]: {
        "atk": weapon["ATK"],
        "element": weapon["Element"],
        "hp": weapon["HP"],
        "id": weapon["ID"],
        "max_evo_level": weapon["Max Evo Level"],
        "name": weapon["Name"],
        "rarity": weapon["Rarity"],
        "skills": str(weapon["Skills"]).split(", ") if weapon["Skills"] else [],
        "type": weapon["Type"],
        "url": weapon["URL"],
    }
    for weapon in raw_weapons_dict
}

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


class WeaponGrid(TypedDict):
    attack: int
    hp: int
    skills: WeaponSkill


default_weapon_skills: WeaponSkill = {
    "damage_cap": 0,
    "damage_cap_special": 0,
    "normal_atk_damage_cap": 0,
    "arcarum_damage_cap": 0,
    "charge_atk_damage": 0,
    "charge_atk_damage_cap": 0,
    "special_charge_atk_damage_cap": 0,
    "charge_atk_supplemental_damage": 0,
    "chain_burst_damage": 0,
    "chain_burst_damage_cap": 0,
    "skill_damage_cap": 0,
    "skill_damage_supplemental": 0,
    "damage_supplemental": 0,
    "charge_gain": 0,
    "normal_atk_amplification": 0,
    "charge_atk_amplification_arcarum": 0,
    "normal_atk_amplification_arcarum": 0,
    "skill_damage_amplification_arcarum": 0,
    "normal_might": 0,
    "omega_might": 0,
    "ex_might": 0,
    "normal_stamina": 0,
    "omega_stamina": 0,
    "normal_enmity": 0,
    "omega_enmity": 0,
    "ex_enmity": 0,
    "ex_might_special": 0,
    "elemental_atk_progession": 0,
    "double_atk_rate": 0,
    "triple_atk_rate": 0,
    "critical": 0,
    "counter_rate": 0,
    "elemental_optimus": 0,
    "elemental_atk": 0,
    "hp": 0,
    "hp_cut": 0,
    "hp_damage": 0,
    "heal_cap": 0,
    "defense": 0,
    "debuff_resistance": 0,
    "fire_resistance": 0,
    "water_resistance": 0,
    "earth_resistance": 0,
    "wind_resistance": 0,
    "light_resistance": 0,
    "dark_resistance": 0,
    "exp_gain": 0,
    "rupie_gain": 0,
}


def calculate_weapon_grid(weapon_grid: list[WeaponInfo]) -> WeaponGrid:
    total_weapon_grid: WeaponGrid = {
        "attack": 0,
        "hp": 0,
        "skills": default_weapon_skills.copy(),
    }

    pprint(weapon_grid)
    for weapon in weapon_grid:
        total_weapon_grid["attack"] += weapon["atk"]
        total_weapon_grid["hp"] += weapon["hp"]

        weapon_skills = weapon["skills"]
        for weapon_skill in weapon_skills:
            if weapon_skill not in skill_mapping:
                continue
            skill_stats = skill_mapping[weapon_skill]
            if skill_stats is None:
                continue

    # for weapon_skill in weapon_grid["skills"]:
    #     for key, value in weapon_skill.items():
    #         total_weapon_grid["skills"][key] += value

    for key, value in total_weapon_grid["skills"].items():
        if key in WEAPON_SKILL_CAPS:
            total_weapon_grid["skills"][key] = min(value, WEAPON_SKILL_CAPS[key])  # type: ignore

    return total_weapon_grid


if __name__ == "__main__":
    weapons_in_grid = ["Celeste Claw Omega", "Celeste Claw Omega", "Celeste Claw Omega"]

    weapon_grid = [weapons_dict[weapon] for weapon in weapons_in_grid]

    weapon_grid_stats = calculate_weapon_grid(weapon_grid)
    print(weapon_grid_stats)
