from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
# Tutorial:
  (0.1, 0, ti_once, [(map_free,0)], [(dialog_box, "str_oim_training_12_text", "str_oim_training_12_caption")]),

#  (1.0, 0, ti_once, [(map_free,0)], [(start_map_conversation,"trp_guide")]),

# Refresh Merchants
  (0.0, 0, 24.0, [],
  [
    (store_mod, ":mod_result", "$g_production_day_count_for_town", 7),
    (try_begin),
      (eq, ":mod_result", 0),
      (call_script, "script_refresh_center_inventories"),
      (call_script, "script_refresh_center_armories"),
      (call_script, "script_refresh_center_stables"),
      (call_script, "script_refresh_center_weaponsmiths"),
    (try_end),
    (val_add, "$g_production_day_count_for_town", 1),
  ]),

# Refresh Armor sellers
  (0.0, 0, 24.0, [],
  [
   #(store_mod, ":mod_result", "$g_production_day_count_for_town", 7),
   #(try_begin),
   #  (eq, ":mod_result", 0),      
   #  (call_script, "script_refresh_center_armories"),
   #(try_end),
  ]),

# Refresh Mercanaries count
#oim code  
  (0.0, 0, ti_once, [],
  [
    (call_script, "script_set_merch_item_parametres"),
    (assign, "$g_wagenburg_is_on", 0),
    (assign, "$g_ai_wagenburg_is_on", 0),
    (assign, "$g_diplomatic_capital", 0),
    (assign, "$g_select_capital_dialog", 0),
    (assign, "$g_ambassador_dialog", 0),
    (assign, "$g_select_extra_good_dialog", 0),
    (assign, "$g_select_extra_officer_dialog", 0),
  ]),	
  
  (0.0, 0, 168.0, [],
  [
    (call_script, "script_set_merch_limit"),
  ]),					 
#oim code

# Refresh Weapon sellers
  (0.0, 0, 24.0, [],
  [
    #(store_mod, ":mod_result", "$g_production_day_count_for_town", 7),
    #(try_begin),
    #  (eq, ":mod_result", 0),
    #  (call_script, "script_refresh_center_weaponsmiths"),
    #(try_end),
  ]),

# Refresh Horse sellers
  (0.0, 0, 24.0, [],
  [
    #(store_mod, ":mod_result", "$g_production_day_count_for_town", 7),		
    #(try_begin),
    #  (eq, ":mod_result", 0),
    #  (call_script, "script_refresh_center_stables"),
    #(try_end),
  ]),
  
#############

#Captivity:

#  (1.0, 0, 0.0, [],
#   [
#       (ge,"$captivity_mode",1),
#       (store_current_hours,reg(1)),
#       (val_sub,reg(1),"$captivity_end_time"),
#       (ge,reg(1),0),
#       (display_message,"str_nobleman_reached_destination"),
#       (jump_to_menu,"$captivity_end_menu"),
#    ]),


  (5.7, 0, 0.0, [(store_num_parties_created,reg(3),"pt_manhunters"),
                 (lt,reg(3),num_max_zendar_manhunters),
                 (store_num_parties_of_template, reg(2), "pt_manhunters"), (lt,reg(2),3)],
                       [(set_spawn_radius,1),(spawn_around_party,"p_zendar","pt_manhunters")]),
#  (5.2, 0, 0.0, [(store_num_parties_created,reg(3),"pt_peasant"),(lt,reg(3),num_max_zendar_peasants),
#                 (store_num_parties_of_template, reg(2), "pt_peasant"), (lt,reg(2),3)],
#                          [(set_spawn_radius,1),(spawn_around_party,"p_zendar","pt_peasant")]),




#Tax Collectors
# Prisoner Trains
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),
#
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),			   
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),

##Caravans
#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
##               (party_is_in_any_town,reg(2)),
##               ],
##              [(store_faction_of_party, ":faction_no", reg(2)),
##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
##               (party_set_ai_object,reg(2),reg0),
##               (party_set_flags, reg(2), pf_default_behavior, 0),
##            ]),
  
  (4.0, 0, 0.0, [(eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
                 (get_party_ai_object,reg(1),"$caravan_escort_party_id"),
                 (neq,reg(1),"$caravan_escort_destination_town"),
                ],
                     [(assign,"$caravan_escort_state",0),
#                      (add_xp_as_reward,100),
                      ]),

#Messengers
#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_swadians"),
#    (assign, "$pin_party_template", "pt_swadian_messenger"),
#    (assign, "$pin_limit", peak_kingdom_messengers),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_vaegirs"),
#    (assign, "$pin_party_template", "pt_vaegir_messenger"),
#    (assign, "$pin_limit", peak_kingdom_caravans),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

  (1.5, 0, 0, [(store_random_party_of_template, reg(2), "pt_messenger_party"),
               (party_is_in_any_town,reg(2)),
               ],
   [(store_faction_of_party, ":faction_no", reg(2)),
    (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),	
    (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
    (party_set_ai_object,reg(2),reg0),
    (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),
  
  

#Deserters

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
  
#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##      (try_end),
      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
##      (try_end),
    (try_end),
    ]),


#Swadians
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),


#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_foragers"),
#                         (assign, "$pin_limit", "$peak_swadian_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_scouts"),
#                         (assign, "$pin_limit", "$peak_swadian_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_patrol"),
#                         (assign, "$pin_limit", "$peak_swadian_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_war_party"),
#                         (assign, "$pin_limit", "$peak_swadian_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
#Vaegirs
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_war_parties",2)]),
  

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_foragers"),
#                         (assign, "$pin_limit", "$peak_vaegir_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_scouts"),
#                         (assign, "$pin_limit", "$peak_vaegir_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_patrol"),
#                         (assign, "$pin_limit", "$peak_vaegir_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_war_party"),
#                         (assign, "$pin_limit", "$peak_vaegir_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Villains etc.
#  (14.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_sea_raiders"),
#                         (assign, "$pin_party_template", "pt_sea_raiders"),
#                         (assign, "$pin_limit", 5),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),


#
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_refugees"),
##                         (assign, "$pin_limit", 5),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),
##
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_farmers"),
##                         (assign, "$pin_limit", 6),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#  [1.0, 96.0, ti_once, [], [[assign,"$peak_dark_hunters",3]]],
  
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_dark_hunters"),
##                         (assign, "$pin_limit", "$peak_dark_hunters"),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#Companion quests

##  (0, 0, ti_once,
##   [
##       (entering_town,"p_town_1"),
##       (main_party_has_troop,"trp_borcha"),
##       (eq,"$borcha_freed",0)
##    ],
##   
##   [
##       (assign,"$borcha_arrive_sargoth_as_prisoner",1),
##       (start_map_conversation,"trp_borcha")
##    ]
##   ),
##
##  (1, 0, ti_once,
##   [
##      (map_free,0),
##      (eq,"$borcha_asked_for_freedom",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation,"trp_borcha")
##    ]
##   ),
##  
##  (2, 0, ti_once,
##   [
##      (map_free, 0),
##      (neq,"$borcha_asked_for_freedom",0),
##      (eq,"$borcha_freed",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation,"trp_borcha"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),
### Defend Nobles Against Peasants quest
##  (0.2, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_succeeded, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_failed, "qst_defend_nobles_against_peasants"),
##       (quest_get_slot, ":quest_target_center", "qst_defend_nobles_against_peasants", slot_quest_target_center),
##       (assign, ":num_active_parties", 0),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_1", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_2", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_3", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_4", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_5", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_6", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_7", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_8", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (eq, ":num_active_parties", 0),
##       (try_begin),
##         (store_div, ":limit", "$qst_defend_nobles_against_peasants_num_nobles_to_save", 2),
##         (ge, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":limit"),
##         (call_script, "script_succeed_quest", "qst_defend_nobles_against_peasants"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_defend_nobles_against_peasants"),
##       (try_end),
##    ],
##   []
##   ),
### Capture Conspirators quest
##  (0.15, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_capture_conspirators"),
##       (neg|check_quest_succeeded, "qst_capture_conspirators"),
##       (neg|check_quest_failed, "qst_capture_conspirators"),
##       (quest_get_slot, ":quest_target_center", "qst_capture_conspirators", slot_quest_target_center),
##       (quest_get_slot, ":faction_no", "qst_capture_conspirators", slot_quest_target_faction),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##         (store_random_in_range, ":random_no", 0, 100),
##         (lt, ":random_no", 20),
##         (set_spawn_radius, 3),
##         (spawn_around_party,":quest_target_center","pt_conspirator"),
##         (val_add, "$qst_capture_conspirators_num_parties_spawned", 1),
##         (party_get_num_companions, ":num_companions", reg0),
##         (val_add, "$qst_capture_conspirators_num_troops_to_capture", ":num_companions"),
##         (party_set_ai_behavior, reg0, ai_bhvr_travel_to_party),
##         (party_set_ai_object, reg0, "$qst_capture_conspirators_party_1"),
##         (party_set_flags, reg0, pf_default_behavior, 0),
##         (try_begin),
##           (le, "$qst_capture_conspirators_party_2", 0),
##           (assign, "$qst_capture_conspirators_party_2", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_3", 0),
##           (assign, "$qst_capture_conspirators_party_3", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_4", 0),
##           (assign, "$qst_capture_conspirators_party_4", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_5", 0),
##           (assign, "$qst_capture_conspirators_party_5", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_6", 0),
##           (assign, "$qst_capture_conspirators_party_6", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_7", 0),
##           (assign, "$qst_capture_conspirators_party_7", reg0),
##         (try_end),
##       (try_end),
##
##       (assign, ":num_active_parties", 0),
##
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_1", 0),
##         (party_is_active, "$qst_capture_conspirators_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_1"),
##           (remove_party, "$qst_capture_conspirators_party_1"),
##         (else_try),
##           (party_get_num_attached_parties, ":num_attachments", "$qst_capture_conspirators_party_1"),
##           (gt, ":num_attachments", 0),
##           (assign, ":leave_meeting", 0),
##           (try_begin),
##             (store_sub, ":required_attachments", "$qst_capture_conspirators_num_parties_to_spawn", 1),
##             (eq, ":num_attachments", ":required_attachments"),
##             (val_add, "$qst_capture_conspirators_leave_meeting_counter", 1),
##             (ge, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (try_begin),
##             (eq, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##             (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_capture_conspirators_party_1"),
##             (assign, ":min_distance", 3),
##             (try_begin),
##               (is_currently_night),
##               (assign, ":min_distance", 2),
##             (try_end),
##             (lt, ":cur_distance", ":min_distance"),
##             (assign, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (eq, ":leave_meeting", 1),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_point),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##           (party_set_ai_target_position, "$qst_capture_conspirators_party_1", pos2),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_2", 0),
##             (party_detach, "$qst_capture_conspirators_party_2"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_2", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_3", 0),
##             (party_detach, "$qst_capture_conspirators_party_3"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_3", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_4", 0),
##             (party_detach, "$qst_capture_conspirators_party_4"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_4", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_5", 0),
##             (party_detach, "$qst_capture_conspirators_party_5"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_5", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_6", 0),
##             (party_detach, "$qst_capture_conspirators_party_6"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_6", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_7", 0),
##             (party_detach, "$qst_capture_conspirators_party_7"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_7", pos2),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_1"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_1"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_1", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_1", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_2", 0),
##         (party_is_active, "$qst_capture_conspirators_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_2"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_2"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_2"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_2"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_2", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_2", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_3", 0),
##         (party_is_active, "$qst_capture_conspirators_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_3"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_3"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_3"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_3"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_3", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_3", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_4", 0),
##         (party_is_active, "$qst_capture_conspirators_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_4"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_4"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_4"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_4"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_4", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_4", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_5", 0),
##         (party_is_active, "$qst_capture_conspirators_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_5"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_5"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_5"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_5"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_5", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_5", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_6", 0),
##         (party_is_active, "$qst_capture_conspirators_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_6"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_6"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_6"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_6"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_6", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_6", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_7", 0),
##         (party_is_active, "$qst_capture_conspirators_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_7"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_7"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_7"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_7"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_7", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_7", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##
##       (eq, ":num_active_parties", 0),
##       (party_count_prisoners_of_type, ":count_captured_conspirators", "p_main_party", "trp_conspirator"),
##       (party_count_prisoners_of_type, ":count_captured_conspirator_leaders", "p_main_party", "trp_conspirator_leader"),
##       (val_add, ":count_captured_conspirators", ":count_captured_conspirator_leaders"),
##       (try_begin),
##         (store_div, ":limit", "$qst_capture_conspirators_num_troops_to_capture", 2),
##         (gt, ":count_captured_conspirators", ":limit"),
##         (call_script, "script_succeed_quest", "qst_capture_conspirators"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_capture_conspirators"),
##       (try_end),
##    ],
##   []
##   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|eq, "$qst_follow_spy_run_away", 1),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_run_away", 1),
           (display_message, "str_qst_follow_spy_noticed_you"),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_run_away", 1),
           (display_message, "str_qst_follow_spy_noticed_you"),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 0),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
### Raiders quest
##  (0.95, 0.0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##
##  (0.7, 0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##  
##  (0.1, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (neg|party_is_active, ":quest_target_party")
##    ],
##   [
##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
##    ]
##   ),
##  
##  (1.3, 0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", slot_quest_target_center),
##       (party_is_in_town,":quest_target_party",":quest_target_center")
##    ],
##   [
##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
##       (display_message, "str_raiders_reached_base"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (remove_party, ":quest_target_party"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT END

#########################################################################
# Random MERCHANT quest triggers
####################################  
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
# Escort merchant caravan:
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                    (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                    (try_begin),
                      (party_is_active, ":quest_target_party"),
                      (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    (try_end),
                    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                 ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 2),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
				  
# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move 

  (0, 0, 24 * 7,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),
		  (assign, ":town_no", 0), 
		  #oim code
		  (try_begin), 
			(eq, ":pretender", "trp_kingdom_1_pretender"), 
			(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_1"), 
			(assign, ":town_no", reg0), 
				(try_begin), 
					(lt, ":town_no", 0), 
					(assign, ":town_no", "p_town_6"), 
				(end_try), 
				(try_begin), 
					(check_quest_active, "qst_oim_getman_main"),
					(neg|check_quest_succeeded, "qst_oim_getman_main"),
					(neg|check_quest_finished,"qst_oim_getman_main"),					
					(quest_slot_ge, "qst_oim_getman_main", slot_quest_current_state, 3),
					(assign, ":town_no", -1), 
				(end_try), 
				
				(try_begin), 
					(eq, "$g_main_quest_active", 1),
					(this_or_next|check_quest_active, "qst_oim_getman_defend_villages"), 
					(             check_quest_active, "qst_oim_getman_main"), 
					(assign, ":town_no", -1), 
					(try_begin), 
						(check_quest_active, "qst_oim_getman_za_radzivilla"), 
						(neg|check_quest_succeeded, "qst_oim_getman_za_radzivilla"),
						(neg|check_quest_finished,"qst_oim_getman_za_radzivilla"),					
						(assign, ":town_no", "p_town_6"), 
					(end_try), 	
				(end_try), 	

		  (else_try), 
			(eq, ":pretender", "trp_kingdom_2_pretender"), 
			(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_3"), 
			(assign, ":town_no", reg0), 
				(try_begin), 
					(lt, ":town_no", 0), 
					(assign, ":town_no", "p_town_11"), 
				(end_try), 
				(try_begin), 
					(check_quest_active, "qst_oim_black_lord"),
					(neg|check_quest_succeeded, "qst_oim_black_lord"),
					(neg|check_quest_finished,"qst_oim_black_lord"),					
					(assign, ":town_no", -1), 
				(end_try), 
		  (else_try), 
			(eq, ":pretender", "trp_kingdom_3_pretender"), 
			(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_5"), 
			(assign, ":town_no", reg0), 
				(try_begin), 
					(lt, ":town_no", 0), 
					(assign, ":town_no", "p_town_11"), 
				(end_try), 
		  (else_try), 
			(eq, ":pretender", "trp_kingdom_4_pretender"), 
			(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_4"), 
			(assign, ":town_no", reg0), 
				(try_begin), 
					(lt, ":town_no", 0), 
					(assign, ":town_no", "p_town_1"), 
				(end_try), 
		  (else_try), 
			(eq, ":pretender", "trp_kingdom_5_pretender"), 
			(check_quest_active, "qst_oim_getman_main"),
			(call_script, "script_cf_select_random_town_with_faction", "fac_kingdom_1"), 
			(assign, ":town_no", reg0), 
				(try_begin), 
					(lt, ":town_no", 0), 
					(assign, ":town_no", "p_town_7"), 
				(end_try), 
		   (end_try), 	

		   (troop_set_slot, ":pretender", slot_troop_cur_center, ":town_no"),
           
            (try_begin),
              (eq, debug_mode, 1),
			  (ge, ":town_no", -1), 
              (str_store_troop_name, 4, ":pretender"),
              (str_store_party_name, 5, ":town_no"),
              (display_message, "@{s4} is in {s5}"),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
#            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        (try_end), 
       ],
[]
),
#Rebellion changes end

#NPC system changes begin
#Move unemployed NPCs around taverns
   (24 * 15 , 0, 0, 
   [
    (call_script, "script_update_companion_candidates_in_taverns"),
    ],
   []
   ),

#Process morale and determine personality clashes
  (0, 0, 24,
   [],
[

#Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
#Set their relation to the player
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),
        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),
        (assign, reg7, ":grievance_divisor"),

#        (display_message, "@{!}Process NPC changes. GD: {reg7}"),



##Activate personality clash from 24 hours ago
        (try_begin), #scheduled personality clashes require at least 24hrs together
             (gt, "$personality_clash_after_24_hrs", 0),
             (eq, "$disable_npc_complaints", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),
#

         
        (try_for_range, ":npc", companions_begin, companions_end),
###Reset meeting variables
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (str_store_troop_name, s31, ":npc"),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (assign, reg4, ":player_renown"),
                (assign, reg5, ":renown_min"),
#                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),


				

				(try_begin),
                (main_party_has_troop, ":npc"),

			#Check for quitting
                (call_script, "script_npc_morale", ":npc"),
                (assign, ":npc_morale", reg0),

                (try_begin),
                    (lt, ":npc_morale", 20),
                    (store_random_in_range, ":random", 0, 100),
                    (val_add, ":npc_morale", ":random"),
                    (lt, ":npc_morale", 20),
                    (assign, "$npc_is_quitting", ":npc"),
                (try_end),

				#Reduce grievance over time (or augment, if party is overcrowded
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),


				#Change personality grievance levels
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),

#Check for new personality clashes

				#Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

				#Personality clash 2 and personality match is triggered by battles
				
            (try_end),
        (try_end),
    ]),


#NPC system changes end


  #OiM code
  
  (0.2, 0, ti_once, [
	#code to check if the quest "Bring tatarin to perekop is active"
		(check_quest_active,"qst_oim_bring_tatarin_to_sich"),
	], [
	#code to start dialog with tatarin
		(str_store_string, s2, "@OiM Ne uspeli otoyti ot kazakov kak plennik 4to-to shumniy stal o4en"),
		(jump_to_menu, "mnu_oim_talk_to_tatarin"),
		(finish_mission),
		(music_set_situation, 0),
	]),

	
	(3, 0, ti_once, [
	#code to check if the quest "Bring tatarin to perekop is active"
		(check_quest_active,"qst_oim_kidalovo_z_konyem"),
		(neg|check_quest_finished,"qst_oim_kidalovo_z_konyem"),
		(neg|check_quest_succeeded,"qst_oim_kidalovo_z_konyem"),
		(quest_slot_eq, "qst_oim_kidalovo_z_konyem", slot_quest_current_state, 0),
	], [
	#code to start dialog with tatarin
		(jump_to_menu, "mnu_oim_talk_to_bandits_horse"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	
	(0.4, 0.3, ti_once, [
		(check_quest_active,"qst_oim_invest_2"),
		#(check_quest_succeeded,"qst_oim_invest_2"),
		(neg|check_quest_finished,"qst_oim_invest_2"),
		#(quest_slot_eq, "qst_oim_invest_2", slot_quest_current_state, 1),
	], [
	#code to start dialog with tatarin
		(str_store_string, s2, "@OiM Da takoe bivaet raz v zhizni"),
		(jump_to_menu, "mnu_oim_invest_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	#OiM potop first wave of invasion	
	(0.4, 0.3, ti_once, [
		(check_quest_active,"qst_oim_potop_main"),
		(quest_slot_ge, "qst_oim_potop_main", slot_quest_current_state, 4),
		(store_distance_to_party_from_party, ":cur_dist1", "p_town_6", "p_main_party"),	#warshaw
		(store_distance_to_party_from_party, ":cur_dist2", "p_town_16", "p_main_party"),	#krakov
		(ge, ":cur_dist1", 5),
		(ge, ":cur_dist2", 5),
		(check_quest_active,"qst_oim_potop_main"),
	], [
		#code to start Potop
		#This code needs to be fixed!
		(call_script, "script_give_center_to_faction", "p_town_6", "fac_kingdom_4"),  
		(call_script, "script_give_center_to_faction", "p_town_16", "fac_kingdom_4"),  
		(call_script, "script_remove_lords_from_center", "p_town_6"), 
		(call_script, "script_remove_lords_from_center", "p_town_16"), 
		(call_script, "script_give_center_to_lord", "p_town_6", "trp_kingdom_4_lord", 0),
		(call_script, "script_give_center_to_lord", "p_town_16", "trp_kingdom_4_lord", 0),
		#add code for spawn of swedisharmies to patrol Krakow and Warshaw
		#(quest_set_slot, "qst_oim_potop_main", slot_quest_current_state, 5), #no need - done in dialogs. 
		#spawning armies of Invasion
		(set_spawn_radius, 1),
	    (spawn_around_party, "p_town_6", "pt_oim_swedish_army"),
		(assign, "$oim_swedish_army", reg0),
		(call_script, "script_oim_spawn_strong_army", "$oim_swedish_army", "fac_kingdom_4"),
		(assign, "$oim_swedish_army", reg0), 
		(party_set_ai_behavior, "$oim_swedish_army", ai_bhvr_patrol_party),
		(party_set_ai_object, "$oim_swedish_army", "p_town_6"),
		(party_set_flags, "$oim_swedish_army", pf_default_behavior, 0),
		(set_spawn_radius, 1),		
	    (spawn_around_party, "p_town_16", "pt_oim_swedish_army"),
		(assign, "$oim_swedish_army", reg0),
		(call_script, "script_oim_spawn_strong_army", "$oim_swedish_army", "fac_kingdom_4"),
		(assign, "$oim_swedish_army", reg0), 
		(party_set_ai_behavior, "$oim_swedish_army", ai_bhvr_patrol_party),
		(party_set_ai_object, "$oim_swedish_army", "p_town_16"),
		(party_set_flags, "$oim_swedish_army", pf_default_behavior, 0),
		#Add code to force start next quest (???)
		(call_script, "script_oim_spawn_strong_army", "p_town_6", "fac_kingdom_4"),
		(call_script, "script_oim_spawn_strong_army", "p_town_16", "fac_kingdom_4"),
	]),

#oim_potop_last_qst_time	

	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_main"),
		(neg|check_quest_finished,"qst_oim_potop_main"),
		(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 2), 
		(store_current_day, ":cur_day"),
		(val_sub, ":cur_day", "$oim_potop_last_qst_time"),
		(ge, ":cur_day", 3), 		
	], [
	#code to start dialog with tatarin
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),

	
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_main"),
		(neg|check_quest_finished,"qst_oim_potop_main"),
		(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 5), 
		(store_current_day, ":cur_day"),
		(val_sub, ":cur_day", "$oim_potop_last_qst_time"),
		(ge, ":cur_day", 7), 		
	], [
	#code to start dialog with tatarin
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),

		
	(12, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_shtirlic"),
		(neg|check_quest_finished,"qst_oim_potop_shtirlic"),
		(quest_slot_eq, "qst_oim_potop_shtirlic", slot_quest_current_state, 3), 
	], [
	#code to start dialog with tatarin
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_main"),
		(neg|check_quest_finished,"qst_oim_potop_main"),
		(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 7), 
		(store_current_day, ":cur_day"),
		(val_sub, ":cur_day", "$oim_potop_last_qst_time"),
		(ge, ":cur_day", 10), 		
	], [
	#code to start dialog with tatarin
		#(str_store_string, s2, "@OiM_text_for_main_qst_talk_to_king_shtirlic"), 
		(jump_to_menu, "mnu_oim_auto_message_menu2"),
		(finish_mission),
		(music_set_situation, 0),
		(quest_set_slot, "qst_oim_potop_main", slot_quest_current_state, 8), 		
	]),
	
	(0, 0, 168, [], [
      #not used weekly trigger.		
    ]),

	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_main"),
		(neg|check_quest_finished,"qst_oim_potop_main"),
		(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 15), 
	], [
	#code to start dialog with tatarin
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),	
	]),
	
	#oim marshal end code
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_marshal_started"),
		(neg|check_quest_succeeded, "qst_oim_potop_marshal_started"), 
		(neg|check_quest_finished,"qst_oim_potop_marshal_started"),
		(quest_slot_eq, "qst_oim_potop_marshal_started", slot_quest_current_state, 1), 
	], [
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	#impossible mission check code
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_mission_impossible"),
		(neg|check_quest_succeeded, "qst_oim_potop_mission_impossible"), 
		(neg|check_quest_finished,"qst_oim_potop_mission_impossible"),
		(quest_slot_eq, "qst_oim_potop_mission_impossible", slot_quest_current_state, 0), 
		(assign, ":result", 0),
		(try_begin),
			(try_begin),
				(store_faction_of_party, ":party_faction", "$oim_potop_target_city_1"),
				(eq, ":party_faction", "fac_kingdom_1"), 
				(val_add, ":result", 1), 
			(try_end), 
			(try_begin),
				(store_faction_of_party, ":party_faction", "$oim_potop_target_city_2"),
				(eq, ":party_faction", "fac_kingdom_1"), 
				(val_add, ":result", 1), 
			(try_end), 
			(try_begin),
				(store_faction_of_party, ":party_faction", "$oim_potop_target_city_3"),
				(eq, ":party_faction", "fac_kingdom_1"), 
				(val_add, ":result", 1), 
			(try_end), 
			(try_begin),
				(store_faction_of_party, ":party_faction", "$oim_potop_target_city_4"),
				(eq, ":party_faction", "fac_kingdom_1"), 
				(val_add, ":result", 1), 
			(try_end), 
		(try_end), 
		(eq, ":result", 4), 
	], [
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(call_script, "script_succeed_quest", "qst_oim_potop_mission_impossible"),
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),

	
	#Trigger runned after city captured
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_radzivill_capture_city"),
		(neg|check_quest_succeeded, "qst_oim_getman_radzivill_capture_city"), 
		(neg|check_quest_finished,"qst_oim_getman_radzivill_capture_city"),
		(quest_slot_eq, "qst_oim_getman_radzivill_capture_city", slot_quest_current_state, 1), 
	], [
		(assign, "$oim_auto_talk_troop", "trp_kingdom_1_pretender"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	#(quest_set_slot, "qst_oim_getman_capture_tatarin", slot_quest_current_state, 1), 
	#slot_quest_target_troop
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_capture_tatarin"),
		(neg|check_quest_succeeded, "qst_oim_getman_capture_tatarin"), 
		(neg|check_quest_finished,"qst_oim_getman_capture_tatarin"),
		(quest_slot_eq, "qst_oim_getman_capture_tatarin", slot_quest_current_state, 1), 
	], [
		(quest_get_slot, ":talk_troop", "qst_oim_getman_capture_tatarin", slot_quest_target_troop), 
		(assign, "$oim_auto_talk_troop", ":talk_troop"), 
		(jump_to_menu, "mnu_oim_getman_letter_text"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	(48, 0.3, 0, [
		(quest_slot_eq, "qst_oim_potop_king_elections_kings_node", slot_quest_current_state, 2),
		(quest_slot_eq, "qst_oim_potop_main", slot_quest_current_state, 20),
	], [
		(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_1"),
		(assign, ":troop_no", reg0),
		(try_begin), 
			(ge, ":troop_no", 0), 
			(call_script, "script_change_troop_faction", ":troop_no", "fac_oim_rebel_faction"), 
			(str_store_troop_name, s2, ":troop_no"), 
			(troop_get_slot, ":lord_party", "trp_kingdom_2_pretender", slot_troop_leaded_party),
			(try_begin), 
				(gt, ":lord_party", 0), 
				(party_set_faction, ":lord_party", "fac_oim_rebel_faction"),
			(end_try), 
			(display_message,"@OiM_add {s2} joined the rebellion of Zagloba"),
		(end_try), 	
		(try_begin), 
			(quest_get_slot, ":qst_time", "qst_oim_potop_king_elections_kings_node", slot_quest_start_time),
			(store_current_day, ":cur_day"),
			(val_sub, ":cur_day", ":qst_time"), 
			(ge, ":cur_day", 7), 
			(str_store_string, s2, "str_oim_polish_defeated"),
			(jump_to_menu, "mnu_oim_last_game_menu"),
			(finish_mission),
			(music_set_situation, 0),
		(end_try), 	
	]),
	
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_destroy_mercs"),
		(neg|check_quest_succeeded, "qst_oim_potop_destroy_mercs"), 
		(neg|check_quest_finished,"qst_oim_potop_destroy_mercs"),
		(quest_get_slot, ":qst_time", "qst_oim_potop_destroy_mercs", slot_quest_start_time),
		(store_current_day, ":cur_day"),
		(val_sub, ":cur_day", ":qst_time"), 
		(ge, ":cur_day", 14), 
		(call_script, "script_count_parties_of_faction_and_party_template", "fac_outlaws", "pt_oim_potop_mercs_army"),
		(gt, reg0, 0), 	
	], [
		(str_store_string, s2, "str_oim_polish_defeated"),
		(jump_to_menu, "mnu_oim_last_game_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),

	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_destroy_mercs"),
		(neg|check_quest_succeeded, "qst_oim_potop_destroy_mercs"), 
		(neg|check_quest_finished,"qst_oim_potop_destroy_mercs"),
		(call_script, "script_count_parties_of_faction_and_party_template", "fac_outlaws", "pt_oim_potop_mercs_army"),
		(eq, reg0, 0), 	
	], [
		(call_script, "script_succeed_quest", "qst_oim_potop_destroy_mercs"), 
		#code to move further 
		#(call_script, "script_setup_troop_meeting", "trp_npc1", 0),
		(assign, "$oim_auto_talk_troop", "trp_npc1"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	
	(1, 1, ti_once, [
		(check_quest_active, "qst_oim_lendliz2"),
		(neg|check_quest_succeeded, "qst_oim_lendliz2"), 
		(neg|check_quest_finished,"qst_oim_lendliz2"),
		(try_begin), 
			(party_is_active, "$oim_lendliz_caravan"), 
			(store_distance_to_party_from_party, ":cur_dist", "$oim_lendliz_caravan", "p_town_14"),
		(else_try), 
			(assign, ":cur_dist", 1),
		(end_try), 	
		(this_or_next|neg|party_is_active, "$oim_lendliz_caravan"), 
        (le, ":cur_dist", 1),
	], [
		(call_script, "script_fail_quest", "qst_oim_lendliz2"),
		(quest_set_slot, "qst_oim_lendliz2", slot_quest_current_state, 1),
		(assign, "$oim_auto_talk_troop", "trp_don_cossack"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_dismiss_king"),
		(neg|check_quest_finished,"qst_oim_potop_dismiss_king"),
		(quest_slot_eq, "qst_oim_potop_dismiss_king", slot_quest_current_state, 0), 
		(call_script, "script_count_parties_of_faction_and_party_type", "fac_kingdom_1", spt_kingdom_hero_party),
		(le, reg0, 7), 
	], [
		#code to finish qst 
		#(call_script, "script_succeed_quest", "qst_oim_potop_dismiss_king"),
		(call_script, "script_end_quest", "qst_oim_potop_dismiss_king"),
		#code to execute the king
		(add_xp_as_reward, 2000),
		#qst_oim_potop_dismiss_king
		(quest_set_slot, "qst_oim_potop_execute_king", slot_quest_giver_troop, "trp_npc1"), 
		(quest_set_slot, "qst_oim_potop_execute_king", slot_quest_current_state, 0),
		(setup_quest_text, "qst_oim_potop_execute_king"),
		(str_store_string, s2, "str_oim_king_revoult"),
		(call_script, "script_start_quest", "qst_oim_potop_execute_king", "trp_npc1"),
	]),

	(2, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_dismiss_king"),
		(neg|check_quest_finished,"qst_oim_potop_dismiss_king"),
		(quest_slot_eq, "qst_oim_potop_dismiss_king", slot_quest_current_state, 1), 
		(call_script, "script_cf_oim_potop_za_zaglobu_check"),
	], [
		#code to finish qst 
		#(call_script, "script_succeed_quest", "qst_oim_potop_dismiss_king"),
		(call_script, "script_end_quest", "qst_oim_potop_dismiss_king"),
		#code to execute the king
		(add_xp_as_reward, 2000),
		#qst_oim_potop_dismiss_king
		(quest_set_slot, "qst_oim_potop_execute_king", slot_quest_giver_troop, "trp_npc1"), 
		(quest_set_slot, "qst_oim_potop_execute_king", slot_quest_current_state, 0),
		(setup_quest_text, "qst_oim_potop_execute_king"),
		(str_store_string, s2, "str_oim_king_revoult"),
		(call_script, "script_start_quest", "qst_oim_potop_execute_king", "trp_npc1"),
	]),
	
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_potop_final_qst"),
		(neg|check_quest_succeeded, "qst_oim_potop_final_qst"),
		(neg|check_quest_finished,"qst_oim_potop_final_qst"),
		(call_script, "script_count_centers"),
		(assign, ":count", reg0),
		(call_script, "script_count_centers_of_faction", "fac_kingdom_1"),
		(assign, ":fac_count", reg0),
		(val_mul, ":count", 65),
		(val_div, ":count", 100),
		(assign, reg1, ":count"),
		(ge, ":fac_count", ":count"),
		(neg|faction_slot_eq, "fac_kingdom_2", slot_faction_state, sfs_active),
		(neg|faction_slot_eq, "fac_kingdom_4", slot_faction_state, sfs_active),
		(neg|faction_slot_eq, "fac_kingdom_5", slot_faction_state, sfs_active),
	], [
		(call_script, "script_succeed_quest", "qst_oim_potop_final_qst"),
        (unlock_achievement, ACHIEVEMENT_POLISH_DRAMA),		
		#code to move further
		(assign, "$oim_auto_talk_troop", "trp_swadian_sergeant"),
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	#(quest_set_slot, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 0),
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_nesvizh_pernach"),
		(neg|check_quest_succeeded, "qst_oim_getman_nesvizh_pernach"), 
		(neg|check_quest_finished,"qst_oim_getman_nesvizh_pernach"),
		(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 0),
        (store_distance_to_party_from_party, ":party_distance", "p_main_party", "p_village_53"),
        (lt, ":party_distance", 10),
	], [
		(assign, "$oim_auto_talk_troop", "trp_npc4"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),	
	
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_nesvizh_pernach"),
		(check_quest_succeeded, "qst_oim_getman_nesvizh_pernach"), 
		(neg|check_quest_finished,"qst_oim_getman_nesvizh_pernach"),
		(quest_slot_eq, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 3),
	], [
		#(call_script, "script_get_random_troop_from_party", "p_main_party"),
		(assign, ":troop_no", "trp_merc_reytar"),
		(quest_set_slot, "qst_oim_getman_nesvizh_pernach", slot_quest_target_troop, ":troop_no"),
		(assign, "$oim_auto_talk_troop", ":troop_no"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),	
	
	
	#		(quest_set_slot, "qst_oim_getman_nesvizh_pernach", slot_quest_current_state, 0),
	(3*24, 0.3, 0, [
		(check_quest_active, "qst_oim_getman_nesvizh_pernach"),
		(neg|check_quest_succeeded, "qst_oim_getman_nesvizh_pernach"), 
		(neg|check_quest_finished,"qst_oim_getman_nesvizh_pernach"),
	], [
		(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_5"),
		(assign, ":lord", reg0),
		(call_script, "script_change_troop_faction", ":lord", "fac_kingdom_1"),
	]),	
	
	(4*24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_nesvizh_pernach"),
		(neg|check_quest_succeeded, "qst_oim_getman_nesvizh_pernach"), 
		(neg|check_quest_finished,"qst_oim_getman_nesvizh_pernach"),
		(call_script, "script_count_lords_of_faction", "fac_kingdom_5"), 
		(le, reg0, 3), 
	], [
		(jump_to_menu, "mnu_oim_getman_quest_failed"),
		(finish_mission),
		(music_set_situation, 0),
	]),	


	(0.3, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_caravan"),
		(neg|check_quest_succeeded, "qst_oim_getman_caravan"), 
		(neg|check_quest_finished,"qst_oim_getman_caravan"),
		(quest_get_slot, ":target_center", "qst_oim_getman_caravan", slot_quest_target_center), 
        (store_distance_to_party_from_party, ":cur_dist", "$oim_barabash_caravan", ":target_center"),
        (lt, ":cur_dist", 2),
	], [
		(display_log_message, "str_caravan_delivered_the_letter"),
		(call_script, "script_fail_quest", "qst_oim_getman_caravan"),
		(call_script, "script_end_quest", "qst_oim_getman_caravan"),
#		(quest_set_slot, "qst_oim_getman_caravan", slot_quest_current_state, 1),
#		(assign, "$oim_auto_talk_troop", "trp_don_cossack"), 
#		(jump_to_menu, "mnu_oim_auto_talk_menu"),
#		(finish_mission),
#		(music_set_situation, 0),
	]),

	#(call_script, "script_succeed_quest", "qst_oim_getman_za_hmelya"),
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_za_hmelya"),
		(check_quest_succeeded, "qst_oim_getman_za_hmelya"), 
		(neg|check_quest_finished,"qst_oim_getman_za_hmelya"),
	], [
		(jump_to_menu, "mnu_oim_getman_hmel_order"),
		(finish_mission),
		(music_set_situation, 0),
	]),	

	#qst_oim_na_rech_pospolitu
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_na_rech_pospolitu"),
		(check_quest_succeeded, "qst_oim_na_rech_pospolitu"), 
		(neg|check_quest_finished,"qst_oim_na_rech_pospolitu"),
	], [
		(jump_to_menu, "mnu_oim_getman_hmel_rebelion"),
		(finish_mission),
		(music_set_situation, 0),
	]),	
	
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_hmel_reb"),
		(check_quest_succeeded, "qst_oim_getman_hmel_reb"), 
		(neg|check_quest_finished,"qst_oim_getman_hmel_reb"),
	], [
		(jump_to_menu, "mnu_oim_getman_casus_beli_hmel"),
		(finish_mission),
		(music_set_situation, 0),
	]),	
	
	
  (1, 0.0, ti_once,
   [
       (check_quest_active, "qst_oim_getman_hmel_greate_war"),
	   (neg|check_quest_succeeded, "qst_oim_getman_hmel_greate_war"),
	   (neg|check_quest_finished, "qst_oim_getman_hmel_greate_war"),
       (quest_slot_eq, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 0),
       (quest_get_slot, ":quest_target_center", "qst_oim_getman_hmel_greate_war", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_oim_getman_hmel_greate_war", slot_quest_target_party),
	   (assign, ":result", 0), 
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 1),
         #(call_script, "script_fail_quest", "qst_oim_getman_hmel_greate_war"),
		 (assign, ":result", 1), 
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (call_script, "script_cf_oim_remove_party", ":quest_target_party"),
         (quest_set_slot, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 2),
		 (assign, ":result", 1), 
       (try_end),
	   (eq, ":result", 1), 
    ],
   [
        #code to start war
		(jump_to_menu, "mnu_oim_getman_casus_beli_hmel_war"),
		(finish_mission),
		(music_set_situation, 0),
   ]
   ),

  (1, 0.0, ti_once,
   [
       (check_quest_active, "qst_oim_getman_hmel_greate_war"),
	   (neg|check_quest_succeeded, "qst_oim_getman_hmel_greate_war"),
	   (neg|check_quest_finished, "qst_oim_getman_hmel_greate_war"),
       (quest_slot_eq, "qst_oim_getman_hmel_greate_war", slot_quest_current_state, 1),
    ],
   [
        #code to start war
		(jump_to_menu, "mnu_oim_getman_casus_beli_hmel_war"),
		(finish_mission),
		(music_set_situation, 0),
   ]
   ),	
	
	(1, 0.3, ti_once, [
  	    (check_quest_active, "qst_oim_getman_last_qst"),
	    (check_quest_succeeded, "qst_oim_getman_last_qst"), 
	    (neg|check_quest_finished,"qst_oim_getman_last_qst"),
	], [
		(assign, "$oim_auto_talk_troop", "trp_volhv"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),	

	#oim_getman_korona_vitovta
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_korona_vitovta"),
		(neg|check_quest_finished,"qst_oim_getman_korona_vitovta"),
		(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 0), 
		(store_current_day, ":cur_day"),
		(quest_get_slot, ":qst_day", "qst_oim_getman_korona_vitovta", slot_quest_start_time), 
		(val_sub, ":cur_day", ":qst_day"),
		(ge, ":cur_day", 1), 	
		#(eq, 0, 1),
	], [
		(assign, "$oim_auto_talk_troop", "trp_npc4"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),
	
	#(quest_set_slot, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 1),
  (1, 0.0, ti_once,
   [	
       (check_quest_active, "qst_oim_getman_korona_vitovta"),
	   (neg|check_quest_succeeded, "qst_oim_getman_korona_vitovta"),
	   (neg|check_quest_finished, "qst_oim_getman_korona_vitovta"),
       (quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 1),
       (quest_get_slot, ":quest_target_center", "qst_oim_getman_korona_vitovta", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_oim_getman_korona_vitovta", slot_quest_target_party),
	   (assign, ":result", 0), 
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
		 (assign, ":result", 1), 
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (call_script, "script_cf_oim_remove_party", ":quest_target_party"),
		 (assign, ":result", 1), 
       (try_end),
	   (eq, ":result", 1), 
    ],
   [
        (quest_set_slot, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 2),   
 		(store_current_day, ":cur_day"),
		(quest_set_slot, "qst_oim_getman_korona_vitovta", slot_quest_start_time, ":cur_day"),
   ]
   ),
	
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_korona_vitovta"),
		(neg|check_quest_finished,"qst_oim_getman_korona_vitovta"),
		(quest_slot_eq, "qst_oim_getman_korona_vitovta", slot_quest_current_state, 2), 
		(store_current_day, ":cur_day"),
		(quest_get_slot	, ":qst_day", "qst_oim_getman_korona_vitovta", slot_quest_start_time), 
		(val_sub, ":cur_day", ":qst_day"),
		(ge, ":cur_day", 4), 		
	], [
		(assign, "$oim_auto_talk_troop", "trp_npc4"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),	
	
	
	#(quest_set_slot, "qst_oim_dmitriy_eleonora", slot_quest_current_state, 1),
	#trp_eleonora
	(1, 0.3, ti_once, [
		(check_quest_active, "qst_oim_dmitriy_eleonora"),
		(neg|check_quest_finished,"qst_oim_dmitriy_eleonora"),
		(quest_slot_eq, "qst_oim_dmitriy_eleonora", slot_quest_current_state, 1), 
		(store_current_day, ":cur_day"),
		(quest_get_slot	, ":qst_day", "qst_oim_dmitriy_eleonora", slot_quest_start_time), 
		(val_sub, ":cur_day", ":qst_day"),
		(ge, ":cur_day", 1), 		
	], [
		(assign, "$oim_auto_talk_troop", "trp_eleonora"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
	]),	


	#oim barabash 
	#(call_script, "script_succeed_quest", "qst_oim_getman_za_barabasha"),
	(1, 1, ti_once, [
		(check_quest_active, "qst_oim_getman_za_barabasha"),
		(check_quest_succeeded,"qst_oim_getman_za_barabasha"),
	], [
		(jump_to_menu, "mnu_oim_barabash_order_mc"),
		(finish_mission),
		(music_set_situation, 0),
	]),	


	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_na_msk_tsarzd"),
		(check_quest_succeeded, "qst_oim_na_msk_tsarzd"), 
		(neg|check_quest_finished,"qst_oim_na_msk_tsarzd"),
	], [
		(jump_to_menu, "mnu_oim_getman_barabash_rebelion"),
		(finish_mission),
		(music_set_situation, 0),
	]),		
	
	(24, 0.3, ti_once, [
		(check_quest_active, "qst_oim_getman_barabash_reb"),
		(check_quest_succeeded, "qst_oim_getman_barabash_reb"), 
		(neg|check_quest_finished,"qst_oim_getman_barabash_reb"),
	], [
		(jump_to_menu, "mnu_oim_getman_casus_beli_barabash"),
		(finish_mission),
		(music_set_situation, 0),
	]),	
	

    (1, 0.0, ti_once,
    [
        (check_quest_active, "qst_oim_getman_barabash_greate_war"),
	    (neg|check_quest_succeeded, "qst_oim_getman_barabash_greate_war"),
	    (neg|check_quest_finished, "qst_oim_getman_barabash_greate_war"),
        (quest_slot_eq, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 0),
        (quest_get_slot, ":quest_target_center", "qst_oim_getman_barabash_greate_war", slot_quest_target_center),
        (quest_get_slot, ":quest_target_party", "qst_oim_getman_barabash_greate_war", slot_quest_target_party),
	    (assign, ":result", 0), 
        (try_begin),
          (neg|party_is_active, ":quest_target_party"),
          (quest_set_slot, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 1),
          #(call_script, "script_fail_quest", "qst_oim_getman_hmel_greate_war"),
	 	 (assign, ":result", 1), 
        (else_try),
          (party_is_in_town, ":quest_target_party", ":quest_target_center"),
          (call_script, "script_cf_oim_remove_party", ":quest_target_party"),
          (quest_set_slot, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 2),
	 	 (assign, ":result", 1), 
        (try_end),
	    (eq, ":result", 1), 
    ],
    [
         #code to start war
	 	(jump_to_menu, "mnu_oim_getman_casus_beli_barabash_war"),
	 	(finish_mission),
	 	(music_set_situation, 0),
    ]
    ),
 
    (1, 0.0, ti_once,
    [
        (check_quest_active, "qst_oim_getman_barabash_greate_war"),
	    (neg|check_quest_succeeded, "qst_oim_getman_barabash_greate_war"),
	    (neg|check_quest_finished, "qst_oim_getman_barabash_greate_war"),
        (quest_slot_eq, "qst_oim_getman_barabash_greate_war", slot_quest_current_state, 1),
     ],
    [
         #code to start war
	 	(jump_to_menu, "mnu_oim_getman_casus_beli_barabash_war"),
	 	(finish_mission),
	 	(music_set_situation, 0),
    ]
    ),	


	(1, 0.3, ti_once, [
		(eq, "$g_razin_rebellion", 1), 
		(store_current_day, ":now_time"),
		(ge, ":now_time", "$g_razin_time_offset"), 
		(troop_get_slot, ":lord_party", "trp_kingdom_2_pretender", slot_troop_leaded_party),
		(gt, ":lord_party", 0), 
        (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),		
		(neg|troop_slot_ge, "trp_kingdom_2_pretender", slot_troop_prisoner_of_party, 0),		
        (store_distance_to_party_from_party, ":cur_dist", ":lord_party", "p_main_party"),
        (ge, ":cur_dist", 10),
	], [
		(call_script, "script_oim_rise_rebellion", "fac_kingdom_2", "trp_kingdom_2_pretender"),
		(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_2"), 
		(assign, ":cur_object_troop", reg0),
		(call_script, "script_change_troop_faction", ":cur_object_troop", "fac_oim_rebel_faction"), 
		(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_2"), 
		(assign, ":cur_object_troop", reg0),
		(call_script, "script_change_troop_faction", ":cur_object_troop", "fac_oim_rebel_faction"), 
		(call_script, "script_diplomacy_start_war_between_kingdoms", "fac_kingdom_2", "fac_oim_rebel_faction", 1),
		(assign, "$g_recalculate_ais", 1),
		(call_script, "script_update_all_notes"),
		(quest_set_slot, "qst_oim_black_lord", slot_quest_current_state, 2), 		
		(assign, "$g_razin_rebellion", 2), 
		#code
		(try_for_range, ":troop_no", heroes_begin, heroes_end), 
			(troop_slot_eq, ":troop_no", slot_troop_support_hero, -1), 
		(end_try), 
	 	(jump_to_menu, "mnu_oim_dmitriy_razin_warn"),
	 	(finish_mission),
	 	(music_set_situation, 0),
	]),


	(24, 0, 24, [
		(eq, "$g_razin_rebellion", 2), 
		(neg|troop_slot_ge, "trp_kingdom_2_pretender", slot_troop_prisoner_of_party, 0),		
	], [
		(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_2"), 
		(assign, ":cur_object_troop", reg0),
		(call_script, "script_change_troop_faction", ":cur_object_troop", "fac_oim_rebel_faction"), 	
		(assign, "$g_recalculate_ais", 1),
		(call_script, "script_update_all_notes"),
	]), 
	

	
	(24*5, 0, 24,  
    [
		(check_quest_active, "qst_oim_black_lord"),
		(neg|check_quest_succeeded, "qst_oim_black_lord"),
		(neg|check_quest_finished,"qst_oim_black_lord"),
		(quest_slot_eq, "qst_oim_black_lord", slot_quest_current_state, 2),
     ],
    [
		(call_script, "script_cf_get_random_lord_except_king_with_faction", "fac_kingdom_2"),
		(assign, ":lord", reg0),
        (call_script, "script_cf_faction_get_random_enemy_faction", "fac_kingdom_2"),
        (assign, ":enemy_faction", reg0),
		(ge, ":lord", 0), 
		(is_between,  kingdoms_begin, kingdoms_end), 
		(call_script, ":enemy_faction", "script_change_troop_faction", ":lord", ":enemy_faction"),
        (troop_get_slot, ":lords_party", ":lord", slot_troop_leaded_party),
        (party_set_faction, ":lords_party", ":enemy_faction"),
		(troop_set_slot, ":lord", slot_troop_support_hero, 1),
		(assign, "$g_recalculate_ais", 1),
		(call_script, "script_update_all_notes"),
    ]
    ),	
	

	(1, 0, 12,  
    [

     ],
    [
        (party_get_morale, ":morale", "p_main_party"),
		(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),                
		(try_begin),
			(lt, ":morale", 40),
			(eq, ":reduce_campaign_ai", 2), #only if "normal"
			(eq, "$g_player_is_captive", 0),
			(eq, "$g_last_rest_center", -1),
			(call_script, "script_start_bunt"),
		(try_end),
    ]
    ),	

    (0, 0, ti_once,  
    [
        
     ],
    [
        (assign, "$oim_deserters_party", 0),
        #(call_script, "script_replace_shturm_item_init_first"),
        (assign, "$oim_illness_count", 0),
        (assign, "$oim_illness_recovery_status", 0),
        (assign, "$oim_illness_camp_start", 0),
        (store_current_hours, ":cur_hours"),
        (assign, "$g_last_rest_payment_until", ":cur_hours"),
		(try_for_range, ":cur_displace", 0, 5),
			(store_add, ":cur_quest", "qst_oim_illness_1", ":cur_displace"),
			(quest_set_slot, ":cur_quest", slot_quest_is_active, 0),
		(try_end),
    ]
    ),	
	
	#"qst_oim_potop_marshal", slot_quest_current_state, 1),
	(24, 0, 1,  
    [],
    [
		#code for marshal
		(try_begin), 
			(check_quest_active,"qst_oim_potop_marshal"),
			(neg|check_quest_failed,"qst_oim_potop_marshal"),
			(neg|check_quest_finished,"qst_oim_potop_marshal"),
			(quest_slot_eq, "qst_oim_potop_marshal", slot_quest_current_state, 0),
			(assign, "$oim_auto_talk_troop", "trp_npc1"), 
			(jump_to_menu, "mnu_oim_auto_talk_menu"),
			(finish_mission),
			(music_set_situation, 0),
		(end_try), 
    ]
    ),	
	
	#qst dmitriy_razin_special_dlg
	(24, 0, 1,  
    [
		(quest_slot_eq, "qst_oim_dmitriy_razin", slot_quest_current_state, 2),
		(neg|check_quest_active, "qst_biyars_specnaz"), 
     ],
    [
		(assign, "$oim_auto_talk_troop", "trp_kingdom_2_pretender"), 
		(jump_to_menu, "mnu_oim_auto_talk_menu"),
		(finish_mission),
		(music_set_situation, 0),
    ]
    ),		
	
	#(quest_set_slot, "qst_oim_potop_main", slot_quest_current_state, 3),
	(1, 0, 1,  
    [
		(check_quest_active, "qst_oim_potop_main"), 
		(neq, "$g_player_is_captive", 1),
		(troop_slot_eq, "trp_npc1", slot_troop_occupation, 0),
		(quest_get_slot, ":state", "qst_oim_potop_main", slot_quest_current_state),
		(is_between, ":state", 2, 16), 
     ],
    [
		(call_script, "script_recruit_troop_as_companion", "trp_npc1"),
    ]
    ),		
	
	(6, 0, 0,
	[
		(check_quest_active, "qst_oim_potop_destroy_mercs"),
		(neg|check_quest_succeeded, "qst_oim_potop_destroy_mercs"),
		(neg|check_quest_finished,"qst_oim_potop_destroy_mercs"),
	],
	[
        (assign, ":count", 0),
		(str_clear, s5),
		(try_for_parties, ":cur_party_no"),
			(party_get_template_id, ":cur_party_template", ":cur_party_no"),
			(eq, ":cur_party_template", "pt_oim_potop_mercs_army"),
			(party_is_active, ":cur_party_no"),
			(call_script, "script_get_party_position_to_s1", ":cur_party_no"),
			(try_begin), 
				(eq, ":count", 0), 
				(str_store_string, s5, "@{s1}"),
			(else_try), 
				(str_store_string, s5, "@{s5}^ {s1}"),	
			(end_try), 
			(val_add, ":count", 1),
		(end_try), 	
		(str_store_string, s6, "str_oim_potop_location_notes"),
		(add_quest_note_from_sreg, "qst_oim_potop_destroy_mercs", 4, s6, 1),
	]), 

	(24, 0, 0,
	[
		(check_quest_active, "qst_oim_potop_zagloba_revoult"),
		(neg|check_quest_succeeded, "qst_oim_potop_zagloba_revoult"),
		(neg|check_quest_finished,"qst_oim_potop_zagloba_revoult"),
		(quest_slot_eq, "qst_oim_potop_zagloba_revoult", slot_quest_current_state, 2),
	],
	[
        (assign, ":count", 0),
		(str_clear, s5),
		(try_for_parties, ":cur_party_no"),
			(party_get_template_id, ":cur_party_template", ":cur_party_no"),
			(eq, ":cur_party_template", "pt_oim_zagloba_party"),
			(party_is_active, ":cur_party_no"),
			(call_script, "script_get_party_position_to_s1", ":cur_party_no"),
			(try_begin), 
				(eq, ":count", 0), 
				(str_store_string, s5, "@{s1}"),
			(else_try), 
				(str_store_string, s5, "@{s5}^ {s1}"),	
			(end_try), 
			(val_add, ":count", 1),
		(end_try), 	
		(str_store_string, s6, "str_oim_potop_location_notes"),
		(add_quest_note_from_sreg, "qst_oim_potop_zagloba_revoult", 4, s6, 1),
	]), 
	
	(1, 0, ti_once, 
	[
		(check_quest_active, "qst_oim_getman_za_hmelya"),
		(neg|check_quest_succeeded, "qst_oim_getman_za_hmelya"), 
		(neg|check_quest_finished,"qst_oim_getman_za_hmelya"),
		(quest_slot_eq, "qst_oim_getman_za_hmelya", slot_quest_current_state, 0), 
		(store_current_day, ":cur_day"),
		(quest_get_slot	, ":qst_day", "qst_oim_dmitriy_eleonora", slot_quest_start_time), 
		(val_sub, ":cur_day", ":qst_day"),
		(ge, ":cur_day", 4), 		
	],
	[
		(call_script, "script_succeed_quest", "qst_oim_getman_za_hmelya"),
		(faction_set_slot, "fac_kingdom_5", slot_faction_marshall, "trp_player"),
	]), 
	
	#OiM new very important code!
	(1, 0, ti_once, 
	[
		#qst_oim_getman_za_barabasha
		(check_quest_active, "qst_oim_getman_za_barabasha"),
		(neg|check_quest_succeeded, "qst_oim_getman_za_barabasha"), 
		(neg|check_quest_finished,"qst_oim_getman_za_barabasha"),
		(assign, ":count", 0),
		(try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
			(troop_slot_eq, ":troop_no", slot_troop_support_hero, 1), 
			(val_add, ":count", 1),
		(end_try), 
		(ge, ":count", 5),
	],
	[
		#tut coda mnogo
		(quest_set_slot, "qst_oim_getman_za_barabasha", slot_quest_current_state, 10), 
		(try_begin), 
			(check_quest_active, "qst_oim_getman_caravan"),
			(call_script, "script_fail_quest", "qst_oim_getman_caravan"),
			(call_script, "script_end_quest", "qst_oim_getman_caravan"),
		(end_try),
		(assign, "$players_kingdom", "fac_player_supporters_faction"),
		(assign, "$g_talk_troop", "trp_kingdom_5_pretender"),
		(troop_set_slot, "$g_talk_troop", slot_troop_discussed_rebellion, 1),
		(try_begin),
			(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
			(assign, "$supported_pretender", "$g_talk_troop"),
			(troop_get_slot, "$supported_pretender_old_faction", "$g_talk_troop", slot_troop_original_faction),
			(troop_set_faction, "$g_talk_troop", "fac_player_supporters_faction"),
			(faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
			(assign, "$g_talk_troop_faction", "fac_player_supporters_faction"),
			(quest_set_slot, "qst_rebel_against_kingdom", slot_quest_giver_troop, "$g_talk_troop"),
			(quest_set_slot, "qst_rebel_against_kingdom", slot_quest_target_faction, "$supported_pretender_old_faction"),
			(str_store_faction_name_link, s14, "$supported_pretender_old_faction"),
			(str_store_troop_name_link, s13, "$g_talk_troop"),
			(setup_quest_text,"qst_rebel_against_kingdom"),
			(str_store_string, s2, "@You promised to help {s13} claim the throne of {s14}."),
			(call_script, "script_start_quest", "qst_rebel_against_kingdom", "$g_talk_troop"),
		(try_end),
		(try_begin),
			(is_between, "$players_oath_renounced_against_kingdom", kingdoms_begin, kingdoms_end),
			(neq, "$players_oath_renounced_against_kingdom", "$g_talk_troop_faction"),
			(store_relation, ":relation", "fac_player_supporters_faction", "$players_oath_renounced_against_kingdom"),
			(val_min, ":relation", -40),
			(call_script, "script_set_player_relation_with_faction", "$players_oath_renounced_against_kingdom", ":relation"),
			(call_script, "script_update_all_notes"),
			(assign, "$g_recalculate_ais", 1),
		(try_end),
		(try_begin),
			(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
			(neq, "$players_kingdom", "fac_player_supporters_faction"),
			(faction_get_slot, ":old_leader", "$players_kingdom", slot_faction_leader),
			(call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, ":old_leader", "$players_kingdom"),
			(call_script, "script_player_leave_faction", 1),
		(try_end),
		(call_script, "script_player_join_faction", "$g_talk_troop_faction"),
		(try_begin),
			(gt, "$g_invite_offered_center", 0),
			(call_script, "script_give_center_to_lord", "$g_invite_offered_center", "trp_player", 0),
			(call_script, "script_add_log_entry", logent_fief_granted_village, "trp_player",  "$g_invite_offered_center", "$g_talk_troop", "$g_talk_troop_faction"),
		(try_end),
		(call_script, "script_add_log_entry", logent_pledged_allegiance,   "trp_player",  -1, "$g_talk_troop", "$g_talk_troop_faction"),
		(try_begin),
			(check_quest_active, "qst_join_faction"),
			(eq, "$g_invite_faction_lord", "$g_talk_troop"),
			(call_script, "script_end_quest", "qst_join_faction"),
		(else_try),
			(check_quest_active, "qst_join_faction"),
			(call_script, "script_abort_quest", "qst_join_faction", 0),
		(try_end),
		(assign, "$player_has_homage" ,1),
		(assign, "$g_player_banner_granted", 1),
		(assign, "$g_invite_faction", 0),
		(assign, "$g_invite_faction_lord", 0),
		(assign, "$g_invite_offered_center", 0),
		(assign, "$g_leave_encounter",1),
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 25),
        (faction_set_slot, "$g_talk_troop_faction", slot_faction_state, sfs_active),
        (party_force_add_members, "p_main_party", "$supported_pretender", 1),
        (troop_set_slot, "$supported_pretender", slot_troop_cur_center, 0),
        (troop_set_auto_equip, "$supported_pretender",0),
        (str_store_troop_name_link, s6, "$supported_pretender"),
        (display_message, "@{s6} has joined your party."),
        (assign, "$player_made_legitimacy_claim", 0),
        (assign, "$player_made_benefit_claim", 0),
        (assign, "$player_made_strength_claim", 0),
        (assign, "$player_made_benefit_claim", 0),
        (store_relation, ":reln", "$supported_pretender_old_faction", "fac_player_supporters_faction"),
        (val_min, ":reln", -50),
        (call_script, "script_set_player_relation_with_faction", "$supported_pretender_old_faction", ":reln"),
        (str_store_faction_name, s1, "$supported_pretender_old_faction"),
        (faction_set_name, "fac_player_supporters_faction", "@{s1} Rebels"),
        (faction_set_color, "fac_player_supporters_faction", 0xFF0000),
		(try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
			(troop_slot_eq, ":troop_no", slot_troop_support_hero, 1),
			(call_script, "script_change_troop_faction", ":troop_no", "fac_player_supporters_faction"),
		(end_try), 
		(assign, "$g_recalculate_ais", 1),		
        (call_script, "script_update_all_notes"),		
	]), 
 
	#Expanded management system -begin
		#MS Init trigers -begin
#  (0, 0, ti_once, [], [
#							(call_script, "script_ms_init"),
#						]),	
##MOVED TO GAME_START SCRIPT
		#MS Init trigers -end
	
		#MS Building control -begin
    (0, 0, 1, [], [
						(call_script, "script_ms_check_building_process"),
						(call_script, "script_parties_fix"),
					]),		
		#MS Building control -end
	
		#MS AI triger -begin
   (0, 0, 24*7, [], [
						(call_script, "script_ms_check_ai_process"),
					]),		
		#MS AI triger -end
		
		#MS Tine triger -begin
  (0, 0, 24, [], [
						(call_script, "script_ms_check_time_event", slot_ms_script_24_hour),
					]),	

  (0, 0, 24*7, [], [                        						
						(call_script, "script_ms_check_time_event", slot_ms_script_7_day),						
					]),		

  (0, 0, 24*30, [], [
						(call_script, "script_ms_check_time_event", slot_ms_script_30_day),
					]),							
		#MS Time triger -end
		
		#MS Additional menu triger -begin
  (0, 0, 1, [], [
						(call_script, "script_ms_check_npc_studing"),
					]),		
	
  (0, 0, 24, [], [
						(call_script, "script_ms_check_deposit_credit"),
						(call_script, "script_ms_init"), 
					]),		
  (0, 0, 1, [], [
						(call_script, "script_ms_check_extra_weapon_time", slot_ms_party_armourer_time),
						(call_script, "script_ms_check_extra_weapon_time", slot_ms_party_protection_time),
						(call_script, "script_ms_check_extra_weapon_time", slot_ms_party_horse_time),
					]),							
		#MS Additional menu triger -end
	#Expanded management system -end
  (0, 0, 1, [], [
					#(try_begin), 
						#(eq, "$castle_traders_re_inited", 0), 
						#(call_script, "script_re_init_castle_traders"), 
						#(assign, "$castle_traders_re_inited", 1), 
					#(end_try), 
					(call_script, "script_check_diplomatic_capital"),
				]),			

  (0, 0, 24*30, [], [
					(call_script, "script_check_trade_deal"),
				]),			
  (0, 0,  1, [], [
					(try_for_range, ":center_no", towns_begin, castles_end),
						(try_for_range, ":cur_slot", slot_ms_officer_lower_level_timer, slot_ms_officer_lower_level_amount),
							(party_slot_ge, ":center_no", ":cur_slot", 1),
							(party_get_slot, ":time", ":center_no", ":cur_slot"),
							(val_sub, ":time", 1),
							(party_set_slot, ":center_no", ":cur_slot", ":time"),
						(try_end),
					(try_end),
					]),	
  
   (0, 0,  ti_once, [], [
							(call_script, "script_ms_fill_ai_officer_troops"),
					]),	
 
 (0, 0,  9, [], [ #was 4*24
					    (call_script, "script_ms_fill_ai_officer_troops"),
						
					]),	
 (0, 0, 3, [], 
 [
	(try_for_range, ":village_no", villages_begin, villages_end), 
		(store_faction_of_party, ":party_faction", ":village_no"),
		(party_get_slot, ":town_no", ":village_no", slot_village_bound_center),
		(store_faction_of_party, ":town_faction", ":town_no"),
		(neq, ":town_faction", ":party_faction"),
		(call_script, "script_give_center_to_faction_aux", ":village_no", ":town_faction"), 
	(end_try),

 ]),
	
 (0, 0, 0, [(eq, "$g_oim_troop_recruiting_time_set", 0)], #bug fix Suvorov
 [
	(assign, "$g_oim_troop_recruiting_time_set", 1), 
	(try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end), 
		(troop_set_slot, ":troop_no", slot_troop_last_recruting_time, -10),
	(end_try),	
	(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
		(party_set_slot, ":center_no", slot_center_last_recruting_time, -10),
	(end_try),
 ]),
 

(1.0, 0, 0, [(eq, "$g_tavern_rest", 1), (store_random_in_range, ":random_no", 0, 120), (is_currently_night), (eq, ":random_no", 0),], 
 [ 
   (jump_to_menu, "mnu_oim_rich_visitor"), 
 ]),


(1, 0.3, 0, 
 [
   (assign, ":number_of_velvets", 0),
   (troop_get_inventory_capacity, ":capacity", "trp_player"),
   (try_for_range, ":cur_slot", 0, ":capacity"),
     (troop_get_inventory_slot, ":item", "trp_player", ":cur_slot"),
	 (eq, ":item", "itm_velvet"),
	 (val_add, ":number_of_velvets", 1),
   (try_end),

   (try_begin),
     (ge, ":number_of_velvets", 10),
	 (unlock_achievement, ACHIEVEMENT_VELVET_COMMANDER),
   (try_end),

   (assign, ":not_completed", 0),
   (store_add, ":fac_kingdom_5_plus_1", "fac_kingdom_5", 1),
   (try_for_range, ":faction_no", "fac_kingdom_1", ":fac_kingdom_5_plus_1"),
     (neq, ":faction_no", "$players_kingdom"),
     (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
	 (assign, ":not_completed", 1),
   (try_end),
   (eq, ":not_completed", 0),
 ], 
 [
   (try_begin),
     (eq, "$players_kingdom", "fac_kingdom_3"),
	 (unlock_achievement, ACHIEVEMENT_RETURN_OF_THE_HORDE),	 
   (else_try),
     (eq, "$players_kingdom", "fac_kingdom_4"),
	 (unlock_achievement, ACHIEVEMENT_SWEDISH_SCOURGE),	 
   (else_try),
     (unlock_achievement, ACHIEVEMENT_POWER_SHIFT),	 
   (try_end),
 ]),
	

]
