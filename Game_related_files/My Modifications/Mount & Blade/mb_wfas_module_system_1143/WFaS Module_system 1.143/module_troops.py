import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below...

def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7 | agi_6 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4
def_attrib_multiplayer_inf = str_14 | agi_20 | int_4 | cha_4



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_2|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_1|knows_riding_1|knows_shield_1|knows_inventory_management_1
knows_merchant_npc = knows_riding_1|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_inventory_management_1

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3|knows_horse_archery_1|knows_weapon_master_5|knows_power_draw_1
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5|knows_horse_archery_2|knows_weapon_master_6|knows_power_draw_2
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6|knows_horse_archery_3|knows_weapon_master_7|knows_power_draw_3
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_6|knows_prisoner_management_3|knows_leadership_7|knows_horse_archery_4|knows_weapon_master_8|knows_power_draw_4
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_8|knows_prisoner_management_3|knows_leadership_9|knows_horse_archery_5|knows_weapon_master_9|knows_power_draw_5

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x000000000610301644c3a544d5962d5c00000000001eeb1e0000000000000000
swadian_face_young_1   = 0x00000001790060183ae6b1a2228dd05e00000000001f40530000000000000000
swadian_face_middle_1  = 0x000000092510349808934c3f508a261b00000000001db5580000000000000000
swadian_face_old_1     = 0x00000009750c14982b15719d5c52169400000000001dc8da0000000000000000
swadian_face_older_1   = 0x0000000e7f0c649848e58548ea4b441b00000000001ec7650000000000000000

swadian_face_younger_2 = 0x000000002800001b551ca9e85bcd403400000000001d46d00000000000000000
swadian_face_young_2   = 0x000000045504501b3ad31164c368b70b00000000001e17690000000000000000
swadian_face_middle_2  = 0x00000006af1045dd33a24ed8b36d96d400000000001d44730000000000000000
swadian_face_old_2     = 0x00000009d41035dd2beb8b452e72447b00000000001e47610000000000000000
swadian_face_older_2   = 0x0000000fc00005dd388a8e5863925a7c00000000001fd4dc0000000000000000

vaegir_face_younger_1 = 0x000000000404100d38aa9ab79ece455d00000000001e56d20000000000000000
vaegir_face_young_1   = 0x000000032908400d23564ab763adb9ac00000000001e67220000000000000000
vaegir_face_middle_1  = 0x00000007d308028d439a89c7a49a195600000000001e78150000000000000000
vaegir_face_old_1     = 0x0000000c840c528828d159268b72b71200000000001d72640000000000000000
vaegir_face_older_1   = 0x0000000e9d105289496155b4f2896b6800000000001c5b2c0000000000000000

vaegir_face_younger_2 = 0x000000001608001022e471ca9c2a5b5800000000001e4d220000000000000000
vaegir_face_young_2   = 0x00000003800c50104b5d6ab6d86ea26a00000000001c974c0000000000000000
vaegir_face_middle_2  = 0x00000007cb0c4390171b7239637596a300000000001d470b0000000000000000
vaegir_face_old_2     = 0x0000000a311073902c6a69dac151a33500000000001da4d20000000000000000
vaegir_face_older_2   = 0x0000000fc81023902b259126692d48a100000000001ce66b0000000000000000

khergit_face_younger_1 = 0x000000003710400026544eb9126926d300000000001db6950000000000000000
khergit_face_young_1   = 0x00000003f710400026144eb9126926d300000000001db6a40000000000000000
khergit_face_middle_1  = 0x00000006f710460016144eb9116126d300000000001db6a20000000000000000
khergit_face_old_1     = 0x0000000af810460016144eb9118126d300000000001db6a20000000000000000
khergit_face_older_1   = 0x0000000ff810460016144eb9118126d300000000001db6920000000000000000

khergit_face_younger_2 = 0x00000000381060003aac6adb2175294b00000000001e351a0000000000000000
khergit_face_young_2   = 0x00000003381060003aac6adb2171294b00000000001e35220000000000000000
khergit_face_middle_2  = 0x00000008bf1066803a2d6adb2171294b00000000001e35220000000000000000
khergit_face_old_2     = 0x0000000c39106700282d6b5b2149294b00000000001e351a0000000000000000
khergit_face_older_2   = 0x0000000ff9106700282d6b5b2141294b00000000001e351a0000000000000000

nord_face_younger_1 = 0x000000007510400147a3d8d96640f53300000000001db84b0000000000000000
nord_face_young_1   = 0x000000044300004156e36e56cb60d90400000000001c57210000000000000000
nord_face_middle_1  = 0x0000000735102041249a8aa91180f13400000000001f4aeb0000000000000000
nord_face_old_1     = 0x0000000c410c5041351b85a953a6411300000000001da95b0000000000000000
nord_face_older_1   = 0x0000000fc20070412352a9bb5bd6eb9b00000000001dc72a0000000000000000

nord_face_younger_2 = 0x000000000000200836db6f2be76ff77f00000000001ef6db0000000000000000
nord_face_young_2   = 0x00000005a80c514815918e592275389200000000001f22a50000000000000000
nord_face_middle_2  = 0x00000007c60c528b356c5629956af69b00000000001c94540000000000000000
nord_face_old_2     = 0x0000000dbf10628b6d5a6e798b6af73600000000001f3d1a0000000000000000
nord_face_older_2   = 0x0000000fd110028b242c72e7cc69cb1500000000001e24a50000000000000000

rhodok_face_younger_1 = 0x000000000d000016370b4934924924dc00000000001da6e30000000000000000
rhodok_face_young_1   = 0x00000002cd000016170b4934926924dc00000000001da6e20000000000000000
rhodok_face_middle_1  = 0x00000004ce0003d1170b4934926924dc00000000001da6e20000000000000000
rhodok_face_old_1     = 0x0000000c530003d1170b4934926924dc00000000001da6e20000000000000000
rhodok_face_older_1   = 0x0000000f950003d1064b4934922524dc00000000001da6d20000000000000000

rhodok_face_younger_2 = 0x000000003f00301738dc6db6d3cd472400000000001e38e40000000000000000
rhodok_face_young_2   = 0x000000057f00301738dc6db6d3cd472400000000001e38e40000000000000000
rhodok_face_middle_2  = 0x00000008ff00355738dc6db6d3cd472400000000001e38e40000000000000000
rhodok_face_old_2     = 0x0000000cbf003517389c6db6d3cd472400000000001e38dc0000000000000000
rhodok_face_older_2   = 0x0000000fff003517389c6db6d3a5472400000000001e38dc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","{!}Do not translate","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_5|agi_5|int_5|cha_5,wp(40),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male", "multiplayer profile troop male","multiplayer profile troop male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_mosk_armyak,itm_selo_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female", "multiplayer profile troop female","multiplayer profile troop female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_pure_baba_pol_3,itm_selo_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Commoner","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat", "find item cheat","find item cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence", "Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants", "Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman", "Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club, itm_botinki,itm_evropa_kava_shlapa_c,itm_evropa_odejda_sela],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer", "Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_samopal,itm_cartridges,itm_old_cavalry_botforts,itm_evropa_shlapa,itm_merc_musket_uniforma_b],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman", "Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword, itm_evropa_pehot_tufli,itm_evropa_musket_shlapa_b,itm_swed_civil_b],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter", "Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter", "Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter", "Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter", "Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1", "Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2", "Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3", "Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4", "Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5", "Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6", "Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7", "Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8", "Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9", "Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10", "Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle", "Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer", "Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_kosa,itm_vily,itm_dubinka,itm_plotnik_toporik,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_ukraine_svitka_c,
    itm_selo_boots,itm_mosk_armyak,itm_mosk_sermyaga],
   str_6|agi_5|level(2),wp(40),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman", "Militiaman","Militiamen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_evropa_pehot_tufli,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa,itm_evropa_shlapa_b,
    itm_kopyo,],
   str_7|agi_6|level(5),wp_melee(75),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman", "Mercenary Halberdier","Mercenary Halberdiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_botinki,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_morion,itm_alebarda,itm_infantry_gloves],
   str_9|agi_7|level(9),wp_melee(100),knows_common|knows_ironflesh_2|knows_athletics_2|knows_weapon_master_2,mercenary_face_1, mercenary_face_2],
  ["caravan_guard", "Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,no_scene,0,fac_commoners,
   [itm_steppe_horse_b,itm_old_cavalry_boots,itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_dobrotna_svitka_d,itm_dobrotna_svitka_e,
    itm_prostoy_jupan,itm_prostoy_jupan_b,itm_prostoy_jupan_c,itm_poland_shapka,
    itm_poland_mehova_shapka,itm_kozak_prosta_shapka,itm_moskowit_shapka,itm_sablya_a,itm_sablya_b,itm_sablya_c,itm_sablya_d],
   str_8|agi_10|level(11),wp_melee(110),knows_common|knows_riding_3|knows_ironflesh_1|knows_weapon_master_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman", "Mercenary Marksman","Mercenary Marksmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_sapogi,itm_prostoy_jupan_b,itm_prostoy_jupan_c,itm_prostoy_jupan,itm_poland_svitka_b,itm_poland_svitka_a,itm_poland_svitka_c,itm_poland_svitka_d,itm_poland_shapka,
    itm_poland_mehova_shapka,itm_kozak_prosta_shapka,itm_moskowit_shapka,itm_sablya_pure_a,itm_sablya_pure_b,
    itm_sablya_pure_c,itm_sablya_pure_d,itm_turk_musket_koleso,itm_turk_musket_fitil_b],
   str_9|agi_9|level(9),wp_melee(80)|wp_crossbow(105),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_3|knows_weapon_master_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade", "Mercenary Pikeman","Mercenary Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_infantry_gloves,itm_infantry_boots,itm_merc_pika_uniforma_a,itm_merc_pika_uniforma_b,itm_evropa_kava_shlapa,itm_kabasset,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,
    itm_evropa_shlapa_b,itm_prosta_pike,itm_pika,itm_old_pike],
   str_9|agi_6|level(9),wp_melee(110),knows_common|knows_weapon_master_2,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman", "Mercenary Musketeer","Mercenary Musketeers",tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_infantry_boots,itm_merc_musket_uniforma_a,itm_merc_musket_uniforma_b,itm_evropa_kava_shlapa,
    itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_evropa_shlapa_b,itm_pehot_palash,
    itm_pehot_palash_old,itm_prosta_shpaga_c,itm_prosta_shpaga_b,itm_prosta_shpaga,itm_musket,itm_kabasset],
   str_9|agi_8|level(9),wp_melee(65)|wp_crossbow(115),knows_common|knows_athletics_2|knows_ironflesh_2|knows_weapon_master_3|knows_power_strike_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman", "Mercenary Light Cavalryman","Mercenary Light Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_saddle_horse_b,itm_infantry_gloves,itm_old_cavalry_botforts,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa,
    itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_evropa_shlapa_b,itm_bolts,itm_good_shpaga,itm_good_shpaga_b,itm_good_shpaga_c,itm_old_pistol,itm_pistol,itm_pistol_b],
  str_9|agi_9|level(11),wp_melee(100)|wp_crossbow(120),knows_common|knows_riding_3|knows_ironflesh_1|knows_weapon_master_3|knows_horse_archery_5,mercenary_face_1, mercenary_face_2],
  ["mercenaries_end", "mercenaries end","mercenaries end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

#----------------------------------------------------------
########## RP#####################
#---------------------------------------------------------
  ["swadian_recruit", "Scythe Wielder","Scythe Wielders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_kosa,itm_poland_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots],
   def_attrib|level(3),wp_melee(50)|wp_crossbow(20)|wp_archery(10),knows_common,swadian_face_younger_1, swadian_face_young_2],

  ["swadian_militia", "Militia Pikeman","Pikeman Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_kopyo,itm_poland_shapka,itm_poland_army_hat_simple,itm_poland_mehova_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots],
   str_7|agi_6|level(4),wp_melee(60),knows_common|knows_athletics_3|knows_ironflesh_2,swadian_face_young_1, swadian_face_young_2],
  ["swadian_militia_levelup", "Militia Pikeman","Pikeman Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_kopyo,itm_poland_shapka,itm_poland_army_hat_simple,itm_poland_mehova_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots],
   str_8|agi_7|level(7),wp_melee(75),knows_common|knows_athletics_3|knows_ironflesh_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_skirmisher", "Musket Militiaman","Musket Militia",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_rusty_toporik,itm_prostoy_toporik,
    itm_old_musket,itm_old_musket_b,itm_cartridges,itm_bolts,itm_poland_shapka,itm_poland_army_hat_simple,
    itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots,itm_poland_mehova_shapka],
   str_7|agi_6|level(4),wp_melee(35)|wp_crossbow(55),knows_common|knows_athletics_1,swadian_face_young_1, swadian_face_young_2],
  ["swadian_skirmisher_levelup", "Musket Militiaman (veteran)","Musket Militiamen (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_rusty_toporik,itm_prostoy_toporik,
    itm_old_musket,itm_old_musket_b,itm_cartridges,itm_bolts,itm_poland_shapka,itm_poland_army_hat_simple,
    itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots,itm_poland_mehova_shapka],
   str_8|agi_7|level(7),wp_melee(50)|wp_crossbow(70),knows_common|knows_athletics_1,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_footman", "Pikeman","Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_prosta_pike,itm_poland_pikiner_uniform,itm_sapogi,itm_poland_army_hat_simple],
   str_9|agi_7|level(6),wp_melee(95),knows_common|knows_athletics_4|knows_weapon_master_1|knows_ironflesh_3|knows_power_strike_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_footman_levelup", "Pikeman (veteran)","Pikemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_pika,itm_poland_pikiner_uniform,itm_sapogi,itm_poland_army_hat_simple],
   str_10|agi_8|level(10),wp_melee(110),knows_common|knows_ironflesh_4|knows_athletics_4|knows_weapon_master_2|knows_power_strike_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_crossbowman", "Zolnier","Zolniers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_musket,itm_bolts,
    itm_poland_musketer_uniform,itm_sapogi,itm_poland_army_hat_simple],
   str_8|agi_7|level(6),wp_melee(60)|wp_crossbow(100),knows_common|knows_athletics_3|knows_weapon_master_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_crossbowman_levelup", "Zolnier (veteran)","Zolniers (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_musket,itm_good_musket,itm_bolts,
    itm_poland_musketer_uniform,itm_sapogi,itm_poland_army_hat_simple],
   str_9|agi_8|level(10),wp_melee(75)|wp_crossbow(115),knows_common|knows_ironflesh_1|knows_athletics_3|knows_weapon_master_2,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_infantry", "German Infantry Pikeman","German Infantry Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_pika,itm_poland_uniforma_german_line,itm_evropa_pehot_tufli,itm_morion_good,itm_kabasset,itm_infantry_gloves],
   str_10|agi_7|level(12),wp_melee(115),knows_common|knows_power_strike_1|knows_weapon_master_2,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_infantry_levelup", "German Infantry Pikeman (veteran)","German Infantry Pikemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_good_pike,itm_poland_uniforma_german_line,itm_evropa_pehot_tufli,itm_morion_good,itm_kabasset,itm_leather_gloves],
   str_11|agi_8|level(16),wp_melee(130),knows_common|knows_ironflesh_1|knows_power_strike_2|knows_weapon_master_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_sharpshooter", "German Infantry Musketeer","German Infantry Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_good_shpaga_b,itm_good_shpaga_c,itm_good_shpaga_d,itm_good_shpaga,itm_good_musket,itm_bolts,
    itm_poland_uniforma_german_line_musketeer,itm_morion_good,itm_kabasset,itm_evropa_pehot_tufli],
   str_10|agi_8|level(12),wp_melee(70)|wp_crossbow(130),knows_common|knows_ironflesh_2|knows_athletics_1|knows_power_strike_2|knows_weapon_master_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sharpshooter_levelup", "German Infantry Musketeer (veteran)","German Infantry Musketeers (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_good_shpaga_b,itm_good_shpaga_c,itm_good_shpaga_d,itm_good_shpaga,itm_mushket_udarniy,itm_bolts,
    itm_poland_uniforma_german_line_musketeer,itm_morion_good,itm_kabasset,itm_evropa_pehot_tufli,itm_infantry_gloves],
   str_11|agi_9|level(16),wp_melee(85)|wp_crossbow(145),knows_common|knows_ironflesh_3|knows_athletics_1|knows_power_strike_3|knows_weapon_master_4,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_man_at_arms", "Volunteer","Volunteers",tf_mounted|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_sablya_b,itm_sablya_a,itm_sablya_c,itm_sablya_d,itm_old_pistol,itm_pistol,itm_pistol_b,itm_cartridges,itm_bolts,
    itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_dobrotna_svitka_d,itm_dobrotna_svitka_e,itm_old_cavalry_boots,itm_cavalry_boots,
    itm_poland_mehova_shapka_s_perom,itm_poland_good_shapka,itm_poland_mehova_shapka,itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c],
   str_9|agi_9|level(10),wp_melee(120)|wp_crossbow(95),knows_common|knows_riding_5|knows_horse_archery_4|knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_levelup", "Volunteer (veteran)","Volunteers (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_sablya_b,itm_sablya_a,itm_sablya_c,itm_sablya_d,itm_old_pistol,itm_pistol,itm_pistol_b,itm_cartridges,itm_bolts,
    itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_dobrotna_svitka_d,itm_dobrotna_svitka_e,itm_old_cavalry_boots,itm_cavalry_boots,
    itm_poland_mehova_shapka_s_perom,itm_poland_good_shapka,itm_poland_mehova_shapka,itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c],
   str_10|agi_10|level(13),wp_melee(135)|wp_crossbow(110),knows_common|knows_riding_5|knows_horse_archery_5|knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_4,swadian_face_middle_1, swadian_face_older_2],
  ["polish_dragoon", "Dragoon","Dragoons",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_sablya_pure_c,itm_sablya_pure_a,itm_sablya_pure_d,itm_sablya_pure_b,itm_karabin,itm_round_shield_c,itm_bolts,
    itm_poland_dragoon_uniform,itm_old_cavalry_boots,itm_poland_army_hat_b,itm_poland_army_hat_a,itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c],
   str_8|agi_9|level(9),wp_melee(85)|wp_crossbow(110),knows_common|knows_riding_3|knows_horse_archery_4|knows_ironflesh_1|knows_weapon_master_3|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["polish_dragoon_levelup", "Dragoon (veteran)","Dragoons (veteran)",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_sablya_c,itm_sablya_a,itm_sablya_d,itm_sablya_b,itm_karabin_good,itm_round_shield_c,itm_bolts,
    itm_poland_dragoon_uniform,itm_old_cavalry_boots,itm_poland_army_hat_b,itm_poland_army_hat_a,itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c],
   str_9|agi_10|level(12),wp_melee(100)|wp_crossbow(125),knows_common|knows_riding_3|knows_horse_archery_5|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_4|knows_shield_4,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_sergeant", "Armored Cossack","Armored Cossacks",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_sablya_c,itm_sablya_d,itm_sablya_a,itm_sablya_b,itm_chekan,itm_klevetz,itm_round_shield_c,
    itm_cavalry_pika_a,itm_luk_c,itm_luk_b,itm_arrows,itm_kolchuga_panzernika,
    itm_cavalry_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_hunter],
   str_10|agi_9|level(16),wp_melee(130)|wp_archery(90),knows_common|knows_riding_4|knows_horse_archery_4|knows_ironflesh_2|knows_weapon_master_4|knows_power_draw_2|knows_shield_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant_levelup", "Armored Cossack (veteran)","Armored Cossacks (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_sablya_c,itm_sablya_d,itm_sablya_a,itm_sablya_b,itm_chekan_good,itm_klevetz_good,itm_round_shield_c,
    itm_cavalry_pika_a,itm_konchar,itm_kompozit_bow_b,itm_luk_c,itm_barbed_arrows,itm_kolchuga_panzernika,
    itm_cavalry_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_hunter],
   str_11|agi_10|level(21),wp_melee(145)|wp_archery(105),knows_common|knows_riding_4|knows_horse_archery_5|knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_5|knows_power_draw_3|knows_shield_5,swadian_face_middle_1, swadian_face_older_2],
  ["polish_reytar", "Polish Reiter","Polish Reiters",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_bolts,itm_old_pistol,itm_pistol,itm_pistol_b,itm_good_shpaga,itm_good_shpaga_b,itm_good_shpaga_c,itm_good_shpaga_d,itm_kirasa,itm_morion,itm_old_cavalry_boots,itm_infantry_gloves,
    itm_saddle_horse_c,itm_saddle_horse_b],
   str_9|agi_9|level(16),wp_melee(125)|wp_crossbow(120),knows_common|knows_riding_3|knows_horse_archery_4|knows_ironflesh_1|knows_weapon_master_4,swadian_face_middle_1, swadian_face_old_2],
  ["polish_reytar_levelup", "Polish Reiter (veteran)","Polish Reiters (veteran)",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_bolts,itm_good_pistol,itm_good_pistol_c,itm_good_pistol_b,itm_good_shpaga,itm_good_shpaga_b,itm_good_shpaga_c,itm_good_shpaga_d,itm_kirasa,itm_morion,itm_old_cavalry_boots,itm_infantry_gloves,
    itm_hunter],
   str_10|agi_10|level(21),wp_melee(140)|wp_crossbow(135),knows_common|knows_riding_4|knows_horse_archery_5|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_5,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_knight", "Winged Hussar","Winged Hussars",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_gusar_lanza,itm_gusar_lanza_b,itm_poland_gusar_panzer,itm_poland_gusar_panzer_bez_kril,itm_good_cavalry_boots,itm_poland_gusar_helmet,itm_hunter],
   str_11|agi_10|level(21),wp_melee(155),knows_common|knows_riding_6|knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_5,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_knight_levelup", "Winged Hussar (veteran)","Winged Hussars (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_gusar_lanza,itm_gusar_lanza_b,itm_poland_gusar_panzer,itm_poland_gusar_panzer_bez_kril,itm_poland_gusar_yaguar,itm_good_cavalry_boots,itm_poland_gusar_helmet,
    itm_poland_gusar_helmet_greben,itm_rich_horse,itm_rich_horse_b],
   str_12|agi_11|level(25),wp_melee(170),knows_common|knows_riding_6|knows_ironflesh_5|knows_power_strike_3|knows_weapon_master_6,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_messenger", "Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_old_cavalry_boots,itm_saddle_horse_c,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_shapka,itm_poland_mehova_shapka,itm_sablya_b,itm_sablya_c],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_deserter", "Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_deserters,
   [itm_selo_boots,itm_sapogi,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_shapka,itm_poland_mehova_shapka,itm_poland_army_hat_a,itm_poland_army_hat_b,
    itm_sablya_pure_c,itm_sablya_pure_b,itm_old_musket,itm_old_musket_b,itm_cartridges,itm_pistol],
   def_attrib|level(10),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_prison_guard", "Prison Guard","Prison Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sapogi,itm_poland_pikiner_uniform,itm_poland_mehova_shapka,itm_poland_army_hat_a,itm_poland_army_hat_b,itm_sablya_b],
   def_attrib|level(20),wp(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_castle_guard", "Guard","Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_botinki,itm_poland_uniforma_german_line,itm_morion,itm_alebarda],
   def_attrib|level(25),wp(150),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_old_2],

#----------------------------------------------------------
##########MOSK###################
#---------------------------------------------------------
  ["vaegir_recruit", "Staff Militiaman","Staff Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_vily,itm_dubinka,itm_plotnik_toporik,itm_plotnik_topor,itm_mosk_armyak,itm_mosk_sermyaga,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_7|agi_5|level(3),wp_melee(35)|wp_crossbow(20)|wp_archery(10),knows_common, vaegir_face_younger_1, vaegir_face_young_2],

  ["vaegir_footman", "Lance Militiaman","Lance Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_kopyo,itm_pure_streletzkiy_mundir_spear,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_8|agi_6|level(4),wp_melee(60),knows_common|knows_ironflesh_4|knows_athletics_4|knows_power_strike_1, vaegir_face_young_1, vaegir_face_young_2],
  ["vaegir_footman_levelup", "Pike Militiaman (veteran)","Pike Militiamen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_kopyo,itm_pure_streletzkiy_mundir_spear,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_9|agi_7|level(7),wp_melee(75),knows_common|knows_ironflesh_5|knows_athletics_4|knows_power_strike_2, vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_skirmisher", "Posad Marksman","Posad Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_sablya_pure_c,itm_sablya_pure_b,itm_sablya_turk_pure_b,itm_sablya_turk_pure_a,itm_old_musket,itm_old_musket_b,
    itm_cartridges,itm_bolts,itm_plotnik_toporik,itm_plotnik_topor,itm_pure_streletzkiy_mundir,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_8|agi_6|level(4),wp_melee(45)|wp_crossbow(50),knows_common|knows_ironflesh_2|knows_athletics_2,vaegir_face_young_1, vaegir_face_young_2],
  ["vaegir_skirmisher_levelup", "Posad Marksman (veteran)","Posad Marksmen (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_sablya_pure_c,itm_sablya_pure_b,itm_sablya_turk_pure_b,itm_sablya_turk_pure_a,itm_old_musket,itm_old_musket_b,
    itm_bolts,itm_rusty_toporik,itm_prostoy_toporik,itm_pure_streletzkiy_mundir,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_9|agi_7|level(7),wp_melee(60)|wp_crossbow(65),knows_common|knows_ironflesh_3|knows_athletics_2,vaegir_face_middle_1, vaegir_face_old_2],

  ["vaegir_veteran", "Marksman Spearman","Marksman Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_kopyo,itm_streletzkiy_mundir_spear,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c],
   str_9|agi_7|level(6),wp_melee(95),knows_common|knows_ironflesh_5|knows_athletics_5|knows_weapon_master_1|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_veteran_levelup", "Marksmen Spearman (veteran)","Marksmen Spearmen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_kopyo,itm_streletzkiy_mundir_spear,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c],
   str_10|agi_8|level(10),wp_melee(110),knows_common|knows_ironflesh_6|knows_athletics_5|knows_power_strike_3|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_archer", "Marksman","Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_musket,itm_bolts,itm_berdish,itm_berdish_b,itm_streletzkiy_mundir,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c],
   str_9|agi_6|level(6),wp_melee(55)|wp_crossbow(90),knows_common|knows_ironflesh_3|knows_athletics_3|knows_weapon_master_1,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_archer_levelup", "Marksman (veteran)","Marksmen (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_musket,itm_bolts,itm_berdish,itm_berdish_b,itm_streletzkiy_mundir,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c],
   str_10|agi_7|level(10),wp_melee(70)|wp_crossbow(105),knows_common|knows_ironflesh_4|knows_athletics_3|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_infantry", "New Order Spearman","New Order Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_prosta_pike,itm_new_line_uniform_spear,itm_sapogi,itm_new_line_helmet,itm_leather_gloves],
   str_10|agi_8|level(11),wp_melee(110),knows_common|knows_ironflesh_6|knows_athletics_3|knows_power_strike_4|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_infantry_levelup", "New Order Pikeman (veteran)","New Order Pikemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_pika,itm_new_line_uniform_spear,itm_kozak_boots,itm_new_line_helmet,itm_cavalry_gloves],
   str_11|agi_9|level(15),wp_melee(125),knows_common|knows_ironflesh_7|knows_athletics_3|knows_power_strike_5|knows_weapon_master_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_marksman", "New Order Marksman","New Order Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_musket,itm_steel_bolts,itm_berdish,itm_berdish_b,itm_new_line_uniform,itm_kozak_boots,itm_new_line_helmet],
   str_10|agi_7|level(11),wp_melee(60)|wp_crossbow(110),knows_common|knows_ironflesh_4|knows_athletics_3|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_marksman_levelup", "New Order Marksman (veteran)","New Order Marksmen (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_musket,itm_steel_bolts,itm_berdish,itm_berdish_b,itm_new_line_uniform,itm_kozak_boots,itm_new_line_helmet],
   str_11|agi_8|level(15),wp_melee(75)|wp_crossbow(125),knows_common|knows_ironflesh_5|knows_athletics_3|knows_power_strike_1|knows_weapon_master_3,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_horseman", "Armed Serf","Armed Serfs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_sovnya,itm_sablya_pure_a,itm_sablya_turk_pure_a,itm_sablya_pure_b,itm_shapka_bumajna_a,
    itm_shapka_bumajna_b,itm_sablya_pure_c,itm_luk,itm_arrows,itm_moskow_tulup_a,itm_moskow_tulup_b,itm_moskow_tulup_c,
    itm_selo_boots,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka,itm_shishak,itm_sumpter_horse],
   str_9|agi_6|level(7),wp_melee(75)|wp_archery(60),knows_common|knows_riding_2|knows_power_draw_1|knows_ironflesh_1|knows_horse_archery_3,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_horseman_levelup", "Battle Serf (veteran)","Battle Serfs (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_sovnya,itm_sablya_pure_a,itm_sablya_turk_pure_a,itm_sablya_pure_b,itm_shapka_bumajna_a,
    itm_shapka_bumajna_b,itm_sablya_pure_c,itm_luk_b,itm_arrows,itm_moskow_tulup_a,itm_moskow_tulup_b,itm_moskow_tulup_c,
    itm_selo_boots,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka,itm_shishak,itm_saddle_horse,itm_saddle_horse_b],
   str_10|agi_7|level(10),wp_melee(90)|wp_archery(75),knows_common|knows_riding_3|knows_power_draw_2|knows_ironflesh_2|knows_horse_archery_4,vaegir_face_middle_1, vaegir_face_older_2],

  ["moskow_dragoon", "Gentry Cavalryman","Gentry Cavalry",tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_sovnya,itm_sablya_turk_c,itm_sablya_turk_b,itm_sablya_a,itm_sablya_b,itm_sablya_c,itm_sablya_d,itm_klevetz,itm_chekan,itm_cavalry_boots,
    itm_east_arrows,itm_luk_b,itm_luk_c,itm_mosk_bahter_b,itm_moskow_tulup_c,itm_moskow_tulup_b,itm_moskow_tulup_a,itm_mosk_bahter_b,itm_mosk_bahter_b,itm_moskow_bahter_a,itm_mosk_bahter_b,itm_shapka_bumajna_a,itm_shapka_bumajna_b,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_c,
    itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c],
   str_11|agi_7|level(15),wp_melee(140)|wp_archery(95),knows_riding_4|knows_horse_archery_4|knows_ironflesh_2|knows_power_strike_1|knows_power_draw_2|knows_weapon_master_4,vaegir_face_middle_1, vaegir_face_old_2],
  ["moskow_dragoon_levelup", "Estate Cavalryman (veteran)","Estate Cavalry (veteran)",tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_sovnya,itm_sablya_turk_c,itm_sablya_turk_b,itm_sablya_a,itm_sablya_b,itm_sablya_c,itm_sablya_d,itm_klevetz_good,itm_chekan_good,itm_mosk_bahter_b,itm_moskow_bahter_a,itm_moskow_kuyak,itm_mosk_bahter_b,
    itm_good_cavalry_boots,itm_barbed_arrows,itm_luk_c,itm_kompozit_bow_b,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_c,itm_shishak,itm_mosk_shishak,itm_saddle_horse_c,itm_hunter,itm_courser],
   str_12|agi_8|level(20),wp_melee(155)|wp_archery(110),knows_riding_5|knows_horse_archery_5|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_3|knows_weapon_master_5,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_knight", "Moscow Reiter","Moscow Reiters",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_palash,itm_pistol,itm_pistol_b,itm_old_pistol,itm_karabin,itm_bolts,itm_shelom,itm_moskow_reytar_helmet,itm_moskow_reytar_armor,itm_old_cavalry_boots,
    itm_saddle_horse,itm_saddle_horse_b,itm_leather_gloves],
   str_10|agi_8|level(16),wp_melee(130)|wp_crossbow(110),knows_common|knows_riding_3|knows_horse_archery_5|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_4,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_knight_levelup", "Moscow Reiter (veteran)","Moscow Reiters (veteran)",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_good_palash,itm_good_palash_b,itm_good_pistol_b,itm_good_pistol_c,itm_karabin_good,
    itm_bolts,itm_shelom,itm_moskow_reytar_helmet,itm_moskow_reytar_armor,itm_cavalry_boots,itm_saddle_horse_c,itm_hunter,itm_cavalry_gloves],
   str_11|agi_9|level(21),wp_melee(145)|wp_crossbow(125),knows_common|knows_riding_4|knows_horse_archery_6|knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_5,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_guard", "Noble Guard","Noble Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_sablya_d,itm_sablya_c,itm_sablya_b,itm_chekan_good,itm_palitza,itm_shestoper,itm_sablya_turk_c,itm_sablya_turk_b,
    itm_cavalry_pika_b,itm_cavalry_pika_a,itm_sovnya,itm_moskow_boyar_uniform,itm_good_cavalry_boots,itm_boyar_helmet,itm_mosk_shishak,
    itm_misurka_s_barmizoy_rich,itm_hunter,itm_cavalry_gloves],
   str_12|agi_7|level(21),wp_melee(165),knows_common|knows_riding_4|knows_ironflesh_4|knows_power_strike_3|knows_weapon_master_5,vaegir_face_middle_1, vaegir_face_old_2],
  ["vaegir_guard_levelup", "Noble Guard (veteran)","Noble Guards (veteran)",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_sablya_d,itm_sablya_c,itm_sablya_b,itm_chekan_good,itm_palitza,itm_shestoper,itm_sablya_turk_c,itm_sablya_turk_b, itm_cavalry_gloves,
    itm_cavalry_pika_b,itm_cavalry_pika_a,itm_sovnya,itm_moskow_boyar_uniform,itm_moskow_zertzalo,itm_good_cavalry_boots,itm_boyar_helmet,itm_mosk_shishak,itm_rich_horse,itm_rich_horse_b],
   str_13|agi_8|level(25),wp_melee(180),knows_common|knows_riding_4|knows_ironflesh_5|knows_power_strike_4|knows_weapon_master_6,vaegir_face_old_1, vaegir_face_older_2],

  ["vaegir_messenger", "Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_saddle_horse_b,itm_sapogi,itm_selo_boots,itm_pure_streletzkiy_mundir_spear,itm_moskowit_shapka,itm_streletz_shapka_c,itm_sablya_pure_a,itm_sablya_turk_pure_a],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_deserter", "Vaegir Deserter","Vaegir Deserters",tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_cartridges,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_selo_boots,itm_mosk_sermyaga,itm_mosk_armyak,itm_pure_streletzkiy_mundir_spear,
    itm_moskowit_shapka,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c,itm_sablya_pure_a,itm_sablya_turk_pure_a,itm_kopyo,itm_samopal,itm_old_musket,
    itm_old_musket_b,itm_luk],
   def_attrib|str_10|level(10),wp(90),knows_ironflesh_1|knows_power_draw_1,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_prison_guard", "Prison Guard","Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_moskow_tulup_b,itm_shishak,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_prostoy_toporik],
   def_attrib|level(20),wp(100),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard", "Guard","Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_sapogi,itm_moskow_reytar_armor,itm_new_line_helmet,itm_good_kopyo],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["rinda", "Tsar Bodyguard","Tsar Bodyguards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_sapogi,itm_rinda_shuba,itm_rinda_hat,itm_berdish],
   def_attrib|level(25),wp(250),knows_athletics_5|knows_shield_5|knows_ironflesh_10,vaegir_face_old_1, vaegir_face_older_2],
  
#----------------------------------------------------------
##########TATAR##################
#---------------------------------------------------------
  ["khergit_tribesman", "Nomad","Nomads",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sablya_tatar_pure_a,itm_sablya_turk_pure_a,itm_yatagan_a,itm_arrows,itm_luk,itm_sumpter_horse,
    itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,itm_tatar_man_hat,itm_selo_boots],
   str_6|agi_7|level(3),wp_melee(40)|wp_crossbow(20)|wp_archery(30),knows_common|knows_riding_2|knows_power_draw_1,khergit_face_younger_1, khergit_face_young_2],

  ["khergit_skirmisher", "Kapikulu","Kapikulu",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_arrows,itm_luk_b,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_a,itm_sablya_turk_pure_b,itm_yatagan_a,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,
    itm_shield,itm_selo_boots,itm_tatar_man_hat],
   str_6|agi_6|level(5),wp_melee(55)|wp_archery(55),knows_common|knows_shield_2|knows_athletics_2|knows_power_draw_1,khergit_face_younger_1, khergit_face_young_2],
  ["khergit_skirmisher_levelup", "Kapikulu (veteran)","Kapikulu (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_luk_b,itm_luk_c,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_a,itm_sablya_turk_pure_b,itm_yatagan_good,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,
    itm_shield,itm_selo_boots,itm_misurka_s_barmizoy_pure],
   str_7|agi_7|level(8),wp_melee(70)|wp_archery(70),knows_common|knows_shield_3|knows_athletics_2|knows_power_draw_2,khergit_face_middle_1, khergit_face_old_2],
  ["khergit_horseman", "Bajrak","Bajraks",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [itm_saddle_horse,itm_saddle_horse_b,itm_arrows,itm_luk_b,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_c,itm_sablya_turk_pure_b,itm_tatar_halat_a,itm_tatar_halat_b,
   itm_old_cavalry_boots,itm_sapogi,itm_cavalry_pika_a,itm_shield,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_tatar_kolpak],
   str_6|agi_7|level(4),wp_melee(55)|wp_archery(55),knows_common|knows_riding_3|knows_power_draw_1|knows_horse_archery_4|knows_shield_2,khergit_face_younger_1, khergit_face_young_2],
  ["khergit_horseman_levelup", "Bajrak (veteran)","Bajraks (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
  [itm_saddle_horse_b,itm_saddle_horse_c,itm_khergit_arrows,itm_luk_c,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_c,itm_sablya_turk_pure_b,itm_tatar_halat_a,itm_tatar_halat_b,
   itm_old_cavalry_boots,itm_sapogi,itm_cavalry_pika_b,itm_shield,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_tatar_kolpak],
   str_7|agi_8|level(7),wp_melee(70)|wp_archery(70),knows_common|knows_riding_4|knows_power_draw_2|knows_horse_archery_5|knows_shield_3,khergit_face_middle_1, khergit_face_old_2],

  ["saymen", "Seymen","Seymens",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_steel_bolts,itm_sapogi,itm_tatar_seymen_armor,itm_tatar_misurka,itm_misurka_s_barmizoy_pure,
    itm_misurka_s_barmizoy_b,itm_yatagan_good,itm_sablya_turk_a,itm_turk_musket_fitil_b],
   str_8|agi_7|level(10),wp_melee(80)|wp_crossbow(70),knows_power_strike_1|knows_ironflesh_1,khergit_face_middle_1, khergit_face_old_2],
  ["saymen_levelup", "Seymen (veteran)","Seymens (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_steel_bolts,itm_sapogi,itm_tatar_seymen_armor,itm_tatar_misurka,itm_misurka_s_barmizoy_b,itm_yatagan_rich,itm_sablya_turk_a,itm_turk_musket_koleso],
   str_9|agi_8|level(14),wp_melee(95)|wp_crossbow(85),knows_power_strike_2|knows_ironflesh_2,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_horse_archer", "Jasaq","Jasaqs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_sablya_turk_pure_a,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_c,itm_sablya_turk_pure_b,itm_luk_c,itm_steppe_horse,itm_steppe_horse_b,
    itm_tatar_halat_a,itm_tatar_halat_b,itm_sapogi,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_tatar_kolpak],
   str_6|agi_8|level(8),wp_melee(85)|wp_archery(95),knows_riding_5|knows_power_draw_2|knows_horse_archery_4,khergit_face_middle_1, khergit_face_old_2],
  ["khergit_horse_archer_levelup", "Jasaq (veteran)","Jasaqs (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_sablya_turk_a,itm_sablya_tatar_a,itm_sablya_turk_c,itm_sablya_turk_b,itm_kompozit_bow_b,itm_steppe_horse,itm_steppe_horse_b,itm_tatar_halat_a,itm_tatar_halat_b,itm_sapogi,
    itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_tatar_kolpak],
   str_7|agi_9|level(11),wp_melee(100)|wp_archery(110),knows_riding_6|knows_power_draw_3|knows_horse_archery_5|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer", "Oglan","Oglans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_cavalry_pika_a,itm_cavalry_pika_b,itm_cavalry_boots,itm_sapogi,itm_tatar_steg_halat_a,
    itm_tatar_steg_halat_b,itm_steppe_horse,itm_steppe_horse_b,itm_round_shield_d,itm_round_shield_c,itm_tatar_oglan_hat,itm_tatar_bayrak_hat,itm_tatar_nogay_hat],
   str_7|agi_8|level(8),wp_melee(85),knows_riding_5|knows_weapon_master_2|knows_shield_4,khergit_face_middle_1, khergit_face_old_2],
  ["khergit_lancer_levelup", "Oglan (veteran)","Oglans (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_kozacka_pika,itm_cavalry_boots,itm_sapogi,itm_tatar_steg_halat_a,itm_tatar_steg_halat_b,itm_steppe_horse,itm_steppe_horse_b,itm_round_shield_d,itm_round_shield_c,
    itm_misurka_s_barmizoy_c,itm_misurka_s_barmizoy_pure,itm_tatar_misurka],
   str_8|agi_9|level(11),wp_melee(100),knows_riding_6|knows_weapon_master_3|knows_ironflesh_1|knows_shield_5,khergit_face_middle_1, khergit_face_older_2],

  ["khergit_veteran_horse_archer", "Mirza Chambul","Mirza Chambul",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_barbed_arrows,itm_khergit_arrows,itm_sablya_turk_c,itm_tatar_helmet_b,itm_tatar_steg_halat_a,itm_tatar_steg_halat_b,itm_sablya_turk_b,itm_sablya_turk_a,itm_kompozit_bow_b,itm_steppe_horse,
    itm_steppe_horse_b,itm_cavalry_boots,itm_cavalry_boots,itm_tatar_misurka,itm_misurka_s_barmizoy_c],
   str_8|agi_9|level(15),wp_melee(110)|wp_archery(110),knows_riding_4|knows_power_draw_3|knows_horse_archery_6|knows_weapon_master_3,khergit_face_middle_1, khergit_face_old_2],
  ["khergit_veteran_horse_archer_levelup", "Mirza Chambul (veteran)","Mirza Chambul (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_barbed_arrows,itm_sablya_turk_c,itm_tatar_helmet_b,itm_tatar_kolcha,itm_tatar_bahter_b,itm_sablya_turk_b,itm_sablya_turk_a,itm_kompozit_bow,itm_kompozit_bow_b,itm_courser,
    itm_cavalry_boots,itm_kalmyk_boots,itm_tatar_misurka,itm_misurka_s_barmizoy_c],
   str_9|agi_10|level(20),wp_melee(125)|wp_archery(125),knows_riding_5|knows_power_draw_4|knows_horse_archery_7|knows_weapon_master_4|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],
  ["asak_bey", "Asak-bey","Asak-beys",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sablya_tatar_a,itm_sablya_turk_b,itm_sablya_turk_c,itm_courser,itm_tatar_kolcha,itm_tatar_bahter_b,itm_tatar_helmet_b,itm_tatar_misurka_rich,itm_kalmyk_boots,itm_round_shield,itm_round_shield_b],
   str_9|agi_9|level(16),wp_melee(135),knows_riding_4|knows_ironflesh_1|knows_weapon_master_4|knows_shield_5,khergit_face_middle_1, khergit_face_old_2],
  ["asak_bey_levelup", "Asak-bey (veteran)","Asak-beys (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sablya_tatar_a,itm_sablya_turk_b,itm_sablya_turk_c,itm_courser,itm_tatar_kolcha,itm_tatar_bahter_b,
    itm_tatar_yushman,itm_tatar_han_helmet,itm_tatar_helmet_b,itm_tatar_misurka_rich,itm_kalmyk_boots,
    itm_round_shield,itm_round_shield_b,itm_round_shield_steel_b],
   str_10|agi_10|level(21),wp_melee(150),knows_riding_5|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_5|knows_shield_6,khergit_face_middle_1, khergit_face_older_2],

  ["zyndjirli", "Nokhor","Nokhors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_kozacka_pika,itm_hunter,itm_tatar_yushman,itm_kalmyk_boots,itm_round_shield_steel_b,itm_tatar_helmet_a],
   str_10|agi_9|level(21),wp_melee(160),knows_riding_5|knows_ironflesh_2|knows_power_strike_3|knows_shield_7|knows_weapon_master_6,khergit_face_middle_1, khergit_face_older_2],
  ["zyndjirli_levelup", "Nokhor (veteran)","Nokhors (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_kozacka_pika,itm_rich_horse,itm_tatar_bahter_a,itm_kalmyk_boots,itm_round_shield_steel_b,itm_tatar_helmet_a],
   str_11|agi_10|level(25),wp_melee(175),knows_riding_6|knows_ironflesh_3|knows_power_strike_4|knows_shield_8|knows_weapon_master_7,khergit_face_old_1, khergit_face_older_2],

  ["khergit_messenger", "Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_steppe_horse_b,itm_old_cavalry_boots,itm_sapogi,itm_tatar_halat_a,itm_tatar_halat_b,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_sablya_tatar_a],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_deserter", "Deserter","Deserters",tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_saddle_horse,itm_sapogi,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_bayrak_hat,itm_tatar_nogay_hat,itm_sablya_turk_pure_a,itm_sablya_tatar_pure_a,itm_luk,itm_luk_b],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_prison_guard", "Prison Guard","Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_sapogi,itm_yatagan_good,itm_shield,itm_tatar_misurka,itm_tatar_kolcha],
   def_attrib|level(20),wp(100),knows_athletics_3|knows_shield_2|knows_ironflesh_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard", "Guard","Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_yatagan_rich,itm_round_shield_b,itm_good_cavalry_boots,itm_tatar_yushman,itm_tatar_misurka],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,khergit_face_middle_1, khergit_face_older_2],

#----------------------------------------------------------
##########SWED###################
#---------------------------------------------------------
  ["nord_recruit", "Town Militiaman","Town Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_kopyo,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_botinki,itm_evropa_shapka],
   str_7|agi_5|level(3),wp_melee(40)|wp_crossbow(20)|wp_archery(10),knows_common,nord_face_younger_1, nord_face_young_2],

  ["nord_footman", "Militia Pikeman","Pikeman Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_old_pike,itm_evropa_odejda_sela_b,itm_evropa_odejda_sela,itm_botinki,itm_evropa_shapka,itm_evropa_shlapa_b,itm_evropa_kava_shlapa],
   str_7|agi_7|level(5),wp_melee(55),knows_ironflesh_1,nord_face_younger_1, nord_face_young_2],
  ["nord_footman_levelup", "Militia Pikeman (veteran)","Pikeman Militia (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_prosta_pike,itm_evropa_odejda_sela_b,itm_evropa_odejda_sela,itm_botinki,itm_evropa_shapka,itm_evropa_shlapa_b,itm_evropa_kava_shlapa],
   str_8|agi_8|level(8),wp_melee(70),knows_ironflesh_2,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman", "Militia Musketeer","Musketeer Militia",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_pehot_palash_old,itm_rusty_shpaga,itm_old_musket,itm_old_musket_b,itm_bolts,
    itm_evropa_odejda_sela_b,itm_evropa_odejda_sela,itm_evropa_pehot_tufli,itm_evropa_shapka,itm_evropa_shlapa_b,itm_evropa_kava_shlapa],
   str_7|agi_7|level(5),wp_melee(40)|wp_crossbow(65),knows_athletics_1,nord_face_younger_1, nord_face_young_2],
  ["nord_huntsman_levelup", "Militia Musketeer (veteran)","Musketeer Militia (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_pehot_palash_old,itm_rusty_shpaga,itm_old_musket,itm_old_musket_b,itm_bolts,
    itm_evropa_odejda_sela_b,itm_evropa_odejda_sela,itm_evropa_pehot_tufli,itm_evropa_shapka,itm_evropa_shlapa_b,itm_evropa_kava_shlapa],
   str_8|agi_8|level(8),wp_melee(55)|wp_crossbow(80),knows_athletics_1,nord_face_middle_1, nord_face_older_2],

  ["nord_trained_footman", "Pikeman","Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_pika,itm_evropa_pika_uniforma,itm_morion,itm_evropa_pehot_tufli,itm_infantry_gloves],
   str_8|agi_6|level(7),wp_melee(85),knows_weapon_master_1,nord_face_middle_1, nord_face_old_2],
  ["nord_trained_footman_levelup", "Pikeman (veteran)","Pikemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_pike,itm_evropa_pika_uniforma,itm_morion_good,itm_evropa_pehot_tufli,itm_infantry_gloves],
   str_9|agi_7|level(11),wp_melee(100),knows_ironflesh_1|knows_weapon_master_2,nord_face_middle_1, nord_face_older_2],
  ["nord_archer", "Musketeer","Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_prosta_shpaga_b,itm_prosta_shpaga_c,itm_prosta_shpaga,itm_pehot_palash,itm_musket,itm_bolts,itm_evropa_musket_uniforma,itm_evropa_pehot_tufli,itm_evropa_musket_shlapa,
    itm_evropa_musket_shlapa_b],
   str_8|agi_8|level(7),wp_melee(60)|wp_crossbow(125),knows_athletics_2|knows_weapon_master_2,nord_face_middle_1, nord_face_old_2],
  ["nord_archer_levelup", "Musketeer (veteran)","Musketeers (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_prosta_shpaga_b,itm_prosta_shpaga_c,itm_prosta_shpaga,itm_pehot_palash,itm_good_musket,itm_bolts,itm_evropa_musket_uniforma,itm_evropa_pehot_tufli,itm_evropa_guard_shlapa,
    itm_evropa_musket_shlapa_b],
   str_9|agi_9|level(11),wp_melee(75)|wp_crossbow(140),knows_ironflesh_1|knows_athletics_2|knows_weapon_master_3|knows_power_strike_1,nord_face_middle_1, nord_face_older_2],

  ["sved_swordmaster", "Swordsman","Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_twohand_sword,itm_twohand_sword_b,itm_dospeh,itm_infantry_boots,itm_morion_good,itm_infantry_gloves],
   str_14|agi_6|level(15),wp_melee(135),knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_5,nord_face_middle_1, nord_face_old_2],
  ["sved_swordmaster_levelup", "Swordsman (veteran)","Swordsmen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_twohand_sword,itm_twohand_sword_b,itm_dospeh,itm_infantry_boots,itm_morion_good,itm_armor_gauntlets],
   str_14|agi_7|level(19),wp_melee(150),knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_6,nord_face_middle_1, nord_face_older_2],
  ["nord_veteran_archer","Swedish Reiters","Lifeguards",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_shpaga_d,itm_good_shpaga_b,itm_good_shpaga,itm_good_shpaga_c,itm_good_pehot_palash,itm_good_pehot_palash_b,itm_infantry_gloves,
    itm_mushket_udarniy,itm_steel_bolts,itm_bolts,itm_evropa_guard_shlapa,itm_evropa_gvardia_uniforma,itm_good_cavalry_botforts],
   str_10|agi_9|level(14),wp_melee(105)|wp_crossbow(135),knows_power_strike_2|knows_ironflesh_3|knows_athletics_2|knows_weapon_master_5,nord_face_middle_1, nord_face_old_2],
  ["nord_veteran_archer_levelup", "Lifeguard (veteran)","Lifeguards (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_shpaga_d,itm_good_shpaga_b,itm_good_shpaga,itm_good_shpaga_c,itm_good_pehot_palash,itm_good_pehot_palash_b,itm_leather_gloves,
    itm_mushket_udarniy_b,itm_steel_bolts,itm_bolts,itm_evropa_guard_shlapa,itm_evropa_gvardia_uniforma,itm_good_cavalry_botforts],
   str_11|agi_10|level(18),wp_melee(120)|wp_crossbow(150),knows_power_strike_3|knows_ironflesh_4|knows_athletics_2|knows_weapon_master_6,nord_face_middle_1, nord_face_older_2],

  ["nord_warrior", "Dragoon","Dragoons",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_prosta_shpaga,itm_prosta_shpaga_b,itm_prosta_shpaga_c,itm_karabin,itm_bolts,itm_evropa_dragoon_uniforma,
    itm_old_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,
    itm_saddle_horse,itm_saddle_horse_b,itm_infantry_gloves],
   str_8|agi_8|level(8),wp_melee(75)|wp_crossbow(130),knows_horse_archery_6|knows_riding_2|knows_weapon_master_3,nord_face_middle_1, nord_face_old_2],
  ["nord_warrior_levelup", "Dragoon (veteran)","Dragoons (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_prosta_shpaga,itm_prosta_shpaga_b,itm_prosta_shpaga_c,itm_karabin_good,itm_bolts,itm_evropa_dragoon_uniforma,
    itm_old_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,
    itm_saddle_horse_c,itm_saddle_horse_b,itm_leather_gloves],
   str_9|agi_9|level(11),wp_melee(90)|wp_crossbow(145),knows_ironflesh_1|knows_horse_archery_7|knows_riding_3|knows_weapon_master_4|knows_power_strike_1,nord_face_middle_1, nord_face_older_2],

  ["nord_champion", "Cuirassier","Cuirassiers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_palash,itm_pehot_palash,itm_old_pistol,itm_pistol,itm_pistol_b,itm_bolts,itm_kirasa_b,itm_kirasa_c,
    itm_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_saddle_horse,itm_saddle_horse_b,itm_infantry_gloves],
   str_9|agi_8|level(15),wp_melee(115)|wp_crossbow(130),knows_ironflesh_2|knows_horse_archery_6|knows_riding_3|knows_weapon_master_4,nord_face_middle_1, nord_face_old_2],
  ["nord_champion_levelup", "Cuirassier","Cuirassiers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_palash,itm_pehot_palash,itm_old_pistol,itm_pistol,itm_pistol_b,itm_bolts,itm_kirasa_b,itm_kirasa_c,
    itm_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_hunter,itm_leather_gloves],
   str_10|agi_9|level(20),wp_melee(130)|wp_crossbow(145),knows_ironflesh_3|knows_power_strike_1|knows_horse_archery_7|knows_riding_4|knows_weapon_master_5,nord_face_middle_1, nord_face_older_2],
 ["sved_lancers", "Cuirassier Spearman","Cuirassier Spearmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_kingdom_4,
   [itm_cavalry_pika_a,itm_kirasa_b,itm_kirasa_c,itm_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_saddle_horse,itm_saddle_horse_b,itm_infantry_gloves],
   str_9|agi_8|level(15),wp_melee(130),knows_common|knows_riding_3|knows_ironflesh_2|knows_weapon_master_4,nord_face_middle_1, nord_face_old_2],
 ["sved_lancers_levelup", "Cuirassier Spearman (veteran)","Cuirassier Spearmen (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_kingdom_4,
   [itm_cavalry_pika_b,itm_kirasa_b,itm_kirasa_c,itm_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_hunter,itm_leather_gloves],
   str_10|agi_9|level(20),wp_melee(145),knows_common|knows_riding_4|knows_ironflesh_3|knows_power_strike_1|knows_weapon_master_5,nord_face_middle_1, nord_face_older_2],

  ["nord_veteran", "Swedish Reiter","Reiters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_palash,itm_good_palash_b,itm_good_pistol,itm_good_pistol_c,itm_good_pistol_b,itm_bolts,itm_reytar_armor,itm_good_cavalry_botforts,itm_reytar_helmet,itm_hunter,itm_infantry_gloves],
   str_13|agi_7|level(21),wp_melee(160)|wp_crossbow(140),knows_ironflesh_6|knows_power_strike_3|knows_horse_archery_6|knows_riding_4|knows_weapon_master_6,nord_face_middle_1, nord_face_old_2],
  ["nord_veteran_levelup", "Swedish Reiter (veteran)","Swedish Reiters (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_palash,itm_good_palash_b,itm_good_pistol,itm_good_pistol_c,itm_good_pistol_b,itm_bolts,itm_reytar_armor,itm_good_cavalry_botforts,itm_armet,itm_reytar_helmet,itm_hunter,itm_reytar_gauntlets],
   str_14|agi_8|level(25),wp_melee(175)|wp_crossbow(160),knows_ironflesh_5|knows_power_strike_4|knows_horse_archery_7|knows_riding_4|knows_weapon_master_7,nord_face_middle_1, nord_face_older_2],

#  ["sved_v_pikiner","Pikeman veteran"," Veteran pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
#   [itm_good_pike,itm_evropa_pika_uniforma,itm_infantry_boots,itm_morion_good,itm_leather_gloves],
#   str_11|agi_8|level(17),wp_melee(140),knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_4,nord_face_old_1, nord_face_older_2],
  ["nord_messenger", "Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_saddle_horse,itm_infantry_gloves,itm_old_cavalry_botforts,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa,
    itm_prosta_shpaga_c,itm_pehot_palash],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_deserter", "Nord Deserter","Nord Deserters",tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_pehot_palash_old,itm_rusty_shpaga,itm_cartridges,itm_botinki,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_evropa_shlapa,itm_evropa_shlapa_b,itm_old_musket,itm_old_musket_b],
   def_attrib|str_10|level(10),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard", "Prison Guard","Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_evropa_pehot_tufli,itm_kirasa,itm_morion,itm_alebarda],
   def_attrib|level(20),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard", "Guard","Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_infantry_boots,itm_kirasa_rich,itm_morion_good,itm_alebarda],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],


#----------------------------------------------------------
########## UKR####################
#---------------------------------------------------------
  ["rhodok_tribesman", "Countryman","Countrymen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_kosa,itm_vily,itm_plotnik_toporik,itm_samopal,itm_samopal_b,itm_cartridges,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_ukraine_svitka_c,itm_selo_boots,itm_ukrine_prosta_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli],
   str_6|agi_6|level(3),wp_melee(35)|wp_crossbow(50)|wp_archery(10),knows_common,rhodok_face_younger_1, rhodok_face_young_2],

  ["rhodok_spearman", "Poor Cossack","Poor Cossacks", tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_plotnik_toporik,itm_sablya_pure_c,itm_sablya_turk_pure_a,itm_sablya_turk_pure_b,itm_ukraine_svitka_c,
    itm_sablya_turk_pure_c,itm_samopal_b,itm_samopal,itm_bolts,itm_cartridges,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_selo_boots,itm_ukrine_prosta_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli],
   str_7|agi_7|level(4),wp_melee(40)|wp_crossbow(65),knows_common|knows_ironflesh_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_young_2],
  ["rhodok_spearman_levelup", "Poor Cossack (veteran)","Poor Cossacks (veteran)", tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_plotnik_toporik,itm_sablya_pure_c,itm_sablya_turk_pure_a,itm_sablya_turk_pure_b,itm_ukraine_svitka_c,
    itm_sablya_turk_pure_c,itm_old_musket_b,itm_old_musket,itm_turk_musket_fitil_a,itm_bolts,
    itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_selo_boots,itm_ukrine_prosta_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli],
   str_8|agi_8|level(7),wp_melee(55)|wp_crossbow(80),knows_common|knows_ironflesh_3|knows_athletics_2,rhodok_face_young_1, rhodok_face_young_2],
  ["ukr_golota", "Poor Cossack Pikeman","Poor Cossack Pikemen", tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_ukraine_svitka_c,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_selo_boots,itm_ukrine_prosta_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli,itm_kosa,itm_vily,itm_plotnik_topor],
   str_7|agi_7|level(4),wp_melee(70),knows_common|knows_ironflesh_4|knows_athletics_2,rhodok_face_young_1, rhodok_face_young_2],
  ["ukr_golota_levelup", "Poor Cossack Pikeman (veteran)","Poor Cossack Pikemen (veteran)", tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_kopyo,itm_ukraine_svitka_c,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_selo_boots,itm_ukrine_prosta_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli],
   str_8|agi_8|level(7),wp_melee(85),knows_common|knows_ironflesh_5|knows_athletics_2,rhodok_face_young_1, rhodok_face_young_2],

  ["rhodok_sergeant", "Zaporozhian Infantryman","Zaporozhian Infantry",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_sablya_pure_d,itm_sablya_pure_c,itm_sablya_pure_b,itm_sablya_pure_a,itm_sablya_turk_pure_c,itm_sablya_turk_pure_b,itm_kozak_shablya,itm_kozak_jupan_c,
    itm_turk_musket_fitil_b,itm_turk_musket_koleso,itm_musket,itm_bolts,itm_steel_bolts,itm_kozak_jupan,
    itm_kozak_jupan_b,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b],
   str_9|agi_9|level(8),wp_melee(90)|wp_crossbow(130),knows_common|knows_ironflesh_4|knows_power_strike_1|knows_athletics_3|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_old_2],
  ["rhodok_sergeant_levelup", "Zaporozhian Infantryman (veteran)","Zaporozhian Infantry (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_sablya_d,itm_sablya_c,itm_sablya_b,itm_sablya_a,itm_sablya_turk_c,itm_sablya_turk_b,itm_kozak_good_shablya,itm_kozak_jupan_c,
    itm_turk_musket,itm_turk_musket_koleso,itm_good_musket,itm_bolts,itm_steel_bolts,itm_kozak_jupan,
    itm_kozak_jupan_b,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d],
   str_10|agi_10|level(12),wp_melee(105)|wp_crossbow(145),knows_common|knows_ironflesh_5|knows_power_strike_2|knows_athletics_3|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman", "Netyag","Netyagi",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_good_shablya,itm_sablya_a,itm_sablya_d,itm_sablya_b,itm_sablya_c,itm_sablya_turk_c,itm_sablya_turk_b,
    itm_pistol,itm_pistol_b,itm_old_pistol,itm_steel_bolts,itm_kozak_jupan_usileniy,itm_cavalry_koja_kurtka,itm_kozak_jupan_c,
    itm_kozak_jupan_b,itm_kozak_jupan,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozacka_shapka_s_misurkoy,
    itm_misurka_s_barmizoy_pure],
   str_10|agi_9|level(9),wp_melee(140)|wp_crossbow(125),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_athletics_4|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_old_2],
  ["rhodok_trained_crossbowman_levelup", "Netyag (veteran)","Netyagi (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_good_shablya,itm_sablya_a,itm_sablya_d,itm_sablya_b,itm_sablya_c,itm_sablya_turk_c,itm_sablya_turk_b,
    itm_good_pistol,itm_good_pistol_b,itm_good_pistol_c,itm_steel_bolts,itm_kozak_jupan_usileniy,itm_cavalry_koja_kurtka,itm_kozak_boots,itm_kozacka_shapka_s_misurkoy,itm_misurka_s_barmizoy_pure],
   str_11|agi_10|level(13),wp_melee(155)|wp_crossbow(140),knows_common|knows_ironflesh_6|knows_power_strike_5|knows_athletics_4|knows_weapon_master_5,rhodok_face_middle_1, rhodok_face_older_2],

  ["rhodok_veteran_spearman", "Serduk","Serduks",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_good_shablya,itm_sablya_a,itm_sablya_d,itm_sablya_turk_b,itm_sablya_turk_c,itm_turk_musket,itm_mushket_udarniy,itm_steel_bolts,itm_serduk_jupan,itm_kozak_boots,itm_serduk_shapka,itm_good_sapogi],
   str_10|agi_9|level(14),wp_melee(95)|wp_crossbow(150),knows_common|knows_ironflesh_5|knows_power_strike_2|knows_athletics_3|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_levelup", "Serduk (veteran)","Serduks (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_good_shablya,itm_sablya_a,itm_sablya_d,itm_sablya_turk_b,itm_sablya_turk_c,itm_turk_musket_b,itm_mushket_udarniy_b,itm_steel_bolts,itm_serduk_jupan,itm_kozak_boots,itm_serduk_shapka,itm_good_sapogi],
   str_11|agi_10|level(18),wp_melee(110)|wp_crossbow(165),knows_common|knows_ironflesh_6|knows_power_strike_3|knows_athletics_3|knows_weapon_master_5,rhodok_face_old_1, rhodok_face_older_2],

  ["rhodok_trained_spearman", "Djura","Djura",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_old_pistol,itm_pistol,itm_pistol_b,itm_karabin_old_b,itm_karabin_old_a,itm_cartridges,itm_saddle_horse,itm_saddle_horse_b,itm_selo_boots,itm_prostoy_jupan_c,itm_prostoy_jupan_b,itm_prostoy_jupan,
    itm_kozak_prosta_shapka,itm_kozak_shapka,itm_kozak_shapka_b,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_turk_pure_c,itm_kozak_shablya],
   str_8|agi_7|level(8),wp_melee(95)|wp_crossbow(85),knows_common|knows_riding_3|knows_ironflesh_2|knows_horse_archery_4,rhodok_face_younger_1, rhodok_face_young_2],
  ["rhodok_trained_spearman_levelup", "Djura (veteran)","Djura (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_old_pistol,itm_pistol,itm_pistol_b,itm_karabin_old_b,itm_karabin_old_a,itm_bolts,itm_saddle_horse_b,itm_saddle_horse_c,itm_sapogi,itm_prostoy_jupan_c,itm_prostoy_jupan_b,itm_prostoy_jupan,
    itm_kozak_prosta_shapka,itm_kozak_shapka,itm_kozak_shapka_b,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_turk_pure_c,itm_kozak_shablya],
   str_9|agi_8|level(11),wp_melee(110)|wp_crossbow(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_horse_archery_5|knows_power_strike_1,rhodok_face_younger_1, rhodok_face_young_2],

  ["rhodok_crossbowman", "Watchman","Watchmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_kozak_shablya,itm_sablya_turk_c,itm_sablya_turk_b,itm_sablya_b,itm_sablya_c,itm_karabin,itm_bolts,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_jupan_c,
    itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka,itm_saddle_horse_c,itm_saddle_horse_b],
   str_9|agi_9|level(12),wp_melee(105)|wp_crossbow(140),knows_common|knows_ironflesh_3|knows_power_strike_1|knows_riding_4|knows_horse_archery_7|knows_weapon_master_2,rhodok_face_middle_1, rhodok_face_old_2],
  ["rhodok_crossbowman_levelup", "Watchman (veteran)","Watchmen (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_shablya,itm_sablya_turk_c,itm_sablya_turk_b,itm_sablya_b,itm_sablya_c,itm_karabin_good,itm_bolts,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_jupan_c,
    itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_saddle_horse_c,itm_saddle_horse_b],
   str_10|agi_10|level(17),wp_melee(120)|wp_crossbow(155),knows_common|knows_ironflesh_4|knows_power_strike_2|knows_riding_5|knows_horse_archery_8|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["ukr_storoja", "Pike Watchman","Pike Watchmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_cavalry_pika_a,itm_cavalry_pika_b,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_jupan_c,
    itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka,itm_saddle_horse_c,itm_saddle_horse_b],
   str_9|agi_9|level(12),wp_melee(130),knows_common|knows_ironflesh_4|knows_power_strike_2|knows_riding_5|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_old_2],
  ["ukr_storoja_levelup", "Pike Watchman (veteran)","Pike Watchmen (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozacka_pika,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_jupan_c,
    itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_saddle_horse_c,itm_saddle_horse_b],
   str_10|agi_10|level(17),wp_melee(145),knows_common|knows_ironflesh_5|knows_power_strike_3|knows_riding_6|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],

  ["rhodok_veteran_crossbowman", "Zaporozhian Cavalryman","Zaporozhian Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_courser,itm_steel_bolts,itm_bolts,itm_good_cavalry_boots,itm_cavalry_boots,itm_good_sapogi,itm_kozak_boots,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_jupan_c,itm_cavalry_koja_kurtka,
    itm_kozak_jupan_usileniy,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_sablya_a,itm_sablya_b,itm_sablya_c,itm_sablya_d,itm_sablya_turk_b,itm_sablya_turk_c,
    itm_kozak_good_shablya,itm_kozacka_pika,itm_klevetz,itm_chekan,itm_karabin_batarey,itm_good_pistol_c,itm_good_pistol_b,itm_good_pistol],
   str_11|agi_10|level(18),wp_melee(145)|wp_crossbow(155),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_riding_5|knows_horse_archery_7|knows_weapon_master_5,rhodok_face_middle_1, rhodok_face_old_2],
  ["rhodok_veteran_crossbowman_levelup", "Zaporozhian Cavalryman (veteran)","Zaporozhian Cavalry (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_courser,itm_steel_bolts,itm_bolts,itm_good_cavalry_boots,itm_cavalry_boots,itm_good_sapogi,itm_kozak_boots,itm_kozak_jupan_na_kolchuge,itm_kolchuga,itm_cavalry_koja_kurtka,
    itm_kozak_jupan_usileniy,itm_misurka_s_barmizoy_rich,itm_tatar_misurka,itm_kozacka_shapka_s_misurkoy,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_sablya_a,itm_sablya_b,itm_sablya_c,itm_sablya_d,itm_sablya_turk_b,itm_sablya_turk_c,
    itm_kozak_good_shablya,itm_pernach,itm_shestoper,itm_kozacka_pika,itm_klevetz_good,itm_chekan_good,itm_karabin_batarey_good,itm_good_pistol_c,itm_good_pistol_b,itm_good_pistol],
   str_12|agi_11|level(22),wp_melee(160)|wp_crossbow(170),knows_common|knows_ironflesh_5|knows_power_strike_4|knows_riding_6|knows_horse_archery_8|knows_weapon_master_6,rhodok_face_middle_1, rhodok_face_older_2],

#  ["rhodok_sharpshooter","Starshina","Starshina",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
#   [itm_kozak_good_shablya,itm_sablya_a,itm_sablya_d,itm_sablya_b,itm_sablya_c,itm_sablya_turk_c,itm_sablya_turk_b,
#    itm_pernach,itm_shestoper,itm_klevetz_good,itm_kozacka_pika,itm_kozak_jupan_na_kolchuge,itm_kolchuga,itm_cavalry_koja_kurtka,
#    itm_cavalry_boots,itm_good_cavalry_boots,itm_kozacka_shapka_s_misurkoy,itm_misurka_s_barmizoy_rich,
#    itm_tatar_misurka_rich,itm_courser,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_good_pistol,itm_good_pistol_b,
#    itm_good_pistol_c,itm_steel_bolts,itm_rich_horse,itm_rich_horse_b],
#   str_12|agi_10|level(22),wp_melee(180)|wp_crossbow(160),knows_common|knows_ironflesh_6|knows_power_strike_5|knows_riding_6|knows_horse_archery_8|knows_weapon_master_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_messenger", "Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_saddle_horse_c,itm_kozak_boots,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shablya,],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_deserter", "Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_cartridges,itm_selo_boots,itm_prostoy_jupan,itm_prostoy_jupan_b,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_kozak_prosta_shapka,itm_kozak_shapka,
    itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shablya,itm_sablya_pure_d,itm_old_musket,itm_old_musket_b],
   def_attrib|str_10|level(10),wp(80),knows_ironflesh_2|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard", "Prison Guard","Prison Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_boots,itm_prostoy_jupan,itm_prostoy_jupan_b,itm_kozak_shablya],
   def_attrib|level(20),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard", "Guard","Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_boots,itm_kozak_jupan_na_kolchuge,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_kozak_good_shablya],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],

# Ryan BEGIN  
  ["looter", "Looter","Looters",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_dubinka,itm_vily,itm_kosa,itm_plotnik_toporik,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_ukraine_svitka_c,itm_mosk_armyak,itm_selo_boots],
   def_attrib|level(1),wp(40),knows_common,bandit_face1, bandit_face2],
# Ryan END
  ["bandit", "Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_samopal,itm_samopal_b,itm_cartridges,itm_kopyo,itm_plotnik_toporik,itm_plotnik_topor,itm_poland_shapka,
    itm_ukrine_prosta_shapka,itm_moskowit_shapka,itm_evropa_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_ukraine_svitka_c,
    itm_mosk_armyak,itm_selo_boots],
   def_attrib|level(4),wp(70),knows_common,bandit_face1, bandit_face2],
  ["brigand", "Brigand","Brigands",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_samopal,itm_samopal_b,itm_cartridges,itm_plotnik_topor,itm_kopyo,itm_poland_shapka,
    itm_ukrine_prosta_shapka,itm_moskowit_shapka,itm_evropa_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_ukraine_svitka_c,
    itm_mosk_armyak,itm_selo_boots,itm_plotnik_toporik],
   def_attrib|level(7),wp(90),knows_common,bandit_face1, bandit_face2],
  ["mountain_bandit", "Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_dubinka,itm_kopyo,itm_plotnik_toporik,itm_samopal,itm_samopal_b,itm_cartridges,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka,
    itm_mosk_armyak,itm_mosk_sermyaga],
   def_attrib|level(6),wp(100),knows_common,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit", "Rebel","Rebels",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_dubinka,itm_plotnik_toporik,itm_samopal,itm_samopal_b,itm_cartridges,itm_poland_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,
    itm_selo_boots],
   def_attrib|level(6),wp(100),knows_common|knows_power_draw_2,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider", "Brigand","Brigands",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,
   [itm_pehot_palash_old,itm_rusty_shpaga,itm_plotnik_toporik,itm_samopal,itm_samopal_b,itm_cartridges,itm_selo_boots,itm_botinki,
    itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_evropa_shapka],
   def_attrib|level(6),wp(100),knows_common,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit", "Tatar Raider","Tatar Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_cavalry_pika_a,itm_luk,itm_arrows,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,itm_selo_boots,itm_saddle_horse,itm_sablya_tatar_pure_a],
   def_attrib|level(6),wp(70),knows_riding_4|knows_horse_archery_2|knows_power_draw_1,khergit_face_middle_1, khergit_face_older_2],
  ["black_khergit_horseman", "Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_cavalry_pika_a,itm_luk,itm_arrows,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,itm_selo_boots,itm_saddle_horse,itm_sablya_tatar_pure_a],
   def_attrib|level(8),wp(100),knows_riding_3|knows_ironflesh_2|knows_horse_archery_3|knows_power_draw_2,khergit_face_young_1, khergit_face_old_2],

  ["manhunter", "Marksman of the Secret Department","Marksmen of the Secret Department",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_sumpter_horse,itm_dubinka,itm_plotnik_toporik,itm_plotnik_toporik,itm_old_musket,itm_karabin,itm_bolts,itm_poland_mehova_shapka,
    itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_dobrotna_svitka_d,itm_dobrotna_svitka_e,itm_selo_boots],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_sword,itm_round_shield,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor,0,0,fac_slavers,
##   [itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver", "Slave Driver","Slave Drivers",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_sumpter_horse,itm_dubinka,itm_plotnik_toporik,itm_plotnik_toporik,itm_old_musket,itm_karabin,itm_bolts,itm_poland_mehova_shapka,
    itm_dobrotna_svitka_a,itm_selo_boots],
   def_attrib|level(10),wp(70),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter", "Slave Hunter","Slave Hunters",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_sumpter_horse,itm_dubinka,itm_plotnik_toporik,itm_plotnik_toporik,itm_old_musket,itm_karabin,itm_bolts,itm_poland_mehova_shapka,
    itm_dobrotna_svitka_a,itm_selo_boots],
   def_attrib|level(10),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher", "Slave Crusher","Slave Crushers",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_sumpter_horse,itm_dubinka,itm_plotnik_toporik,itm_plotnik_toporik,itm_old_musket,itm_karabin,itm_bolts,itm_poland_mehova_shapka,
    itm_dobrotna_svitka_a,itm_selo_boots],
   def_attrib|level(15),wp(100),knows_common,bandit_face1, bandit_face2],
  ["slaver_chief", "Slaver Chief","Slaver Chiefs",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_manhunters,
   [itm_sumpter_horse,itm_dubinka,itm_plotnik_toporik,itm_plotnik_toporik,itm_old_musket,itm_karabin,itm_bolts,itm_poland_mehova_shapka,
    itm_dobrotna_svitka_a,itm_selo_boots],
   def_attrib|level(20),wp(150),knows_common,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief






#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  ["follower_woman", "Camp Follower","Camp Follower",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_bolts,itm_old_pistol,itm_pure_baba_swd_1,itm_pure_baba_swd_2],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Commoner","Huntresses",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_bolts,itm_old_pistol,itm_pure_baba_swd_1,itm_pure_baba_swd_2],
   def_attrib|level(10),wp(85),knows_common,refugee_face1,refugee_face2],
  ["fighter_woman", "Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_old_pistol,itm_pure_baba_swd_1,itm_pure_baba_swd_2],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister", "Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_bolts,itm_old_pistol,itm_pure_baba_swd_1,itm_pure_baba_swd_2],
   def_attrib|level(22),wp(140),knows_common|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],

##=========================================================================================================================
  ["basurman_azap", "Azap","Azaps",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_kingdom_3,
   [itm_janissary_tapki,itm_azap_forma,itm_turban,itm_sablya_turk_pure_a,itm_yatagan_a,itm_tarch_a,itm_tarch_b],
   str_8|agi_7|level(6),wp_melee(85),knows_common|knows_ironflesh_1|knows_weapon_master_2|knows_power_strike_1|knows_shield_3,khergit_face_middle_1, khergit_face_old_2],
  ["basurman_azap_levelup","Janissaries","Azaps (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_kingdom_3,
   [itm_janissary_tapki,itm_azap_forma,itm_turban,itm_sablya_turk_a,itm_yatagan_good,itm_tarch_a,itm_tarch_b],
   str_9|agi_8|level(10),wp_melee(100),knows_common|knows_ironflesh_2|knows_weapon_master_3|knows_power_strike_2|knows_shield_4,khergit_face_middle_1, khergit_face_older_2],
  ["basurman_jebelu", "Cebelu","Cebelu",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,no_scene,reserved,fac_kingdom_3,
   [itm_janissary_tapki,itm_azap_forma,itm_turban,itm_cavalry_pika_a,itm_shield,itm_luk_b,itm_khergit_arrows,itm_courser,],
   str_8|agi_8|level(10),wp_melee(95)|wp_archery(95),knows_common|knows_weapon_master_2|knows_shield_3|knows_riding_4|knows_power_draw_2|knows_horse_archery_4,khergit_face_middle_1, khergit_face_old_2],
  ["basurman_jebelu_levelup", "Cebelu (veteran)","Cebelu (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,no_scene,reserved,fac_kingdom_3,
   [itm_janissary_tapki,itm_azap_forma,itm_turban,itm_cavalry_pika_b,itm_shield,itm_luk_c,itm_east_arrows,itm_courser,],
   str_9|agi_9|level(13),wp_melee(110)|wp_archery(110),knows_common|knows_ironflesh_1|knows_weapon_master_3|knows_power_strike_1|knows_shield_4|knows_riding_5|knows_power_draw_3|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["janissar", "Janissary","Yanichary",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_turk_musket,itm_yatagan_good,itm_sablya_turk_a,itm_steel_bolts,itm_janissary_tapki,itm_yanichar_forma_a,itm_yanichar_forma_b,itm_janissar_hat_a,itm_janissar_hat_b],
   str_10|agi_8|level(13),wp_melee(100)|wp_crossbow(120),knows_power_strike_3|knows_ironflesh_4|knows_athletics_3|knows_weapon_master_4,man_face_young_1, man_face_old_2],
  ["janissar_levelup", "Janissary (veteran)","Janissaries (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_turk_musket_b,itm_yatagan_rich,itm_sablya_turk_a,itm_steel_bolts,itm_janissary_tapki,itm_yanichar_forma_a,itm_yanichar_forma_b,itm_janissar_hat_a,itm_janissar_hat_b],
   str_11|agi_9|level(17),wp_melee(115)|wp_crossbow(135),knows_power_strike_4|knows_ironflesh_5|knows_athletics_3|knows_weapon_master_5,man_face_middle_1, man_face_older_2],

  ["scott_pika", "Scottish Pikeman","Scottish Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_kingdom_4,
   [itm_infantry_boots,itm_scott_uniforma,itm_kabasset,itm_morion_good,itm_prosta_pike,itm_pika],
   str_10|agi_6|level(7),wp_melee(100),knows_common|knows_ironflesh_1|knows_weapon_master_1|knows_power_strike_1,mercenary_face_1, mercenary_face_2],
  ["scott_pika_levelup", "Scottish Pikeman (veteran)","Scottish Pikemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_kingdom_4,
   [itm_infantry_boots,itm_scott_uniforma,itm_kabasset,itm_morion_good,itm_pika,itm_good_pike],
   str_11|agi_7|level(11),wp_melee(115),knows_common|knows_ironflesh_2|knows_weapon_master_2|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["scott_musket", "Scottish Musketeer","Scottish Musketeers",tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_kingdom_4,
   [itm_bolts,itm_infantry_boots,itm_scott_uniforma_musketeer,itm_beret_a,itm_beret_b,itm_beret_c,itm_scott_palash,itm_musket],
   str_10|agi_8|level(7),wp_melee(70)|wp_crossbow(95),knows_common|knows_athletics_3|knows_ironflesh_2|knows_weapon_master_3|knows_power_strike_2,mercenary_face_1, mercenary_face_2],
  ["scott_musket_levelup", "Scottish Musketeer (veteran)","Scottish Musketeers (veteran)",tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_kingdom_4,
   [itm_bolts,itm_infantry_boots,itm_scott_uniforma_musketeer,itm_beret_a,itm_beret_b,itm_beret_c,itm_scott_palash,itm_good_musket],
   str_11|agi_9|level(11),wp_melee(85)|wp_crossbow(110),knows_common|knows_athletics_3|knows_ironflesh_3|knows_weapon_master_4|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["scott_sword", "Scottish Swordsman","Scottish Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_kingdom_4,
   [itm_infantry_boots,itm_scott_uniforma,itm_beret_a,itm_beret_b,itm_beret_c,itm_scott_kleymor_a],
   str_13|agi_7|level(13),wp_melee(130),knows_common|knows_ironflesh_3|knows_weapon_master_5|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["scott_sword_levelup", "Scottish Swordsman (veteran)","Scottish Swordsmen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_kingdom_4,
   [itm_infantry_boots,itm_scott_uniforma,itm_beret_a,itm_beret_b,itm_beret_c,itm_scott_kleymor_b],
   str_14|agi_8|level(17),wp_melee(145),knows_common|knows_ironflesh_4|knows_weapon_master_6|knows_power_strike_4,mercenary_face_1, mercenary_face_2],

  ["pruss_pike", "German Pikeman","German Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_pika,itm_simple_reytar_armor,itm_morion,itm_infantry_boots,itm_infantry_gloves],
   str_8|agi_6|level(7),wp_melee(105),knows_power_strike_1|knows_weapon_master_2,nord_face_middle_1, nord_face_old_2],
  ["pruss_pike_levelup", "German Pikeman (veteran)","German Pikemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_pike,itm_simple_reytar_armor,itm_morion,itm_infantry_boots,itm_infantry_gloves],
   str_9|agi_7|level(11),wp_melee(120),knows_ironflesh_1|knows_power_strike_1|knows_weapon_master_3,nord_face_middle_1, nord_face_older_2],
  ["rundashir", "Rondartschier","Rondartschiere",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_infantry_boots,itm_poland_uniforma_german_line,itm_merc_pika_uniforma_a,itm_merc_pika_uniforma_b,itm_kabasset,itm_pehot_palash,itm_rundash],
   str_9|agi_6|level(7),wp_melee(120),knows_power_strike_1|knows_weapon_master_4|knows_shield_5,nord_face_middle_1, nord_face_old_2],
  ["rundashir_levelup", "Rondartschier (veteran)","Rondartschiere (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_infantry_boots,itm_poland_uniforma_german_line,itm_merc_pika_uniforma_a,itm_merc_pika_uniforma_b,itm_kabasset,itm_pehot_palash,itm_rundash,itm_infantry_gloves],
   str_10|agi_7|level(11),wp_melee(135),knows_ironflesh_1|knows_power_strike_2|knows_weapon_master_5|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  ["tatar_merc_peh", "Tatar Infantryman","Tatar Infantrymen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_arrows,itm_khergit_arrows,itm_luk_b,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_a,itm_sablya_turk_pure_b,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,itm_shield,
    itm_selo_boots,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b],
   str_6|agi_8|level(6),wp_melee(60)|wp_archery(60),knows_common|knows_shield_3|knows_athletics_3|knows_power_draw_1,khergit_face_middle_1, khergit_face_old_2],
  ["tatar_merc_peh_levelup", "Tatar Infantryman (veteran)","Tatar Infantrymen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_luk_c,itm_sablya_tatar_pure_a,itm_sablya_turk_pure_a,itm_sablya_turk_pure_b,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,itm_shield,
    itm_selo_boots,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b],
   str_7|agi_9|level(10),wp_melee(75)|wp_archery(75),knows_common|knows_shield_4|knows_athletics_3|knows_power_draw_2,khergit_face_middle_1, khergit_face_older_2],

  ["litva_musket", "Lithuanian Musketeer","Lithuanian Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_musket,itm_bolts,
    itm_moskow_tulup_a,itm_moskow_tulup_b,itm_moskow_tulup_c,itm_sapogi,itm_poland_army_hat_simple],
   str_7|agi_6|level(6),wp_melee(60)|wp_crossbow(85),knows_common|knows_ironflesh_1|knows_athletics_1|knows_weapon_master_1,swadian_face_middle_1, swadian_face_old_2],
  ["litva_musket_levelup", "Lithuanian Musketeer (veteran)","Lithuanian Musketeers (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_musket,itm_bolts,
    itm_moskow_tulup_a,itm_moskow_tulup_b,itm_moskow_tulup_c,itm_sapogi,itm_poland_army_hat_simple],
   str_8|agi_7|level(10),wp_melee(75)|wp_crossbow(100),knows_common|knows_ironflesh_2|knows_athletics_1|knows_weapon_master_2,swadian_face_middle_1, swadian_face_older_2],
  ["gorod_kozak", "Town Cossack","Town Cossacks",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_musket,itm_bolts,
    itm_reestr_kozak_uniform,itm_sapogi,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka],
   str_9|agi_8|level(6),wp_melee(65)|wp_crossbow(125),knows_common|knows_ironflesh_3|knows_athletics_3|knows_weapon_master_2,rhodok_face_middle_1, rhodok_face_old_2],
  ["gorod_kozak_levelup", "Town Cossack (veteran)","Town Cossacks (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_sablya_pure_a,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_d,itm_good_musket,itm_bolts,
    itm_reestr_kozak_uniform,itm_sapogi,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka],
   str_9|agi_9|level(10),wp_melee(80)|wp_crossbow(140),knows_common|knows_ironflesh_4|knows_athletics_2|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["finn_arcebuz", "Finnish Harquebusier","Finnish Harquebusiers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_prosta_shpaga_b,itm_prosta_shpaga_c,itm_prosta_shpaga,itm_steel_bolts,itm_old_musket,itm_old_musket_b,itm_kirasa_b,itm_kirasa_c,itm_evropa_pehot_tufli,itm_kabasset],
   str_7|agi_6|level(6),wp_melee(55)|wp_crossbow(85),knows_ironflesh_2|knows_weapon_master_1,nord_face_middle_1, nord_face_old_2],
  ["finn_arcebuz_levelup", "Finnish Harquebusier (veteran)","Finnish Harquebusiers (veteran)",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_prosta_shpaga_b,itm_prosta_shpaga_c,itm_prosta_shpaga,itm_steel_bolts,itm_old_musket,itm_old_musket_b,itm_kirasa_b,itm_kirasa_c,itm_evropa_pehot_tufli,itm_kabasset],
   str_8|agi_7|level(10),wp_melee(70)|wp_crossbow(100),knows_ironflesh_3|knows_weapon_master_2|knows_power_strike_1,nord_face_middle_1, nord_face_older_2],

  ["don_cossack", "Village Cossack","Village Cossacks",tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_bolts,itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c,itm_old_cavalry_boots,itm_sapogi,itm_prostoy_jupan_c,itm_prostoy_jupan_b,itm_prostoy_jupan,
    itm_ukrine_prosta_shapka,itm_sablya_pure_b,itm_sablya_pure_c,itm_sablya_pure_a,itm_sablya_turk_pure_b,itm_sablya_turk_pure_c,itm_cavalry_pika_a,itm_karabin,
    itm_karabin_old_b,itm_karabin_old_a],
   str_9|agi_9|level(12),wp_melee(125)|wp_crossbow(130),knows_riding_5|knows_horse_archery_4|knows_ironflesh_2,vaegir_face_middle_1, vaegir_face_old_2],
  ["don_cossack_levelup", "Don Cossack (veteran)","Don Cossacks (veteran)",tf_mounted|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_bolts,itm_saddle_horse,itm_saddle_horse_b,itm_saddle_horse_c,itm_old_cavalry_boots,itm_sapogi,itm_prostoy_jupan_c,itm_prostoy_jupan_b,itm_prostoy_jupan,
    itm_ukrine_prosta_shapka,itm_sablya_b,itm_sablya_c,itm_sablya_a,itm_sablya_turk_b,itm_sablya_turk_c,itm_cavalry_pika_b,itm_karabin,itm_karabin_good],
   str_10|agi_10|level(17),wp_melee(140)|wp_crossbow(140),knows_riding_6|knows_horse_archery_5|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["reestrovuy_kozak", "Rank Cossack","Rank Cossacks",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_kozak_shablya,itm_sablya_d,itm_sablya_b,itm_sablya_c,itm_sablya_a,itm_sablya_turk_c,itm_sablya_turk_a,itm_pistol,itm_sablya_turk_pure_b,itm_cavalry_pika_a,itm_karabin,itm_pistol_b,itm_pistol,
    itm_old_pistol,itm_steel_bolts,itm_reestr_kozak_uniform,itm_cavalry_boots,itm_reestr_shapka,itm_steppe_horse,itm_steppe_horse_b],
   str_9|agi_9|level(12),wp_melee(115)|wp_crossbow(145),knows_common|knows_riding_4|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_3|knows_horse_archery_5,rhodok_face_middle_1, rhodok_face_old_2],
  ["reestrovuy_kozak_levelup", "Rank Cossack (veteran)","Rank Cossacks (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_kozak_shablya,itm_sablya_d,itm_sablya_b,itm_sablya_c,itm_sablya_a,itm_sablya_turk_c,itm_sablya_turk_a,itm_pistol,itm_sablya_turk_pure_b,itm_cavalry_pika_b,itm_karabin_good,itm_pistol_b,itm_pistol,
    itm_old_pistol,itm_steel_bolts,itm_reestr_kozak_uniform,itm_cavalry_boots,itm_reestr_shapka,itm_steppe_horse,itm_steppe_horse_b],
   str_10|agi_10|level(17),wp_melee(130)|wp_crossbow(160),knows_common|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_4|knows_horse_archery_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["lisovchiki", "Lisowczyk","Lisowczycy",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,no_scene,0,fac_kingdom_1,
   [itm_saddle_horse,itm_saddle_horse_b,itm_east_arrows,itm_bolts,itm_steel_bolts,itm_cavalry_boots,itm_old_cavalry_boots,itm_poland_svitka_a,itm_poland_svitka_c,itm_poland_svitka_d,
    itm_poland_svitka_b,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_sablya_turk_b,itm_sablya_turk_c,itm_sablya_d,itm_sablya_a,
    itm_pehot_palash,itm_konchar,itm_kozacka_pika,itm_karabin,itm_pistol_b,itm_luk_c],
   str_9|agi_10|level(12),wp_melee(120)|wp_crossbow(120)|wp_archery(85),knows_common|knows_riding_4|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_3|knows_horse_archery_5|knows_power_draw_3,swadian_face_middle_1, swadian_face_old_1],
  ["lisovchiki_levelup", "Lisowczyk (veteran)","Lisowczycy (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,no_scene,0,fac_kingdom_1,
   [itm_saddle_horse_c,itm_saddle_horse_b,itm_barbed_arrows,itm_bolts,itm_steel_bolts,itm_cavalry_boots,itm_old_cavalry_boots,itm_poland_svitka_a,itm_poland_svitka_c,itm_poland_svitka_d,
    itm_poland_svitka_b,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_sablya_turk_b,itm_sablya_turk_c,itm_sablya_d,itm_sablya_a,
    itm_good_pehot_palash,itm_good_pehot_palash_b,itm_konchar,itm_kozacka_pika,itm_karabin,itm_pistol_b,itm_kompozit_bow_b],
   str_10|agi_11|level(17),wp_melee(135)|wp_crossbow(135)|wp_archery(100),knows_common|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_weapon_master_4|knows_horse_archery_6|knows_power_draw_4,swadian_face_middle_1, swadian_face_older_1],
  ["litva_lipki", "Lithuanian Tatar","Lithuanian Tatars",tf_mounted|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_sablya_tatar_a,itm_luk_b,itm_khergit_arrows,itm_mosk_bahter_b,itm_kalmyk_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_tatar_misurka,
    itm_steppe_horse,itm_steppe_horse_b],
   str_8|agi_9|level(11),wp_melee(100)|wp_archery(90),knows_common|knows_riding_3|knows_horse_archery_4|knows_ironflesh_1|knows_weapon_master_3|knows_power_draw_2,khergit_face_middle_1, khergit_face_old_2],
  ["litva_lipki_levelup", "Lithuanian Tatar (veteran)","Lithuanian Tatars (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_sablya_tatar_a,itm_kompozit_bow_b,itm_khergit_arrows,itm_mosk_bahter_b,itm_kalmyk_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_tatar_misurka,
    itm_steppe_horse,itm_steppe_horse_b],
   str_9|agi_10|level(16),wp_melee(115)|wp_archery(105),knows_common|knows_riding_4|knows_horse_archery_5|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_4|knows_power_draw_3,khergit_face_middle_1, khergit_face_older_2],
  ["ttr_nogay", "Nogai","Nogai",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sablya_tatar_pure_a,itm_steppe_horse,itm_steppe_horse_b,itm_tatar_halat_a,itm_tatar_halat_b,itm_kalmyk_boots,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_shield],
   str_7|agi_8|level(8),wp_melee(115),knows_riding_5|knows_ironflesh_1,khergit_face_middle_1, khergit_face_old_2],
  ["ttr_nogay_levelup", "Nogai (veteran)","Nogai (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sablya_tatar_a,itm_steppe_horse,itm_steppe_horse_b,itm_tatar_halat_a,itm_tatar_halat_b,itm_kalmyk_boots,itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_shield],
   str_8|agi_9|level(11),wp_melee(130),knows_riding_6|knows_ironflesh_2,khergit_face_middle_1, khergit_face_older_2],
  ["ttr_cherkes", "Circassian","Circassians",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_east_arrows,itm_sablya_turk_pure_a,itm_luk_c,itm_saddle_horse,itm_saddle_horse_b,itm_kolchuga,itm_kalmyk_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_tatar_misurka],
   str_8|agi_8|level(12),wp_melee(100)|wp_archery(90),knows_riding_2|knows_power_draw_3|knows_horse_archery_4,khergit_face_middle_1, khergit_face_old_2],
  ["ttr_cherkes_levelup", "Circassian (veteran)","Circassians (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_east_arrows,itm_sablya_turk_a,itm_luk_c,itm_saddle_horse,itm_saddle_horse_b,itm_kolchuga,itm_kalmyk_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_tatar_misurka],
   str_9|agi_9|level(17),wp_melee(115)|wp_archery(105),knows_riding_3|knows_power_draw_4|knows_horse_archery_5|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],
  ["mosk_kalmyk", "Kalmyk","Kalmyks",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_east_arrows,itm_luk_c,itm_kalmyk_helmet,itm_kalmyk_puzo,itm_kalmyk_boots,itm_saddle_horse_b,itm_saddle_horse,itm_kalmyk_palash],
   str_9|agi_8|level(13),wp_melee(105)|wp_archery(95),knows_riding_3|knows_power_draw_2|knows_horse_archery_4,khergit_face_middle_1, khergit_face_old_2],
  ["mosk_kalmyk_levelup", "Kalmyk (veteran)","Kalmyks (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_east_arrows,itm_luk_c,itm_kalmyk_helmet,itm_kalmyk_puzo,itm_kalmyk_boots,itm_saddle_horse_b,itm_saddle_horse_c,itm_kalmyk_palash],
   str_10|agi_9|level(18),wp_melee(120)|wp_archery(110),knows_riding_3|knows_power_draw_3|knows_horse_archery_5|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],
  ["tatar_merc_cav", "Tatar Cavalryman","Tatar Cavalrymen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_sablya_tatar_pure_a,itm_luk_b,itm_steppe_horse,itm_steppe_horse_b,itm_tatar_halat_a,itm_tatar_halat_b,itm_sapogi,
    itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b],
   str_7|agi_9|level(8),wp_melee(75)|wp_archery(85),knows_riding_4|knows_power_draw_1|knows_horse_archery_5,khergit_face_middle_1, khergit_face_old_2],
  ["tatar_merc_cav_levelup", "Tatar Cavalryman (veteran)","Tatar Cavalrymen (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_sablya_tatar_a,itm_luk_c,itm_steppe_horse,itm_steppe_horse_b,itm_tatar_halat_a,itm_tatar_halat_b,itm_sapogi,
    itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b],
   str_8|agi_10|level(11),wp_melee(90)|wp_archery(100),knows_riding_5|knows_power_draw_2|knows_horse_archery_6|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],

  ["merc_reytar", "Reiter","Reiters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_palash,itm_good_pistol,itm_good_pistol_c,itm_good_pistol_b,itm_bolts,itm_simple_reytar_armor,
    itm_old_cavalry_botforts,itm_black_reytar_helmet,itm_hunter,itm_infantry_gloves],
   str_12|agi_7|level(19),wp_melee(145)|wp_crossbow(140),knows_ironflesh_4|knows_power_strike_3|knows_horse_archery_6|knows_riding_5|knows_weapon_master_5,nord_face_middle_1, nord_face_old_2],
  ["merc_reytar_levelup", "Black Reiter (veteran)","Black Reiters (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_palash,itm_good_palash_b,itm_good_pistol,itm_good_pistol_c,itm_good_pistol_b,itm_bolts,itm_simple_reytar_armor,
    itm_old_cavalry_botforts,itm_black_reytar_helmet,itm_hunter,itm_black_reytar_gauntlets],
   str_13|agi_8|level(23),wp_melee(160)|wp_crossbow(155),knows_ironflesh_5|knows_power_strike_4|knows_horse_archery_7|knows_riding_5|knows_weapon_master_6,nord_face_middle_1, nord_face_older_2],

##=========================================================================================================

  ["refugee", "Refugee","Refugees",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_pure_baba_pol_1,itm_pure_baba_pol_2,itm_pure_baba_swd_1,itm_pure_baba_swd_2,itm_pure_baba_mosk_1,itm_pure_baba_mosk_2,itm_dubinka, itm_kosa, itm_vily,itm_moskowit_postoli,itm_moskowit_postoli_b],
   def_attrib|level(1),wp(30),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Commoner","Peasant Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,
   [itm_pure_baba_pol_1,itm_pure_baba_pol_2,itm_pure_baba_swd_1,itm_pure_baba_swd_2,itm_pure_baba_mosk_1,itm_pure_baba_mosk_2,itm_dubinka, itm_kosa, itm_vily,itm_moskowit_postoli,itm_moskowit_postoli_b],
   def_attrib|level(1),wp(30),knows_common,refugee_face1,refugee_face2],

 
  ["caravan_master", "Caravan Master","Caravan Master",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_is_merchant,0,0,fac_commoners,
   [itm_saddle_horse_b,itm_saddle_horse,itm_saddle_horse_c,itm_cavalry_boots,itm_kozak_boots,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,
    itm_kozak_civil_jupan_a,itm_kozak_civil_jupan_b,itm_mosk_civil_a,itm_mosk_civil_b,itm_sablya_b,itm_sablya_c,itm_sablya_turk_b],
   def_attrib|level(5),wp(100),knows_common|knows_riding_4|knows_ironflesh_4,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl", "Kidnapped Girl","Kidnapped Girls",tf_hero|tf_female|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_pure_baba_swd_1,itm_pure_baba_swd_2],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1", "Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2", "Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["village_walker_1", "Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2", "Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

   ["rich_baba_pol", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_hose,itm_pol_bab_hat_1,itm_pol_bab_hat_2,itm_rich_baba_pol_4,itm_rich_baba_pol_2,itm_rich_baba_pol_3],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["pure_baba_pol", "Commoner","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_pure_baba_pol_1,itm_pure_baba_pol_2],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["rich_mujik_pol", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sapogi,itm_kozak_boots,itm_good_sapogi,itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_dobrotna_svitka_d,itm_dobrotna_svitka_e,itm_poland_mehova_shapka,itm_poland_mehova_shapka_s_perom,itm_poland_good_shapka],
   def_attrib|level(3),wp(60),knows_common,swadian_face_younger_1,swadian_face_older_2],
   ["pure_mujik_pol", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_moskowit_postoli_b,itm_moskowit_postoli,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_poland_shapka],
   def_attrib|level(3),wp(60),knows_common,swadian_face_younger_1,swadian_face_older_2],

   
   ["rich_baba_mosk", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_hose,itm_rich_baba_mosk_1,itm_rich_baba_mosk_2,itm_rich_baba_mosk_3],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["pure_baba_mosk", "Commoner","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_mosk_platok_1,itm_mosk_platok_2,itm_pure_baba_mosk_1,itm_pure_baba_mosk_2],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["rich_mujik_mosk", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sapogi,itm_kozak_boots,itm_good_sapogi,itm_mosk_civil_a,itm_mosk_civil_b,itm_moskowit_shapka,itm_streletz_shapka_c],
   def_attrib|level(3),wp(60),knows_common,vaegir_face_younger_1,vaegir_face_older_2],
   ["pure_mujik_mosk", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_moskowit_postoli_b,itm_moskowit_postoli,itm_mosk_armyak,itm_mosk_sermyaga],
   def_attrib|level(3),wp(60),knows_common,vaegir_face_younger_1,vaegir_face_older_2],

   ["rich_baba_ttr", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_hose,itm_rich_baba_ttr_1,itm_rich_baba_ttr_2,itm_tatar_bab_hat_rich],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["pure_baba_ttr", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_selo_boots,itm_pure_baba_ttr_1,itm_pure_baba_ttr_2,itm_tatar_bab_hat1,itm_tatar_bab_hat2],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["rich_mujik_ttr", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sapogi,itm_kozak_boots,itm_good_sapogi,itm_ttr_civil_a,itm_ttr_civil_b,itm_tatar_man_hat],
   def_attrib|level(3),wp(60),knows_common,khergit_face_younger_1,khergit_face_old_2],
   ["pure_mujik_ttr", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,itm_tatar_man_hat],
   def_attrib|level(3),wp(60),knows_common,khergit_face_younger_1,khergit_face_old_2],

   ["rich_baba_swd", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_hose,itm_rich_baba_swd_1,itm_rich_baba_swd_2,itm_rich_baba_swd_3,itm_rich_baba_swd_4],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["pure_baba_swd", "Commoner","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_pure_baba_swd_1,itm_pure_baba_swd_2],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["rich_mujik_swd", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_botinki,itm_infantry_boots,itm_evropa_pehot_tufli,itm_swed_civil_a,itm_swed_civil_b,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa],
   def_attrib|level(3),wp(60),knows_common,nord_face_younger_1,nord_face_older_2],
   ["pure_mujik_swd", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_botinki,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa,itm_evropa_shlapa_b],
   def_attrib|level(3),wp(60),knows_common,nord_face_younger_1,nord_face_older_2],

   ["rich_baba_ukr", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_hose,itm_pol_bab_hat_1,itm_pol_bab_hat_2,itm_rich_baba_pol_1,itm_rich_baba_pol_2,itm_rich_baba_pol_3],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["pure_baba_ukr", "Commoner","Commoner",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_pure_baba_pol_3,itm_pure_baba_pol_1],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
   ["rich_mujik_ukr", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [itm_sapogi,itm_kozak_boots,itm_good_sapogi,itm_kozak_civil_jupan_a,itm_kozak_civil_jupan_b,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d],
   def_attrib|level(3),wp(60),knows_common,rhodok_face_younger_1,rhodok_face_older_2],
   ["pure_mujik_ukr", "Commoner","Commoner",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_selo_boots,itm_moskowit_postoli_b,itm_moskowit_postoli,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_ukraine_svitka_c,itm_ukrine_prosta_shapka,itm_kozak_prosta_shapka],
   def_attrib|level(3),wp(60),knows_common,rhodok_face_younger_1,rhodok_face_older_2],

 ["spy_walker_1","Ordinary Townsmen","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_selo_boots,itm_moskowit_postoli_b,itm_moskowit_postoli,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_poland_shapka],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2", "Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_pure_baba_swd_1,itm_pure_baba_swd_2,itm_pure_baba_pol_1,itm_pure_baba_pol_2,itm_pure_baba_mosk_1,itm_pure_baba_mosk_2, itm_blue_hose],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master", "Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer", "Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["constable_hareck", "Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_robe],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["ramun_the_slave_trader", "Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_janissary_tapki, itm_ttr_civil_b, itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,0x000000018e04638028ce8ec552f1d69e00000000001dc8ee0000000000000000],

  ["guide", "Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["xerina", "Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_robe],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["dranton", "Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_robe],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["kradus", "Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_robe],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer", "Training Ground Master","Training Ground Master",tf_hero, scn_training_ground|entry(2),reserved, fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["galeas", "Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village", "Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots,no_scene,reserved,fac_commoners,
   [itm_mosk_armyak, itm_selo_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1", "Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2", "Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3", "Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4", "Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5", "Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_robe],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_2", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_3", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_4", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_5", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_c,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_6", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_7", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_8", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_c,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_9", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_c,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],
  ["ransom_broker_10", "Ransom Broker","Ransom Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_common,khergit_face_middle_1,khergit_face_older_2],

# Tavern traveler.
  ["tavern_traveler_1", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_ukraine_svitka_b,],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_moskowit_postoli_b,itm_ukraine_svitka_a,],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_moskowit_postoli,itm_mosk_armyak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_ukraine_svitka_b,],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_moskowit_postoli,itm_mosk_armyak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_mosk_armyak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_moskowit_postoli,itm_ukraine_svitka_a,],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_mosk_armyak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_moskowit_postoli_b,itm_mosk_armyak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10", "Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_selo_boots,itm_mosk_armyak],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1", "Book Merchant","Book Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_sapogi,itm_evropa_odejda_sela,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2", "Book Merchant","Book Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_sapogi,itm_evropa_odejda_sela_b,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1", "Bard","Bards",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_evropa_odejda_sela_b,itm_sapogi],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  
#NPC system changes begin
#Companions
  ["npc1", "Colonel Zagloba","Colonel Zagloba",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_sumpter_horse, itm_sapogi, itm_dobrotna_svitka_a, itm_poland_mehova_shapka, itm_sablya_pure_b],
   str_9|agi_5|int_12|cha_12|level(4),wp(75),
   knows_ironflesh_5|knows_power_strike_3|knows_riding_1|knows_leadership_3|knows_trainer_3, #skills 2/3 player at that level
   0x0000000e600013d1064969df62c37a4f00000000001f14350000000000000000],
  ["npc2", "Tepes","Tepes", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,
   [itm_saddle_horse,itm_sapogi, itm_infantry_gloves, itm_evropa_odejda_sela_b,itm_sablya_pure_d],
   str_8|agi_8|int_10|cha_6|level(3),wp(60),
   knows_weapon_master_1|knows_ironflesh_1|knows_leadership_3|knows_riding_2|knows_trainer_2|knows_engineer_1|knows_spotting_2,
   0x000000063f1014495be2d76fde34a79d00000000001ca8fb0000000000000000],
  ["npc3", "Priest Spasokukotsky","Priest Spasokukotsky",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,
   [itm_selo_boots, itm_robe, itm_prosta_pike],
   str_8|agi_6|int_15|cha_6|level(5),wp(50),
   knows_wound_treatment_1|knows_trade_2|knows_first_aid_2|knows_surgery_1|knows_riding_1|knows_looting_2,
   0x0000000cf30c00ce220702cff8edb6db00000000001f80890000000000000000],
  ["npc4", "Mamai","Mamai",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_saddle_horse_c, itm_kozak_boots, itm_kozak_jupan_b, itm_kozak_shapka_d, itm_kozak_shablya, itm_cavalry_pika_b],
   str_10|agi_10|int_14|cha_12|level(10),wp(135),
   knows_weapon_master_4|knows_power_strike_3|knows_riding_3|knows_athletics_3|knows_ironflesh_2,
   0x000000000f0823c059844e369a25277300000000001fd8540000000000000000],
  ["npc5", "Karlsson","Karlsson",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_evropa_pehot_tufli,itm_kirasa_b, itm_pehot_palash_old],
   str_10|agi_7|int_8|cha_8|level(5),wp(70)|wp_polearm(120),
   knows_power_strike_2|knows_weapon_master_2|knows_ironflesh_2|knows_athletics_2,
   0x0000000d9b0465cf26c36c575e56e67c00000000001df6d80000000000000000],
  ["npc6", "Fedot","Fedot",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_bolts, itm_moskowit_postoli_b, itm_pure_streletzkiy_mundir, itm_streletz_shapka, itm_sablya_pure_c, itm_old_musket_b],
   str_8|agi_10|int_8|cha_7|level(6),wp_melee(50)|wp_crossbow(100),
   knows_weapon_master_1|knows_power_strike_1|knows_athletics_2|knows_spotting_3|knows_pathfinding_3|knows_tracking_2,
  0x0000000a340812c409513248de8dd85d00000000001db4930000000000000000],
  ["npc7", "Yelisei","Yelisei",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_saddle_horse_b, itm_old_cavalry_boots, itm_mosk_sermyaga, itm_streletz_shapka_c, itm_sablya_turk_pure_a],
   str_8|agi_9|int_12|cha_8|level(5),wp(70),
   knows_riding_4|knows_athletics_2|knows_engineer_4,
   0x00000000131000020cda52b113a0d89400000000001d235d0000000000000000],
  ["npc8", "Bakhyt","Bakhyt",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_selo_boots, itm_tatar_halat_pure_a, itm_plotnik_topor],
   str_10|agi_5|int_6|cha_4|level(7),wp(50)|wp_two_handed(100),
   knows_weapon_master_1|knows_power_strike_4|knows_prisoner_management_4|knows_looting_3,
   0x0000000a1b0075c036154f5f59f4b6c400000000001f42e80000000000000000],
  ["npc9", "Algirdas","Algirdas",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_saddle_horse, itm_sapogi, itm_poland_svitka_b, itm_sablya_pure_d],
   str_7|agi_8|int_10|cha_10|level(4),wp(70),
   knows_riding_2|knows_athletics_1|knows_leadership_4|knows_tactics_2|knows_power_strike_1|knows_ironflesh_1,
   0x00000005120c040438e5b2975255d8e200000000001eb45c0000000000000000],
  ["npc10", "Victor de la Buscador","Victor de la Buscador",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_infantry_boots, itm_infantry_gloves, itm_evropa_gvardia_uniforma, itm_morion, itm_prosta_shpaga],
   str_10|agi_8|int_12|cha_14|level(8),wp_melee(125),
   knows_weapon_master_4|knows_tactics_4|knows_leadership_2|knows_trainer_2|knows_riding_2,
   0x0000000dfb00148106db64bb8449566b00000000001e34db0000000000000000],
  ["npc11", "Nogai","Nogai",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_saddle_horse_c, itm_sapogi, itm_tatar_halat_a, itm_tatar_man_hat, itm_sablya_tatar_pure_a],
   str_8|agi_10|int_8|cha_10|level(6),wp(80),
   knows_weapon_master_3|knows_riding_3|knows_athletics_3|knows_ironflesh_3|knows_power_draw_2|knows_horse_archery_3,
   0x000000093f0c628044ed4ee214cd14aa00000000001e38de0000000000000000],
  ["npc12", "Sarabun","Sarabun",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_pilgrim_disguise, itm_selo_boots, itm_dubinka],
   str_7|agi_7|int_14|cha_8|level(6),wp(50),  
   knows_surgery_3|knows_wound_treatment_3|knows_first_aid_4,
   0x0000000ea70c55d26af48e599f5458cc00000000001ebb190000000000000000],
  ["npc13", "Oksana","Oksana",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_sumpter_horse, itm_plotnik_toporik, itm_rich_baba_pol_1, itm_selo_boots],
   str_7|agi_7|int_12|cha_12|level(5),wp(40),
   knows_riding_1|knows_leadership_2|knows_athletics_1|knows_power_strike_1|knows_surgery_1|knows_wound_treatment_2|knows_first_aid_1|knows_pathfinding_2|knows_looting_1,
   0x000000003f0c00014752b0c4438a54a300000000001eba220000000000000000],
  ["npc14", "Ingri","Ingri",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_rusty_shpaga, itm_samopal_b, itm_cartridges, itm_pure_baba_swd_1, itm_botinki],
   str_7|agi_8|int_11|cha_9|level(5),wp(65),
   knows_inventory_management_4|knows_trade_4,
   0x00000007400020050b8888c8c66ec42600000000001d268b0000000000000000],
  ["npc15", "Varvara","Varvara",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_selo_boots, itm_rich_baba_mosk_2, itm_dubinka],
   str_8|agi_7|int_8|cha_10|level(4),wp(50),
   knows_trade_1|knows_spotting_1|knows_inventory_management_2|knows_wound_treatment_2|knows_power_strike_3|knows_ironflesh_2,
   0x00000007d610100237c8633ac9c63b9e00000000001eb8470000000000000000],
  ["npc16", "Fatima","Fatima",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,
   [itm_pure_baba_ttr_1, itm_throwing_daggers, itm_shield, itm_yatagan_a, itm_janissary_tapki],
   str_8|agi_11|int_9|cha_9|level(8),wp(90),
   knows_power_throw_4|knows_athletics_4|knows_power_strike_1|knows_riding_3|knows_shield_3,
   0x00000000220c3004392db25b04859d5400000000001e464c0000000000000000],
#NPC system changes end

  ["kingdom_heroes_including_player_begin","list heroes, including the player","list heroes, including players",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord", "King Jan Kasimir","Kingdom 1 Lord",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_rich_horse_b,   itm_dobrotna_svitka_b,        itm_poland_gusar_yaguar,                  itm_good_cavalry_boots,               itm_poland_gusar_helmet, itm_leather_gloves,    itm_sablya_a],          knight_attrib_5,wp(220),knight_skills_5, 0x000000043a001690177c70bfa688632a00000000001df7270000000000000000],
  ["kingdom_2_lord", "Tsar Alexei Mikhailovich","Kingdom 2 Lord",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_rich_horse,    itm_tzar_odyag,      itm_good_cavalry_boots,              itm_good_cavalry_boots,              itm_moskow_zertzalo, itm_leather_gloves,      itm_chekan_good, itm_shapka_monomaha, itm_misurka_s_barmizoy_rich],    knight_attrib_5,wp(220),knight_skills_5, 0x000000048000538416dbccc88561fcfb00000000001ec6330000000000000000],
  ["kingdom_3_lord", "Khan Islam Giray","Kingdom 3 Lord",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_rich_horse,   itm_ttr_civil_a,             itm_good_cavalry_boots,              itm_good_cavalry_boots,           itm_tatar_bahter_a,  itm_klevetz_good, itm_tatar_han_helmet],      knight_attrib_5,wp(220),knight_skills_5, 0x0000000a7f00301b4aaa935b1ba1966a00000000001d97490000000000000000],
  ["kingdom_4_lord", "King Carl Gustaf","Kingdom 4 Lord",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_rich_horse_b,    itm_swed_civil_b,    itm_good_cavalry_botforts,              itm_good_cavalry_botforts,                 itm_reytar_armor,  itm_leather_gloves,    itm_good_shpaga_b, itm_morion_perfect],            knight_attrib_5,wp(220),knight_skills_5, 0x00000006f00026863bbd61d693e0758300000000001c6ce60000000000000000],
  ["kingdom_5_lord", "Hetman Bogdan Hmelnitski","Kingdom 5 Lord",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_rich_horse,  itm_kozak_civil_jupan_a,             itm_good_sapogi,              itm_good_sapogi,   itm_kolchuga,    itm_kozak_shapka_d,    itm_pernach],         knight_attrib_5,wp(220),knight_skills_5, 0x0000000df50c554426fa123f8fc0767200000000001d530c0000000000000000],


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes:        
  #Older knights with higher skills moved to top
  ["knight_1_1", "Colonel Andrzej Kmicic","knight 1 1", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse_b,      itm_dobrotna_svitka_b,      itm_koja_kurtka_s_podbivom,   itm_good_cavalry_boots, itm_good_cavalry_boots,       itm_poland_mehova_shapka,           itm_sablya_a],   knight_attrib_4,wp(250),knight_skills_4, 0x000000086b0414dd288a6fc7db89f5bc00000000001ca2880000000000000000],
  ["knight_1_2", "Colonel Michal Wolodyjowski","knight 1 2", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse,      itm_dobrotna_svitka_e,     itm_dobrotna_svitka_c,                 itm_good_cavalry_boots,              itm_good_cavalry_boots,                      itm_poland_mehova_shapka,  itm_sablya_d],    knight_attrib_5,wp(400),knight_skills_5, 0x0000000683085618269cad4ac5c1a4d800000000001edc6d0000000000000000],
  ["knight_1_3", "Colonel Jan Skrzetuski","knight 1 3", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse,           itm_dobrotna_svitka_c,        itm_kolchuga_panzernika,                   itm_good_cavalry_boots,            itm_good_cavalry_boots,                   itm_poland_mehova_shapka_s_perom,    itm_sablya_c],   knight_attrib_4,wp(250),knight_skills_4, 0x00000007df08240e06016db71a81f6d500000000001d99330000000000000000],
  ["knight_1_4", "Warlord Alexander Oginsky","knight 1 4", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,           itm_dobrotna_svitka_a,      itm_poland_gusar_panzer_bez_kril,               itm_good_cavalry_boots,            itm_good_cavalry_boots,                    itm_poland_mehova_shapka_s_perom,   itm_sablya_c],       knight_attrib_3,wp(200),knight_skills_3, 0x00000006d010149937332656738ddcdb00000000001f49530000000000000000],
  ["knight_1_5", "Warlord Stanislav Liantskoronsky","knight 1 5", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,          itm_dobrotna_svitka_b,     itm_kolchuga_panzernika,                 itm_good_cavalry_boots,          itm_good_cavalry_boots,        itm_poland_mehova_shapka_s_perom,  itm_pernach],  knight_attrib_3,wp(220),knight_skills_5, 0x0000000abd00010f47348c46e949d69600000000001c36e20000000000000000],
  ["knight_1_6", "Warlord Fyodor Obukhovich","knight 1 6", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_mosk_civil_b,        itm_moskow_bahter_a,                    itm_good_cavalry_boots,            itm_good_cavalry_boots,                      itm_poland_good_shapka,   itm_pernach],    knight_attrib_3,wp(190),knight_skills_3, 0x00000007ca0835503c6156105c47424c00000000001dc5130000000000000000],
  ["knight_1_7", "Count Casimir Tyszkiewicz","knight 1 7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_dobrotna_svitka_c,      itm_poland_gusar_yaguar,           itm_cavalry_boots,            itm_cavalry_boots,                itm_poland_gusar_helmet,   itm_palitza],   knight_attrib_2,wp(175),knight_skills_2, 0x00000006ab08361b4c92b1d31b4d2a6c00000000001cd99d0000000000000000],
  ["knight_1_8", "Warlord Janusz Kiszka","knight 1 8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_dobrotna_svitka_e,       itm_koja_kurtka_s_podbivom,           itm_good_sapogi,          itm_good_sapogi,                   itm_poland_shapka,  itm_palitza],    knight_attrib_4,wp(160),knight_skills_3|knows_trainer_6, 0x000000090000035536fa766753a5f04f00000000001d02150000000000000000],
  ["knight_1_9", "Hetman Pavel Sapega","knight 1 9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse,            itm_dobrotna_svitka_c,        itm_poland_gusar_panzer_bez_kril,                   itm_cavalry_boots,            itm_cavalry_boots,                   itm_poland_mehova_shapka,   itm_sablya_b, itm_karabin_batarey_good,  itm_steel_bolts],      knight_attrib_4,wp(200),knight_skills_4, 0x00000002ff1005491ca24e5dde41571f00000000001c97f80000000000000000],
  ["knight_1_10", "Colonel Jerzy Halecki","knight 1 0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse_b,            itm_dobrotna_svitka_c,      itm_koja_kurtka_s_podbivom,               itm_good_cavalry_boots,          itm_good_cavalry_boots,                      itm_poland_good_shapka, itm_sablya_d, itm_good_pistol, itm_bolts], knight_attrib_3,wp(200),knight_skills_3, 0x00000004e91003ce336565b4e7576ca600000000001ea4f30000000000000000],
  ["knight_1_11", "Colonel Jan Zenowicz","knight 1 1", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_dobrotna_svitka_d,      itm_kolchuga_panzernika,                     itm_cavalry_boots,            itm_cavalry_boots,                itm_poland_good_shapka,   itm_sablya_a],   knight_attrib_1,wp(150),knight_skills_1, 0x00000004d900450e450dc9beda6542d600000000001d86a30000000000000000],
  ["knight_1_12", "Warlord Jan Zamojski","knight 1 2", tf_hero, 0, reserved,  fac_kingdom_1, [itm_courser,      itm_dobrotna_svitka_a,     itm_koja_kurtka_s_podbivom,                 itm_good_sapogi,              itm_good_sapogi,                      itm_poland_mehova_shapka_s_perom,   itm_sablya_d],    knight_attrib_2,wp(190),knight_skills_2, 0x00000002c51024865d7a765fdfe07ad700000000001c36a80000000000000000],
  ["knight_1_13", "Cornet Siegmund Slushka","knight 1 3", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,           itm_dobrotna_svitka_b,        itm_poland_dragoon_uniform,                   itm_cavalry_boots,            itm_cavalry_boots,                   itm_poland_mehova_shapka,   itm_klevetz_good],   knight_attrib_2,wp(170),knight_skills_1, 0x00000006f904349768826dac9ca9dc2100000000001dd89e0000000000000000],
  ["knight_1_14", "Hetman Jan Sobieski","knight 1 4", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse,           itm_dobrotna_svitka_b,      itm_poland_gusar_yaguar,               itm_good_cavalry_boots,            itm_good_cavalry_boots,                    itm_poland_good_shapka,  itm_palitza],       knight_attrib_4,wp(200),knight_skills_4, 0x00000003cb0843d7575b6a2920b1f92500000000001fbafb0000000000000000],
  ["knight_1_15", "Hetman Stanislaw Potocki","knight 1 5", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,          itm_dobrotna_svitka_d,     itm_poland_gusar_yaguar,                 itm_good_sapogi,          itm_good_sapogi,        itm_misurka_s_barmizoy_rich, itm_sablya_a,   itm_good_pistol_b, itm_cartridges],  knight_attrib_5,wp(200),knight_skills_5, 0x0000000ec010035c09334c2bd46150cc00000000001d02bc0000000000000000],
  ["knight_1_16", "Hetman Stefan Czarniecki","knight 1 6", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_dobrotna_svitka_c,        itm_kolchuga_panzernika,                    itm_good_cavalry_boots,            itm_good_cavalry_boots,                      itm_misurka_s_barmizoy_rich, itm_sablya_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000cc000138a26f36ded0d20389d00000000001d26230000000000000000],
  ["knight_1_17", "Warlord Krzysztof Grzymultowski","knight 1 7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_dobrotna_svitka_e,      itm_koja_kurtka_s_podbivom,           itm_cavalry_boots,            itm_cavalry_boots,                itm_misurka_s_barmizoy_rich, itm_sablya_b],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000f1b00354d4ae23238de8a590d00000000001ea1240000000000000000],
  ["knight_1_18", "Colonel Alexander Casimir Wolowicz","knight 1 8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_dobrotna_svitka_c,       itm_kolchuga_panzernika,           itm_good_cavalry_boots,          itm_good_cavalry_boots,                   itm_poland_mehova_shapka_s_perom, itm_sablya_b],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000f4000041536db6db6db6db6db00000000001db6db0000000000000000],
  ["knight_1_19", "Prince Boguslav Nesvizhsky","knight 1 9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse_b,            itm_dobrotna_svitka_e,        itm_kolchuga_panzernika,                   itm_good_sapogi,            itm_good_sapogi,                   itm_poland_gusar_helmet, itm_sablya_a],      knight_attrib_3,wp(200),knight_skills_3, 0x0000000252103690166b90ad9da8b6ab00000000001cd2ac0000000000000000],
  ["knight_1_20", "Prince Michal Vishnevetsky","knight 1 0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_rich_horse,            itm_dobrotna_svitka_d,      itm_koja_kurtka_s_podbivom,               itm_good_sapogi,          itm_good_sapogi,                      itm_misurka_s_barmizoy_rich, itm_sablya_a], knight_attrib_4,wp(200),knight_skills_4, 0x0000000897043510366cb5c5536d78da00000000001dc4a90000000000000000],



  
#  ["knight_1_21", "Lord Swadian 21", "knight_1_7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,                                                              ],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],
 # ["knight_1_22", "Lord Swadian 22", "knight_1_8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,                                                  ],    knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
#  ["knight_1_23", "Lord Swadian 23", "knight_1_9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,                                     itm_woolen_hose,                                         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
#  ["knight_1_24", "Lord Swadian 24", "knight_1_0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,                                                     ], knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],

  
  
  ["knight_2_1", "Warlord Yuri Buynosov-Rostovsky","knight 2 1", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse,      itm_mosk_civil_b,     itm_moskow_boyar_uniform,                   itm_good_sapogi,            itm_good_sapogi,        itm_boyar_helmet,    itm_sablya_turk_b],    knight_attrib_4,wp(150),knight_skills_4, 0x000000098b08538f46cca9aa7b6dd65d00000000001e670c0000000000000000],
  ["knight_2_2", "Prince Ivan Sontsov-Zasekin","knight 2 2", tf_hero, 0, reserved,  fac_kingdom_2, [  itm_mosk_civil_a,        itm_moskow_zertzalo,               itm_good_sapogi,            itm_good_sapogi,            itm_shapka_boyara,       itm_mosk_shishak,  itm_berdish,    itm_good_musket, itm_bolts],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000a1c0c218524e288999b69b75400000000001cd4ec0000000000000000],
  ["knight_2_3", "Prince Semyon Prozorovsky","knight 2 3", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse_b,            itm_mosk_civil_a,        itm_moskow_kuyak,                   itm_kozak_boots,            itm_kozak_boots,            itm_shapka_boyara,      itm_shapka_bumajna_b, itm_sablya_turk_c],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000a7500535066d3939d46e0b6c400000000001fd61f0000000000000000],
  ["knight_2_4", "Warlord Semyon Rakhmanin","knight 2 4", tf_hero, 0, reserved,  fac_kingdom_2, [itm_saddle_horse,      itm_mosk_civil_b,     itm_moskow_boyar_uniform,               itm_good_sapogi,          itm_good_sapogi,                      itm_moskowit_shapka, itm_sablya_turk_b],    knight_attrib_4,wp(200),knight_skills_4, 0x00000009af10139c070451cb1d454e0b00000000001eca9b0000000000000000],
  ["knight_2_5", "Warlord Boris Repnin-Obolevsky","knight 2 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_mosk_civil_b,        itm_moskow_bahter_a,                     itm_cavalry_boots,          itm_cavalry_boots,                   itm_boyar_helmet, itm_sablya_a],       knight_attrib_3,wp(250),knight_skills_3, 0x0000000c7f006350471b889ecf49fadf00000000001d99bb0000000000000000],
  ["knight_2_6", "Warlord Fyodor Volkonsky","knight 2 6", tf_hero, 0, reserved,  fac_kingdom_2, [itm_saddle_horse,      itm_mosk_civil_a,      itm_streletzkiy_mundir_spear,                   itm_cavalry_boots,            itm_cavalry_boots,                   itm_shapka_bumajna_a,  itm_sablya_b],   knight_attrib_2,wp(250),knight_skills_2, 0x000000099408534e14a421c9526ecd2200000000001c98dc0000000000000000],
  ["knight_2_7", "Chief Naum Vasiliev","Ralcha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse,      itm_ttr_civil_b,     itm_kolchuga,                   itm_kozak_boots,          itm_kozak_boots,                      itm_boyar_helmet,  itm_toporik_rich],     knight_attrib_4,wp(230),knight_skills_4, 0x0000000a750c23502f1372d152952d1b00000000001db0a40000000000000000],
  ["knight_2_8", "Noble Alexei Vorotynsky","knight 2 8", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_mosk_civil_a,             itm_moskow_kuyak,                     itm_good_cavalry_boots,            itm_good_cavalry_boots,                  itm_shapka_boyara, itm_mosk_shishak,       itm_shestoper],    knight_attrib_4,wp(200),knight_skills_4, 0x0000000f450c135b254b512853d578dd00000000001ea2f40000000000000000],
  ["knight_2_9", "Prince Yakov Cherkassky","knight 2 9", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse_b,      itm_ttr_civil_b,        itm_moskow_bahter_a,                     itm_good_sapogi,          itm_good_sapogi,           itm_shapka_boyara,        itm_tatar_helmet_b,  itm_sablya_c],    knight_attrib_3,wp(200),knight_skills_3, 0x00000006c40c418e569a91b9052cbefb00000000001f46230000000000000000],
  ["knight_2_10", "Prince Alexei Trubetskoi","knight 2 0", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,          itm_mosk_civil_b,        itm_moskow_bahter_a,               itm_good_cavalry_boots,            itm_good_cavalry_boots,        itm_shapka_boyara,              itm_boyar_helmet,  itm_sovnya,      itm_chekan_good],      knight_attrib_4,wp(190),knight_skills_3, 0x0000000ed000039a565e6a3dd94c592400000000001db7ac0000000000000000],
  ["knight_2_11", "Warlord Vasiliy Buturlin","knight 2 1", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse,      itm_mosk_civil_a,     itm_moskow_tulup_c,                   itm_good_sapogi,            itm_good_sapogi,        itm_moskow_reytar_helmet, itm_klevetz_good],    knight_attrib_1,wp(150),knight_skills_1, 0x0000000f7c00534a55324a249a864ae500000000001ecda90000000000000000],
  ["knight_2_12", "Noble Vasiliy Sheremetyev","knight 2 2", tf_hero, 0, reserved,  fac_kingdom_2, [itm_saddle_horse,      itm_mosk_civil_b,        itm_moskow_tulup_b,               itm_cavalry_boots,            itm_cavalry_boots,           itm_shapka_boyara,        itm_shishak,  itm_toporik_rich],    knight_attrib_2,wp(170),knight_skills_2, 0x00000004d400029b37dba53b4541be3f00000000001e95730000000000000000],
  ["knight_2_13", "Prince Semyon Urusov","knight 2 3", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse_b,            itm_mosk_civil_a,        itm_moskow_tulup_a,                   itm_cavalry_boots,            itm_cavalry_boots,            itm_shapka_boyara,       itm_moskow_reytar_helmet,  itm_sablya_turk_b],     knight_attrib_3,wp(190),knight_skills_3, 0x000000011d00431d16956eb692f1486c00000000001e42a40000000000000000],
  ["knight_2_14", "Prince Yuri Boryatinsky","knight 2 4", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse,      itm_mosk_civil_a,     itm_moskow_bahter_a,               itm_good_sapogi,          itm_good_sapogi,             itm_shapka_bumajna_b,         itm_shapka_boyara,  itm_sablya_a],    knight_attrib_2,wp(220),knight_skills_2, 0x0000000f3b0c328e4a898895854e22b300000000001cd6ad0000000000000000],
  ["knight_2_15", "Warlord Fyodor Hvorostinin","knight 2 5", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_mosk_civil_a,        itm_moskow_boyar_uniform,                     itm_good_cavalry_boots,          itm_good_cavalry_boots,                   itm_boyar_helmet, itm_sablya_a],       knight_attrib_5,wp(250),knight_skills_5, 0x00000008540c058646b4acc512c2f66d00000000001f174d0000000000000000],
  ["knight_2_16", "Prince Andrei Khovansky","knight 2 6", tf_hero, 0, reserved,  fac_kingdom_2, [itm_rich_horse_b,      itm_mosk_civil_a,      itm_moskow_tulup_a,                   itm_good_sapogi,            itm_good_sapogi,        itm_shapka_boyara,           itm_misurka_s_barmizoy_b,  itm_palitza],   knight_attrib_1,wp(170),knight_skills_1, 0x000000035400130e36dc6db71ba1831b00000000001d862b0000000000000000],
  ["knight_2_17", "Warlord Nikita Odoevsky","Ralcha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_steppe_horse,      itm_mosk_civil_a,     itm_moskow_kuyak,                   itm_kozak_boots,          itm_kozak_boots,                      itm_boyar_helmet,   itm_palitza],     knight_attrib_2,wp(150),knight_skills_2, 0x00000003ff0012d83742a93ddcc6b4ce00000000001e922f0000000000000000],
  ["knight_2_18", "Chief Pavel Neskachikhin","knight 2 8", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter,            itm_mosk_civil_b,             itm_tatar_kolcha,                     itm_good_cavalry_boots,            itm_good_cavalry_boots,                   itm_streletz_shapka_c,  itm_sablya_b],    knight_attrib_3,wp(180),knight_skills_3, 0x00000008b50c034e195b92273375aba100000000001e171b0000000000000000],
  ["knight_2_19", "Warlord Boris Pushkin","knight 2 9", tf_hero, 0, reserved,  fac_kingdom_2, [itm_saddle_horse,      itm_mosk_civil_b,        itm_moskow_zertzalo,                     itm_good_sapogi,          itm_good_sapogi,                   itm_misurka_s_barmizoy_c, itm_palitza],    knight_attrib_4,wp(200),knight_skills_4, 0x000000096a08135016a38edca3adccf300000000001dc96b0000000000000000],
  ["knight_2_20", "Warlord Afanasiy Ordin-Naschokin","knight 2 0", tf_hero, 0, reserved,  fac_kingdom_2, [itm_saddle_horse_b,          itm_mosk_civil_b,        itm_moskow_tulup_c,               itm_kozak_boots,            itm_kozak_boots,                      itm_boyar_helmet,  itm_toporik_rich],      knight_attrib_3,wp(240),knight_skills_3, 0x0000000b8c00034e77da74df4f04375b00000000001cdbae0000000000000000],

#khergit civilian clothes:    
  ["knight_3_1", "Baesid-khan","knight 3 1", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_ttr_civil_a ,  itm_tatar_bahter_a ,itm_good_cavalry_boots,  itm_good_cavalry_boots, itm_tatar_han_helmet, itm_sablya_turk_b, itm_kompozit_bow, itm_bodkin_arrows, itm_round_shield_steel_a],  knight_attrib_4,wp(220),knight_skills_5, 0x0000000dbf0462403323abd99269c30200000000001da4b30000000000000000],
  ["knight_3_2", "Ahmed-pasha","knight 3 2", tf_hero, 0, reserved,  fac_kingdom_3, [itm_rich_horse, itm_ttr_civil_a,   itm_tatar_yushman, itm_good_cavalry_boots,  itm_good_cavalry_boots, itm_tatar_misurka_rich, itm_sablya_turk_b], knight_attrib_2,wp(200),knight_skills_2, 0x0000000c3f005700245d4fab0ae6148900000000001f32a40000000000000000],
  ["knight_3_3", "Imad-pasha","knight 3 3", tf_hero, 0, reserved,  fac_kingdom_3, [itm_rich_horse, itm_ttr_civil_a, itm_tatar_bahter_a,itm_good_cavalry_boots,  itm_good_cavalry_boots,  itm_tatar_misurka_rich, itm_sablya_turk_b],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000a3f1036c0089e6aa6954194c400000000001db7380000000000000000],
  ["knight_3_4", "Mirza Enikey","knight 3 4", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_ttr_civil_b,  itm_tatar_kolcha, itm_cavalry_boots,  itm_cavalry_boots,   itm_tatar_oglan_hat, itm_sablya_turk_c],  knight_attrib_2,wp(220),knight_skills_2, 0x0000000bff08568046b26f53a4ae191b00000000001e39320000000000000000],
  ["knight_3_5", "Mirza Yanmamed","knight 3 5", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_ttr_civil_a,  itm_tatar_bahter_a, itm_cavalry_boots,  itm_cavalry_boots, itm_tatar_oglan_hat, itm_sablya_turk_c],  knight_attrib_2,wp(250),knight_skills_2, 0x0000000a7f00268044ce6a60dd49445400000000001ca3620000000000000000],
  ["knight_3_6", "Shirin-bey","knight 3 6", tf_hero, 0, reserved,  fac_kingdom_3, [itm_saddle_horse_c, itm_ttr_civil_b, itm_tatar_kolcha, itm_old_cavalry_boots, itm_old_cavalry_boots,  itm_tatar_misurka_rich,  itm_sablya_turk_c], knight_attrib_3,wp(150),knight_skills_3, 0x00000009230c468027254747556dc4cd00000000001d57640000000000000000],
  ["knight_3_7", "Mirza Davletshi","knight 3 7", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_ttr_civil_b, itm_tatar_yushman, itm_old_cavalry_boots, itm_old_cavalry_boots, itm_tatar_misurka_rich, itm_sablya_turk_b], knight_attrib_1,wp(150),knight_skills_1, 0x000000047f0022401a6c33b30961a4c900000000001ec6ab0000000000000000],
  ["knight_3_8", "Bukryn-bey","knight 3 8", tf_hero, 0, reserved,  fac_kingdom_3, [itm_saddle_horse_c,  itm_ttr_civil_a, itm_tatar_kolcha, itm_cavalry_boots, itm_cavalry_boots, itm_tatar_han_helmet, itm_klevetz_good],  knight_attrib_3,wp(190),knight_skills_3, 0x00000005b304364026454f5b4e84a30b00000000001ea2710000000000000000],
  ["knight_3_9", "Baryn-bet","knight 3 9", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter,  itm_ttr_civil_b, itm_tatar_bahter_a,  itm_good_cavalry_boots, itm_good_cavalry_boots,  itm_tatar_misurka_rich, itm_sablya_turk_c],  knight_attrib_4,wp(220),knight_skills_4, 0x00000002bf0846c0389d8baa5b69244200000000001e28b50000000000000000],
  ["knight_3_10", "Argun-bey","knight 3 0", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_ttr_civil_a, itm_tatar_kolcha, itm_old_cavalry_boots, itm_old_cavalry_boots,  itm_tatar_misurka_rich, itm_sablya_tatar_a], knight_attrib_5,wp(250),knight_skills_5, 0x00000002e41060001a268f389a448d1b00000000001cb89b0000000000000000],
  ["knight_3_11", "Sedjet-bey","knight 3 1", tf_hero, 0, reserved,  fac_kingdom_3, [itm_saddle_horse_c, itm_ttr_civil_b, itm_tatar_kolcha, itm_cavalry_boots, itm_cavalry_boots,  itm_tatar_helmet_a,  itm_sablya_tatar_a],  knight_attrib_1,wp(150),knight_skills_1, 0x00000004fb0c5200271d92a6dc2d36d200000000001e56e40000000000000000],
  ["knight_3_12", "Mansur-bey","knight 3 2", tf_hero, 0, reserved,  fac_kingdom_3, [itm_saddle_horse_c, itm_ttr_civil_a, itm_tatar_yushman, itm_good_sapogi, itm_good_sapogi,  itm_tatar_han_helmet,  itm_sablya_tatar_a,  itm_round_shield_c], knight_attrib_3,wp(170),knight_skills_4, 0x0000000efb08320044de6add5589266a00000000001de6f10000000000000000],
  ["knight_3_13", "Yashlav-bey","knight 3 3", tf_hero, 0, reserved,  fac_kingdom_3, [itm_saddle_horse_c, itm_ttr_civil_b,  itm_tatar_bahter_a, itm_good_cavalry_boots, itm_good_cavalry_boots,  itm_tatar_helmet_b, itm_sablya_tatar_a],  knight_attrib_3,wp(200),knight_skills_3, 0x0000000edc1043002cb483666b72486200000000001d24530000000000000000],
  ["knight_3_14", "Mirza Argyn","knight 3 4", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_ttr_civil_a, itm_tatar_steg_halat_a, itm_cavalry_boots, itm_cavalry_boots, itm_tatar_helmet_a, itm_klevetz_good],  knight_attrib_4,wp(200),knight_skills_4, 0x00000002a404470066ac0aa45e14a71800000000001d66ec0000000000000000],
  ["knight_3_15", "Mirza Agish","knight 3 5", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,   itm_ttr_civil_b, itm_tatar_yushman, itm_old_cavalry_boots, itm_old_cavalry_boots,  itm_tatar_han_helmet, itm_sablya_tatar_a],  knight_attrib_3,wp(240),knight_skills_3, 0x00000008ff082440397673a99952169300000000001db6aa0000000000000000],
  ["knight_3_16", "Mirza Divey","knight 3 6", tf_hero, 0, reserved,  fac_kingdom_3, [itm_saddle_horse_c, itm_ttr_civil_a,  itm_tatar_steg_halat_b,  itm_old_cavalry_boots,  itm_old_cavalry_boots,  itm_tatar_helmet_b, itm_sablya_tatar_a],  knight_attrib_1,wp(120),knight_skills_1, 0x00000005fe1046803ce68757146e79e500000000001ec8dc0000000000000000],
  ["knight_3_17", "Mirza Appak","knight 3 7", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_ttr_civil_b, itm_tatar_bahter_b, itm_good_cavalry_boots, itm_good_cavalry_boots, itm_tatar_han_helmet, itm_sablya_turk_b],  knight_attrib_2,wp(150),knight_skills_2, 0x000000023700400056dd8aa71e852b5b00000000001e64e60000000000000000],
  ["knight_3_18", "Mirza Karach","knight 3 8", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser,  itm_ttr_civil_a, itm_tatar_kolcha, itm_good_sapogi, itm_good_sapogi,  itm_tatar_misurka_rich, itm_sablya_tatar_a, itm_luk_c,itm_khergit_arrows],   knight_attrib_3,wp(175),knight_skills_3, 0x0000000a770456c0474e6f26c3a922da00000000001d5adb0000000000000000],
  ["knight_3_19", "Mirza Yelchy","knight 3 9", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter,   itm_ttr_civil_b, itm_tatar_yushman, itm_cavalry_boots, itm_cavalry_boots,  itm_tatar_helmet_a, itm_klevetz_good],  knight_attrib_4,wp(210),knight_skills_4, 0x00000008fb005180249d42bad48a429b00000000001e4b640000000000000000],
  ["knight_3_20", "Uzyn-bey","knight 3 0", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_ttr_civil_a, itm_tatar_bahter_b, itm_good_cavalry_boots, itm_good_cavalry_boots, itm_tatar_han_helmet, itm_sablya_turk_b],  knight_attrib_1,wp(140),knight_skills_1, 0x000000022f08368044dc875654ca369a00000000001e49120000000000000000],

  ["knight_4_1", "General Brahe Wisingsborg","knight 4 1", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter, itm_swed_civil_a,  itm_reytar_armor,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts,  itm_morion_perfect, itm_good_shpaga_d], knight_attrib_5,wp(150),knight_skills_5, 0x0000000bd90c5690308c6d3a83e546c700000000001c0d5f0000000000000000],
  ["knight_4_2", "Governor-General Magnus De la Gardie","knight 4 2", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_horse_b, itm_swed_civil_a,  itm_kirasa_rich, itm_cavalry_botforts,  itm_cavalry_botforts,  itm_parik, itm_good_shpaga_d],  knight_attrib_5,wp(200),knight_skills_5, 0x000000070008460606cbb14d8ec4e4e300000000001cb71f0000000000000000],
  ["knight_4_3", "Count Orvar von Goya","knight 4 3", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter, itm_swed_civil_a,  itm_kirasa_rich,   itm_infantry_boots,  itm_infantry_boots,  itm_morion_good,   itm_good_shpaga_c, itm_pistol, itm_cartridges],  knight_attrib_2,wp(180),knight_skills_2, 0x00000006ef04010658e2ba5ccc49a4cc00000000001cd89e0000000000000000],
  ["knight_4_4", "Governor Anders Eriksson","knight 4 4", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_swed_civil_b,   itm_reytar_armor,   itm_old_cavalry_botforts,  itm_old_cavalry_botforts, itm_morion_good, itm_good_shpaga_d],  knight_attrib_3,wp(150),knight_skills_3, 0x00000008761055864ada11588445caab00000000001e18cc0000000000000000],
  ["knight_4_5", "Elector Frederick William","knight 4 5", tf_hero, 0, reserved,  fac_kingdom_4, [itm_saddle_horse_b, itm_swed_civil_b,   itm_dospeh,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts,  itm_parik, itm_good_shpaga_c], knight_attrib_3,wp(250),knight_skills_3, 0x00000005600c36102872725de7c07af600000000001dd69e0000000000000000],
  ["knight_4_6", "Ratsherr Dirich Werneken","knight 4 6", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_swed_civil_a,   itm_reytar_armor,  itm_old_cavalry_botforts,  itm_old_cavalry_botforts,   itm_reytar_helmet, itm_good_shpaga_c],   knight_attrib_2,wp(190),knight_skills_2, 0x000000063e0c0086289349e9c58934cb00000000001d294a0000000000000000],
  ["knight_4_7", "General Arvid Vittenberg","knight 4 7", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_hunter,    itm_swed_civil_b,   itm_kirasa_rich,   itm_old_cavalry_botforts,  itm_old_cavalry_botforts,  itm_morion_perfect, itm_bolts,   itm_good_palash, itm_good_pistol_b,itm_armor_gauntlets],   knight_attrib_3,wp(180),knight_skills_5, 0x0000000dc010010f16f36076c482f29a00000000001d1c9b0000000000000000],
  ["knight_4_8", "General Gustaf Evertsson Horn","knight 4 8", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_horse_b, itm_swed_civil_b,  itm_black_dospeh,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts,   itm_parik, itm_good_palash_b],   knight_attrib_4,wp(200),knight_skills_4, 0x0000000a3210211004bb6d6fdd81f50700000000001d06b60000000000000000],
  ["knight_4_9", "Ratsherr Alexander Leslie","knight 4 9", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_swed_civil_a,   itm_scott_uniforma, itm_cavalry_botforts,  itm_cavalry_botforts,  itm_beret_c, itm_leather_gloves, itm_steel_bolts, itm_mushket_udarniy_b,   itm_scott_palash],  knight_attrib_4,wp(200),knight_skills_4, 0x00000005150c12cf08fa72e7946d38cd00000000001d34640000000000000000],
  ["knight_4_10", "Baron Gustaf Wrangel","knight 4 0", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_swed_civil_b,   itm_dospeh,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts,  itm_morion_perfect,itm_good_shpaga_b],  knight_attrib_4,wp(250),knight_skills_4, 0x000000061c1051104d5c85ddce89f69600000000001c35a40000000000000000],
  ["knight_4_11", "Baron Christopher Bjolke","knight 4 1", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter, itm_swed_civil_a,  itm_reytar_armor,   itm_old_cavalry_botforts,  itm_old_cavalry_botforts,  itm_parik,  itm_good_shpaga_b], knight_attrib_2,wp(150),knight_skills_2, 0x00000005c70c25906d3469a2ce69c4f100000000001e24e30000000000000000],
  ["knight_4_12", "Ratsherr Lennart Torstenson","knight 4 2", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter, itm_swed_civil_b,  itm_kirasa_rich, itm_old_cavalry_botforts,  itm_old_cavalry_botforts,  itm_evropa_guard_shlapa,  itm_good_shpaga],  knight_attrib_2,wp(200),knight_skills_2, 0x00000003250002c646cb6a6b916ec6db00000000001e97260000000000000000],
  ["knight_4_13", "Ratsherr Otto Standbok","knight 4 3", tf_hero, 0, reserved,  fac_kingdom_4, [itm_saddle_horse_b, itm_swed_civil_b,  itm_dospeh,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts, itm_evropa_guard_shlapa,   itm_good_shpaga],  knight_attrib_4,wp(200),knight_skills_4, 0x000000035704611037618a16d935c45500000000001dc71a0000000000000000],
  ["knight_4_14", "General Simon Grundel-Hemfet","knight 4 4", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,  itm_swed_civil_a,   itm_reytar_armor,   itm_cavalry_botforts,  itm_cavalry_botforts,  itm_morion_perfect, itm_good_palash_b],  knight_attrib_5,wp(200),knight_skills_3, 0x0000000fe5083109214db5b11399d98b00000000001d484b0000000000000000],
  ["knight_4_15", "Ratsherr Konrad Marenfeld","knight 4 5", tf_hero, 0, reserved,  fac_kingdom_4, [itm_saddle_horse_b,   itm_swed_civil_b,   itm_kirasa_rich,   itm_cavalry_botforts,itm_cavalry_botforts, itm_evropa_guard_shlapa, itm_good_palash_b], knight_attrib_3,wp(200),knight_skills_3, 0x000000065904410f354b4f289369c6ea00000000001e5aa90000000000000000],
  ["knight_4_16", "Ratsherr Fabian von Wersen","knight 4 6", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,   itm_swed_civil_a,   itm_kirasa,  itm_good_cavalry_botforts,  itm_good_cavalry_botforts,   itm_reytar_helmet, itm_good_palash],   knight_attrib_2,wp(170),knight_skills_2, 0x00000001130c5082488d89c9638de4a100000000001e589c0000000000000000],
  ["knight_4_17", "Ratsherr Hans von Koenigsmark","knight 4 7", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter,  itm_swed_civil_b,   itm_kirasa_rich,   itm_cavalry_botforts,  itm_cavalry_botforts,  itm_kabasset, itm_good_palash],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x00000005600836c65893a9b6d18238ea00000000001caad40000000000000000],
  ["knight_4_18", "Ratsherr Nilson Kagg","knight 4 8", tf_hero, 0, reserved,  fac_kingdom_4, [itm_hunter, itm_swed_civil_a,  itm_kirasa_rich,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts,   itm_reytar_helmet, itm_good_pehot_palash],   knight_attrib_3,wp(180),knight_skills_3, 0x00000004970022102b234e464a6ae88d00000000001e48440000000000000000],
  ["knight_4_19", "General Robert Douglas","knight 4 9", tf_hero, 0, reserved,  fac_kingdom_4, [itm_swed_civil_a,   itm_scott_uniforma, itm_cavalry_botforts,  itm_cavalry_botforts, itm_beret_a,  itm_armet,  itm_scott_kleymor_b],  knight_attrib_4,wp(210),knight_skills_4, 0x00000006a804058446eba994c97226cd00000000001d57230000000000000000],
  ["knight_4_20", "Ratsherr Carl Lebenhaupt","knight 4 0", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_horse_b,   itm_swed_civil_a,   itm_kirasa_rich,   itm_good_cavalry_botforts,  itm_good_cavalry_botforts, itm_morion_good,itm_good_pehot_palash_b],  knight_attrib_4,wp(250),knight_skills_4, 0x00000006690c110637a288c75c4a39a500000000001d27140000000000000000],

  ["knight_5_1", "Colonel Anton Zhdanovich","knight 5 1", tf_hero, 0, reserved,  fac_kingdom_5, [itm_kozak_civil_jupan_a,   itm_kolchuga,       itm_kozak_boots,    itm_kozak_boots,     itm_pernach,  itm_kozak_shapka_c, itm_kozak_shapka_c, itm_turk_musket_b, itm_steel_bolts],     knight_attrib_4,wp(200),knight_skills_4, 0x0000000cff04049536d44dc4dace492c00000000001ea6f00000000000000000],
  ["knight_5_2", "Colonel Bogdan Popovich","knight 5 2", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rich_horse_b,    itm_kozak_civil_jupan_a,       itm_kolchuga,    itm_kozak_boots,    itm_kozak_boots,    itm_kozacka_shapka_s_misurkoy, itm_pernach],     knight_attrib_3,wp(200),knight_skills_3, 0x0000000efe045493225b8d639a71c69300000000001e26dc0000000000000000],
  ["knight_5_3", "Army Chief Pavlo Gomon","knight 5 3", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rich_horse,     itm_kozak_civil_jupan_b,  itm_serduk_jupan,     itm_cavalry_boots,      itm_cavalry_boots,  itm_kozak_shapka_d, itm_pernach],    knight_attrib_5,wp(200),knight_skills_5, 0x0000000cf6000412372253491389549c00000000001da8e80000000000000000],
  ["knight_5_4", "Colonel Ivan Fedorenko","knight 5 4", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_kozak_civil_jupan_a,     itm_kolchuga,       itm_cavalry_boots,      itm_cavalry_boots,    itm_poland_mehova_shapka_s_perom, itm_pernach],    knight_attrib_5,wp(300),knight_skills_5, 0x0000000b13003085323495b8d44dd56c00000000001ec8a30000000000000000],
  ["knight_5_5", "Colonel Ivan Bogun","knight 5 5", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rich_horse_b,     itm_kozak_civil_jupan_b,  itm_kozak_jupan,     itm_kozak_boots,    itm_kozak_boots,    itm_kozacka_shapka_s_misurkoy, itm_pernach], knight_attrib_5,wp(250),knight_skills_5, 0x00000008370024530c9b6d290dc4f8d600000000001e37320000000000000000],
  ["knight_5_6", "Colonel Petro Doroshenko","knight 5 6", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rich_horse,    itm_kozak_civil_jupan_a,      itm_kolchuga,       itm_cavalry_boots,      itm_cavalry_boots, itm_kozak_shapka_c,     itm_chekan_good],    knight_attrib_3,wp(150),knight_skills_3, 0x0000000b3d00370539bb69a954a5472400000000001db73d0000000000000000],
  ["knight_5_7", "Colonel Lukyan Mozyra","knight 5 7", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse_c,     itm_kozak_civil_jupan_b,       itm_kolchuga,   itm_cavalry_boots,    itm_cavalry_boots,  itm_kozak_shapka_c,       itm_sablya_turk_c],     knight_attrib_2,wp(200),knight_skills_2, 0x00000009260c5554449b3a9b1175daea00000000001dbb130000000000000000],
  ["knight_5_8", "Headquarters Clerk Ivan Vygovsky","knight 5 8", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rich_horse, itm_kozak_civil_jupan_a,     itm_kozak_civil_jupan_a,    itm_cavalry_boots,      itm_cavalry_boots,    itm_kozak_shapka_b,  itm_sablya_turk_b],    knight_attrib_4,wp(250),knight_skills_4, 0x00000007fd00308e095bc5cb1ca5571d00000000001da6f90000000000000000],
  ["knight_5_9", "Colonel Vasil Zolotarenko","knight 5 9", tf_hero, 0, reserved,  fac_kingdom_5, [itm_rich_horse_b,     itm_kozak_civil_jupan_b,     itm_kolchuga,   itm_kozak_boots,    itm_kozak_boots,       itm_kozacka_shapka_s_misurkoy, itm_chekan_good],   knight_attrib_4,wp(200),knight_skills_4, 0x00000006f80c3414490a88c7a29096d500000000001eb8b30000000000000000],
  ["knight_5_10", "Colonel Maksim Nesterenko","knight 5 0", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser,     itm_kozak_civil_jupan_a,  itm_cavalry_koja_kurtka,     itm_cavalry_boots,  itm_cavalry_boots,       itm_kozak_shapka_b, itm_kozak_good_shablya],  knight_attrib_4,wp(250),knight_skills_4, 0x00000003c2080511470a99c5a569a73600000000001e26e40000000000000000],
  ["knight_5_11", "Colonel Prokop Shumeiko","knight 5 1", tf_hero, 0, reserved,  fac_kingdom_5, [itm_saddle_horse_b,     itm_kozak_civil_jupan_b,       itm_kozak_jupan_na_kolchuge,       itm_cavalry_boots,    itm_cavalry_boots,    itm_kozak_shapka,  itm_kozak_good_shablya],     knight_attrib_1,wp(130),knight_skills_1, 0x00000006ca041491255d591ad52952da00000000001ee6680000000000000000],
  ["knight_5_12", "Colonel Ivan Sirko","knight 5 2", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser,    itm_kozak_civil_jupan_b,       itm_kozak_jupan_na_kolchuge,    itm_cavalry_boots,    itm_cavalry_boots,  itm_kozacka_pika,  itm_kozak_good_shablya],     knight_attrib_5,wp(250),knight_skills_5|knows_trainer_5, 0x0000000bc8001514049376b94d4a46fc00000000001eb6f80000000000000000],
  ["knight_5_13", "Colonel Fyodor Loboda","knight 5 3", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_kozak_civil_jupan_a,  itm_kolchuga,     itm_cavalry_boots,      itm_cavalry_boots,  itm_kozacka_shapka_s_misurkoy, itm_chekan_good],    knight_attrib_3,wp(190),knight_skills_3, 0x000000084d0000d76adb7139958a68d400000000001e35340000000000000000],
  ["knight_5_14", "Colonel Timofiy Nosach","knight 5 4", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_kozak_civil_jupan_b,     itm_kozak_jupan_na_kolchuge,       itm_good_sapogi,      itm_good_sapogi,    itm_kozak_shapka, itm_kozak_good_shablya],    knight_attrib_3,wp(200),knight_skills_3, 0x000000009504545318aba94bec8ad8e200000000001e28530000000000000000],
  ["knight_5_15", "Colonel Matviy Gladkiy","knight 5 5", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_kozak_civil_jupan_a,  itm_kolchuga,     itm_kozak_boots,    itm_kozak_boots,    itm_serduk_shapka, itm_kozak_good_shablya], knight_attrib_5,wp(200),knight_skills_2, 0x000000033c04140a18da933b9ce92d6c00000000001ea6d90000000000000000],
  ["knight_5_16", "Colonel Martyn Pushkarenko","knight 5 6", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser,    itm_kozak_civil_jupan_b,      itm_kozak_jupan_na_kolchuge,       itm_kozak_boots,      itm_kozak_boots,    itm_serduk_shapka, itm_toporik_good],    knight_attrib_2,wp(190),knight_skills_2, 0x0000000fc00004513ecc72551cc55af300000000001eb6d20000000000000000],
  ["knight_5_17", "Colonel Filon Jalaliy","knight 5 7", tf_hero, 0, reserved,  fac_kingdom_5, [itm_steppe_horse_b,     itm_kozak_civil_jupan_a,       itm_kolchuga,   itm_kozak_boots,    itm_kozak_boots,       itm_serduk_shapka,  itm_chekan_good],     knight_attrib_3,wp(200),knight_skills_3, 0x000000075d0405113acc9478d44e38a400000000001db3630000000000000000],
  ["knight_5_18", "Company Commander Ivan Hmara","knight 5 8", tf_hero, 0, reserved,  fac_kingdom_5, [itm_courser, itm_kozak_civil_jupan_b,     itm_serduk_jupan,    itm_kozak_boots,      itm_kozak_boots,    itm_poland_mehova_shapka_s_perom,       itm_pernach],    knight_attrib_4,wp(200),knight_skills_4, 0x000000023f00109204a34e26e2d1d56e00000000001dab380000000000000000],
  ["knight_5_19", "Company Commander Lavrin Sinonos","knight 5 9", tf_hero, 0, reserved,  fac_kingdom_5, [itm_steppe_horse_b,     itm_kozak_civil_jupan_a,     itm_kolchuga,   itm_kozak_boots,    itm_kozak_boots,       itm_kozacka_shapka_s_misurkoy, itm_kozak_good_shablya],   knight_attrib_4,wp(200),knight_skills_4, 0x00000007870c550e52ec2a45164d42e900000000001d431b0000000000000000],
  ["knight_5_20", "Company Commander Les' Gritsenko","knight 5 0", tf_hero, 0, reserved,  fac_kingdom_5, [itm_steppe_horse_b,     itm_kozak_civil_jupan_b,  itm_kozak_jupan_na_kolchuge,     itm_kozak_boots,  itm_kozak_boots,       itm_serduk_shapka, itm_toporik_rich],  knight_attrib_3,wp(170),knight_skills_3, 0x00000003bf04061136db6db6db6db6db00000000001db6db0000000000000000],

  ["kingdom_1_pretender", "Janusz Radziwill","Kingdom 1 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_saddle_horse_c,   itm_dobrotna_svitka_c,  itm_good_sapogi,   itm_good_sapogi,      itm_kolchuga_panzernika,      itm_infantry_gloves,     itm_poland_mehova_shapka, itm_sablya_a],          lord_attrib,wp(175),knows_lord_1, 0x0000000d9f0c35170a2295e58fc0413200000000001daae80000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender", "Stepan Razin","Kingdom 2 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_mosk_sermyaga,      itm_old_cavalry_boots,              itm_old_cavalry_boots,              itm_moskow_bahter_a,       itm_palitza,       itm_streletz_shapka_c],    lord_attrib,wp(200),knows_lord_1, 0x0000000adb0422ce375bbab95f206f3a00000000001cd7700000000000000000],
#had his patrimony falsified

  ["kingdom_3_pretender", "Mehmed Giray","Kingdom 3 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_ttr_civil_b,             itm_sapogi,              itm_sapogi,           itm_tatar_kolcha,         itm_sablya_turk_b,              itm_tatar_han_helmet],      lord_attrib,wp(200),knows_lord_1, 0x0000000bff043200287673b75a6ee4f300000000001db2e30000000000000000],
#of the family

  ["kingdom_4_pretender", "Former Queen Christina","Kingdom 4 Lord",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_rich_baba_swd_2,    itm_janissary_tapki,              itm_janissary_tapki,                 itm_rich_baba_swd_2,           itm_good_shpaga_d],            lord_attrib,wp(100),knows_lord_1, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender", "Ivan Barabash","Kingdom 5 Lord",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_kozak_civil_jupan_b,             itm_kozak_boots,              itm_kozak_boots,   itm_kozak_jupan_na_kolchuge,           itm_pernach,         itm_reestr_shapka],         lord_attrib,wp(175),knows_lord_1, 0x0000000dc01010523b1349e6dbc6a69b00000000001e26c90000000000000000],
#republican

  
#  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[        itm_tab_shield_small_round_c],          lord_attrib,wp(220),knows_lord_1, 0x0000000dc010148a3b1349e6dbc6a69b00000000001e26c90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members
  ["knight_1_1_wife", "Panna Olena Billewicz","knight 1 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [   itm_blue_hose,   itm_rich_baba_pol_2 ,   itm_pol_bab_hat_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["knight_2_1_wife", "Noblewoman Alina","knight 2 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_blue_hose,  itm_rich_baba_mosk_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["knight_3_1_wife", "Alsu","knight 3 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [  itm_blue_hose,   itm_rich_baba_ttr_1      ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["knight_4_1_wife", "Lady Agnes","knight 4 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [   itm_blue_hose,   itm_rich_baba_swd_1 ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_5_1_wife", "Pani Marina","knight 5 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [  itm_blue_hose,    itm_rich_baba_pol_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],

  ["knight_1_2_wife", "Panna Annie Fastreacher","knight 1 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [  itm_blue_hose,    itm_rich_baba_pol_3 ,   itm_pol_bab_hat_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["knight_2_2_wife", "Noblewoman Marfa","knight 2 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [ itm_blue_hose,     itm_rich_baba_mosk_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["knight_3_2_wife", "Bariya","knight 3 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_blue_hose,    itm_rich_baba_ttr_2   ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["knight_4_2_wife", "Lady Annel","knight 4 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [   itm_blue_hose,   itm_rich_baba_swd_2 ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_5_2_wife", "Pani Galina","knight 5 1 wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [  itm_blue_hose,    itm_rich_baba_pol_4],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],

  ["knight_1_1_daughter", "Panna Agneshka","knight 1 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [   itm_blue_hose, itm_rich_baba_pol_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_2_1_daughter", "Noblewoman Arina","knight 2 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_blue_hose,  itm_rich_baba_mosk_3], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["knight_3_1_daughter", "Nadira","knight 3 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [  itm_blue_hose, itm_rich_baba_ttr_2     ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["knight_4_1_daughter", "Lady Cecilia","knight 4 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [ itm_blue_hose,   itm_rich_baba_swd_3 ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_5_1_daughter", "Pani Hanna","knight 5 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [itm_blue_hose, itm_rich_baba_pol_3], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],

  ["knight_1_2_daughter", "Panna Angela","knight 1 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [  itm_blue_hose,  itm_rich_baba_pol_1], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["knight_2_2_daughter", "Noblewoman Maria","knight 2 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_blue_hose,   itm_rich_baba_mosk_2 ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["knight_3_2_daughter", "Gulnur","knight 3 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [   itm_blue_hose,  itm_rich_baba_ttr_1  ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["knight_4_2_daughter", "Lady Freja","knight 4 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [  itm_blue_hose,  itm_rich_baba_swd_4], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["knight_5_2_daughter", "Pani Irina","knight 5 1 daughter",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [itm_blue_hose, itm_rich_baba_pol_2], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [  ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [   ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [ ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [     ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [           ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [         ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               ],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                            ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                          ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [              ], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,                         ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,                 itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,                itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,                            itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,                                                     ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,                                           ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,               itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,                  ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,                                                    ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,              itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,                       itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,                                                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,                                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,                                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,                       itm_woolen_hose,         ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,                                         ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,                     itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,                                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,                           itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,                                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "Town 1 Seneschal","Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b,itm_parik], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "Town 2 Seneschal","Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_swed_civil_a,itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "Town 3 Seneschal","Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "Town 4 Seneschal","Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_b,itm_poland_shapka],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "Town 5 Seneschal","Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_kozak_civil_jupan_b,itm_kozak_shapka_d],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "Town 6 Seneschal","Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_dobrotna_svitka_a, itm_poland_mehova_shapka_s_perom],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "Town 7 Seneschal","Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_c,itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "Town 8 Seneschal","Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_mosk_civil_b,itm_streletz_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "Town 9 Seneschal","Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "Town 10 Seneschal","Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_a, itm_tatar_nogay_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "Town 11 Seneschal","Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_mosk_civil_a, itm_moskowit_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "Town 12 Seneschal","Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli,itm_swed_civil_a, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "Town 13 Seneschal","Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_mosk_civil_b, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "Town 14 Seneschal","Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b,itm_tatar_man_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "Town 15 Seneschal","Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_kozak_civil_jupan_b, itm_kozak_shapka_c],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "Town 16 Seneschal","Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_b,itm_poland_shapka],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "Town 17 Seneschal","Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b, itm_tatar_nogay_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "Town 18 Seneschal","Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_tatar_halat_pure_a,itm_tatar_man_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_seneschal", "Castle 1 Seneschal","Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "Castle 2 Seneschal","Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "Castle 3 Seneschal","Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "Castle 4 Seneschal","Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "Castle 5 Seneschal","Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "Castle 6 Seneschal","Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "Castle 7 Seneschal","Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "Castle 8 Seneschal","Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "Castle 9 Seneschal","Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "Castle 10 Seneschal","Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "Castle 11 Seneschal","Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "Castle 2 Seneschal","Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "Castle 3 Seneschal","Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "Castle 4 Seneschal","Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "Castle 5 Seneschal","Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "Castle 6 Seneschal","Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "Zaporozhian Cossack","Zaporozhian Cossack", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "Castle 8 Seneschal","Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "Castle 9 Seneschal","Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "Castle 20 Seneschal","Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "Castle 11 Seneschal","Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "Castle 2 Seneschal","Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "Castle 3 Seneschal","Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "Castle 4 Seneschal","Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "Castle 5 Seneschal","Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "Castle 6 Seneschal","Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "Castle 7 Seneschal","Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "Castle 8 Seneschal","Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "Castle 9 Seneschal","Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "Castle 20 Seneschal","Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "Castle 11 Seneschal","Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "Castle 2 Seneschal","Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "Castle 3 Seneschal","Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "Castle 4 Seneschal","Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "Castle 5 Seneschal","Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "Castle 6 Seneschal","Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "Castle 7 Seneschal","Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "Castle 8 Seneschal","Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "Castle 9 Seneschal","Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "Castle 20 Seneschal","Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Arena Masters
  ["town_1_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[ ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[     ],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[ ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[     ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[     ],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[    ], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[    ],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[   ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[    ], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[   ],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[   ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[   ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[   ],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[   ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[   ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[    ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[   ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master", "Tournament Master","Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[    ],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[         ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[               ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_evropa_pehot_tufli, itm_swed_civil_a, itm_evropa_shlapa_b ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_botinki, itm_swed_civil_b, itm_parik],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_sapogi,  itm_kozak_civil_jupan_a, itm_kozak_shapka_d],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_good_sapogi,itm_dobrotna_svitka_a, itm_poland_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_sapogi, itm_kozak_civil_jupan_b, itm_kozak_shapka_b],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_selo_boots, itm_poland_svitka_a,itm_poland_mehova_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots,itm_dobrotna_svitka_b, itm_poland_mehova_shapka_s_perom],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi, itm_mosk_civil_b, itm_streletz_shapka_b],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_sapogi, itm_mosk_civil_a,itm_streletz_shapka_c],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_nogay_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots, itm_mosk_civil_a, itm_streletz_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_botinki, itm_evropa_odejda_sela_b,itm_evropa_shlapa],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi,  itm_mosk_civil_a,  itm_moskowit_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_selo_boots, itm_tatar_halat_pure_b,itm_tatar_nogay_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_sapogi, itm_kozak_civil_jupan_a,itm_kozak_shapka_c],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi,itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer", "Armorer","Armorer",  tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[ itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi, itm_evropa_odejda_sela_b, itm_parik],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_botinki, itm_swed_civil_b, itm_evropa_kava_shlapa],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_selo_boots, itm_poland_svitka_a,itm_kozak_shapka_b],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots, itm_kozak_civil_jupan_a, itm_kozak_shapka_c],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_good_sapogi,itm_dobrotna_svitka_c,itm_poland_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|tf_is_merchant, 0, 0, fac_commoners,[itm_good_sapogi, itm_mosk_sermyaga,itm_streletz_shapka_b],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots, itm_mosk_sermyaga,  itm_moskowit_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_kozak_boots,itm_mosk_sermyaga,  itm_streletz_shapka_c],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_evropa_pehot_tufli,itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa_c],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi, itm_mosk_civil_a,itm_streletz_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_bayrak_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_good_sapogi,itm_dobrotna_svitka_a, itm_poland_good_shapka],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[ itm_sapogi,  itm_tatar_halat_pure_b, itm_tatar_bayrak_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith", "Weaponsmith","Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_kozak_boots, itm_tatar_halat_pure_b,itm_tatar_nogay_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_evropa_pehot_tufli, itm_swed_civil_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_sapogi, itm_swed_civil_b],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_sapogi, itm_kozak_jupan],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_4_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_kozak_boots,itm_dobrotna_svitka_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_sapogi,itm_poland_svitka_b],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_6_tavern|entry(9),0,   fac_commoners,[ itm_sapogi, itm_dobrotna_svitka_c],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_7_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_selo_boots,itm_poland_svitka_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_8_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_selo_boots, itm_mosk_sermyaga],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_sapogi,itm_mosk_sermyaga],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_10_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_kozak_boots, itm_tatar_halat_pure_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_11_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_11_tavern|entry(9),0,  fac_commoners,[ itm_sapogi,itm_mosk_sermyaga],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_12_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[ itm_botinki, itm_swed_civil_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_sapogi,itm_mosk_sermyaga],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_14_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[ itm_kozak_boots, itm_tatar_halat_pure_b],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_15_tavern|entry(9),0,  fac_commoners,[ itm_selo_boots, itm_kozak_jupan_b],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_16_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[ itm_sapogi, itm_poland_svitka_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_good_sapogi,itm_tatar_halat_pure_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_18_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_kozak_boots, itm_tatar_halat_pure_b],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

#Goods Merchants

  ["town_1_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_evropa_pehot_tufli, itm_swed_civil_a, itm_evropa_shlapa_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [ itm_sapogi, itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [ itm_kozak_boots, itm_poland_svitka_b,itm_kozak_shapka_c],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_selo_boots, itm_dobrotna_svitka_c,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_kozak_boots, itm_poland_svitka_b, itm_kozak_shapka_d],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_selo_boots,itm_dobrotna_svitka_a, itm_poland_mehova_shapka_s_perom],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [ itm_selo_boots,itm_poland_svitka_a,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [ itm_sapogi, itm_mosk_civil_a,itm_streletz_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_good_sapogi, itm_mosk_civil_b, itm_streletz_shapka_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_good_sapogi,itm_ttr_civil_a,itm_tatar_man_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [ itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant", "Merchant","Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_merchant", "Merchant","Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_kozak_boots,itm_mosk_civil_b,itm_streletz_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [ itm_kozak_boots, itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [ itm_kozak_boots,  itm_kozak_civil_jupan_b,itm_kozak_shapka_c],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant", "Merchant","Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_good_sapogi, itm_dobrotna_svitka_b, itm_poland_good_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_merchant", "Merchant","Merchant",tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [ itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_merchant", "Merchant","Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_good_sapogi, itm_tatar_halat_pure_b, itm_tatar_bayrak_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],

  ["salt_mine_merchant", "Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [ ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant", "Horse Merchant","Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_horse_merchant", "Horse Merchant","Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[ itm_sapogi, itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa_c],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant", "Horse Merchant","Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[ itm_kozak_boots, itm_poland_svitka_a, itm_poland_shapka],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant", "Horse Merchant","Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[ itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant", "Horse Merchant","Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,    0, 0, fac_commoners,[itm_good_sapogi, itm_kozak_civil_jupan_a, itm_kozak_shapka_d],   def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_horse_merchant", "Horse Merchant","Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[ itm_selo_boots,itm_dobrotna_svitka_a, itm_poland_good_shapka],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant", "Horse Merchant","Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant", "Horse Merchant","Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_sapogi, itm_mosk_civil_a,itm_streletz_shapka_b],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant", "Horse Merchant","Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_kozak_boots,itm_mosk_civil_a,itm_streletz_shapka_b],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant", "Horse Merchant","Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[itm_selo_boots, itm_ttr_civil_a, itm_tatar_man_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_horse_merchant", "Horse Merchant","Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_good_sapogi,itm_mosk_sermyaga, itm_moskowit_shapka],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant", "Horse Merchant","Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[ itm_sapogi, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant", "Horse Merchant","Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_kozak_boots, itm_mosk_sermyaga, itm_moskowit_shapka],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant", "Horse Merchant","Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[ itm_sapogi, itm_tatar_halat_pure_b, itm_tatar_nogay_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_horse_merchant", "Horse Merchant","Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[ itm_kozak_boots, itm_poland_svitka_b, itm_poland_shapka],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant", "Horse Merchant","Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant", "Horse Merchant","Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_good_sapogi,itm_tatar_halat_pure_a, itm_tatar_nogay_hat],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant", "Horse Merchant","Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,  0, 0, fac_commoners,[ itm_kozak_boots,itm_tatar_halat_pure_b,itm_tatar_man_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],


#Town Mayors      
  ["town_1_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_a, itm_evropa_kava_shlapa_b], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_kava_shlapa_c],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_civil_jupan_b, itm_kozak_shapka_d], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_civil_jupan_b, itm_kozak_shapka_b],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_c,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka_b], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi, itm_ttr_civil_b, itm_tatar_man_hat],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_botinki, itm_swed_civil_a, itm_parik], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_a, itm_kozak_shapka_d],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi,  itm_dobrotna_svitka_b,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Mayor","Mayor", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi, itm_ttr_civil_a,  itm_tatar_bayrak_hat],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


   #Castle elders
   ["castle_1_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
   ["castle_2_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_3_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_4_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_5_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_6_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_7_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_8_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_9_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_10_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_11_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_12_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_13_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_14_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_15_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_16_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_17_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_18_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_19_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
   ["castle_20_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_21_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_22_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_23_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_24_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_25_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_26_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_27_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_28_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_29_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_30_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_31_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_32_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_33_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_34_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_35_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_36_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_37_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_38_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_39_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
   ["castle_40_elder", "Mayor","Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],  

    ["town_1_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b,itm_parik], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_swed_civil_a,itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_b,itm_poland_shapka],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_kozak_civil_jupan_b,itm_kozak_shapka_d],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_dobrotna_svitka_a, itm_poland_mehova_shapka_s_perom],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_c,itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_mosk_civil_b,itm_streletz_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_a, itm_tatar_nogay_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_mosk_civil_a, itm_moskowit_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli,itm_swed_civil_a, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_mosk_civil_b, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b,itm_tatar_man_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_kozak_civil_jupan_b, itm_kozak_shapka_c],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_b,itm_poland_shapka],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b, itm_tatar_nogay_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_tatar_halat_pure_a,itm_tatar_man_hat],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["castle_1_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_trade_guild_master", "Trade Guild Master","Trade Guild Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

  ["town_1_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash], def_attrib|level(20),wp(200),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash],   def_attrib|level(20),wp(200),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach], def_attrib|level(20),wp(200),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],     def_attrib|level(20),wp(200),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach],   def_attrib|level(20),wp(200),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],   def_attrib|level(20),wp(200),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],   def_attrib|level(20),wp(200),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],   def_attrib|level(20),wp(200),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza], def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],     def_attrib|level(20),wp(200),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],   def_attrib|level(20),wp(200),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash], def_attrib|level(20),wp(200),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],   def_attrib|level(20),wp(200),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],     def_attrib|level(20),wp(200),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach],     def_attrib|level(20),wp(200),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],     def_attrib|level(20),wp(200),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],     def_attrib|level(20),wp(200),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],     def_attrib|level(20),wp(200),knows_common, 0x000000000004728b01c293c694944b05],

  ["castle_1_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],    def_attrib|level(20),wp(200),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],   def_attrib|level(20),wp(200),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a], def_attrib|level(20),wp(200),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash],   def_attrib|level(20),wp(200),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza], def_attrib|level(20),wp(200),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a], def_attrib|level(20),wp(200),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash],   def_attrib|level(20),wp(200),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a], def_attrib|level(20),wp(200),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach],   def_attrib|level(20),wp(200),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach], def_attrib|level(20),wp(200),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza], def_attrib|level(20),wp(200),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],   def_attrib|level(20),wp(200),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a], def_attrib|level(20),wp(200),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach],   def_attrib|level(20),wp(200),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a], def_attrib|level(20),wp(200),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza], def_attrib|level(20),wp(200),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash],   def_attrib|level(20),wp(200),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d,itm_pernach], def_attrib|level(20),wp(200),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash],   def_attrib|level(20),wp(200),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kolchuga_panzernika, itm_poland_good_shapka,itm_sablya_a],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_infantry_gloves, itm_kirasa_rich, itm_morion_perfect,itm_scott_palash], def_attrib|level(20),wp(200),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza],   def_attrib|level(20),wp(200),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],    def_attrib|level(20),wp(200),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi, itm_moskow_reytar_armor, itm_new_line_helmet,itm_palitza], def_attrib|level(20),wp(200),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_garrison_officer", "Garrison Commander","Garrison Commander", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[itm_kalmyk_boots, itm_tatar_kolcha, itm_tatar_misurka_rich,itm_sablya_tatar_a],   def_attrib|level(20),wp(200),knows_common, 0x00000000000440c601e1cd45cfb38550],

#Village stores
  ["village_1_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_moskowit_postoli_b,itm_poland_svitka_a,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_prostoy_jupan,itm_ukrine_prosta_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_evropa_odejda_sela,itm_evropa_kava_shlapa ],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_poland_svitka_a,itm_ukrine_prosta_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_evropa_odejda_sela_b,itm_evropa_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_prostoy_jupan,itm_poland_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_mosk_sermyaga,itm_moskowit_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_man_hat ],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_prostoy_jupan_b,itm_kozak_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_moskowit_postoli,itm_poland_svitka_b,itm_streletz_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_pure_streletzkiy_mundir_spear,itm_streletz_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_sapogi,itm_poland_svitka_a,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_mosk_sermyaga,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_poland_svitka_b,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_a, itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_pure_streletzkiy_mundir_spear,itm_streletz_shapka_b ],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_poland_svitka_b,itm_poland_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_mosk_sermyaga,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_pure_streletzkiy_mundir_spear,itm_moskowit_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_prostoy_jupan,itm_kozak_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_prostoy_jupan_b,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_tatar_halat_pure_a,itm_tatar_bayrak_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_mosk_sermyaga,itm_kozak_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_ukrine_prosta_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_man_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_evropa_odejda_sela,itm_evropa_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_evropa_odejda_sela_b,itm_evropa_shlapa_b],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_evropa_odejda_sela,itm_evropa_kava_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_poland_svitka_a,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_poland_svitka_b,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_evropa_odejda_sela_b,itm_evropa_shlapa_b],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_evropa_odejda_sela,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_prostoy_jupan,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_prostoy_jupan,itm_kozak_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_bayrak_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_tatar_bayrak_hat ],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_tatar_halat_pure_a,itm_tatar_man_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_poland_svitka_b,itm_poland_mehova_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_prostoy_jupan_b,itm_kozak_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_prostoy_jupan_b,itm_poland_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_mosk_sermyaga,itm_moskowit_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots, itm_evropa_odejda_sela,itm_evropa_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_sapogi,itm_prostoy_jupan_b,itm_kozak_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_b,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_a,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_prostoy_jupan,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_evropa_odejda_sela_b,itm_evropa_shlapa_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_mosk_sermyaga,itm_streletz_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_prostoy_jupan_b,itm_kozak_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_evropa_odejda_sela,itm_evropa_kava_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_pure_streletzkiy_mundir_spear,itm_moskowit_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_a,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b, itm_prostoy_jupan_b,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_prostoy_jupan,itm_kozak_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder", "Zamoshye Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_mosk_sermyaga,itm_poland_mehova_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_poland_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_prostoy_jupan,itm_kozak_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_evropa_odejda_sela_b,itm_evropa_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_a,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_poland_svitka_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_poland_svitka_b,itm_poland_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_prostoy_jupan_b,itm_kozak_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_mosk_sermyaga,itm_streletz_shapka_b],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_b,itm_streletz_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_tatar_halat_pure_a,itm_tatar_man_hat ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_evropa_odejda_sela,itm_evropa_shlapa_b ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_prostoy_jupan,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_prostoy_jupan_b,itm_ukrine_prosta_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_poland_svitka_b,itm_streletz_shapka_c],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_selo_boots,itm_evropa_odejda_sela,itm_evropa_shlapa_b],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_poland_svitka_a,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli,itm_prostoy_jupan,itm_kozak_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_prostoy_jupan,itm_kozak_prosta_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_prostoy_jupan_b,itm_poland_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_moskowit_postoli_b,itm_pure_streletzkiy_mundir_spear,itm_poland_shapka ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sapogi,itm_evropa_odejda_sela,itm_evropa_kava_shlapa],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_tatar_halat_pure_b,itm_tatar_bayrak_hat ],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[ itm_sapogi,itm_prostoy_jupan_b,itm_kozak_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder", "Village Elder","village 1 elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_selo_boots,itm_prostoy_jupan_b,itm_ukrine_prosta_shapka],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end", "merchants end","merchants end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[    ], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     ], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[           itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     ],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[          itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[    ],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     ], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ ],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ ], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[      itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[       itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[      ],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a", "temp array a","temp array a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b", "temp array b","temp array b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c", "temp array c","temp array c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts", "stack selection amounts","stack selection amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids", "stack selection ids","stack selection ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types", "notification menu types","notification menu types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1", "notification menu var1","notification menu var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2", "notification menu var2","notification menu var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["banner_background_color_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

  ["local_merchant", "Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, 0,0, fac_commoners,
   [itm_sablya_b, itm_good_sapogi, itm_dobrotna_svitka_b, itm_poland_mehova_shapka_s_perom],
   def_attrib|level(15),wp(140),knows_power_strike_5, merchant_face_1, merchant_face_2],
  ["tax_rebel", "Peasant Rebel","Peasant Rebels",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_stones, itm_sablya_b, itm_good_sapogi, itm_dobrotna_svitka_b, itm_poland_mehova_shapka_s_perom],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant", "Peasant","Peasants",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_stones, itm_sablya_b, itm_good_sapogi, itm_dobrotna_svitka_b, itm_poland_mehova_shapka_s_perom],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive", "Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [ itm_selo_boots, itm_pilgrim_disguise, itm_throwing_daggers,itm_toporik_rich, itm_klevetz, itm_pehot_palash],
   def_attrib|str_20|agi_20|level(25),wp(250),knows_common|knows_power_throw_5|knows_power_strike_5|knows_ironflesh_10,man_face_middle_1, man_face_old_2],
  ["spy", "Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_pilgrim_disguise, itm_selo_boots, itm_pilgrim_hood],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
  ["oim_monfor", "Jaques de Clermont","Montfort", tf_hero|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_swed_civil_a, itm_good_cavalry_botforts, itm_good_shpaga_d],
   def_attrib|str_22|agi_26|level(26),wp(250),knows_common|knows_power_strike_8|knows_ironflesh_10,0x000000018e0034db2acc70bd118f371500000000001ca6dd0000000000000000],
  ["oim_trakai_ksendz", "Priest","Peasant Rebels",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_selo_boots, itm_robe],
   def_attrib|level(5),wp(50),knows_common, swadian_face_middle_1, swadian_face_old_2],
  ["oim_polish_taver_visitor", "Pub Haunter","Peasant Rebels",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sablya_c, itm_kozak_boots, itm_dobrotna_svitka_c, itm_poland_mehova_shapka],
   def_attrib|level(8),wp(90),knows_common,swadian_face_young_1, swadian_face_old_2],
  ["oim_tatarin_zolotarenko", "Tatar","Tatar",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_sapogi, itm_tatar_halat_b, itm_tatar_man_hat, itm_sablya_tatar_a],
   def_attrib|level(10),wp(100),knows_common,khergit_face_middle_1, khergit_face_middle_2],	 

  ["oim_polish_lord", "Swedish Officer","{!}Do not translate",tf_hero|tf_guarantee_armor|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_kirasa_c, itm_evropa_guard_shlapa, itm_pehot_palash, itm_cavalry_botforts],
   str_16|agi_14|int_12|cha_12|level(20),wp(250),
   knows_ironflesh_6|knows_power_strike_6|knows_riding_5, swadian_face_middle_1, swadian_face_older_2],	 

  ["oim_zagloba_qst", "Onufry Zagloba","{!}Do not translate",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_kolchuga_panzernika, itm_misurka_s_barmizoy_c, itm_sapogi, itm_sablya_a,itm_saddle_horse],
   str_12|agi_5|int_12|cha_12|level(10),wp(150),
   knows_ironflesh_10|knows_power_strike_4|knows_riding_2,
   0x0000000e600013d1064969df62c37a4f00000000001f14350000000000000000],	
  #old man Black Getman qst 
  ["oim_old_man_qst", "Old Man","{!}Do not translate",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_kozak_boots, itm_kozak_jupan, itm_kozak_good_shablya],
   def_attrib|level(12),wp(120),knows_common, rhodok_face_old_1, rhodok_face_older_2],	

  ["oim_killer_qst", "Gentryman","{!}Do not translate",tf_mounted|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sablya_b,itm_sablya_a,itm_sablya_c,itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_old_cavalry_boots,itm_poland_mehova_shapka,itm_poland_mehova_shapka_s_perom,itm_poland_good_shapka],
   def_attrib|level(10),wp_melee(100)|wp_crossbow(100)|wp_archery(20),knows_common|knows_riding_3|knows_ironflesh_1|knows_power_strike_1,swadian_face_middle_1, swadian_face_old_2],
 
   
  ["oim_getman_pafnutiy", "Pafnuty","{!}Do not translate",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_selo_boots, itm_robe],
   def_attrib|level(15),wp(100),knows_common,vaegir_face_middle_1, vaegir_face_old_2],

  #heroes for  
  ["oim_dmitriy_yevangelik", "Gerasim Evangelic","{!}Do not translate",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_kozak_boots, itm_serduk_jupan, itm_kozak_good_shablya],
   str_10|agi_8|level(15),wp(140),knows_common,rhodok_face_older_1, rhodok_face_older_2],
  
  #trp_volhv
  ["volhv","Soothsayer","volhv",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
  [itm_pilgrim_disguise, itm_moskowit_postoli_b, itm_quarter_staff],
   def_attrib|level(15),wp(100),knows_common,vaegir_face_older_1, vaegir_face_older_2],

  ["halberdier", "Halberdier","Halberdiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_botinki,itm_poland_uniforma_german_line,itm_morion_good,itm_alebarda],
   str_11|agi_7|level(15),wp_melee(125),knows_common|knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_4,mercenary_face_1, mercenary_face_2],

  ["moskov_straj", "Guard","Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,
   [itm_berdish,itm_new_line_uniform,itm_sapogi,itm_new_line_helmet],
    str_10|agi_7|level(15),wp_melee(115),knows_common|knows_ironflesh_5|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],  
   
    #OiM tavern fights code
  ["oim_tavern_visitor_rp", "Pub Visitor","Pub Visitor",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_sablya_pure_a,itm_sablya_pure_b, itm_sablya_pure_c, itm_sablya_pure_d, itm_selo_boots, itm_sapogi, itm_poland_svitka_a, itm_poland_svitka_b, itm_poland_shapka, itm_poland_mehova_shapka,
    itm_poland_army_hat_simple],
     str_9|agi_9|level(10),wp_melee(100),knows_common|knows_ironflesh_5|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],  

  ["oim_tavern_visitor_mc", "Pub Visitor","Pub Visitor",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_moskowit_postoli, itm_moskowit_postoli_b, itm_mosk_sermyaga, itm_pure_streletzkiy_mundir_spear, itm_moskowit_shapka, itm_sablya_pure_c, itm_rusty_toporik, itm_plotnik_toporik, itm_plotnik_topor],
     str_9|agi_9|level(10),wp_melee(100),knows_common|knows_ironflesh_5|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],  

  ["oim_tavern_visitor_swed", "Pub Visitor","Pub Visitor",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_botinki, itm_evropa_pehot_tufli, itm_evropa_odejda_sela, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa, itm_evropa_kava_shlapa_b, itm_evropa_kava_shlapa_c, itm_evropa_shlapa, itm_evropa_shlapa_b,
    itm_prosta_shpaga, itm_prosta_shpaga_b, itm_prosta_shpaga_c],
     str_9|agi_9|level(10),wp_melee(100),knows_common|knows_ironflesh_5|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],  

  ["oim_tavern_visitor_tatar", "Pub Visitor","Pub Visitor",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_selo_boots, itm_sapogi, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_tatar_halat_a, itm_tatar_halat_b, itm_tatar_man_hat, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_yatagan_a,
    itm_sablya_turk_pure_a, itm_sablya_turk_pure_b, itm_sablya_turk_pure_c],
    str_9|agi_9|level(10),wp_melee(100),knows_common|knows_ironflesh_5|knows_power_strike_3,khergit_face_middle_1, khergit_face_older_2],  

  ["oim_tavern_visitor_cossack", "Pub Visitor","Pub Visitor",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_selo_boots, itm_sapogi, itm_prostoy_jupan, itm_prostoy_jupan_b, itm_kozak_jupan, itm_kozak_jupan_b, itm_kozak_prosta_shapka, itm_kozak_shapka, itm_kozak_shapka_b, itm_sablya_pure_d, itm_sablya_turk_pure_c,
    itm_kozak_shablya],
     str_9|agi_9|level(10),wp_melee(100),knows_common|knows_ironflesh_5|knows_power_strike_3,rhodok_face_middle_1, rhodok_face_older_2],  
 
  ["eleonora", "Eleanor","Eleanor",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [      itm_rich_baba_mosk_3,   itm_blue_hose, itm_selo_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],

  ["alevtina", "Alevtina","Alevtina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [      itm_rich_baba_ttr_1, itm_blue_hose, itm_selo_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  
  #oim_guild_master
  ["oim_guild_master","{!}Do not translate","{!}Do not translate",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [      itm_pure_baba_swd_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],  

  #temp!
  ["oim_guild_master_end", "{!}Do not translate","{!}Do not translate",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [      itm_pure_baba_swd_1],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],  
  
  ["oim_caravan_master", "Caravan Driver","Caravan Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_saddle_horse_b,itm_saddle_horse,itm_saddle_horse_c,itm_cavalry_boots,itm_kozak_boots,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,
    itm_kozak_civil_jupan_a,itm_kozak_civil_jupan_b,itm_mosk_civil_a,itm_mosk_civil_b,itm_sablya_b,itm_sablya_c,itm_sablya_turk_b],
   def_attrib|level(5),wp(100),knows_common|knows_riding_4|knows_ironflesh_4,mercenary_face_1, mercenary_face_2],
  
  
  ["oim_rich_visitor", "Rich Townsman","Rich Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_outlaws, [itm_sablya_d,itm_sablya_a,itm_good_pistol_c,itm_bolts,itm_kozak_boots,itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_poland_shapka,
    itm_poland_mehova_shapka,], str_12|agi_10|level(15),wp_melee(150),knows_ironflesh_5|knows_power_strike_4|knows_weapon_master_8,swadian_face_middle_1, swadian_face_old_2],  
	
  ["spy_partner", "Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_courser,itm_leather_gloves,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots],
   def_attrib|agi_11|level(10),wp(100),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_knife,itm_pitch_fork,itm_stones],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword, itm_saddle_horse],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_robe, ],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],

 #New_ Merchants 
    ["mercanary_captain_tatars", "Mercenary Captain","Mercenary Captains",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_helmet,0,reserved,fac_commoners,
   [itm_round_shield_steel_b,itm_kalmyk_boots,itm_tatar_yushman,itm_tatar_helmet_a,itm_yatagan_rich],
    def_attrib|level(25),wp(200),knows_common,khergit_face_middle_1, khergit_face_older_2], 
   
   ["mercanary_captain_kozaks", "Cossack Ataman","Cossack Atamans",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_helmet,0,reserved,fac_commoners,
   [itm_kozak_boots,itm_kozak_jupan_usileniy,itm_kozak_shapka_c,itm_pernach],
    def_attrib|level(25),wp(200),knows_common,rhodok_face_middle_1, rhodok_face_older_2], 
   
   ["mercanary_captain_polyak", "Mercenary Captain","Mercenary Captains",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_helmet,0,reserved,fac_commoners,
   [itm_good_sapogi,itm_kolchuga_panzernika,itm_poland_mehova_shapka_s_perom,itm_sablya_a],
    def_attrib|level(25),wp(200),knows_common,swadian_face_middle_1, swadian_face_older_2], 
     
   ["mercanary_captain_shved", "Mercenary Captain","Mercenary Captains",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_helmet,0,reserved,fac_commoners,
   [itm_infantry_boots,itm_kirasa,itm_morion_good,itm_good_shpaga_b],
    def_attrib|level(25),wp(200),knows_common,nord_face_middle_1, nord_face_older_2], 	  
  
   ["mercanary_captain_moskov", "Mercenary Captain","Mercenary Captains",tf_hero|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_horse|tf_guarantee_helmet,0,reserved,fac_commoners,
   [itm_sapogi,itm_moskow_reytar_armor,itm_new_line_helmet,itm_sablya_d],
    def_attrib|level(25),wp(200),knows_common,vaegir_face_middle_1, vaegir_face_older_2],  
   
    # ======= 0
   ["tatar_merch_novice_infantry", "Tatar mercenary infantryman (recruit)","Tatar mercenary infantry (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_7|agi_8|level(5),wp_melee(67)|wp_crossbow(30)|wp_archery(41),knows_weapon_master_2|knows_athletics_3|knows_riding_1|knows_power_draw_1,khergit_face_middle_1, khergit_face_older_2],
   
   ["tatar_merch_regular_infantry", "Tatar mercenary infantryman (experienced)","Tatar mercenary infantry (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_9|level(10),wp_melee(82)|wp_crossbow(41)|wp_archery(52),knows_weapon_master_3|knows_ironflesh_1|knows_athletics_3|knows_power_strike_1|knows_riding_1|knows_power_draw_2,khergit_face_middle_1, khergit_face_older_2],
   
    ["tatar_merch_veteran_infantry", "Tatar mercenary infantryman (veteran)","Tatar mercenary infantry (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_10|level(15),wp_melee(97)|wp_crossbow(52)|wp_archery(70),knows_weapon_master_4|knows_ironflesh_2|knows_athletics_3|knows_power_strike_2|knows_riding_2|knows_power_draw_3,khergit_face_middle_1, khergit_face_older_2],
		
   ["tatar_merch_champion_infantry", "Tatar mercenary infantryman (elite)","Tatar mercenary infantry (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_11|level(20),wp_melee(113)|wp_crossbow(64)|wp_archery(75),knows_weapon_master_5|knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_riding_2|knows_power_draw_4,khergit_face_middle_1, khergit_face_older_2],
   # ======= 4
    
	["tatar_merch_novice_archer", "Tatar mercenary rifleman (recruit)","Tatar mercenary riflemen (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_6|agi_9|level(5),wp_melee(30)|wp_crossbow(37)|wp_archery(64),knows_weapon_master_1|knows_athletics_2|knows_riding_1|knows_power_draw_2|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
   
   ["tatar_merch_regular_archer", "Tatar mercenary rifleman (experienced)","Tatar mercenary riflemen (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_7|agi_10|level(10),wp_melee(45)|wp_crossbow(49)|wp_archery(75),knows_weapon_master_1|knows_athletics_2|knows_riding_1|knows_power_draw_3|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
    
	["tatar_merch_veteran_archer", "Tatar mercenary rifleman (veteran)","Tatar mercenary riflemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_11|level(15),wp_melee(60)|wp_crossbow(60)|wp_archery(86),knows_weapon_master_2|knows_athletics_2|knows_riding_2|knows_power_draw_4|knows_horse_archery_2,khergit_face_middle_1, khergit_face_older_2],
    
	["tatar_merch_champion_archer", "Tatar mercenary rifleman (elite)","Tatar mercenary riflemen (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_12|level(20),wp_melee(75)|wp_crossbow(71)|wp_archery(97),knows_weapon_master_3|knows_ironflesh_1|knows_athletics_2|knows_riding_2|knows_power_draw_5|knows_horse_archery_2,khergit_face_middle_1, khergit_face_older_2],
        
  # ======= 8
	["tatar_merch_novice_horse", "Tatar mercenary cavalryman (recruit)","Tatar mercenary cavalry (recruit)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_7|agi_9|level(5),wp_melee(45)|wp_crossbow(26)|wp_archery(56),knows_weapon_master_2|knows_power_strike_1|knows_riding_4|knows_power_draw_1|knows_horse_archery_3,khergit_face_middle_1, khergit_face_older_2],
    
  ["tatar_merch_regular_horse", "Tatar mercenary cavalryman (experienced)","Tatar mercenary cavalry (experienced)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_10|level(10),wp_melee(60)|wp_crossbow(37)|wp_archery(67),knows_weapon_master_3|knows_ironflesh_1|knows_power_strike_1|knows_riding_5|knows_power_draw_2|knows_horse_archery_4,khergit_face_middle_1, khergit_face_older_2],
    
	["tatar_merch_veteran_horse", "Tatar mercenary cavalryman (veteran)","Tatar mercenary cavalry (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_11|level(15),wp_melee(75)|wp_crossbow(49)|wp_archery(79),knows_weapon_master_4|knows_ironflesh_2|knows_power_strike_2|knows_riding_6|knows_power_draw_3|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
   
  ["tatar_merch_champion_horse", "Tatar mercenary cavalryman (elite)","Tatar mercenary cavalry (elite)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_12|level(20),wp_melee(90)|wp_crossbow(60)|wp_archery(90),knows_weapon_master_5|knows_ironflesh_2|knows_power_strike_3|knows_riding_7|knows_power_draw_4|knows_horse_archery_6,khergit_face_middle_1, khergit_face_older_2],

    # ======= 12
   ["kazak_merch_novice_infantry", "Cossack mercenary infantryman (recruit)","Cossack mercenary infantry (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_7|level(5),wp_melee(67)|wp_crossbow(63)|wp_archery(15),knows_weapon_master_3|knows_ironflesh_4|knows_athletics_2|knows_power_strike_1|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],

      ["kazak_merch_regular_infantry", "Cossack mercenary infantryman (experienced)","Cossack mercenary infantry (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_8|level(10),wp_melee(82)|wp_crossbow(75)|wp_archery(22),knows_weapon_master_4|knows_ironflesh_5|knows_athletics_2|knows_power_strike_2|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
     	
   ["kazak_merch_veteran_infantry", "Cossack mercenary infantryman (veteran)","Cossack mercenary infantry (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_9|level(15),wp_melee(97)|wp_crossbow(86)|wp_archery(30),knows_weapon_master_5|knows_ironflesh_6|knows_athletics_2|knows_power_strike_3|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
       
   ["kazak_merch_champion_infantry", "Cossack mercenary infantryman (elite)","Cossack mercenary infantry (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_10|level(20),wp_melee(112)|wp_crossbow(97)|wp_archery(37),knows_weapon_master_6|knows_ironflesh_7|knows_athletics_2|knows_power_strike_4|knows_riding_2,rhodok_face_middle_1, rhodok_face_older_2],
     
     # ======= 16
	  ["kazak_merch_novice_archer", "Cossack mercenary rifleman (recruit)","Cossack mercenary riflemen (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_7|agi_8|level(5),wp_melee(37)|wp_crossbow(86)|wp_archery(15),knows_weapon_master_1|knows_ironflesh_3|knows_athletics_2|knows_riding_1|knows_horse_archery_7,rhodok_face_middle_1, rhodok_face_older_2],
      
	  ["kazak_merch_regular_archer", "Cossack mercenary rifleman (experienced)","Cossack mercenary riflemen (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_9|level(10),wp_melee(52)|wp_crossbow(97)|wp_archery(22),knows_weapon_master_2|knows_ironflesh_4|knows_athletics_2|knows_power_strike_1|knows_riding_1|knows_horse_archery_1,rhodok_face_middle_1, rhodok_face_older_2],
     
	 ["kazak_merch_veteran_archer", "Cossack mercenary rifleman (veteran)","Cossack mercenary riflemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_10|level(15),wp_melee(67)|wp_crossbow(108)|wp_archery(30),knows_weapon_master_3|knows_ironflesh_5|knows_athletics_2|knows_power_strike_1|knows_riding_2|knows_horse_archery_2,rhodok_face_middle_1, rhodok_face_older_2],
       
	["kazak_merch_champion_archer", "Cossack mercenary rifleman (elite)","Cossack mercenary riflemen (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_11|level(20),wp_melee(82)|wp_crossbow(120)|wp_archery(37),knows_weapon_master_4|knows_ironflesh_6|knows_athletics_2|knows_power_strike_2|knows_riding_2|knows_horse_archery_2,rhodok_face_middle_1, rhodok_face_older_2],
       # ======= 20
     
	   ["kazak_merch_novice_horse", "Cossack mercenary cavalryman (recruit)","Cossack mercenary cavalry (recruit)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_8|level(5),wp_melee(60)|wp_crossbow(78)|wp_archery(15),knows_weapon_master_3|knows_ironflesh_3|knows_power_strike_1|knows_riding_3|knows_horse_archery_4,rhodok_face_middle_1, rhodok_face_older_2],
     
	["kazak_merch_regular_horse", "Cossack mercenary cavalryman (experienced)","Cossack mercenary cavalry (experienced)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_9|level(10),wp_melee(75)|wp_crossbow(90)|wp_archery(22),knows_weapon_master_4|knows_ironflesh_4|knows_power_strike_2|knows_riding_4|knows_horse_archery_5,rhodok_face_middle_1, rhodok_face_older_2],
       
	   ["kazak_merch_veteran_horse", "Cossack mercenary cavalryman (veteran)","Cossack mercenary cavalry (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_10|level(15),wp_melee(90)|wp_crossbow(101)|wp_archery(30),knows_weapon_master_5|knows_ironflesh_5|knows_power_strike_3|knows_riding_5|knows_horse_archery_6,rhodok_face_middle_1, rhodok_face_older_2],
     
	 ["kazak_merch_champion_horse", "Cossack mercenary cavalryman (elite)","Cossack mercenary cavalry (elite)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_11|level(20),wp_melee(105)|wp_crossbow(112)|wp_archery(37),knows_weapon_master_6|knows_ironflesh_6|knows_power_strike_4|knows_riding_6|knows_horse_archery_7,rhodok_face_middle_1, rhodok_face_older_2],
      # ======= 24
	  
  ["polyak_merch_novice_infantry", "Polish mercenary infantryman (recruit)","Polish mercenary infantry (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_7|level(5),wp_melee(71)|wp_crossbow(41)|wp_archery(26), knows_weapon_master_2|knows_ironflesh_1|knows_athletics_3|knows_power_strike_2|knows_riding_2|knows_power_draw_1,swadian_face_middle_1, swadian_face_older_2],
    
	["polyak_merch_regular_infantry", "Polish mercenary infantryman (experienced)","Polish mercenary infantry (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_8|level(10),wp_melee(86)|wp_crossbow(52)|wp_archery(37), knows_weapon_master_3|knows_ironflesh_2|knows_athletics_3|knows_power_strike_3|knows_riding_2|knows_power_draw_1,swadian_face_middle_1, swadian_face_older_2],
     
   ["polyak_merch_veteran_infantry", "Polish mercenary infantryman (veteran)","Polish mercenary infantry (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_9|level(15),wp_melee(101)|wp_crossbow(64)|wp_archery(48), knows_weapon_master_4|knows_ironflesh_3|knows_athletics_3|knows_power_strike_4|knows_riding_3|knows_power_draw_2,swadian_face_middle_1, swadian_face_older_2],
      
   ["polyak_merch_champion_infantry", "Polish mercenary infantryman (elite)","Polish mercenary infantry (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_10|level(20),wp_melee(116)|wp_crossbow(75)|wp_archery(60), knows_weapon_master_5|knows_ironflesh_4|knows_athletics_3|knows_power_strike_5|knows_riding_3|knows_power_draw_2,swadian_face_middle_1, swadian_face_older_2],
      
   # ======= 28

   ["polyak_merch_novice_archer", "Polish mercenary rifleman (recruit)","Polish mercenary riflemen (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_7|level(5),wp_melee(22)|wp_crossbow(56)|wp_archery(39), knows_weapon_master_2|knows_ironflesh_1|knows_athletics_3|knows_power_strike_1|knows_riding_2|knows_power_draw_2|knows_horse_archery_1,swadian_face_middle_1, swadian_face_older_2],
        
   ["polyak_merch_regular_archer", "Polish mercenary rifleman (experienced)","Polish mercenary riflemen (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_8|level(10),wp_melee(37)|wp_crossbow(67)|wp_archery(52), knows_weapon_master_3|knows_ironflesh_2|knows_athletics_3|knows_power_strike_2|knows_riding_2|knows_power_draw_2|knows_horse_archery_1,swadian_face_middle_1, swadian_face_older_2],
      
   ["polyak_merch_veteran_archer", "Polish mercenary rifleman (veteran)","Polish mercenary riflemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_9|level(15),wp_melee(52)|wp_crossbow(78)|wp_archery(63), knows_weapon_master_4|knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_riding_3|knows_power_draw_3|knows_horse_archery_2,swadian_face_middle_1, swadian_face_older_2],
        
  ["polyak_merch_champion_archer", "Polish mercenary rifleman (elite)","Polish mercenary riflemen (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_10|level(20),wp_melee(67)|wp_crossbow(90)|wp_archery(75), knows_weapon_master_5|knows_ironflesh_4|knows_athletics_3|knows_power_strike_4|knows_riding_3|knows_power_draw_3|knows_horse_archery_2,swadian_face_middle_1, swadian_face_older_2],
    # =======    32
 
 ["polyak_merch_novice_horse", "Polish mercenary cavalryman (recruit)","Polish mercenary cavalry (recruit)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_9|level(5),wp_melee(86)|wp_crossbow(52)|wp_archery(31), knows_weapon_master_3|knows_ironflesh_1|knows_athletics_1|knows_power_strike_1|knows_riding_3|knows_power_draw_1|knows_horse_archery_1,swadian_face_middle_1, swadian_face_older_2],
      
   ["polyak_merch_regular_horse", "Polish mercenary cavalryman (experienced)","Polish mercenary cavalry (experienced)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_10|level(10),wp_melee(93)|wp_crossbow(63)|wp_archery(45), knows_weapon_master_4|knows_ironflesh_2|knows_athletics_1|knows_power_strike_2|knows_riding_4|knows_power_draw_2|knows_horse_archery_2,swadian_face_middle_1, swadian_face_older_2],
     
   ["polyak_merch_veteran_horse", "Polish mercenary cavalryman (veteran)","Polish mercenary cavalry (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_11|level(15),wp_melee(100)|wp_crossbow(75)|wp_archery(56), knows_weapon_master_5|knows_ironflesh_3|knows_athletics_1|knows_power_strike_3|knows_riding_5|knows_power_draw_3|knows_horse_archery_3,swadian_face_middle_1, swadian_face_older_2],
      
   ["polyak_merch_champion_horse", "Polish mercenary cavalryman (elite)","Polish mercenary cavalry (elite)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_12|level(20),wp_melee(108)|wp_crossbow(86)|wp_archery(67), knows_weapon_master_6|knows_ironflesh_4|knows_athletics_1|knows_power_strike_4|knows_riding_6|knows_power_draw_4|knows_horse_archery_4,swadian_face_middle_1, swadian_face_older_2],
     # =======   36

  ["shved_merch_novice_infantry", "European mercenary infantryman (recruit)","European mercenary infantry (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_7|level(5),wp_melee(78)|wp_crossbow(41)|wp_archery(0),knows_weapon_master_4|knows_ironflesh_2|knows_power_strike_1|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],

    ["shved_merch_regular_infantry", "European mercenary infantryman (experienced)","European mercenary infantry (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_8|level(10),wp_melee(93)|wp_crossbow(52)|wp_archery(0),knows_weapon_master_5|knows_ironflesh_3|knows_power_strike_2|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],
     
   ["shved_merch_veteran_infantry", "European mercenary infantryman (veteran)","European mercenary infantry (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_9|level(15),wp_melee(108)|wp_crossbow(63)|wp_archery(0),knows_weapon_master_6|knows_ironflesh_4|knows_power_strike_3|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],
    
   ["shved_merch_champion_infantry", "European mercenary infantryman (elite)","European mercenary infantry (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_10|level(20),wp_melee(123)|wp_crossbow(75)|wp_archery(0),knows_weapon_master_7|knows_ironflesh_5|knows_power_strike_4|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],

    # =======   40
	 ["shved_merch_novice_archer", "European mercenary rifleman (recruit)","European mercenary riflemen (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_8|agi_8|level(5),wp_melee(30)|wp_crossbow(71)|wp_archery(0),knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_1|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],
     
   ["shved_merch_regular_archer", "European mercenary rifleman (experienced)","European mercenary riflemen (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_8|level(10),wp_melee(45)|wp_crossbow(82)|wp_archery(0),knows_weapon_master_3|knows_ironflesh_2|knows_athletics_1|knows_power_strike_2|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],
     
   ["shved_merch_veteran_archer", "European mercenary rifleman (veteran)","European mercenary riflemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_9|level(15),wp_melee(60)|wp_crossbow(93)|wp_archery(0),knows_weapon_master_4|knows_ironflesh_3|knows_athletics_1|knows_power_strike_2|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],
        
   ["shved_merch_champion_archer", "European mercenary rifleman (elite)","European mercenary riflemen (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_10|level(20),wp_melee(75)|wp_crossbow(105)|wp_archery(10),knows_weapon_master_5|knows_ironflesh_4|knows_athletics_1|knows_power_strike_3|knows_riding_1|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],

      # =======  44
   ["shved_merch_novice_horse", "European mercenary cavalryman (recruit)","European mercenary cavalry (recruit)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_6|level(5),wp_melee(82)|wp_crossbow(63)|wp_archery(0),knows_weapon_master_3|knows_ironflesh_2|knows_power_strike_1|knows_riding_2|knows_horse_archery_2,nord_face_middle_1, nord_face_older_2],
     
     ["shved_merch_regular_horse", "European mercenary cavalryman (experienced)","European mercenary cavalry (experienced)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_7|level(10),wp_melee(93)|wp_crossbow(75)|wp_archery(0),knows_weapon_master_4|knows_ironflesh_3|knows_power_strike_2|knows_riding_3|knows_horse_archery_3,nord_face_middle_1, nord_face_older_2],
     
   ["shved_merch_veteran_horse", "European mercenary cavalryman (veteran)","European mercenary cavalry (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_8|level(15),wp_melee(105)|wp_crossbow(86)|wp_archery(0),knows_weapon_master_5|knows_ironflesh_4|knows_power_strike_3|knows_riding_4|knows_horse_archery_4,nord_face_middle_1, nord_face_older_2],
   
   ["shved_merch_champion_horse", "European mercenary cavalryman (elite)","European mercenary cavalry (elite)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_13|agi_9|level(20),wp_melee(116)|wp_crossbow(97)|wp_archery(0),knows_weapon_master_6|knows_ironflesh_5|knows_power_strike_4|knows_riding_5|knows_horse_archery_5,nord_face_middle_1, nord_face_older_2],

      # =======    48
    ["moskov_merch_novice_infantry", "Muscovite mercenary infantryman (recruit)","Muscovite mercenary infantry (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_5|level(5),wp_melee(75)|wp_crossbow(39)|wp_archery(32),knows_weapon_master_1|knows_ironflesh_5|knows_power_strike_2|knows_riding_1|knows_power_draw_1|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],
  
     ["moskov_merch_regular_infantry", "Muscovite mercenary infantryman (experienced)","Muscovite mercenary infantry (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_6|level(10),wp_melee(90)|wp_crossbow(52)|wp_archery(45),knows_weapon_master_2|knows_ironflesh_6|knows_power_strike_3|knows_riding_1|knows_power_draw_1|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],

  ["moskov_merch_veteran_infantry", "Muscovite mercenary infantryman (veteran)","Muscovite mercenary infantry (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_7|level(15),wp_melee(105)|wp_crossbow(63)|wp_archery(56),knows_weapon_master_3|knows_ironflesh_7|knows_power_strike_4|knows_riding_1|knows_power_draw_1|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],
    
  ["moskov_merch_champion_infantry", "Muscovite mercenary infantryman (elite)","Muscovite mercenary infantry (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_13|agi_8|level(20),wp_melee(120)|wp_crossbow(75)|wp_archery(67),knows_weapon_master_4|knows_ironflesh_8|knows_power_strike_5|knows_riding_1|knows_power_draw_1|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],
     # =======   52
    
   ["moskov_merch_novice_archer", "Muscovite mercenary rifleman (recruit)","Muscovite mercenary riflemen (recruit)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_9|agi_6|level(5),wp_melee(52)|wp_crossbow(56)|wp_archery(39),knows_weapon_master_1|knows_ironflesh_3|knows_athletics_1|knows_power_strike_1|knows_riding_1|knows_power_draw_1|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["moskov_merch_regular_archer", "Muscovite mercenary rifleman (experienced)","Muscovite mercenary riflemen (experienced)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_7|level(10),wp_melee(67)|wp_crossbow(67)|wp_archery(52),knows_weapon_master_2|knows_ironflesh_4|knows_athletics_1|knows_power_strike_2|knows_riding_1|knows_power_draw_2|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],

  ["moskov_merch_veteran_archer", "Muscovite mercenary rifleman (veteran)","Muscovite mercenary riflemen (veteran)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_11|agi_8|level(15),wp_melee(82)|wp_crossbow(78)|wp_archery(63),knows_weapon_master_3|knows_ironflesh_5|knows_athletics_1|knows_power_strike_3|knows_riding_1|knows_power_draw_3|knows_horse_archery_2,vaegir_face_middle_1, vaegir_face_older_2],
     
   ["moskov_merch_champion_archer", "Muscovite mercenary rifleman (elite)","Muscovite mercenary riflemen (elite)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_9|level(20),wp_melee(97)|wp_crossbow(90)|wp_archery(75),knows_weapon_master_4|knows_ironflesh_6|knows_athletics_1|knows_power_strike_4|knows_riding_1|knows_power_draw_4|knows_horse_archery_2,vaegir_face_middle_1, vaegir_face_older_2],
      # =======  56
  
   ["moskov_merch_novice_horse", "Muscovite mercenary cavalryman (recruit)","Muscovite mercenary cavalry (recruit)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_10|agi_5|level(5),wp_melee(75)|wp_crossbow(48)|wp_archery(39),knows_weapon_master_2|knows_ironflesh_3|knows_power_strike_2|knows_riding_2|knows_power_draw_1|knows_horse_archery_1,vaegir_face_middle_1, vaegir_face_older_2],
  
   ["moskov_merch_regular_horse", "Muscovite mercenary cavalryman (experienced)","Muscovite mercenary cavalry (experienced)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_12|agi_6|level(10),wp_melee(90)|wp_crossbow(60)|wp_archery(45),knows_weapon_master_3|knows_ironflesh_4|knows_power_strike_3|knows_riding_2|knows_power_draw_2|knows_horse_archery_2,vaegir_face_middle_1, vaegir_face_older_2],

  ["moskov_merch_veteran_horse", "Muscovite mercenary cavalryman (veteran)","Muscovite mercenary cavalry (veteran)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_13|agi_7|level(15),wp_melee(105)|wp_crossbow(71)|wp_archery(56),knows_weapon_master_4|knows_ironflesh_5|knows_power_strike_4|knows_riding_3|knows_power_draw_3|knows_horse_archery_3,vaegir_face_middle_1, vaegir_face_older_2],
   
   ["moskov_merch_champion_horse", "Muscovite mercenary cavalryman (elite)","Muscovite mercenary cavalry (elite)",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [],
   str_14|agi_8|level(20),wp_melee(120)|wp_crossbow(82)|wp_archery(67),knows_weapon_master_5|knows_ironflesh_6|knows_power_strike_5|knows_riding_4|knows_power_draw_4|knows_horse_archery_4,vaegir_face_middle_1, vaegir_face_older_2],
    # =======  60

     ["array_factions", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["array_faction_troop_count_without_npc", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["array_factions_2", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  
  
   ["array_agents", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["array_agents_horses", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

   ["castle_tavernkeeper", "Tavern Keeper","Tavern Keeper",tf_hero|tf_randomize_face, 0,0,  fac_commoners,[itm_kozak_boots, itm_tatar_halat_pure_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],

   #Arrays for merches and their armors/clothes
   ["week_limit_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["merch_type_price_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["merch_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["merch_price_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["merch_arms_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["merch_arms_price_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["cur_merch_arms_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
   ["cur_merch_arms_price_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
    
	#Arrays to controll ladder shturm
	["ladder_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ladder_infantry_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ladder_infantry_state_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ladder_archers_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ladder_archers_state_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
     


	#Expanded management system -begin
	["town_building_arsenal", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_b],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_waterpipe", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_school", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_merchant_guild", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_defense", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_treasury", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_barrack", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_building_stable", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_b],def_attrib|level(18),wp(60),knows_common, 0],
	
	["town_upgrade_armourer", "Weaponsmith","Weaponsmith",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_b],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_protection", "Armorer","Armorer",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_b],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_groom", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_adviser", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_secret_order", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_tax_supervisor", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_trading_master", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_priest", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_garrison_commander", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_officer_infantry", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_sapogi,itm_kirasa],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_officer_cavalry", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_old_cavalry_boots,itm_kirasa],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_officer_infantry_guard", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_kirasa],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_officer_cavalry_guard", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_cavalry_boots,itm_kirasa],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_officer_elite_guard", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_kirasa_rich],def_attrib|level(18),wp(60),knows_common, 0],
	["town_upgrade_officer_mercenary", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_infantry_boots,itm_kirasa],def_attrib|level(18),wp(60),knows_common, 0],
	
	["village_building_mill", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_armyak],def_attrib|level(18),wp(60),knows_common, 0],
	["village_building_barn", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_armyak],def_attrib|level(18),wp(60),knows_common, 0],
	["village_building_school", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["village_building_secret_place","{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_armyak],def_attrib|level(18),wp(60),knows_common, 0],
	["village_building_administration", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_b],def_attrib|level(18),wp(60),knows_common, 0],
	
	["village_upgrade_judge", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_b],def_attrib|level(18),wp(60),knows_common, 0],
	["village_upgrade_treasurer", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["village_upgrade_priest", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_c],def_attrib|level(18),wp(60),knows_common, 0],
	["village_upgrade_police_master", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[itm_selo_boots, itm_poland_svitka_d],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_end", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	
	["militiaman", "Militiaman","Militiamen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,
   [itm_old_pike,itm_evropa_odejda_sela,itm_evropa_odejda_sela_b,itm_selo_boots],
   str_8|agi_7|level(5),wp_melee(75),knows_ironflesh_1|knows_weapon_master_1,nord_face_middle_1, nord_face_older_2],
    
	["ms_elder_menu_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_ai_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
    ["ms_temp_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_temp_array_rank", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_temp_array_additional", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_temp_array_extra_category", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_temp_extra_category_elements", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_temp_extra_category_elements_prices", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_temp_extra_adviser_menu", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	
	#Expanded management system -end
	
	["diplomatic_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["diplomatic_temp_array", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	
	["polsk_ambassador", "Polish Commonwealth Ambassador","Polish Commonwealth Ambassador",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_dobrotna_svitka_e,itm_poland_good_shapka,itm_good_sapogi],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_old_1, swadian_face_old_2],
    ["moskov_ambassador", "Muscovite Tsardom Ambassador","Muscovite Tsardom Ambassador",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_mosk_civil_b,itm_shapka_boyara,itm_sapogi],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,vaegir_face_old_1, vaegir_face_old_2],
     ["tatar_ambassador", "Crimean Khanate Ambassador","Crimean Khanate Ambassador",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_ttr_civil_a,itm_tatar_oglan_hat,itm_kalmyk_boots],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,khergit_face_old_1, khergit_face_old_2],
    ["shved_ambassador", "Swedish Kingdom Ambassador","Swedish Kingdom Ambassador",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_swed_civil_a,itm_evropa_guard_shlapa,itm_evropa_pehot_tufli],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,nord_face_old_1, nord_face_old_2],
     ["kozak_ambassador", "Zaporozhian Cossack Ambassador","Zaporozhian Cossack Ambassador",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_civil_jupan_a,itm_kozak_shapka_d,itm_kozak_boots],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,rhodok_face_old_1, rhodok_face_old_2],

    ["ms_player_officer_elements","{!}ms_player_officer_elements","{!}ms_player_officer_elements",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_player_officer_elements_prices","{!}ms_player_officer_elements_prices","{!}ms_player_officer_elements_prices",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	
	["ms_ai_officer_fac1", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_ai_officer_fac2", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_ai_officer_fac3", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_ai_officer_fac4", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_ai_officer_fac5", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	
	["ms_ai_officer_temp", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
	["ms_ai_chance_temp", "{!}Do not translate","{!}Do not translate",tf_hero|tf_inactive|tf_randomize_face, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],


    ["armor_smith_pol", "Armorer","Armorer",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_poland_svitka_a,itm_poland_shapka,itm_good_sapogi],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_old_1, swadian_face_old_2],
    ["armor_smith_rus", "Armorer","Armorer",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_mosk_sermyaga,itm_streletz_shapka,itm_sapogi],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,vaegir_face_old_1, vaegir_face_old_2],
     ["armor_smith_tatar", "Armorer","Armorer",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_tatar_halat_pure_b,itm_tatar_man_hat,itm_kalmyk_boots],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,khergit_face_old_1, khergit_face_old_2],
    ["armor_smith_swed", "Armorer","Armorer",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_evropa_odejda_sela,itm_evropa_shapka,itm_evropa_pehot_tufli],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,nord_face_old_1, nord_face_old_2],
     ["armor_smith_ukr", "Armorer","Armorer",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_jupan,itm_kozak_shapka,itm_kozak_boots],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,rhodok_face_old_1, rhodok_face_old_2],

    ["weapon_smith_pol", "Weaponsmith","Weaponsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_poland_svitka_b,itm_poland_mehova_shapka,itm_good_sapogi],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_old_1, swadian_face_old_2],
    ["weapon_smith_rus", "Weaponsmith","Weaponsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_mosk_sermyaga,itm_streletz_shapka_b,itm_sapogi],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,vaegir_face_old_1, vaegir_face_old_2],
     ["weapon_smith_tatar", "Weaponsmith","Weaponsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_tatar_halat_pure_a,itm_tatar_man_hat,itm_kalmyk_boots],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,khergit_face_old_1, khergit_face_old_2],
    ["weapon_smith_swed", "Weaponsmith","Weaponsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_evropa_odejda_sela_b,itm_evropa_kava_shlapa_c,itm_evropa_pehot_tufli],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,nord_face_old_1, nord_face_old_2],
     ["weapon_smith_ukr", "Weaponsmith","Weaponsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_jupan_b,itm_kozak_shapka_b,itm_kozak_boots],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,rhodok_face_old_1, rhodok_face_old_2],

    ["castle_cmd_pol", "Commander","Commander",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_kolchuga_panzernika,itm_poland_good_shapka,itm_good_sapogi,itm_sablya_a],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_old_1, swadian_face_old_2],
    ["castle_cmd_rus", "Commander","Commander",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_moskow_reytar_armor,itm_shelom,itm_sapogi,itm_palitza],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,vaegir_face_old_1, vaegir_face_old_2],
     ["castle_cmd_tatar", "Commander","Commander",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_tatar_kolcha,itm_tatar_misurka_rich,itm_kalmyk_boots,itm_yatagan_rich],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,khergit_face_old_1, khergit_face_old_2],
    ["castle_cmd_swed", "Commander","Commander",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_kirasa_rich,itm_morion_good,itm_evropa_pehot_tufli,itm_good_pehot_palash_b],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,nord_face_old_1, nord_face_old_2],
     ["castle_cmd_ukr", "Commander","Commander",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_jupan_na_kolchuge,itm_kozak_shapka_d,itm_kozak_boots,itm_kozak_good_shablya],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,rhodok_face_old_1, rhodok_face_old_2],



  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Musketeers","Polish Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bad_sablya_a,itm_norm_sablya_a,itm_bad_toporik,itm_bad_musket,itm_norm_musket,itm_good_musket_m,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,
    itm_poland_musketer_uniform,itm_poland_musketer_uniform,itm_sapogi,itm_poland_army_hat_simple,itm_poland_army_hat_a,itm_poland_army_hat_b,itm_poland_uniforma_german_line_musketeer],
   str_8|agi_8|level(10),wp_melee(75)|wp_crossbow(110),knows_common|knows_ironflesh_1|knows_athletics_4|knows_weapon_master_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer_ai","Infantry","Polish Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bad_pike,itm_norm_pika,itm_poland_pikiner_uniform,itm_poland_pikiner_uniform,itm_poland_uniforma_german_line,itm_sapogi,itm_poland_army_hat_simple],
   str_8|agi_8|level(10),wp_melee(85),knows_common|knows_athletics_2|knows_ironflesh_1|knows_weapon_master_2|knows_power_strike_1,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_man_at_arms_multiplayer_ai","Cavalry","Polish Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_bad_sablya_a,itm_norm_sablya_a,itm_bad_karabin,itm_norm_karabin,itm_good_karabin,itm_norm_shield,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_bad_lance,itm_norm_lance,itm_bad_chekan,
    itm_bad_arrows,itm_norm_arrows,itm_good_arrows,itm_bad_luk,itm_norm_luk,itm_gud_luk,
    itm_poland_mehova_shapka_s_perom,itm_poland_good_shapka,itm_kolchuga_panzernika,itm_koja_kurtka_s_podbivom,
    itm_poland_dragoon_uniform,itm_old_cavalry_boots,itm_poland_army_hat_b,itm_poland_army_hat_a,itm_norm_horse,itm_good_horse,itm_tank_horse],
   str_8|agi_9|level(15),wp_melee(110)|wp_crossbow(100)|wp_archery(80),knows_common|knows_riding_5|knows_power_draw_3|knows_horse_archery_4|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_4|knows_shield_4,swadian_face_middle_1, swadian_face_older_2],
  ["vaegir_archer_multiplayer_ai","Marksmen","Russian Riflemen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bad_musket,itm_norm_musket,itm_good_musket_m,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_bad_berdish,itm_streletzkiy_mundir,itm_new_line_uniform,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c,itm_new_line_helmet],
   str_10|agi_6|level(10),wp_melee(80)|wp_crossbow(90),knows_common|knows_ironflesh_6|knows_athletics_3|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Infantry","Russian Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bad_spear,itm_good_spear,itm_streletzkiy_mundir_spear,itm_new_line_uniform_spear,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c,itm_new_line_helmet],
   str_10|agi_6|level(10),wp_melee(90),knows_common|knows_ironflesh_6|knows_athletics_4|knows_power_strike_3|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Cavalry","Russian Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_m_sovnya,itm_bad_sablya_b,itm_norm_sablya_b,itm_shapka_bumajna_a,itm_moskow_bahter_a,
    itm_shapka_bumajna_b,itm_sablya_pure_c,itm_bad_luk,itm_norm_luk,itm_gud_luk,itm_bad_arrows,itm_norm_arrows,itm_good_arrows,itm_moskow_tulup_a,itm_moskow_tulup_b,itm_moskow_tulup_c,itm_mosk_bahter_b,
    itm_selo_boots,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka,itm_shishak,itm_very_bad_horse,itm_bad_horse,itm_norm_horse,itm_shelom],
   str_9|agi_7|level(15),wp_melee(100)|wp_archery(85),knows_common|knows_riding_3|knows_power_draw_4|knows_ironflesh_4|knows_horse_archery_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai", "Tatar Infantryman","Tatar Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_bad_arrows,itm_norm_arrows,itm_good_arrows,itm_bad_luk,itm_norm_luk,itm_gud_luk,itm_sapogi,itm_tatar_seymen_armor,itm_tatar_misurka,
    itm_misurka_s_barmizoy_pure,itm_bad_shield,
    itm_misurka_s_barmizoy_b,itm_t_bad_sablya_a,itm_t_norm_sablya_a,itm_t_bad_musket,itm_t_norm_musket,itm_t_good_musket,itm_tatar_bayrak_hat,itm_tatar_nogay_hat,itm_tatar_man_hat,
    itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c],
   str_8|agi_7|level(9),wp_melee(85)|wp_crossbow(80)|wp_archery(90),knows_ironflesh_1|knows_power_draw_3,khergit_face_middle_1, khergit_face_old_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Mounted Archers","Tatar Horse Riflemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_bad_arrows,itm_norm_arrows,itm_good_arrows,itm_t_bad_sablya_a,itm_t_norm_sablya_a,itm_bad_luk,itm_norm_luk,itm_gud_luk,itm_norm_horse,itm_good_horse,itm_fast_horse,itm_tatar_halat_a,
    itm_tatar_halat_b,itm_tatar_steg_halat_a,itm_tatar_steg_halat_b,itm_sapogi,itm_bad_shield,
    itm_tatar_kochevnik_hat_a,itm_tatar_kochevnik_hat_b,itm_misurka_s_barmizoy_c,itm_misurka_s_barmizoy_pure,itm_tatar_misurka],
   str_7|agi_9|level(11),wp_melee(100)|wp_archery(100),knows_riding_6|knows_power_draw_4|knows_horse_archery_5|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Lancers","Tatar Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_bad_lance,itm_norm_lance,itm_cavalry_boots,itm_sapogi,itm_tatar_steg_halat_a,itm_tatar_steg_halat_b,itm_tatar_kolcha,itm_tatar_bahter_b,itm_steppe_horse,
    itm_steppe_horse_b,itm_good_shield,itm_bad_shield,
    itm_misurka_s_barmizoy_c,itm_misurka_s_barmizoy_pure,itm_tatar_misurka,itm_tatar_helmet_a,itm_norm_horse,itm_good_horse,itm_fast_horse,],
   str_8|agi_8|level(14),wp_melee(110),knows_riding_6|knows_weapon_master_3|knows_ironflesh_1|knows_shield_7,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Infantry","Swedish Infantry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_bad_pike,itm_norm_pika,itm_evropa_pika_uniforma,itm_morion,itm_kabasset,itm_morion_good,itm_evropa_kava_shlapa,itm_evropa_pehot_tufli,itm_infantry_gloves],
   str_9|agi_7|level(10),wp_melee(90),knows_weapon_master_2,nord_face_middle_1, nord_face_old_2],
  ["nord_scout_multiplayer_ai","Cavalry","Swedish Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_bad_lance,itm_norm_lance,itm_bad_palash,itm_norm_palash,itm_power_pistol,itm_norm_pistol,itm_bad_pistol,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_kirasa_b,itm_evropa_dragoon_uniforma,itm_kirasa_c,itm_simple_reytar_armor,
    itm_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_bad_horse,itm_norm_horse,itm_tank_horse,itm_infantry_gloves],
   str_8|agi_8|level(15),wp_melee(110)|wp_crossbow(110),knows_ironflesh_2|knows_horse_archery_5|knows_riding_3|knows_weapon_master_4,nord_face_middle_1, nord_face_old_2],
  ["nord_archer_multiplayer_ai","Musketeers","Swedish Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_bad_shpaga,itm_norm_shpaga,itm_bad_p_palash,itm_norm_p_palash,itm_bad_musket,itm_norm_musket,itm_good_musket_m,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_evropa_musket_uniforma,itm_evropa_pehot_tufli,itm_evropa_guard_shlapa,
    itm_evropa_musket_shlapa_b,itm_evropa_gvardia_uniforma,itm_evropa_guard_shlapa],
   str_8|agi_8|level(10),wp_melee(75)|wp_crossbow(120),knows_ironflesh_1|knows_athletics_2|knows_weapon_master_3,nord_face_middle_1, nord_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Infantry","Zaporozhian Riflemen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_t_bad_sablya_a,itm_t_norm_sablya_a,itm_norn_k_shablya,itm_kozak_jupan_c,
    itm_t_bad_musket,itm_t_norm_musket,itm_t_good_musket,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_steel_bolts,itm_kozak_jupan,
    itm_kozak_jupan_b,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d],
   str_9|agi_9|level(11),wp_melee(100)|wp_crossbow(130),knows_common|knows_ironflesh_3|knows_power_strike_1|knows_athletics_4|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai", "Zaporozhian Infantryman","Zaporozhian Infantry",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_t_bad_sablya_a,itm_t_norm_sablya_a,itm_norn_k_shablya,itm_bad_bulava,itm_bad_chekan,
    itm_fast_pistol,itm_norm_pistol,itm_bad_pistol,itm_bad_bullets,itm_norm_bullets,itm_good_bullets,itm_kozak_jupan_usileniy,itm_cavalry_koja_kurtka,itm_kozak_boots,itm_kozacka_shapka_s_misurkoy],
   str_10|agi_8|level(11),wp_melee(120)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai", "Zaporozhian Horseman","Zaporozhian Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_t_bad_sablya_a,itm_t_norm_sablya_a,itm_norn_k_shablya,itm_bad_karabin,itm_norm_karabin,itm_good_karabin,itm_fast_pistol,itm_norm_pistol,itm_bad_pistol,itm_bad_bullets,itm_norm_bullets,
    itm_good_bullets,itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka,itm_norm_horse,itm_good_horse,itm_fast_horse,
    itm_kozak_jupan_usileniy,itm_cavalry_koja_kurtka,itm_kozak_jupan_na_kolchuge],
   str_9|agi_9|level(14),wp_melee(115)|wp_crossbow(120),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_riding_5|knows_horse_archery_6|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_old_2],
  ["sarranid_infantry_multiplayer_ai", "Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai", "Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai", "Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,
   [],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer", "Musketeer","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bad_bullets, itm_bad_musket, itm_m_pol_strelok_forma, itm_bad_boots],
   def_attrib_multiplayer|level(20),wpex(70,70,70,40,165,75),knows_common|knows_ironflesh_1|knows_weapon_master_3|knows_athletics_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_infantry_multiplayer", "Infantryman","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bad_spear,itm_m_pol_pehota_forma,itm_bad_boots],
   def_attrib_multiplayer_inf|level(20),wpex(110,80,110,30,55,40),knows_common|knows_ironflesh_6|knows_athletics_6|knows_weapon_master_4|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_man_at_arms_multiplayer", "Cavalryman","Swadian Men at Arms",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bad_sablya_a,itm_m_pol_kava_forma,itm_bad_boots,itm_very_bad_horse],
   def_attrib_multiplayer|level(20),wpex(85,85,140,85,65,50),knows_common|knows_riding_5|knows_horse_archery_4|knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_4|knows_power_draw_3|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer", "Marksman","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_bad_bullets,itm_bad_musket,itm_m_mosk_strelok_forma,itm_bad_boots_mosk],
   def_attrib_multiplayer|level(20),wpex(80,105,55,65,135,85),knows_common|knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_2|knows_athletics_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer", "Infantryman","Vaegir spearman",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_bad_spear,itm_m_mosk_pehota_forma,itm_bad_boots_mosk],
   def_attrib_multiplayer_inf|level(20),wpex(110,130,80,20,45,40),knows_common|knows_ironflesh_7|knows_athletics_4|knows_power_strike_5|knows_weapon_master_5,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer", "Cavalryman","Vaegir Horsemen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_bad_sablya_a,itm_bad_boots_mosk,itm_m_mosk_kava_forma,itm_very_bad_horse],
   def_attrib_multiplayer|level(20),wpex(120,85,100,70,70,40),knows_riding_4|knows_horse_archery_3|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_2|knows_weapon_master_3,vaegir_face_middle_1, vaegir_face_old_2],
  ["khergit_veteran_footman_multiplayer", "Tatar Infantryman","Tatar Infantrymen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_bad_boots, itm_m_ttr_kava_forma, itm_t_bad_sablya_a, itm_bad_shield],
   def_attrib_multiplayer_inf|level(20),wpex(95,60,75,100,95,50),knows_ironflesh_4|knows_athletics_8|knows_weapon_master_2|knows_power_draw_4|knows_shield_4|knows_power_strike_2,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer", "Mounted Archer","Khergit Horse Archers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_bad_arrows,itm_bad_luk,itm_t_bad_sablya_a,itm_m_ttr_archer_forma,itm_bad_boots,itm_very_bad_horse],
   def_attrib_multiplayer|level(20),wpex(75,50,60,140,40,20),knows_riding_5|knows_power_draw_5|knows_horse_archery_6,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer", "Lancer","Khergit Lancers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_bad_lance,itm_m_ttr_kava_forma,itm_bad_boots,itm_very_bad_horse],
   def_attrib_multiplayer|level(20),wpex(110,75,110,65,30,20),knows_riding_7|knows_weapon_master_3|knows_ironflesh_2|knows_shield_5,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer", "Musketeer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_bad_bullets,itm_bad_musket,itm_m_swed_strelok_forma,itm_bad_boots_swed],
   def_attrib_multiplayer|level(20),wpex(50,45,50,10,180,70),knows_weapon_master_3|knows_athletics_2,nord_face_middle_1, nord_face_older_2],
  ["nord_veteran_multiplayer", "Infantryman","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_bad_pike,itm_m_swed_pehot_forma,itm_bad_boots_swed],
   def_attrib_multiplayer_inf|level(20),wpex(70,120,120,10,50,30),knows_weapon_master_4|knows_ironflesh_9|knows_athletics_3|knows_power_strike_3,nord_face_middle_1, nord_face_old_2],
  ["nord_scout_multiplayer", "Cavalryman","Nord Scouts",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_bad_palash,itm_m_swed_kava_forma,itm_bad_boots_swed,itm_very_bad_horse],
   def_attrib_multiplayer|level(20),wpex(100,60,120,20,75,20),knows_ironflesh_2|knows_horse_archery_4|knows_power_strike_1|knows_riding_5|knows_weapon_master_4,nord_face_middle_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer", "Infantryman","Riflemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_bad_bullets,itm_samopal_m,itm_m_ukr_strelok_forma,itm_bad_boots],
   def_attrib_multiplayer|level(20),wpex(85,40,75,50,130,110),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_athletics_4|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer", "Rifleman","Riflemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_bad_bullets,itm_bad_pistol,itm_t_bad_sablya_a,itm_m_ukr_pehota_forma,itm_bad_boots],
   def_attrib_multiplayer_inf|level(20),wpex(105,60,95,40,90,20),knows_common|knows_ironflesh_5|knows_power_strike_2|knows_athletics_8|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer", "Rider","Riders",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_bad_bullets,itm_bad_karabin,itm_t_bad_sablya_a,itm_m_ukr_kava_forma,itm_bad_boots,itm_very_bad_horse],
   def_attrib_multiplayer|level(20),wpex(90,60,85,40,120,20),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_riding_6|knows_horse_archery_6|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_old_2],


##  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_5,
##   [itm_arrows,
##  ],
##   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_5|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
##  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_5,
##   [itm_bamboo_spear, itm_tab_shield_kite_a,
##    ],
##   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
##  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
##   [itm_lance,itm_tab_shield_small_round_a,
##    ,itm_saddle_horse],
##   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

#----------------------------------------------------------
########## RP#####################
#---------------------------------------------------------
  ["mp_swadian_militia", "Militia Pikeman","Pikemen Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bad_spear,itm_poland_shapka,itm_poland_army_hat_simple,itm_poland_mehova_shapka,itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots],
   str_7|agi_6|level(3),wp_melee(60),knows_common|knows_athletics_2|knows_ironflesh_2,swadian_face_young_1, swadian_face_young_2],
  ["mp_swadian_footman", "Pikeman recruit","Pikemen Recruits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bad_pike,itm_poland_pikiner_uniform,itm_sapogi,itm_poland_army_hat_simple],
   str_9|agi_7|level(7),wp_melee(80),knows_common|knows_athletics_3|knows_weapon_master_1|knows_ironflesh_3|knows_power_strike_1,swadian_face_middle_1, swadian_face_old_2],
  ["mp_swadian_footman_levelup", "Veteran Pikeman","Pikemen Veterans",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_norm_pika,itm_norm_pika,itm_good_p_palash,itm_m_pol_light_armor,itm_sapogi,itm_m_pol_light_helmet,itm_bad_gloves],
   str_9|agi_8|level(11),wp_melee(90),knows_common|knows_ironflesh_4|knows_athletics_4|knows_weapon_master_2|knows_power_strike_2,swadian_face_middle_1, swadian_face_older_2],
  ["mp_swadian_infantry", "German Infantry Pikeman","German Infantry Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_1,
   [itm_good_pike_m,itm_good_pike_m,itm_poland_uniforma_german_line,itm_evropa_pehot_tufli,itm_morion_good,itm_kabasset,itm_infantry_gloves,itm_bad_chekan],
   str_10|agi_9|level(16),wp_melee(110),knows_common|knows_power_strike_2|knows_weapon_master_3|knows_athletics_4|knows_ironflesh_5,swadian_face_middle_1, swadian_face_old_2],

  ["mp_swadian_skirmisher", "Militia Musketeer","Musketeer Militia",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bad_sablya_a, itm_bad_musket,itm_bad_bullets,itm_poland_shapka,itm_poland_army_hat_simple,
    itm_poland_svitka_a,itm_poland_svitka_b,itm_poland_svitka_c,itm_poland_svitka_d,itm_selo_boots,itm_poland_mehova_shapka],
   str_7|agi_6|level(3),wp_melee(20)|wp_crossbow(55),knows_common|knows_athletics_1,swadian_face_young_1, swadian_face_young_2],
  ["mp_swadian_crossbowman", "Zolnier recruit","Zolnier recruits",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bad_sablya_a,itm_norm_sablya_a, itm_norm_musket,itm_bad_musket,itm_sablya_pure_d,itm_norm_bullets,itm_bad_bullets,
    itm_m_pol_light_armor,itm_sapogi,itm_poland_army_hat_simple],
   str_8|agi_7|level(7),wp_melee(35)|wp_crossbow(80),knows_common|knows_athletics_2|knows_weapon_master_1,swadian_face_middle_1, swadian_face_old_2],
  ["mp_swadian_crossbowman_levelup", "Zolnier veteran","Zolnier veterans",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_norm_sablya_a, itm_good_musket_m,itm_norm_bullets,
    itm_m_pol_light_armor,itm_sapogi,itm_m_pol_light_helmet],
   str_8|agi_8|level(11),wp_melee(50)|wp_crossbow(100),knows_common|knows_ironflesh_1|knows_athletics_2|knows_weapon_master_2,swadian_face_middle_1, swadian_face_older_2],
  ["mp_swadian_sharpshooter", "German Infantry Musketeer","German Infantry Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_good_toporik,itm_good_musket_m,itm_good_bullets,
    itm_poland_uniforma_german_line_musketeer,itm_morion_good,itm_kabasset,itm_evropa_pehot_tufli],
   str_9|agi_8|level(16),wp_melee(75)|wp_crossbow(120),knows_common|knows_ironflesh_2|knows_athletics_3|knows_weapon_master_4,swadian_face_middle_1, swadian_face_old_2],
  
  ["mp_swadian_man_at_arms", "Volunteer","Volunteers",tf_mounted|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_bad_sablya_a,itm_old_pistol,itm_bad_pistol,itm_bad_bullets,
    itm_dobrotna_svitka_a,itm_dobrotna_svitka_b,itm_dobrotna_svitka_c,itm_dobrotna_svitka_d,itm_dobrotna_svitka_e,itm_old_cavalry_boots,itm_cavalry_boots,
    itm_poland_mehova_shapka_s_perom,itm_poland_good_shapka,itm_poland_mehova_shapka,itm_norm_horse,itm_bad_horse],
   str_8|agi_8|level(5),wp_melee(75)|wp_crossbow(80),knows_common|knows_riding_3|knows_horse_archery_2|knows_ironflesh_1|knows_weapon_master_3,swadian_face_middle_1, swadian_face_old_2],
  ["mp_polish_dragoon", "Dragoon","Dragoons",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_bad_sablya_b,itm_bad_karabin,itm_norm_karabin, itm_norm_shield,itm_norm_bullets,
    itm_poland_dragoon_uniform,itm_old_cavalry_boots,itm_poland_army_hat_b,itm_poland_army_hat_a,itm_norm_horse],
   str_8|agi_9|level(10),wp_melee(90)|wp_crossbow(100),knows_common|knows_riding_3|knows_horse_archery_3|knows_ironflesh_1|knows_weapon_master_3|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["mp_swadian_sergeant", "Armored Cossack","Armored Cossacks",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_norm_sablya_b,itm_norm_sablya_a,itm_good_chekan,itm_norm_shield,
    itm_norm_lance,itm_norm_luk,itm_norm_arrows,itm_kolchuga_panzernika,
    itm_cavalry_boots,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_b,itm_misurka_s_barmizoy_c,itm_good_horse],
   str_9|agi_9|level(15),wp_melee(120)|wp_archery(80),knows_common|knows_riding_4|knows_horse_archery_4|knows_power_strike_1|knows_ironflesh_2|knows_weapon_master_4|knows_power_draw_2|knows_shield_4,swadian_face_middle_1, swadian_face_old_2],
  ["mp_swadian_knight", "Winged Hussar","Winged Hussars",tf_mounted|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_gusar_lance,itm_poland_gusar_panzer,itm_poland_gusar_panzer_bez_kril,itm_good_cavalry_boots,itm_poland_gusar_helmet,itm_uber_horse,itm_norm_pistol,itm_good_bullets,itm_good_shield],
   str_10|agi_9|level(20),wp_melee(140),knows_common|knows_riding_6|knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_5,swadian_face_middle_1, swadian_face_old_2],


#----------------------------------------------------------
##########MOSK###################
#---------------------------------------------------------
  ["mp_vaegir_footman", "Posad Spearman","Posad Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bad_spear,itm_pure_streletzkiy_mundir_spear,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_8|agi_6|level(3),wp_melee(70),knows_common|knows_ironflesh_4|knows_athletics_4|knows_power_strike_1, vaegir_face_young_1, vaegir_face_young_2],
  ["mp_vaegir_veteran", "Marksman Spearman","Marksman Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_spear,itm_good_spear,itm_streletzkiy_mundir_spear,itm_sapogi,itm_m_mosk_light_helmet,itm_norm_gloves,itm_bad_toporik,itm_bad_toporik],
   str_9|agi_7|level(7),wp_melee(85),knows_common|knows_ironflesh_5|knows_athletics_5|knows_weapon_master_1|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_old_2],
  ["mp_vaegir_veteran_levelup", "Veteran Marksman Spearman","Veteran Marksman Spearmen",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_norm_pika,itm_streletzkiy_mundir_spear,itm_sapogi,itm_m_mosk_light_helmet,itm_good_gloves,itm_good_toporik,itm_m_mosk_bad_armor],
   str_9|agi_8|level(11),wp_melee(105),knows_common|knows_ironflesh_5|knows_athletics_6|knows_power_strike_3|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["mp_vaegir_infantry", "New Order Spearman","New Order Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_m_sovnya,itm_m_mosk_light_armor,itm_sapogi,itm_m_mosk_norm_helmet,itm_good_gloves],
   str_10|agi_8|level(16),wp_melee(120),knows_common|knows_ironflesh_7|knows_athletics_6|knows_power_strike_4|knows_weapon_master_3,vaegir_face_middle_1, vaegir_face_old_2],


  ["mp_vaegir_skirmisher", "Posad Marksman","Posad Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bad_toporik,itm_bad_musket,itm_bad_bullets,itm_pure_streletzkiy_mundir,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka],
   str_8|agi_6|level(3),wp_melee(30)|wp_crossbow(50),knows_common|knows_ironflesh_1|knows_athletics_2,vaegir_face_young_1, vaegir_face_young_2],
  ["mp_vaegir_archer", "Marksman","Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_bad_musket,itm_norm_musket,itm_bad_bullets,itm_norm_bullets,itm_bad_berdish,itm_streletzkiy_mundir,itm_sapogi,itm_streletz_shapka,itm_streletz_shapka_b,itm_streletz_shapka_c],
   str_9|agi_6|level(7),wp_melee(40)|wp_crossbow(75),knows_common|knows_ironflesh_2|knows_athletics_3|knows_weapon_master_1,vaegir_face_middle_1, vaegir_face_old_2],
  ["mp_vaegir_archer_levelup", "Veteran Marksman","Veteran Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_musket_m,itm_norm_bullets,itm_norm_sablya_a,itm_m_mosk_bad_armor,itm_sapogi,itm_m_mosk_light_helmet,itm_good_gloves],
   str_9|agi_7|level(11),wp_melee(60)|wp_crossbow(95),knows_common|knows_ironflesh_3|knows_athletics_4|knows_weapon_master_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["mp_vaegir_marksman", "New Order Marksman","New Order Marksmen",tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_good_musket_m,itm_good_bullets,itm_good_berdish,itm_new_line_uniform,itm_kozak_boots,itm_new_line_helmet,itm_good_gloves],
   str_10|agi_7|level(16),wp_melee(80)|wp_crossbow(110),knows_common|knows_ironflesh_4|knows_athletics_4|knows_weapon_master_3,vaegir_face_middle_1, vaegir_face_old_2],

  ["mp_vaegir_horseman", "Local Serf","Local Serfs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_m_sovnya,itm_bad_sablya_a,itm_shapka_bumajna_a,
    itm_shapka_bumajna_b,itm_bad_luk,itm_bad_arrows,itm_moskow_tulup_a,itm_moskow_tulup_b,itm_moskow_tulup_c,
    itm_selo_boots,itm_moskowit_postoli,itm_moskowit_postoli_b,itm_moskowit_shapka,itm_shishak,itm_very_bad_horse],
   str_9|agi_6|level(5),wp_melee(60)|wp_archery(55),knows_common|knows_riding_2|knows_power_draw_1|knows_ironflesh_1|knows_horse_archery_3,vaegir_face_middle_1, vaegir_face_old_2],
  ["mp_moskow_dragoon", "Gentry Cavalryman","Gentry Cavalry",tf_mounted|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_bad_arrows,itm_norm_arrows,itm_norm_luk,itm_norm_sablya_a,itm_m_sovnya,itm_cavalry_boots,
    itm_m_mosk_light_armor,itm_shapka_bumajna_a,itm_shapka_bumajna_b,itm_misurka_s_barmizoy,itm_misurka_s_barmizoy_c,itm_bad_horse,itm_norm_sablya_a,itm_m_sovnya],
   str_10|agi_7|level(10),wp_melee(75)|wp_archery(65),knows_riding_3|knows_horse_archery_4|knows_ironflesh_2|knows_power_strike_1|knows_power_draw_2|knows_weapon_master_3,vaegir_face_middle_1, vaegir_face_old_2],
  ["mp_vaegir_knight", "Reiter","Reiters",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_good_bullets,itm_norm_pistol,itm_power_pistol,itm_good_karabin,itm_norm_karabin,itm_norm_palash,itm_shelom,itm_moskow_reytar_helmet,itm_moskow_reytar_armor,itm_old_cavalry_boots,
    itm_norm_horse,itm_leather_gloves],
   str_10|agi_8|level(15),wp_melee(90)|wp_crossbow(75),knows_common|knows_riding_4|knows_horse_archery_5|knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_4,vaegir_face_middle_1, vaegir_face_old_2],
  ["mp_vaegir_guard", "Boyar Noble Guard","Boyar Noble Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_2,
   [itm_good_sablya_b,itm_m_sovnya,itm_m_sovnya,itm_m_mosk_good_armor,itm_good_cavalry_boots,itm_boyar_helmet,itm_mosk_shishak,
    itm_misurka_s_barmizoy_rich,itm_tank_horse,itm_cavalry_gloves],
   str_11|agi_7|level(20),wp_melee(135),knows_common|knows_riding_4|knows_ironflesh_3|knows_power_strike_3|knows_weapon_master_5,vaegir_face_middle_1, vaegir_face_old_2],
  
#----------------------------------------------------------
##########TATAR##################
#---------------------------------------------------------
  ["mp_khergit_skirmisher", "Kapikulu","Kapikulu",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_bad_arrows,itm_bad_bullets,itm_t_bad_sablya_a,itm_bad_luk,itm_t_bad_musket,itm_tatar_halat_pure_a,itm_tatar_halat_pure_b,itm_tatar_halat_pure_c,
    itm_bad_shield,itm_selo_boots,itm_tatar_man_hat],
   str_6|agi_6|level(3),wp_melee(55)|wp_archery(55)|wp_crossbow(55),knows_common|knows_shield_2|knows_athletics_2|knows_power_draw_1,khergit_face_younger_1, khergit_face_young_2],
  ["mp_khergit_skirmisher_levelup", "Kapikulu (veteran)","Kapikulu (veterans)",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_norm_bullets,itm_t_norm_musket,itm_t_norm_sablya_a,itm_m_ttr_light_armor_a,itm_m_ttr_light_armor_b,
    itm_norm_shield,itm_selo_boots,itm_m_ttr_norm_helmet],
   str_7|agi_7|level(7),wp_melee(70)|wp_archery(70)|wp_crossbow(70),knows_common|knows_shield_3|knows_athletics_2|knows_power_draw_2,khergit_face_middle_1, khergit_face_old_2],
  ["mp_saymen", "Seymen","Seymeni",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_bad_chekan,itm_good_boots_ttr,itm_tatar_seymen_armor,itm_tatar_misurka,itm_misurka_s_barmizoy_pure,
    itm_misurka_s_barmizoy_b,itm_gud_luk,itm_bad_arrows,itm_norm_shield],
   str_8|agi_7|level(11),wp_melee(80)|wp_crossbow(80),knows_power_strike_2|knows_shield_3|knows_athletics_3|knows_ironflesh_3|knows_power_draw_2,khergit_face_middle_1, khergit_face_old_2],
  ["mp_janissar", "Janissary","Janissaries",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_good_bullets,itm_uber_mushket,itm_m_yatagan_good,itm_janissary_tapki,itm_m_yanichar_forma,itm_janissar_hat_a,itm_janissar_hat_b,itm_good_shield],
   str_9|agi_9|level(16),wp_melee(100)|wp_crossbow(100),knows_power_strike_3|knows_shield_3|knows_ironflesh_4|knows_athletics_4|knows_weapon_master_4,man_face_young_1, man_face_old_2],
 

  ["mp_khergit_horseman", "Cebelu","Cebelu",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_bad_horse,itm_bad_boots,itm_t_bad_sablya_a,itm_m_ttr_bad_armor_a,itm_m_ttr_bad_armor_b,itm_m_pol_shapka,itm_bad_luk,itm_bad_arrows],
    str_6|agi_8|level(5),wp_melee(50)|wp_archery(60),knows_common|knows_riding_3|knows_power_draw_1|knows_horse_archery_4,khergit_face_younger_1, khergit_face_young_2],
  ["mp_khergit_horse_archer", "Veteran Cebelu","Veteran Cebelu",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_good_horse,itm_norm_arrows,itm_norm_luk,itm_t_norm_sablya_a,itm_m_ttr_light_armor_a,itm_m_ttr_light_armor_b,itm_m_ttr_shapka,itm_bad_boots_k],
   str_6|agi_9|level(10),wp_melee(60)|wp_archery(85),knows_riding_3|knows_power_draw_2|knows_horse_archery_4,khergit_face_middle_1, khergit_face_old_2],
  ["mp_khergit_veteran_horse_archer", "Circassian","Circassians",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_uber_horse,itm_m_ttr_norm_armor,itm_t_good_sablya_a,itm_m_ttr_shapka,itm_gud_luk,itm_norm_arrows,itm_norm_boots_k],
   str_7|agi_10|level(15),wp_melee(70)|wp_archery(100),knows_riding_4|knows_ironflesh_1|knows_power_draw_3|knows_horse_archery_5|knows_weapon_master_4,khergit_face_middle_1, khergit_face_old_2],
  ["mp_zyndjirli", "Veteran Circassian","Veteran Circassians",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_fast_horse,itm_norm_shield,itm_m_ttr_norm_helmet,itm_uber_luk,itm_good_arrows,itm_t_good_sablya_a,itm_m_ttr_norm_armor,itm_good_boots_ttr],
   str_8|agi_11|level(20),wp_melee(80)|wp_archery(130),knows_riding_5|knows_power_draw_4|knows_horse_archery_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_weapon_master_6,khergit_face_middle_1, khergit_face_older_2],


#----------------------------------------------------------
##########SWED###################
#---------------------------------------------------------
  ["mp_nord_footman", "Militia Pikeman","Pikeman Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_bad_pike,itm_m_swed_light_armor,itm_botinki,itm_m_swed_shapka,itm_bad_bullets,itm_bad_pistol],
   str_7|agi_7|level(3),wp_melee(65),knows_ironflesh_2,nord_face_younger_1, nord_face_young_2],
  ["mp_nord_trained_footman", "Pikeman","Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_pike_m,itm_norm_p_palash,itm_good_pike_m,itm_m_swed_norm_armor,itm_m_swed_light_helmet,itm_evropa_pehot_tufli,itm_infantry_gloves],
   str_8|agi_7|level(7),wp_melee(85),knows_weapon_master_1|knows_ironflesh_3|knows_power_strike_2,nord_face_middle_1, nord_face_old_2],
  ["mp_nord_trained_footman_levelup", "Veteran Pikeman","Veteran Pikemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_m_alebarda,itm_evropa_pika_uniforma,itm_morion_good,itm_evropa_pehot_tufli,itm_infantry_gloves],
   str_9|agi_7|level(11),wp_melee(100),knows_ironflesh_4|knows_power_strike_2|knows_weapon_master_3,nord_face_middle_1, nord_face_older_2],
  ["mp_sved_swordmaster", "Swordsman","Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_m_kleymor,itm_dospeh,itm_infantry_boots,itm_m_swed_good_p_helmet,itm_uber_gloves],
   str_12|agi_6|level(16),wp_melee(135),knows_ironflesh_5|knows_power_strike_4|knows_weapon_master_5,nord_face_middle_1, nord_face_old_2],

  ["mp_nord_huntsman", "Militia Musketeer","Musketeer Militia",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_bad_bullets,itm_bad_musket,itm_bad_shpaga, itm_bad_p_palash,
    itm_evropa_odejda_sela_b,itm_evropa_odejda_sela,itm_evropa_pehot_tufli,itm_evropa_shapka,itm_evropa_shlapa_b,itm_evropa_kava_shlapa],
   str_7|agi_7|level(3),wp_melee(40)|wp_crossbow(65),knows_athletics_1,nord_face_younger_1, nord_face_young_2],
  ["mp_nord_archer", "Musketeer","Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_norm_bullets,itm_evropa_musket_uniforma,itm_evropa_pehot_tufli,itm_evropa_musket_shlapa,
    itm_evropa_musket_shlapa_b,itm_norm_musket,itm_norm_shpaga,itm_norm_p_palash],
   str_8|agi_8|level(7),wp_melee(50)|wp_crossbow(90),knows_athletics_2|knows_weapon_master_2,nord_face_middle_1, nord_face_old_2],
  ["mp_nord_archer_levelup", "Veteran Musketeer","Veteran Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_good_bullets,itm_m_swed_light_armor,itm_norm_botforts,itm_m_swed_light_helmet,itm_good_musket_m,itm_good_shpaga_m,itm_norm_p_palash],
   str_9|agi_8|level(11),wp_melee(60)|wp_crossbow(100),knows_ironflesh_1|knows_athletics_3|knows_weapon_master_3,nord_face_middle_1, nord_face_older_2],
  ["mp_nord_veteran_archer","Reiters","Gentlemen-at-arms",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_bullets,itm_good_gloves,itm_uber_mushket,itm_good_p_palash,
    itm_evropa_guard_shlapa,itm_evropa_gvardia_uniforma,itm_good_botforts,itm_m_swed_light_helmet],
   str_9|agi_9|level(16),wp_melee(80)|wp_crossbow(120),knows_power_strike_1|knows_ironflesh_2|knows_athletics_4|knows_weapon_master_5,nord_face_middle_1, nord_face_old_2],

  ["mp_nord_warrior", "Dragoon","Dragoons",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_norm_bullets,itm_evropa_dragoon_uniforma,itm_norm_karabin,itm_bad_palash,
    itm_old_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,
    itm_very_bad_horse,itm_bad_horse,itm_infantry_gloves],
   str_7|agi_8|level(5),wp_melee(60)|wp_crossbow(80),knows_horse_archery_3|knows_riding_2|knows_weapon_master_3,nord_face_middle_1, nord_face_old_2],
  ["mp_sved_lancers", "Lancer","Lancers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_kingdom_4,
   [itm_norm_lance,itm_kirasa_b,itm_kirasa_c,itm_cavalry_botforts,itm_evropa_kava_shlapa,itm_evropa_kava_shlapa_b,itm_evropa_kava_shlapa_c,itm_evropa_shlapa,itm_good_horse,itm_infantry_gloves],
   str_9|agi_8|level(10),wp_melee(90),knows_common|knows_riding_3|knows_ironflesh_3|knows_weapon_master_4,nord_face_middle_1, nord_face_old_2],
 ["mp_nord_champion", "Cuirassier","Cuirassiers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_bullets,itm_kirasa_b,itm_kirasa_c,itm_norm_pistol,itm_good_palash_m,
    itm_cavalry_botforts,itm_m_swed_light_helmet,itm_norm_horse,itm_norm_gloves],
   str_10|agi_9|level(15),wp_melee(100)|wp_crossbow(90),knows_ironflesh_4|knows_horse_archery_4|knows_riding_3|knows_weapon_master_4,nord_face_middle_1, nord_face_old_2],
  ["mp_nord_veteran", "Reiter","Reiters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_bullets,itm_norm_karabin,itm_power_pistol,itm_reytar_armor,itm_good_cavalry_botforts,itm_reytar_helmet,itm_tank_horse,itm_uber_gloves,itm_bad_palash,itm_good_lance,itm_bad_palash,itm_good_lance],
   str_12|agi_7|level(20),wp_melee(125)|wp_crossbow(100),knows_ironflesh_5|knows_power_strike_3|knows_horse_archery_4|knows_riding_5|knows_weapon_master_6,nord_face_middle_1, nord_face_old_2],


#----------------------------------------------------------
########## UKR####################
#---------------------------------------------------------
["mp_n_rhodok_spearman", "Poor Cossack Pistoleer","Poor Cossack Pistoleers",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_bad_bullets,itm_ukraine_svitka_c,itm_bad_pistol,itm_bad_sablya_b,
    itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_selo_boots,itm_m_ukr_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli],
   str_7|agi_7|level(3),wp_melee(65)|wp_crossbow(35),knows_common|knows_ironflesh_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_young_2],
  ["mp_n_rhodok_sergeant", "Zaporozhian Pistoleer","Zaporozhian Pistoleers",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_norm_bullets,itm_kozak_jupan_c,itm_good_pistol,itm_good_spear,
    itm_m_ukr_bad_armor,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b],
   str_9|agi_8|level(7),wp_melee(70)|wp_crossbow(50),knows_common|knows_ironflesh_3|knows_power_strike_1|knows_athletics_2|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_old_2],
  ["mp_n_rhodok_trained_crossbowman", "Netyag Pistoleer","Netyag Pistoleers",tf_guarantee_boots|tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_norm_bullets,itm_m_ukr_light_armor,itm_m_ukr_norm_armor,itm_fast_pistol,itm_good_bulava,itm_kozak_boots,
   itm_kozak_shapka,itm_kozak_shapka_b,itm_kozacka_shapka_s_misurkoy,itm_misurka_s_barmizoy_pure,itm_norm_gloves],
   str_10|agi_9|level(11),wp_melee(85)|wp_crossbow(60),knows_common|knows_ironflesh_4|knows_power_strike_2|knows_athletics_3|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_old_2],
  ["mp_n_rhodok_veteran_spearman", "Serduk Pistoleer","Serduk Pistoleers",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_norm_bullets,itm_m_ukr_good_armor,itm_kozak_boots,itm_m_ukr_light_helmet,itm_good_sapogi,itm_power_pistol,itm_good_k_shablya,itm_good_spear,itm_good_spear,itm_norm_gloves],
   str_9|agi_10|level(16),wp_melee(110)|wp_crossbow(75),knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_4|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],

## Cossack ranged units 
  ["mp_rhodok_spearman", "Poor Cossack Harquebusier","Poor Cossack Harquebusiers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_bad_bullets,itm_ukraine_svitka_c,itm_samopal_m,itm_noob_dubinka,itm_ukraine_svitka_a,itm_ukraine_svitka_b,itm_selo_boots,itm_ukrine_prosta_shapka,itm_moskowit_postoli_b,itm_moskowit_postoli],
   str_7|agi_7|level(3),wp_melee(40)|wp_crossbow(65),knows_common|knows_ironflesh_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_young_2],
  ["mp_rhodok_sergeant", "Zaporozhian Infantryman","Zaporozhian Infantry",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_norm_bullets,itm_kozak_jupan_c,itm_bad_karabin,itm_norn_k_shablya,itm_kozak_jupan,itm_kozak_jupan_b,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b],
   str_9|agi_8|level(7),wp_melee(60)|wp_crossbow(85),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_athletics_3|knows_weapon_master_2,rhodok_face_middle_1, rhodok_face_old_2],
  ["mp_rhodok_trained_crossbowman", "Netyag","Netyagi",tf_guarantee_boots|tf_guarantee_ranged|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_norm_bullets,itm_good_karabin,itm_m_ukr_norm_armor,itm_bad_bulava,itm_bad_chekan,itm_bad_bulava,itm_bad_chekan,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozacka_shapka_s_misurkoy,
    itm_misurka_s_barmizoy_pure],
   str_10|agi_9|level(11),wp_melee(70)|wp_crossbow(100),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_4|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_old_2],
  ["mp_rhodok_veteran_spearman", "Serduk","Serduks",tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_good_bullets,itm_m_ukr_bad_armor,itm_kozak_boots,itm_bad_gloves,itm_serduk_shapka,itm_good_sapogi,itm_uber_karabin,itm_good_k_shablya],
   str_9|agi_10|level(16),wp_melee(80)|wp_crossbow(115),knows_common|knows_ironflesh_4|knows_power_strike_2|knows_athletics_5|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_older_2],  

  
  #replacable troop, not used
  ["new_multiplayer_troops_end", "{!}new_multiplayer_troops_end","{!}new_multiplayer_troops_end",tf_hero,0,reserved,fac_kingdom_1, [], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1", "Reiter","Reiters", tf_hero,0,0,fac_kingdom_1,
   [itm_hunter, itm_steel_bolts, itm_black_reytar_gauntlets, itm_old_cavalry_botforts, itm_simple_reytar_armor, itm_black_reytar_helmet, itm_good_palash, itm_good_pistol_c],
   str_14|agi_10|level(25),wp(200),knows_riding_4|knows_athletics_1|knows_weapon_master_5|knows_power_strike_2|knows_ironflesh_5,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2", "Hussar","Hussars", tf_hero,0,0,fac_kingdom_1,
   [itm_rich_horse, itm_leather_gloves, itm_good_cavalry_boots, itm_poland_gusar_panzer_bez_kril, itm_poland_gusar_helmet_greben, itm_gusar_lanza_b, itm_sablya_a],
   str_13|agi_12|level(25),wp(200),knows_riding_6|knows_athletics_1|knows_weapon_master_5|knows_power_strike_3|knows_ironflesh_3,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3", "Boyar","Boyars", tf_hero,0,0,fac_kingdom_1,
   [itm_rich_horse_b, itm_east_arrows, itm_cavalry_gloves, itm_cavalry_boots, itm_moskow_zertzalo, itm_mosk_shishak, itm_palitza, itm_round_shield_steel_b, itm_luk_c],
   str_14|agi_10|level(25),wp(200),knows_riding_5|knows_shield_4|knows_weapon_master_5|knows_power_strike_4|knows_ironflesh_6|knows_power_draw_3|knows_horse_archery_3,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4", "Cuirassier","Cuirassiers", tf_hero,0,0,fac_kingdom_1,
   [itm_courser, itm_infantry_gloves, itm_cavalry_botforts, itm_kirasa, itm_evropa_kava_shlapa, itm_cavalry_pika_b, itm_pehot_palash],
   str_12|agi_14|level(20),wp(150),knows_riding_5|knows_athletics_2|knows_weapon_master_3|knows_power_strike_2|knows_ironflesh_3,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5", "Mounted Archer","Mounted Archers", tf_hero,0,0,fac_kingdom_1,
   [itm_steppe_horse_b, itm_barbed_arrows, itm_kalmyk_boots, itm_tatar_steg_halat_a, itm_tatar_oglan_hat, itm_sablya_tatar_a, itm_kompozit_bow],
   str_11|agi_15|level(20),wp(150),knows_riding_4|knows_athletics_3|knows_weapon_master_2|knows_power_draw_4|knows_power_strike_1|knows_ironflesh_1|knows_horse_archery_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6", "Musketeer","Musketeers", tf_hero,0,0,fac_kingdom_1,
   [itm_bolts, itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_c, itm_prostoy_toporik, itm_good_musket],
   str_12|agi_10|level(20),wp(150),knows_athletics_3|knows_weapon_master_2|knows_power_strike_1|knows_ironflesh_1,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7", "Netyag","Netyagi", tf_hero,0,0,fac_kingdom_1,
   [itm_steel_bolts, itm_kozak_boots, itm_kozak_jupan_na_kolchuge, itm_kozak_shapka_d, itm_kozak_good_shablya, itm_good_pistol],
   str_12|agi_11|level(20),wp(150),knows_athletics_5|knows_weapon_master_4|knows_power_strike_3|knows_ironflesh_3,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8", "Swordsman","Swordsmen", tf_hero,0,0,fac_kingdom_1,
   [itm_armor_gauntlets, itm_infantry_boots, itm_dospeh, itm_armet, itm_twohand_sword],
   str_14|agi_8|level(20),wp(150),knows_athletics_1|knows_weapon_master_5|knows_power_strike_5|knows_ironflesh_5,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9", "Rondartschier","Rondartschiere", tf_hero,0,0,fac_kingdom_1,
   [itm_evropa_pehot_tufli, itm_merc_pika_uniforma_b, itm_kabasset, itm_pehot_palash, itm_rundash],
   str_13|agi_9|level(20),wp(150),knows_athletics_2|knows_shield_6|knows_weapon_master_3|knows_power_strike_1|knows_ironflesh_10,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10", "Pikeman","Pikemen", tf_hero,0,0,fac_kingdom_1,
   [itm_evropa_pehot_tufli,itm_merc_pika_uniforma_a, itm_morion, itm_good_pike, itm_pehot_palash],
   str_12|agi_10|level(20),wp(150),knows_weapon_master_3|knows_power_strike_3|knows_ironflesh_4,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11", "Halberdier","Halberdiers", tf_hero,0,0,fac_kingdom_1,
   [itm_leather_gloves, itm_infantry_boots, itm_scott_uniforma, itm_beret_c,itm_alebarda,itm_pehot_palash],
   str_12|agi_12|level(20),wp(100),knows_athletics_2|knows_weapon_master_4|knows_power_strike_2|knows_ironflesh_3,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1", "Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2", "Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3", "Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4", "Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1", "Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer", "Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1", "Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2", "Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman", "Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [ itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [ itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end", "startup merchants end","startup merchants end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader", "Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [
    ],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader", "Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_stones],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end", "bandit leaders end","bandit leaders end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end", "relative of merchants end","relative of merchants end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     
  
    ["horse_smith_pol", "Polish Armorsmith","Polish Armorsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_poland_svitka_a,itm_poland_shapka,itm_good_sapogi],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_old_1, swadian_face_old_2],
    ["horse_smith_rus", "Muscovite Armorsmith","Muscovite Armorsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_mosk_sermyaga,itm_streletz_shapka,itm_sapogi],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,vaegir_face_old_1, vaegir_face_old_2],
     ["horse_smith_tatar", "Tatar Armorsmith","Tatar Armorsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_tatar_halat_pure_b,itm_tatar_man_hat,itm_kalmyk_boots],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,khergit_face_old_1, khergit_face_old_2],
    ["horse_smith_swed", "Swedish Armorsmith","Swedish Armorsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_evropa_odejda_sela,itm_evropa_shapka,itm_evropa_pehot_tufli],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,nord_face_old_1, nord_face_old_2],
     ["horse_smith_ukr", "Cossack Armorsmith","Cossack Armorsmith",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_kozak_jupan,itm_kozak_shapka,itm_kozak_boots],
   def_attrib|agi_10|level(15),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,rhodok_face_old_1, rhodok_face_old_2],

  ["castle_1_armorer", "Armorer", "{!}Castle 1 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_armorer", "Armorer", "{!}Castle 2 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_armorer", "Armorer", "{!}Castle 3 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_armorer", "Armorer", "{!}Castle 4 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_armorer", "Armorer", "{!}Castle 5 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_armorer", "Armorer", "{!}Castle 6 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_armorer", "Armorer", "{!}Castle 7 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_armorer", "Armorer", "{!}Castle 8 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_armorer", "Armorer", "{!}Castle 9 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_armorer", "Armorer", "{!}Castle 10 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_armorer", "Armorer", "{!}Castle 11 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_armorer", "Armorer", "{!}Castle 2 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_armorer", "Armorer", "{!}Castle 3 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_armorer", "Armorer", "{!}Castle 4 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_armorer", "Armorer", "{!}Castle 5 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_armorer", "Armorer", "{!}Castle 6 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_armorer", "Armorer", "{!}Castle 7 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_armorer", "Armorer", "{!}Castle 8 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_armorer", "Armorer", "{!}Castle 9 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_armorer", "Armorer", "{!}Castle 20 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_armorer", "Armorer", "{!}Castle 11 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_armorer", "Armorer", "{!}Castle 2 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_armorer", "Armorer", "{!}Castle 3 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_armorer", "Armorer", "{!}Castle 4 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_armorer", "Armorer", "{!}Castle 5 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_armorer", "Armorer", "{!}Castle 6 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_armorer", "Armorer", "{!}Castle 7 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_armorer", "Armorer", "{!}Castle 8 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_armorer", "Armorer", "{!}Castle 9 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_armorer", "Armorer", "{!}Castle 20 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_armorer", "Armorer", "{!}Castle 11 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_armorer", "Armorer", "{!}Castle 2 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_armorer", "Armorer", "{!}Castle 3 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_armorer", "Armorer", "{!}Castle 4 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_armorer", "Armorer", "{!}Castle 5 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_armorer", "Armorer", "{!}Castle 6 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_armorer", "Armorer", "{!}Castle 7 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_armorer", "Armorer", "{!}Castle 8 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_armorer", "Armorer", "{!}Castle 9 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_armorer", "Armorer", "{!}Castle 20 armorer", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  
  ["castle_1_weaponsmith", "Weaponsmith", "{!}Castle 1 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_weaponsmith", "Weaponsmith", "{!}Castle 2 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_weaponsmith", "Weaponsmith", "{!}Castle 3 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_weaponsmith", "Weaponsmith", "{!}Castle 4 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_weaponsmith", "Weaponsmith", "{!}Castle 5 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_weaponsmith", "Weaponsmith", "{!}Castle 6 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_weaponsmith", "Weaponsmith", "{!}Castle 7 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_weaponsmith", "Weaponsmith", "{!}Castle 8 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_weaponsmith", "Weaponsmith", "{!}Castle 9 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_weaponsmith", "Weaponsmith", "{!}Castle 10 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_weaponsmith", "Weaponsmith", "{!}Castle 11 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_weaponsmith", "Weaponsmith", "{!}Castle 2 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_weaponsmith", "Weaponsmith", "{!}Castle 3 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_weaponsmith", "Weaponsmith", "{!}Castle 4 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_weaponsmith", "Weaponsmith", "{!}Castle 5 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_weaponsmith", "Weaponsmith", "{!}Castle 6 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_weaponsmith", "Weaponsmith", "{!}Castle 7 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_weaponsmith", "Weaponsmith", "{!}Castle 8 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_weaponsmith", "Weaponsmith", "{!}Castle 9 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_weaponsmith", "Weaponsmith", "{!}Castle 20 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_weaponsmith", "Weaponsmith", "{!}Castle 11 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_weaponsmith", "Weaponsmith", "{!}Castle 2 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_weaponsmith", "Weaponsmith", "{!}Castle 3 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_weaponsmith", "Weaponsmith", "{!}Castle 4 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_weaponsmith", "Weaponsmith", "{!}Castle 5 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_weaponsmith", "Weaponsmith", "{!}Castle 6 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_weaponsmith", "Weaponsmith", "{!}Castle 7 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_weaponsmith", "Weaponsmith", "{!}Castle 8 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_weaponsmith", "Weaponsmith", "{!}Castle 9 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_weaponsmith", "Weaponsmith", "{!}Castle 20 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_weaponsmith", "Weaponsmith", "{!}Castle 11 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_weaponsmith", "Weaponsmith", "{!}Castle 2 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_weaponsmith", "Weaponsmith", "{!}Castle 3 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_weaponsmith", "Weaponsmith", "{!}Castle 4 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_weaponsmith", "Weaponsmith", "{!}Castle 5 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_weaponsmith", "Weaponsmith", "{!}Castle 6 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_weaponsmith", "Weaponsmith", "{!}Castle 7 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_weaponsmith", "Weaponsmith", "{!}Castle 8 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_weaponsmith", "Weaponsmith", "{!}Castle 9 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_weaponsmith", "Weaponsmith", "{!}Castle 20 weaponsmith", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  
  ["castle_1_horse_merchant", "Horse Merchant", "{!}Castle 1 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_horse_merchant", "Horse Merchant", "{!}Castle 2 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_horse_merchant", "Horse Merchant", "{!}Castle 3 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_horse_merchant", "Horse Merchant", "{!}Castle 4 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_horse_merchant", "Horse Merchant", "{!}Castle 5 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_horse_merchant", "Horse Merchant", "{!}Castle 6 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_horse_merchant", "Horse Merchant", "{!}Castle 7 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_horse_merchant", "Horse Merchant", "{!}Castle 8 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_horse_merchant", "Horse Merchant", "{!}Castle 9 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_horse_merchant", "Horse Merchant", "{!}Castle 10 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_horse_merchant", "Horse Merchant", "{!}Castle 11 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_horse_merchant", "Horse Merchant", "{!}Castle 2 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_horse_merchant", "Horse Merchant", "{!}Castle 3 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_horse_merchant", "Horse Merchant", "{!}Castle 4 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_horse_merchant", "Horse Merchant", "{!}Castle 5 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_horse_merchant", "Horse Merchant", "{!}Castle 6 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_horse_merchant", "Horse Merchant", "{!}Castle 7 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_horse_merchant", "Horse Merchant", "{!}Castle 8 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_horse_merchant", "Horse Merchant", "{!}Castle 9 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_horse_merchant", "Horse Merchant", "{!}Castle 20 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_horse_merchant", "Horse Merchant", "{!}Castle 11 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_horse_merchant", "Horse Merchant", "{!}Castle 2 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_horse_merchant", "Horse Merchant", "{!}Castle 3 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_horse_merchant", "Horse Merchant", "{!}Castle 4 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_horse_merchant", "Horse Merchant", "{!}Castle 5 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_horse_merchant", "Horse Merchant", "{!}Castle 6 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_horse_merchant", "Horse Merchant", "{!}Castle 7 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_horse_merchant", "Horse Merchant", "{!}Castle 8 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_horse_merchant", "Horse Merchant", "{!}Castle 9 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_horse_merchant", "Horse Merchant", "{!}Castle 20 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_horse_merchant", "Horse Merchant", "{!}Castle 11 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_horse_merchant", "Horse Merchant", "{!}Castle 2 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_horse_merchant", "Horse Merchant", "{!}Castle 3 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_horse_merchant", "Horse Merchant", "{!}Castle 4 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_horse_merchant", "Horse Merchant", "{!}Castle 5 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_horse_merchant", "Horse Merchant", "{!}Castle 6 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_horse_merchant", "Horse Merchant", "{!}Castle 7 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_horse_merchant", "Horse Merchant", "{!}Castle 8 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_horse_merchant", "Horse Merchant", "{!}Castle 9 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_horse_merchant", "Horse Merchant", "{!}Castle 20 horse_merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],

  ["castle_1_merchant", "Merchant", "{!}Castle 1 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_merchant", "Merchant", "{!}Castle 2 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_merchant", "Merchant", "{!}Castle 3 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_a,itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_merchant", "Merchant", "{!}Castle 4 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_botinki, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_merchant", "Merchant", "{!}Castle 5 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_swed_civil_b, itm_evropa_shlapa],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_merchant", "Merchant", "{!}Castle 6 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_merchant", "Merchant", "{!}Castle 7 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_kozak_boots, itm_sapogi, itm_selo_boots, itm_tatar_halat_pure_a, itm_tatar_halat_pure_b, itm_ttr_civil_a, itm_ttr_civil_b, itm_tatar_bayrak_hat, itm_tatar_nogay_hat, itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_merchant", "Merchant", "{!}Castle 8 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_merchant", "Merchant", "{!}Castle 9 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_b, itm_poland_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_merchant", "Merchant", "{!}Castle 10 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_merchant", "Merchant", "{!}Castle 11 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_poland_svitka_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_merchant", "Merchant", "{!}Castle 2 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_evropa_odejda_sela_b, itm_evropa_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_merchant", "Merchant", "{!}Castle 3 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_b,itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_merchant", "Merchant", "{!}Castle 4 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a, itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_merchant", "Merchant", "{!}Castle 5 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_poland_svitka_b, itm_kozak_shapka_d],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_merchant", "Merchant", "{!}Castle 6 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_kozak_civil_jupan_b,itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_merchant", "Merchant", "{!}Castle 7 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_merchant", "Merchant", "{!}Castle 8 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_sermyaga, itm_moskowit_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_merchant", "Merchant", "{!}Castle 9 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_a, itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_merchant", "Merchant", "{!}Castle 20 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_dobrotna_svitka_b, itm_poland_good_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_merchant", "Merchant", "{!}Castle 11 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_kozak_civil_jupan_a,itm_kozak_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_merchant", "Merchant", "{!}Castle 2 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_ttr_civil_b, itm_tatar_bayrak_hat],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_merchant", "Merchant", "{!}Castle 3 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_mehova_shapka_s_perom], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_merchant", "Merchant", "{!}Castle 4 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots,itm_kozak_civil_jupan_a,itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_merchant", "Merchant", "{!}Castle 5 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi, itm_dobrotna_svitka_b,itm_poland_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_merchant", "Merchant", "{!}Castle 6 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_selo_boots, itm_dobrotna_svitka_b,itm_poland_mehova_shapka], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_merchant", "Merchant", "{!}Castle 7 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_good_sapogi, itm_dobrotna_svitka_c, itm_poland_shapka],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_merchant", "Merchant", "{!}Castle 8 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots,itm_dobrotna_svitka_a,itm_poland_mehova_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_merchant", "Merchant", "{!}Castle 9 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_civil_b,itm_streletz_shapka], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_merchant", "Merchant", "{!}Castle 20 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_ttr_civil_a, itm_tatar_nogay_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_merchant", "Merchant", "{!}Castle 11 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_mosk_sermyaga, itm_streletz_shapka_b],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_merchant", "Merchant", "{!}Castle 2 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_botinki, itm_swed_civil_a,  itm_evropa_kava_shlapa_b],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_merchant", "Merchant", "{!}Castle 3 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,itm_kozak_civil_jupan_a, itm_kozak_shapka_b], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_merchant", "Merchant", "{!}Castle 4 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_swed_civil_a,  itm_parik],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_merchant", "Merchant", "{!}Castle 5 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi, itm_dobrotna_svitka_c, itm_poland_good_shapka],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_merchant", "Merchant", "{!}Castle 6 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_evropa_pehot_tufli, itm_evropa_odejda_sela_b, itm_evropa_kava_shlapa_c], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_merchant", "Merchant", "{!}Castle 7 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_selo_boots, itm_mosk_civil_b,  itm_streletz_shapka_c],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_merchant", "Merchant", "{!}Castle 8 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_kozak_boots, itm_tatar_halat_pure_a, itm_tatar_bayrak_hat],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_merchant", "Merchant", "{!}Castle 9 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sapogi,itm_mosk_civil_a,  itm_streletz_shapka_c], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_merchant", "Merchant", "{!}Castle 20 merchant", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_sapogi,  itm_tatar_halat_pure_b,itm_tatar_man_hat],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  
["oim_monfore_tutorial", "Jaques de Clermont","Jaques de Clermont", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_kirasa_rich, itm_morion_perfect, itm_good_cavalry_botforts, itm_good_shpaga_d],
   def_attrib|str_20|agi_10|level(20),wp(75),knows_common|knows_ironflesh_10|knows_weapon_master_10|knows_riding_2,0x000000018e0034db2acc70bd118f371500000000001ca6dd0000000000000000],
  ["foot_gop", "Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_mosk_armyak,itm_mosk_sermyaga,itm_selo_boots,itm_noob_dubinka],
   def_attrib|level(1),wp(60),knows_common,bandit_face1, bandit_face2],
  ["mounted_gop", "Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots|tf_mounted|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_sumpter_horse,itm_mosk_armyak,itm_mosk_sermyaga, itm_selo_boots,itm_noob_dubinka],
   def_attrib|level(1),wp(40),knows_common|knows_riding_1,bandit_face1, bandit_face2],
  ["pahan_gop", "Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_mosk_armyak,itm_mosk_sermyaga,itm_selo_boots,itm_noob_toporik,itm_ukrine_prosta_shapka],
   def_attrib|level(1),wp(35),knows_common,bandit_face1, bandit_face2],
  ["schwarzer_ritter", "Cuirassier","Cuirassiers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_palash,itm_good_palash_b,itm_good_pistol,itm_good_pistol_c,itm_good_pistol_b,itm_bolts,itm_black_dospeh,itm_old_cavalry_botforts,itm_black_reytar_helmet,itm_hunter,itm_infantry_gloves],
   str_13|agi_7|level(21),wp_melee(100)|wp_crossbow(150),knows_ironflesh_5|knows_power_strike_2|knows_horse_archery_8|knows_riding_4|knows_weapon_master_5,nord_face_middle_1, nord_face_old_2], 
["oim_shoha1_tutorial", "Cuirassier","Cuirassiers", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_kirasa_c, itm_evropa_shlapa_b, itm_cavalry_botforts, itm_good_palash,itm_leather_gloves],
   def_attrib|str_15|agi_10|level(15),wp(50),knows_common|knows_ironflesh_5|knows_weapon_master_5|knows_riding_2,nord_face_middle_1, nord_face_old_2],
["oim_shoha2_tutorial", "Cuirassier","Cuirassiers", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_kirasa_b, itm_evropa_kava_shlapa_b, itm_infantry_boots, itm_good_palash_b, itm_infantry_gloves],
   def_attrib|str_15|agi_10|level(15),wp(50),knows_common|knows_ironflesh_5|knows_weapon_master_5|knows_riding_2,nord_face_middle_1, nord_face_old_2],

  
## NEW CAPTAIN TROOPS (ukr & crimea)

## Cossack mounted units
  ["mp_rhodok_trained_spearman", "Djura","Djura",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_bad_bullets,itm_norm_horse,itm_selo_boots,itm_prostoy_jupan_c,itm_prostoy_jupan_b,itm_prostoy_jupan,itm_norn_k_shablya,itm_bad_lance,
    itm_kozak_prosta_shapka,itm_kozak_shapka,itm_kozak_shapka_b,itm_bad_pistol,itm_bad_lance],
   str_7|agi_8|level(5),wp_melee(75)|wp_crossbow(65),knows_common|knows_riding_3|knows_ironflesh_2|knows_horse_archery_3,rhodok_face_younger_1, rhodok_face_young_2],
  ["mp_rhodok_crossbowman", "Watchman","Watchmen",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_norm_bullets,itm_m_ukr_bad_armor,itm_norm_karabin,itm_good_chekan,
    itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka,itm_good_horse,itm_bad_gloves],
   str_8|agi_9|level(10),wp_melee(90)|wp_crossbow(75),knows_common|knows_ironflesh_3|knows_power_strike_1|knows_riding_3|knows_horse_archery_4|knows_weapon_master_2,rhodok_face_middle_1, rhodok_face_old_2],
  ["mp_ukr_storoja", "Pike Watchman","Pike Watchmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_5,
   [itm_good_lance,itm_good_lance,itm_m_ukr_light_armor,itm_power_pistol,itm_good_bullets,
    itm_cavalry_boots,itm_kozak_boots,itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_prosta_shapka,itm_fast_horse],
   str_9|agi_8|level(15),wp_melee(105)|wp_crossbow(85),knows_common|knows_ironflesh_4|knows_power_strike_2|knows_riding_4|knows_horse_archery_5|knows_weapon_master_4,rhodok_face_middle_1, rhodok_face_old_2],
  ["mp_rhodok_veteran_crossbowman", "Zaporozhian Cavalryman","Zaporozhian Cavalry",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_good_bullets,itm_good_cavalry_boots,itm_cavalry_boots,itm_good_sapogi,itm_kozak_boots,itm_m_ukr_good_armor,
    itm_good_k_shablya,itm_norm_lance,itm_good_k_shablya,
    itm_kozak_shapka,itm_kozak_shapka_b,itm_kozak_shapka_c,itm_kozak_shapka_d,itm_uber_horse,itm_good_karabin],
   str_10|agi_10|level(20),wp_melee(120)|wp_crossbow(95),knows_common|knows_ironflesh_5|knows_power_strike_3|knows_riding_5|knows_horse_archery_6|knows_weapon_master_5,rhodok_face_middle_1, rhodok_face_old_2],


## Crimea Lancers
  ["mp_n_khergit_horseman", "Bajrak","Bajraks",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_good_horse,itm_m_ttr_bad_armor_a,itm_m_ttr_bad_armor_b,itm_bad_boots_k,itm_m_ttr_shapka,itm_t_bad_sablya_a,itm_bad_chekan,itm_bad_shield,itm_bad_lance],
    str_6|agi_7|level(5),wp_melee(75),knows_common|knows_riding_4|knows_shield_2,khergit_face_younger_1, khergit_face_young_2],
  ["mp_n_khergit_horse_archer", "Jasaq","Jasaqs",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_good_horse,itm_norm_boots_k,itm_m_ttr_light_armor_a,itm_m_ttr_light_armor_b,itm_m_ttr_light_helmet,itm_good_shield,itm_t_norm_sablya_a,itm_norm_lance],
   str_6|agi_8|level(10),wp_melee(85),knows_riding_5|knows_power_strike_2|knows_shield_3|knows_weapon_master_3,khergit_face_middle_1, khergit_face_old_2],
  ["mp_n_khergit_veteran_horse_archer", "Murza-chambul","Murza-chambuls",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_fast_horse,itm_good_boots_ttr,itm_m_ttr_norm_armor,itm_m_ttr_norm_helmet,itm_stal_shield,itm_good_lance,itm_t_good_sablya_a,],
   str_8|agi_9|level(15),wp_melee(100),knows_riding_6|knows_ironflesh_2|knows_shield_4|knows_power_strike_3|knows_weapon_master_4,khergit_face_middle_1, khergit_face_old_2],
  ["mp_n_zyndjirli", "Nokhor","Nokhors",tf_mounted|tf_guarantee_boots|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_uber_horse,itm_good_boots_ttr,itm_m_ttr_good_helmet,itm_m_ttr_good_armor,itm_norm_lance,itm_good_chekan,itm_stal_shield],
   str_10|agi_9|level(20),wp_melee(130),knows_riding_7|knows_ironflesh_3|knows_power_strike_4|knows_shield_5|knows_weapon_master_5,khergit_face_middle_1, khergit_face_older_2],

## CoOp troops

    ["coop_moscovite_watchmen", "Moscovite Watchman","Moscovite Watchmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_norm_horse,itm_mosk_sermyaga,itm_mosk_armyak,itm_bad_arrows,itm_bad_sablya_b,itm_bad_luk],
   str_9|agi_6|level(5),wp_melee(75)|wp_archery(60),knows_common|knows_riding_2|knows_power_draw_1|knows_ironflesh_1|knows_horse_archery_3,vaegir_face_middle_1, vaegir_face_old_2],
  ["coop_dragoons", "Dragoon","Dragoons",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_tank_horse,itm_m_swed_kava_forma,itm_bad_botforts,itm_m_swed_shapka,itm_norm_lance,itm_bad_karabin,itm_bad_bullets,itm_bad_gloves],
   str_8|agi_8|level(10),wp_melee(70)|wp_crossbow(100),knows_horse_archery_4|knows_riding_2|knows_weapon_master_3,nord_face_middle_1, nord_face_old_2],
  ["coop_cossack_wildriders", "Cossack Wildrider","Cossack Wildriders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_norm_boots_k,itm_good_horse,itm_bad_bullets,itm_power_pistol,itm_good_k_shablya,itm_m_ukr_light_armor,],
   str_10|agi_10|level(15),wp_melee(110)|wp_crossbow(110),knows_common|knows_ironflesh_4|knows_power_strike_2|knows_riding_6|knows_horse_archery_5|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["coop_crimean_horse_archers", "Crimean Horse Archer","Crimean Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_fast_horse,itm_m_ttr_norm_helmet,itm_uber_luk,itm_good_arrows,itm_t_norm_sablya_a,itm_m_ttr_norm_armor,itm_good_boots_ttr],
   str_9|agi_10|level(20),wp_melee(90)|wp_archery(135),knows_riding_7|knows_power_draw_4|knows_horse_archery_6|knows_weapon_master_4|knows_ironflesh_1,khergit_face_middle_1, khergit_face_older_2],
  ["coop_winged_hussars", "Winged Hussar","Winged Hussars",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_1,
   [itm_m_pol_good_helmet,itm_m_pol_uber_k_armor,itm_good_gloves,itm_uber_horse,itm_norm_shield,itm_gusar_lance,itm_good_sablya_a,itm_norm_boots_k],
   str_11|agi_10|level(20),wp_melee(150),knows_common|knows_riding_4|knows_ironflesh_5|knows_power_strike_4|knows_weapon_master_5,swadian_face_middle_1, swadian_face_old_2],
  
  ["coop_janissary", "Janissary","Janissary",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_m_janissar_hat,itm_m_yanichar_forma,itm_m_janissary_tapki,itm_m_yatagan_bad,itm_bad_spear,itm_bad_shield],
   str_6|agi_7|level(3),wp_melee(70)|wp_archery(60),knows_common|knows_shield_2|knows_athletics_3|knows_power_draw_2,khergit_face_younger_1, khergit_face_young_2],
  ["coop_cossack_swordmen", "Cossack Swordsman","Cossack Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_m_ukr_bad_armor,itm_m_ukr_light_helmet,itm_bad_boots_p,itm_bad_bulava,itm_good_k_shablya],
   str_10|agi_9|level(7),wp_melee(90)|wp_crossbow(60),knows_common|knows_ironflesh_2|knows_power_strike_2|knows_athletics_5|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_old_2],
  ["coop_polish_axemen", "Polish Axeman","Polish Axemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_good_toporik,itm_good_shield,itm_m_pol_norm_armor,itm_m_pol_norm_helmet,itm_bad_gloves,itm_norm_boots_p],
   str_10|agi_8|level(11),wp_melee(100),knows_common|knows_ironflesh_3|knows_athletics_3|knows_weapon_master_3|knows_power_strike_2,swadian_face_middle_1, swadian_face_older_2],
  ["coop_russian_polearmsmen", "Russian Polearmsman","Russian Polearmsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_2,
   [itm_m_mosk_notsogood_armor,itm_m_mosk_good_helmet,itm_good_gloves,itm_norm_boots_p,itm_good_berdish,itm_m_sovnya],
  str_11|agi_9|level(16),wp_melee(130),knows_common|knows_ironflesh_5|knows_athletics_3|knows_power_strike_4|knows_weapon_master_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["coop_swedish_swordsmen", "Swedish Swordsman","Swedish Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_m_kleymor,itm_norm_p_palash,itm_m_swed_uber_p_armor,itm_m_swed_good_p_helmet,itm_good_botforts,itm_uber_gloves],
   str_14|agi_7|level(16),wp_melee(150),knows_ironflesh_4|knows_power_strike_5|knows_weapon_master_6,nord_face_middle_1, nord_face_older_2],

  ["coop_volunteer_militia", "Volunteer Militia","Volunteer Militia",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_noob_dubinka,itm_bad_spear,itm_bad_musket,itm_bad_bullets,itm_m_mosk_strelok_forma,itm_bad_boots_mosk],
   str_8|agi_6|level(5),wp_melee(50)|wp_crossbow(50),knows_common|knows_athletics_2,vaegir_face_young_1, vaegir_face_young_2],
  ["coop_cossack_pistoleers", "Cossack Pistoleer","Cossack Pistoleers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_fast_pistol,itm_good_bullets,itm_norn_k_shablya,itm_m_ukr_light_armor,itm_norm_boots_p,],
   str_9|agi_9|level(7),wp_melee(90)|wp_crossbow(85),knows_common|knows_ironflesh_2|knows_power_strike_1|knows_athletics_4|knows_weapon_master_3,rhodok_face_middle_1, rhodok_face_old_2],
  ["coop_lithunian_defenders", "Lithunian Defender","Lithunian Defenders",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_good_karabin,itm_norm_bullets,itm_norm_pika,itm_m_pol_light_armor,itm_m_pol_shapka,itm_norm_gloves,itm_good_boots_p],
   str_9|agi_8|level(11),wp_melee(80)|wp_crossbow(95),knows_common|knows_ironflesh_3|knows_athletics_3|knows_weapon_master_3,swadian_face_middle_1, swadian_face_older_2],
  ["coop_crimean_hawkeyes", "Crimean Hawkeye","Crimean Hawkeyes",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_uber_luk,itm_norm_arrows,itm_bad_chekan,itm_norm_shield,itm_tatar_seymen_armor,itm_norm_boots_p],
   str_11|agi_9|level(16),wp_melee(95)|wp_archery(115),knows_power_strike_3|knows_ironflesh_3|knows_athletics_5|knows_weapon_master_5|knows_power_draw_4,man_face_middle_1, man_face_older_2],
  ["coop_miquelet_musketeers", "Miquelet Musketeer","Miquelet Musketeers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_good_bullets,itm_uber_mushket,itm_m_swed_light_helmet,itm_m_swed_light_armor,itm_good_gloves,itm_good_botforts,itm_norm_shpaga],
   str_11|agi_10|level(16),wp_melee(80)|wp_crossbow(130),knows_power_strike_1|knows_ironflesh_3|knows_athletics_4|knows_weapon_master_4,nord_face_middle_1, nord_face_older_2],
   
   ["coop_troops_end", "{!}coop_troops_end","{!}coop_troops_end",0,0,0,fac_kingdom_4,
   [], 0,0,0,nord_face_middle_1, nord_face_older_2],
]

upgrade(troops,"farmer", "townsman")
upgrade(troops,"townsman","watchman")

upgrade2(troops,"swadian_recruit","swadian_skirmisher","swadian_militia")
upgrade(troops,"swadian_militia","swadian_militia_levelup")
upgrade(troops,"swadian_skirmisher","swadian_skirmisher_levelup")
upgrade(troops,"swadian_crossbowman","swadian_crossbowman_levelup")
upgrade(troops,"swadian_footman","swadian_footman_levelup")
upgrade(troops,"swadian_man_at_arms","swadian_man_at_arms_levelup")
upgrade(troops,"polish_dragoon","polish_dragoon_levelup")
upgrade(troops,"swadian_infantry","swadian_infantry_levelup")
upgrade(troops,"swadian_sharpshooter","swadian_sharpshooter_levelup")
upgrade(troops,"swadian_sergeant","swadian_sergeant_levelup")
upgrade(troops,"polish_reytar","polish_reytar_levelup")
upgrade(troops,"swadian_knight","swadian_knight_levelup")
upgrade(troops,"reestrovuy_kozak","reestrovuy_kozak_levelup")
upgrade(troops,"gorod_kozak","gorod_kozak_levelup")
upgrade(troops,"litva_musket","litva_musket_levelup")
upgrade(troops,"litva_lipki","litva_lipki_levelup")

upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade(troops,"nord_huntsman","nord_huntsman_levelup")
upgrade(troops,"nord_footman","nord_footman_levelup")
upgrade(troops,"nord_trained_footman","nord_trained_footman_levelup")
upgrade(troops,"nord_archer","nord_archer_levelup")
upgrade(troops,"sved_swordmaster","sved_swordmaster_levelup")
upgrade(troops,"nord_veteran_archer","nord_veteran_archer_levelup")
upgrade(troops,"nord_warrior","nord_warrior_levelup")
upgrade(troops,"nord_champion","nord_champion_levelup")
upgrade(troops,"sved_lancers","sved_lancers_levelup")
upgrade(troops,"nord_veteran","nord_veteran_levelup")
upgrade(troops,"finn_arcebuz","finn_arcebuz_levelup")
upgrade(troops,"merc_reytar","merc_reytar_levelup")
upgrade(troops,"pruss_pike","pruss_pike_levelup")

upgrade2(troops,"vaegir_recruit","vaegir_footman","vaegir_skirmisher")
upgrade(troops,"vaegir_skirmisher","vaegir_skirmisher_levelup")
upgrade(troops,"vaegir_footman","vaegir_footman_levelup")
upgrade(troops,"vaegir_archer","vaegir_archer_levelup")
upgrade(troops,"vaegir_veteran","vaegir_veteran_levelup")
upgrade(troops,"vaegir_infantry","vaegir_infantry_levelup")
upgrade(troops,"vaegir_marksman","vaegir_marksman_levelup")
upgrade(troops,"vaegir_horseman","vaegir_horseman_levelup")
upgrade(troops,"moskow_dragoon","moskow_dragoon_levelup")
upgrade(troops,"vaegir_knight","vaegir_knight_levelup")
upgrade(troops,"vaegir_guard","vaegir_guard_levelup")
upgrade(troops,"don_cossack","don_cossack_levelup")

upgrade2(troops,"rhodok_tribesman","rhodok_spearman","ukr_golota")
upgrade(troops,"ukr_golota","ukr_golota_levelup")
upgrade(troops,"rhodok_spearman","rhodok_spearman_levelup")
upgrade(troops,"rhodok_sergeant","rhodok_sergeant_levelup")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_trained_crossbowman_levelup")
upgrade(troops,"rhodok_veteran_spearman","rhodok_veteran_spearman_levelup")
upgrade(troops,"rhodok_trained_spearman","rhodok_trained_spearman_levelup")
upgrade(troops,"rhodok_crossbowman","rhodok_crossbowman_levelup")
upgrade(troops,"ukr_storoja","ukr_storoja_levelup")
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_veteran_crossbowman_levelup")

upgrade2(troops,"khergit_tribesman","khergit_skirmisher","khergit_horseman")
upgrade(troops,"khergit_skirmisher","khergit_skirmisher_levelup")
upgrade(troops,"khergit_horseman","khergit_horseman_levelup")
upgrade(troops,"khergit_lancer","khergit_lancer_levelup")
upgrade(troops,"khergit_horse_archer","khergit_horse_archer_levelup")
upgrade(troops,"saymen","saymen_levelup")
upgrade(troops,"asak_bey","asak_bey_levelup")
upgrade(troops,"khergit_veteran_horse_archer","khergit_veteran_horse_archer_levelup")
upgrade(troops,"zyndjirli","zyndjirli_levelup")
upgrade(troops,"ttr_nogay","ttr_nogay_levelup")
upgrade(troops,"ttr_cherkes","ttr_cherkes_levelup")

upgrade(troops,"janissar","janissar_levelup")
upgrade(troops,"basurman_azap","basurman_azap_levelup")
upgrade(troops,"basurman_jebelu","basurman_jebelu_levelup")
upgrade(troops,"scott_musket","scott_musket_levelup")
upgrade(troops,"scott_pika","scott_pika_levelup")
upgrade(troops,"scott_sword","scott_sword_levelup")
upgrade(troops,"rundashir","rundashir_levelup")
upgrade(troops,"tatar_merc_peh","tatar_merc_peh_levelup")
upgrade(troops,"tatar_merc_cav","tatar_merc_cav_levelup")

upgrade(troops,"looter","mountain_bandit")

upgrade(troops,"bandit","brigand")

upgrade(troops,"tatar_merch_novice_infantry","tatar_merch_regular_infantry")
upgrade(troops,"tatar_merch_regular_infantry","tatar_merch_veteran_infantry")
upgrade(troops,"tatar_merch_veteran_infantry","tatar_merch_champion_infantry")

upgrade(troops,"kazak_merch_novice_infantry","kazak_merch_regular_infantry")
upgrade(troops,"kazak_merch_regular_infantry","kazak_merch_veteran_infantry")
upgrade(troops,"kazak_merch_veteran_infantry","kazak_merch_champion_infantry")

upgrade(troops,"polyak_merch_novice_infantry","polyak_merch_regular_infantry")
upgrade(troops,"polyak_merch_regular_infantry","polyak_merch_veteran_infantry")
upgrade(troops,"polyak_merch_veteran_infantry","polyak_merch_champion_infantry")

upgrade(troops,"shved_merch_novice_infantry","shved_merch_regular_infantry")
upgrade(troops,"shved_merch_regular_infantry","shved_merch_veteran_infantry")
upgrade(troops,"shved_merch_veteran_infantry","shved_merch_champion_infantry")

upgrade(troops,"moskov_merch_novice_infantry","moskov_merch_regular_infantry")
upgrade(troops,"moskov_merch_regular_infantry","moskov_merch_veteran_infantry")
upgrade(troops,"moskov_merch_veteran_infantry","moskov_merch_champion_infantry")

upgrade(troops,"tatar_merch_novice_archer","tatar_merch_regular_archer")
upgrade(troops,"tatar_merch_regular_archer","tatar_merch_veteran_archer")
upgrade(troops,"tatar_merch_veteran_archer","tatar_merch_champion_archer")

upgrade(troops,"kazak_merch_novice_archer","kazak_merch_regular_archer")
upgrade(troops,"kazak_merch_regular_archer","kazak_merch_veteran_archer")
upgrade(troops,"kazak_merch_veteran_archer","kazak_merch_champion_archer")

upgrade(troops,"polyak_merch_novice_archer","polyak_merch_regular_archer")
upgrade(troops,"polyak_merch_regular_archer","polyak_merch_veteran_archer")
upgrade(troops,"polyak_merch_veteran_archer","polyak_merch_champion_archer")

upgrade(troops,"shved_merch_novice_archer","shved_merch_regular_archer")
upgrade(troops,"shved_merch_regular_archer","shved_merch_veteran_archer")
upgrade(troops,"shved_merch_veteran_archer","shved_merch_champion_archer")

upgrade(troops,"moskov_merch_novice_archer","moskov_merch_regular_archer")
upgrade(troops,"moskov_merch_regular_archer","moskov_merch_veteran_archer")
upgrade(troops,"moskov_merch_veteran_archer","moskov_merch_champion_archer")

upgrade(troops,"tatar_merch_novice_horse","tatar_merch_regular_horse")
upgrade(troops,"tatar_merch_regular_horse","tatar_merch_veteran_horse")
upgrade(troops,"tatar_merch_veteran_horse","tatar_merch_champion_horse")

upgrade(troops,"kazak_merch_novice_horse","kazak_merch_regular_horse")
upgrade(troops,"kazak_merch_regular_horse","kazak_merch_veteran_horse")
upgrade(troops,"kazak_merch_veteran_horse","kazak_merch_champion_horse")

upgrade(troops,"polyak_merch_novice_horse","polyak_merch_regular_horse")
upgrade(troops,"polyak_merch_regular_horse","polyak_merch_veteran_horse")
upgrade(troops,"polyak_merch_veteran_horse","polyak_merch_champion_horse")

upgrade(troops,"shved_merch_novice_horse","shved_merch_regular_horse")
upgrade(troops,"shved_merch_regular_horse","shved_merch_veteran_horse")
upgrade(troops,"shved_merch_veteran_horse","shved_merch_champion_horse")

upgrade(troops,"moskov_merch_novice_horse","moskov_merch_regular_horse")
upgrade(troops,"moskov_merch_regular_horse","moskov_merch_veteran_horse")
upgrade(troops,"moskov_merch_veteran_horse","moskov_merch_champion_horse")