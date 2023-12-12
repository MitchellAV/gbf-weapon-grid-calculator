# https://gbf.wiki/Damage_Formula/Detailed_Damage_Formula#Character_total_ATK

import numpy as np

# Damage cap
# Attack = 440,000
# Charge = 1,650,000
# Hard Cap = 13,000,000

# Weapon skills
# Max total damage cap = 20%


normal_atk_mod = 0  # encompasses all the Normal weapon skills that increase ATK with no requirement on character HP level.
optimus_aura = 0  # the modifier from the Optimus Series summons aura (and their Demi Optimus counterparts): Agni, Varuna, Titan, Zephyrus, Zeus and Hades.
bahamut_mod = 0
ultima_mod = 0
normal_summon_aura = (
    0  # the X% boost to Normal ATK modifer from summons such as Grand Order.
)
normal_buffs = (
    0  #  the ATK up effects that can come from skills, enemies or summon calls.
)
normal_debuffs = (
    0  #  the ATK down effects that can come from skills, enemies or summon calls.
)

normal_atk_boost = (
    1
    + normal_atk_mod * (1 + optimus_aura)
    + bahamut_mod
    + ultima_mod
    + normal_summon_aura
    + normal_buffs
    - normal_debuffs
)

omega_atk_mod = 0  # encompass all the Omega weapon skills that increase ATK with no requirement on character HP level.
omega_aura = 0  # the modifier from the Omega Series SSR summons aura: Colossus, Leviathan, Yggdrasil, Tiamat, Luminiera and Celeste.

omega_atk_boost = 1 + omega_atk_mod * (1 + omega_aura)


usual_ex_atk_mod = 0  # encompass all the EX weapon skills that increase ATK with no requirement on character HP level, excluding the iDOLM@STER event weapon Mysterious EX skills.
mysterious_ex_atk_mod = 0  # the iDOLM@STER event weapon Mysterious EX skills.
ranko_aura = 0  # The Ranko Kanzaki aura affects the Mysterious EX ATK modifiers from iDOLM@STER event EX weapons.

ex_atk_boost = 1 + usual_ex_atk_mod + mysterious_ex_atk_mod * (1 + ranko_aura)

# Enmity and Stamina modifiers are the ATK up weapon skill modifiers that depend on the HP level of the character. They are present on Normal, Omega and EX weapons.

# Normal and Omega Enmity/Stamina modifiers are affected by the Optimus/Omega auras, but not the EX modifiers.

normal_enmity_mod = 0
normal_stamina_mod = 0
omega_enmity_mod = 0
omega_stamina_mod = 0
ex_enmity_mod = 0
ex_stamina_mod = 0


normal_enmity_boost = 1 + normal_enmity_mod * (1 + optimus_aura)
normal_stamina_boost = 1 + normal_stamina_mod * (1 + optimus_aura)
omega_enmity_boost = 1 + omega_enmity_mod * (1 + omega_aura)
omega_stamina_boost = 1 + omega_stamina_mod * (1 + omega_aura)
ex_enmity_boost = 1 + ex_enmity_mod
ex_stamina_boost = 1 + ex_stamina_mod

fixed_atk_modifiers = 0  # Absolute modifiers of the ATK computation, such as the 15% ATK cut from Qinglong Manewhip.

normal_omega_ex_boosts = (
    normal_atk_boost
    * normal_enmity_boost
    * normal_stamina_boost
    * omega_atk_boost
    * omega_enmity_boost
    * omega_stamina_boost
    * ex_atk_boost
    * ex_enmity_boost
    * ex_stamina_boost
) - fixed_atk_modifiers


elemental_superiority = (
    0  # 0.5 for 50% superiority, -0.25 for 25% inferiority, 0 for neutral
)
element_summon_mod = 0  # auras of the type X% boost to [Element] Elemental ATK.
element_emp_buffs = 0  # EMPs of the type [Element] ATK up.
elem_atk_buffs = 0  # the [Element] ATK up effects that can come from skills, weapons, enemies or summon calls.
elem_atk_debuffs = 0  # the [Element] ATK down effects that can come from skills, weapons, enemies or summon calls.

elemental_boost = (
    1
    + elemental_superiority
    + element_summon_mod
    + element_emp_buffs
    + elem_atk_buffs
    - elem_atk_debuffs
)


# Jammed and Strength are character buffs originating from skills, weapons, summons or charge attacks.
jammed_mod = 0
strength_mod = 0

# EMP modifiers and Ring modifiers respectively come from the EMP perks and the Coronation Rings, Lineage Rings, and Intricacy Rings associated to the character.
enmity_emp_mod = 0
stamina_emp_mod = 0
ring_enmity_mod = 0
ring_stamina_mod = 0

# AX modifiers come from AX skill in the grid that's currently being used and is added to all characters.
ax_enmity_mod = 0
ax_stamina_mod = 0

char_enmity_boosts = 1 + jammed_mod + enmity_emp_mod + ring_enmity_mod + ax_enmity_mod

char_stamina_boost = (
    1 + strength_mod + stamina_emp_mod + ring_stamina_mod + ax_stamina_mod
)


perpetuity_mod = 0  # Perpetuity modifiers are ATK up effects originating from the Perpetuity Ring, the Shield of Eternal Splendor Wonder, and rarely some buffs, such as Heavenly Howl

perpetuity_boost = 1 + perpetuity_mod

# Unique Stackable modifiers are ATK up effects that come from ATK Up (Stackable) and its variants. Unique Stackable boosts that use the same frame will stack additively and count toward the same cap. The cap used is dependent on highest active effect. Unique Stackable boosts will only count to the cap if it is applied while the current boost is below its individual cap (e.g. If Lunalu copies Indominus 5 times then Blade Impulse 1 time, she will have a 50% boost. If the order of copied skills is switched, she will have a 60% boost.) Unique Stackable boosts in separate frames count toward separate caps (e.g. at max stacks Indominus and Satyr (Summon) will have 60% + 30% = 90%). These are different from other stackable ATK boosts, like Assassin's Motivating Draft, which are under the Normal ATK modifier.


unique_stackable_mod = 0  # see above

unique_stackable_boost = 1 + unique_stackable_mod

# https://gbf.wiki/Assassin_(Buff)

# Assassin modifiers are ATK up effects that come from buffs such Salted Wound, Defiance, Path of Destruction and other variants. In addition to the boost, all known assassin boosts also increase the damage cap.


assassin_mod = 0  # see above
assassin_boost = 1 + assassin_mod

# Total Char Unique ATK boosts is the product of all the Unique ATK up effects present on a character. Essentially, each Unique ATK up effect behaves like its own boost category, applied multiplicatively in the damage formula.


unique_atk_mod = 0  # see above

total_char_unique_atk_boosts = 1 + unique_atk_mod


crew_ship_mod = 0  # the X% [Element] ATK up effect present on the active crew airship.
crew_skill_mod = 0  # the X% [Element] ATK up effect triggered by certain crew skills.

crew_ship_boost = 1 + crew_ship_mod
crew_skills_boost = 1 + crew_skill_mod


atk_down_mod = (
    0  # encompasses all non-elemental X% ATK down debuffs present on the character.
)
atk_down_debuff_effect = 1 - atk_down_mod


character_total_atk = 0  # The sum of the character's base ATK, grid weapons' ATK values, and summon ATK values. If a weapon matches the character's weapon specialty, it contributes at 120% of its base ATK instead of 100%.


base_damage = (
    character_total_atk
    * elemental_boost
    * normal_omega_ex_boosts
    * char_enmity_boosts
    * char_stamina_boost
    * perpetuity_boost
    * unique_stackable_boost
    * assassin_boost
    * total_char_unique_atk_boosts
    * crew_ship_boost
    * crew_skills_boost
    * atk_down_debuff_effect
)

# # Supplemental Damage
#
# Supplemental Damage is an effect present on certain skills, such as Halluel and Malluel's Everbane debuff or the Hollowsky Weapons's Covenant skills and are directly added without taking into account Base Damage or Defense.
#
# Please refer to Supplemental Damage for more information.
# https://gbf.wiki/Supplemental_Damage

# # Seraphic boost
#
# Seraphic boost is an effect present on some characters' passive skills (Eternals and Lancelot (Wind), for instance), and on the Seraphic Weapons skills.
#
# It is applied after every other modifier has been applied, on every damage instance, and also affects the character's damage cap. However, Supplemental Damage is only boosted by Seraphic boosts for skill damage and C.A. Damage. Normal Attacks will not get their Supplemental Damage increased by a Seraphic boost.
#
# Therefore, in all the following subsections describing the different instances of damage (excluding the exception described above), the final damage will be computed as such if a Seraphic modifier is present:


instance_damage = 0
instance_damage_cap = 0

seraphic_mod = 0

final_damage = instance_damage * (1 + seraphic_mod)
final_damage_cap = instance_damage_cap * (1 + seraphic_mod)

# # Sleeping Boost
# Sleeping boost is associated to the Stared Stiff, Sleep and Comatose status effects applied to the enemy. The boost depends on the status: Stared Stiff = 10%, Sleep = 25%, Comatose = 50%.


sleeping_boost = 1  # see above
random_modifier = 1  # random modifier between 0.95 and 1.05 step 0.01

innate_defense = 10  # Innate DEF has a nominal value of 10, with high defense enemies using higher values and low defense enemies using lower values.
def_up_mods = 0  # DEF up mods are all the DEF up effects present on the enemy. Damage Cuts and Repel effects are not taken into account.
def_down_mods = 0  # DEF down mods encompass all the DEF down or [Element] DEF down debuffs present on the enemy.

# Note that the total value of DEF up and DEF down mods is hard capped at 50%.

# Unique DEF down mods are DEF down effects that are not affected by the hard DEF down cap. These include for instance Feower's Forfeit and Gabriel (Summon)'s Pureflow (10% each, but don't stack).


enemy_defense = innate_defense + def_up_mods - def_down_mods

normal_damage = base_damage * sleeping_boost * random_modifier / enemy_defense


critical_mods = 0  # Critical mods is the sum of every multiplier linked to the critical skills that have successfully triggered for this damage instance (since critical damage only has a fixed chance to happen for each critical skill).

# Critical attacks have a chance to replace Normal attacks when using an element-superior team (or under certain field effects). They are described by a chance and a multiplier, usually labeled X% chance to deal Y% supplemental damage.
critial_damage = normal_damage * (1 + critical_mods)


normal_damage_wo_supplemental = normal_damage
bonus_multiplier = 0  # Bonus multiplier is the X% Bonus Damage description of the echo-providing skills.


# Bonus Damage, colloquially referred to as "echo", originates from certain skills, charge attacks, summons or weapons. It is another instance of damage present alongside the normal attacks. Each echo is computed independently.
bonus_damage = normal_damage_wo_supplemental * bonus_multiplier


counter_multiplier = 0  # Counter multiplier is the percentage value present on the Counter skill description.

counterattack_damage = normal_damage * (1 + counter_multiplier)


charge_attack_multiplier = 0  # Charge Attack multiplier is a percentage value associated to the "strength" of the Charge Attack (medium, big, massive, otherworldly).

charge_attack_damage_up_mods = 0  # CA Damage Up mods are boost to Charge Attack DMG effects, that can originate from EMP perks, active or passive skills or summon calls.

charge_attack_buff_boost = 1 + charge_attack_damage_up_mods

charge_attack_weapon_mods = 0  # CA weapon mods are boost to Charge Attack DMG effects present on certain weapon skills, in particular Sentence or Mystery.

charge_attack_weapon_boost = 1 + charge_attack_weapon_mods

fixed_charge_attack_damage = 0  # Fixed CA damage is present in very small amounts (2000 for Shiva) on all Charge Attacks and in large amounts on certain characters' Charge Attacks, such as Yodarha (SSR).

charge_attack_damage = (
    normal_damage
    * charge_attack_multiplier
    * charge_attack_buff_boost
    * charge_attack_weapon_boost
) + fixed_charge_attack_damage


total_party_charge_attack_damage = 0

burst_constant = 0  # Burst constant depends on the number of Charge Attacks involved in the Chain Burst: 25% for 2 CA, 33.3% for 3 CA, 50% for 4 CA and more.

burst_boost = 0  # Burst boost is the sum of all stacking Boost to Chain burst DMG effects from skills, weapons or summons.

burst_damage = (
    total_party_charge_attack_damage
    * burst_constant
    * elemental_superiority
    * burst_boost
)


skill_table_normal = {
    "small": {1: 0.01, 10: 0.1, 15: 0.12, 20: 0.13},
    "medium": {1: 0.03, 10: 0.12, 15: 0.145, 20: 0.16},
    "big": {1: 0.06, 10: 0.15, 15: 0.18, 20: 0.2},
    "big 2": {1: 0.07, 10: 0.16, 15: 0.2, 20: 0.22},
    "massive": {1: 0.08, 10: 0.17, 15: 0.22, 20: 0.255},
}
skill_table_ex = {
    "small": {1: 0.01, 10: 0.1, 15: 0.12},
    "medium": {1: 0.03, 10: 0.12, 15: 0.145},
    "big": {1: 0.06, 10: 0.15, 15: 0.18, 20: 0.2},
    "massive": {1: 0.08, 10: 0.17, 15: 0.22, 20: 0.255},
    "unworldly": {1: 0.12, 10: 0.25, 15: 0.33, 20: 0.37},
}
skill_table_omega = {
    "medium": {1: 0.03, 10: 0.12, 15: 0.145, 20: 0.16},
    "big": {1: 0.06, 10: 0.15, 15: 0.18, 20: 0.2},
}
