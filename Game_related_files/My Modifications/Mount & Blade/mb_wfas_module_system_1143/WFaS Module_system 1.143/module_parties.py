from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar", "Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

  ("town_1", "Koenigsberg", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.55, -8.5),[], 170),
  ("town_2", "Reval", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64, 66),[], 120),
  ("town_3", "Kiev", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.192857, -48.330658),[], 80),
  ("town_4", "Vilna", icon_ewro_fort|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.83, 5.32),[], 290),
  ("town_5", "Sich", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.28, -60.79),[], 90),
  ("town_6", "Warsaw", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.24, -34.71),[], 155),
  ("town_7", "Lviv", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36, -60.48),[], 240),

  ("town_8", "Moscow", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.671, 74.781),[], 175),
  ("town_9", "Pskov", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.79, 56.89),[], 90),
  ("town_10", "Azaq-kale", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.32, -55.91),[], 310),
  ("town_11", "Cherkassk", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.74, -44.94),[], 150),
  ("town_12", "Riga", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-61.82, 35),[], 25),
  ("town_13", "Smolensk", icon_rus_castle|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(42.518, 35.922),[], 60),
  ("town_14", "Bakhchisaray", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52, -97.8),[], 135),

  ("town_15", "Chernigov", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.99, -29.37),[], 135),
  ("town_16", "Krakov", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54, -55.98),[], 135),
  ("town_17", "Akkerman", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.02, -100.29),[], 135),
  ("town_18", "Kyzykermen", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.95, -71.87),[], 135),

#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1", "Zbarazh Fortress", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.28, -52.88),[],50),
  ("castle_2", "Kezlev Fortress", icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.18, -94.74),[],75),
  ("castle_3", "Polotsk", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.38, 28.59),[],100),
  ("castle_4", "Vyborg", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32, 96.2),[],180),
  ("castle_5", "Dzvinsk Castle", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36, 42.74),[],90),
  ("castle_6", "Novgorod", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.45, 92.41),[],55),
  ("castle_7", "Kilburun Fortress", icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.39, -79.66),[],45),
  ("castle_8", "Tver'", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.264, 78.142),[],30),
  ("castle_9", "Poltava", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.22, -22.3527),[],100),
  ("castle_10", "Kovno Fortress", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.82, 13.37),[],110),
  ("castle_11", "Myadzelsk Castle", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.12, 30.23),[],75),
  ("castle_12", "Narva", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.44, 73.51),[],95),
  ("castle_13", "Slutsk", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.68, -15.22),[],115),
  ("castle_14", "Bratslav", icon_rus_castle|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.34, -70.27),[],90),
  ("castle_15", "Cherkassy", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.457, -53.226),[],235),
  ("castle_16", "Korsun", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17, -57.94),[],45),
  ("castle_17", "Perekop", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.676 , -83.257),[],15),
  ("castle_18", "Rzhev Fortress", icon_rus_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.975, 57.794),[],300),
  ("castle_19", "Kursk", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.13, 15.6),[],280),
  ("castle_20", "Lodz Castle", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.15, -64.52),[],260),
  ("castle_21", "Pereyaslav", icon_ukr_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.33, -34.36),[],260),
  ("castle_22", "Kafa", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.53, -90.42),[],260),
  ("castle_23", "Dubensk Castle", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.336, -51.239),[],80),
  ("castle_24", "Kamenets", icon_ewro_fort|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.40, -93.347),[],260),
  ("castle_25", "Lublin", icon_ewro_fort|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.51, -33.79),[],260),
  ("castle_26", "Minsk", icon_ewro_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.7369, -27.73),[],260),
  ("castle_27", "Berestye Fortress", icon_rus_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.95, -23.63),[],260),
  ("castle_28", "Bar Fortress", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.99, -69.95),[],260),
  ("castle_29", "Bryansk Fortress", icon_rus_town|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.94, 6.25),[],280),
  ("castle_30", "Izmail Fortress", icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.16, -88.58),[],260),
  ("castle_31", "Ryazan", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(98.311, 63.525),[],260),
  ("castle_32", "Allenstein Castle", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87, -20.7),[],260),
  ("castle_33", "Ladyzhyn Fortress", icon_rus_castle|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.98, -72.52),[],80),
  ("castle_34", "Dorpat Fortress", icon_ewro_town|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.13, 52.36),[],260),
  ("castle_35", "Lida Castle", icon_ewro_fort|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.35, -7.571),[],260),
  ("castle_36", "Dynaburg Fortress", icon_ewro_town|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.32, 39.6),[],260),
  ("castle_37", "Tula", icon_rus_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.988, 49.865),[],260),
  ("castle_38", "Kalanchak Fortress", icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.32, -85),[],260),
  ("castle_39", "Izum Fortress", icon_rus_town|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.41, -33.56),[],280),
  ("castle_40", "Kyzyl-yar Fortress", icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.76, -54.85),[],260),
 
# Rinimad      
# Rietal Derchios Gerdus
# Tuavus Pamir Vezona 
  
  ("village_1", "Plotsk", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.12,-45.94),[], 100),
  ("village_2", "Wadowice", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.92,-60.23),[], 110),
  ("village_3", "Ovruch", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-18,0.44),[], 120),
  ("village_4", "Dunayivtsi", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.3,-89.41),[], 130),
  ("village_5", "Elbing", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-97.4, -19.54),[], 170),
  ("village_6", "Widawa", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.19,-68.17),[], 100),
  ("village_7", "Amere", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76.44, -84.8),[], 110),
  ("village_8", "Wesenberg", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52.64, 66.16),[], 120),
  ("village_9", "Pohrebysche", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3.009, -63.56),[], 130),
  ("village_10", "Redkino", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53.833, 81.383),[], 170),

  ("village_11", "Ordash", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.46, -73),[], 100),
  ("village_12", "Boguslav", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.36, -63.7),[], 110),
  ("village_13", "Stryi", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.45, -75.00),[], 120),
  ("village_14", "Slantsy", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.31, 63.46),[], 130),
  ("village_15", "Baranovichi", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.12,-24.78),[], 170),
  ("village_16", "Tarusa", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.874, 66.518),[], 170),
  ("village_17", "Krivichi", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.34, 53.2),[], 35),
  ("village_18", "Ponyri", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.51, 32.25),[], 170),
  ("village_19", "Pokrovskoye", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(74.535 , 42.43),[], 170),
  ("village_20", "Yefremovo", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.3, 21.16),[], 170),

  ("village_21", "Oboyan", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.4 , 1.81),[], 100),
  ("village_22", "Lgov", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.26, 3.27),[], 110),
  ("village_23", "Magdalenovka", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.63, -32.24),[], 120),
  ("village_24", "Sinelnikovo", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.11, -51.98),[], 130),
  ("village_25", "Dzhankoy", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.76, -86.68),[], 170),
  ("village_26", "Snovsk", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.73,-23.09),[], 170),
  ("village_27", "Slavuta", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10 , -46.79),[], 170),
  ("village_28", "Sivash", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.97, -78.9),[], 170),
  ("village_29", "Siegevold", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.75,48.18),[], 170),

  ("village_30", "Salis", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.11, 44.31),[], 170),
  ("village_31", "Pilve", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.5, 48.24),[], 100),
  ("village_32", "Staronowice", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.5, -41),[], 110),
  ("village_33", "Radzilow", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.97, -25.27),[], 120),
  ("village_34", "Molodechno", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.019, -14.731),[], 130),
  ("village_35", "Snechko", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.21, 35.13),[], 170),
  ("village_36", "Nidritsa", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.19, -29.93),[], 170),
  ("village_37", "Budjak", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.28, -92.5),[], 170),
  ("village_38", "Solechniki", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.62, -16.34),[], 170),
  ("village_39", "Ostrovets", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.07, 6.4),[], 170),
  ("village_40", "Kryliv", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.48, -59.89),[], 170),

  ("village_41", "Tumnek", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(92.1, -76.76),[], 100),
  ("village_42", "Pologi", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.68, -62),[], 110),
  ("village_43", "Ak-Mechet", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.36, -92.884),[], 120),
  ("village_44", "Esaq", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(94.94, -63.72),[], 130),
  ("village_45", "Inkerman", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.189 , -93.217),[], 170),
  ("village_46", "Ilyintsy", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-6.63, -65.6899),[], 170),
  ("village_47", "Zolotonosha", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28, -44.69),[], 170),
  ("village_48", "Potoki", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-22.61, -76.1),[], 170),
  ("village_49", "Nugai", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.7, -41.4),[], 10),
  ("village_50", "Sofronovo", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.73, 43.89),[], 170),

  ("village_51", "Weissenstein", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-52, 57.26),[], 100),
  ("village_52", "Khorol", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.86, -30.27),[], 110),
  ("village_53", "Nesvizh", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.248, -8.536),[], 120),
  ("village_54", "Chenstokhova", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.45, -53.97),[], 130),
  ("village_55", "Luga", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.558, -57.445),[], 170),
  ("village_56", "Torma", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-42.72, 65.52),[], 170),
  ("village_57", "Babice", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.19, -71.94),[], 170),
  ("village_58", "Yartsy", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.194, 61.428),[], 170),
  ("village_59", "Loyew", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.1 , -32.73),[], 170),
  ("village_60", "Dobrush", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.34, -21.357),[], 170),

  ("village_61", "Leal", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-66.95, 56.02),[], 100),
  ("village_62", "Staritsa", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.819, 66.397),[], 100),
  ("village_63", "Ostroleka", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.71, -30.75),[], 100),
  ("village_64", "Kobelyaki", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.55, -42.07),[], 100),
  ("village_65", "Dubechnya", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.6, -39.5),[], 100),
  ("village_66", "Zamoshye", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.97, 14.27),[], 100),
  ("village_67", "Rudnya", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.26, 32.64),[], 100),
  ("village_68", "Lubenets", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.47, -23.44),[], 100),
  ("village_69", "Tapiau", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.64, -6.29),[], 100),
  ("village_70", "Lyubotin", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.11, -43.4),[], 100),

  ("village_71", "Sambir", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.22, -78.69),[], 20),
  ("village_72", "Vydzy", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.014, 15.311),[], 60),
  ("village_73", "Kozelets", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.96, -26.15),[], 55),
  ("village_74", "Klin", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(69.37, 79.286),[], 15),
  ("village_75", "Ludinovo", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.54 , 15.13),[], 10),
  ("village_76", "Czaple", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.72,  -80.6),[], 35),
  ("village_77", "Panevezys", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.36, 24.12),[], 160),
  ("village_78", "Pavoloch", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(5.553, -44.845),[], 180),
  ("village_79", "Borispol", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.33, -38.45),[], 0),
  ("village_80", "Vendau", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.79, 19.41),[], 40),

  ("village_81", "Siauliai", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.64, 24.6),[], 20),
  ("village_82", "Trakai", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.77, -1.7),[], 60),
  ("village_83", "Lisyanka", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.82, -65.53),[], 55),
  ("village_84", "Maslov Brod", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.82, -53.53),[], 15),
  ("village_85", "Loknya", icon_village_pol_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.44, 39.98),[], 10),
  ("village_86", "Valuiki", icon_oim_rus_derevnya|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.83, -11.52),[], 35),
  ("village_87", "Plunge", icon_village_swed_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-85.65, 6.1),[], 160),
  ("village_88", "Kiliya", icon_village_ttr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.21, -73.9),[], 180),
  ("village_89", "Leschinovka", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(36.03, -44.15),[], 0),
  ("village_90", "Kolomak", icon_village_ukr_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(55.33, -17.31),[], 40),
  
  ("salt_mine", "Salt Mine", icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99.66, -80.8),[]),
  ("four_ways_inn", "Four Ways Inn", icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.59, 9.22),[]),
  ("test_scene", "test scene", icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields", "battlefields", pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(9.53, -11.85),[]),
  ("dhorak_keep", "Dhorak Keep", icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.79,-60.13),[]),

  ("training_ground", "Mercenary camp", pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.12, 5.07),[]),

  ("training_ground_1", "Mercenary camp", icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(72.87,66.2),[], 100),
  ("training_ground_2", "Mercenary camp", icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.3, 52.47),[], 100),
  ("training_ground_3", "Mercenary camp", icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.89, -56.94),[], 100),
  ("training_ground_4", "Mercenary camp", icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(48.6 , -90.58),[], 100),
  ("training_ground_5", "Mercenary camp", icon_training_ground|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.32, -65.48),[], 100),
  ("temp_party_3", "{!}temp party 3", pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),

#  bridge_a
  ("bridge_1", "{!}1", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.25, 36.43),[], 4),
  ("bridge_2", "{!}2", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.53, 2.78),[], 7),
  ("bridge_3", "{!}3", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.67, 17.47),[], 79),
  ("bridge_4", "{!}4", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(8.81, -78.97),[], 103),
  ("bridge_5", "{!}5", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.921, 75.508),[], 45),
  ("bridge_6", "{!}6", icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.41, -40.28),[], 149),
  ("bridge_7", "{!}7", icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.04, -70.75),[], 63),
  ("bridge_8", "{!}8", icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.0635, -47.21),[], 163),
  ("bridge_9", "{!}9", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.66, -28.06),[], 22),
  ("bridge_10", "{!}10", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.7, -74),[], 0),
  ("bridge_11", "{!}11", icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-82.25, -38.864),[], 10),
  ("bridge_12", "{!}12", icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12.04, 36.86),[], 10),
  ("bridge_13", "{!}13", icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.22, -49.27),[], 23),
  ("bridge_14", "{!}14", icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.79, -17.2),[], 74),
  ("bridge_15", "{!}15", icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-41.8, -77.05),[], 0),
  #looter/bandit
  ("steppe_bandit_spawn_point_1", "{!}steppe bandit sp 1", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(46.77, -85.73),[]),
  ("steppe_bandit_spawn_point_2", "{!}steppe bandit sp 2", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(59.50, -67.00),[]),
  ("forest_bandit_spawn_point_1", "{!}forest bandit sp 1", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-34, -43.77),[]),
  ("mountain_bandit_spawn_point_1", "{!}mountain bandit sp 1", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(56.07, 53.01),[]),
  ("sea_raider_spawn_point_1", "{!}sea raider sp", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-76.22, -1.52),[]),
  ("sea_raider_spawn_point_2", "{!}sea raider sp", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-55.84, 55.57),[]),
 # add extra towns before this point     
  ("forest_bandit_spawn_point_2", "{!}forest bandit sp 2", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-19.65, -58.13),[]),
  ("mountain_bandit_spawn_point_2", "{!}mountain bandit sp 2", pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(12.00, 76.67),[]),
  ("spawn_points_end", "{!}last_spawn_point", pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[]),
  ("reserved_1", "{!}reserved 1", pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[]),
  ("reserved_2", "{!}reserved 2", pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[]),
  ("reserved_3", "{!}reserved 3", pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[]),
  ]