from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################

#pilgrim_disguise = [itm_pilgrim_hood,itm_pilgrim_disguise,itm_practice_staff, itm_throwing_daggers]
#af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian

#pilgrim_disguise = [itm_pilgrim_hood,itm_pilgrim_disguise,itm_practice_staff, itm_dagger, itm_throwing_daggers]

pilgrim_disguise = [itm_dobrotna_svitka_b, itm_sapogi, itm_poland_shapka, itm_sablya_a, itm_old_pistol, itm_bolts]

pilgrim_disguise_oim = [itm_pilgrim_hood,itm_pilgrim_disguise]
tatar_disguise_oim = [itm_tatar_steg_halat_a, itm_dagger, itm_throwing_daggers] 
af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian

oim_duel_equip = [itm_duel_sword, itm_poland_svitka_a, itm_selo_boots]
oim_duel_equip_swed = [itm_rusty_shpaga, itm_evropa_odejda_sela, itm_selo_boots]

oim_duel_equip_npc = [itm_sablya_turk_b, itm_poland_svitka_a, itm_selo_boots]
oim_duel_equip_swed_npc = [itm_good_shpaga_b, itm_evropa_odejda_sela, itm_selo_boots]
oim_ranged_practice = [itm_samopal, itm_steel_bolts_10]

oim_hand_to_hand = [itm_mosk_sermyaga, itm_selo_boots]

oim_duel_equip_alevtina_hanum = [itm_tatar_halat_b, itm_tatar_bayrak_hat, itm_sablya_tatar_a, itm_pistol_b, itm_norm_bullets, itm_janissary_tapki] 

##OiM Mp code:

oim_common_ladders_system_init = (
  ti_before_mission_start, 0, 0, [],
  [
	(call_script, "script_get_ladder_mission"), 
	(assign, "$num_ladders", reg1), #should be changed
	(assign, "$cur_ladder_to_assign_archers", 0), 
	(assign, "$cur_ladder_to_assign_infantry", 0), 
  ] 
 )  
  
oim_common_ladders_system_process = (
 0.1, 0, 0, [], 
 [
 (call_script, "script_process_siege_attackers"),
 ])

oim_on_horse_dismount = (
 ti_on_agent_dismount, 0, 0, [],
 [
	(store_trigger_param_1, ":cur_agent"),
	(call_script, "script_game_event_agent_dismounted", ":cur_agent"),
 ])
 
 
 #process_siege_attackers_no_stack
oim_common_process_siege_attackers_no_stack = (
 0.1, 0, 0, [], 
 [
 (call_script, "script_process_siege_attackers_no_stack"),
 ])

 
oim_common_ladders_system_process_simple_order = (
 0, 0, 0, [], 
 [
    (try_begin),
		(this_or_next|game_key_clicked, gk_order_1),
		(this_or_next|game_key_clicked, gk_order_2),
		(this_or_next|game_key_clicked, gk_order_3),
		(this_or_next|game_key_clicked, gk_order_4),
		(this_or_next|game_key_clicked, gk_order_5),
		(             game_key_clicked, gk_order_6),
		(get_player_agent_no, ":player_agent"),
		(agent_get_team, ":agent_team", ":player_agent"),
		(this_or_next|eq, ":agent_team", "$attacker_team"),
		(             eq, ":agent_team", "$attacker_team_2"),
		(call_script, "script_remove_script_behavior"), 
	(end_try), 	
  ])	

custom_oim_replace_items_begin = (
  ti_on_agent_spawn, 0, 0, [], 
  [
    #(store_trigger_param_1, ":cur_agent"),
    (store_trigger_param_1, ":cur_agent"),
    (call_script, "script_replace_agent_items_assault", ":cur_agent"),	
    (call_script, "script_setup_bot_initials", ":cur_agent"),	
  ])
  
custom_oim_replace_items_nerf = (
  ti_on_agent_spawn, 0, 0, [], 
  [
   # No need to nerf items this way anymore. We do this in the code - Armagan
    # (store_trigger_param_1, ":cur_agent"),
	# (agent_is_active, ":cur_agent"),
	# #(get_average_game_difficulty, ":difficulty"),
	# (options_get_combat_ai, ":difficulty"),
	# (get_player_agent_no, ":player_agent"),
	# (agent_is_active, ":player_agent"),
	# (agent_get_team, ":agent_team", ":player_agent"),
	# (agent_get_team, ":cur_agent_team", ":cur_agent"),
	# (try_begin), 
		# (eq, ":difficulty", 2),
		# (this_or_next|eq, ":agent_team", "$attacker_team"),
		# (             eq, ":agent_team", "$attacker_team_2"),
		# (this_or_next|eq, ":cur_agent_team", "$defender_team"),
		# (             eq, ":cur_agent_team", "$defender_team_2"),
		# (call_script, "script_replace_agent_items_nerf", ":cur_agent"),	
	# (else_try), 
		# (eq, ":difficulty", 2),
		# (this_or_next|eq, ":agent_team", "$defender_team"),
		# (             eq, ":agent_team", "$defender_team_2"),
		# (this_or_next|eq, ":cur_agent_team", "$attacker_team"),
		# (             eq, ":cur_agent_team", "$attacker_team_2"),
		# (call_script, "script_replace_agent_items_nerf", ":cur_agent"),		
	# (end_try), 	
  ])  

multiplayer_set_map_weather = (
  ti_before_mission_start, 0, 0, [],
  [
    (store_current_scene, ":cur_scene"),
    (try_begin),
      (eq, ":cur_scene", "scn_mp_new_3"),
      (scene_set_day_time, 6),
      (set_skybox, 14, 15), #skybox_cloud_1
      (set_fog_distance, 200, 0xFF60545B),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,188,180,140),
      (set_startup_ambient_light,6,4,2),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
      (eq, ":cur_scene", "scn_mp_old_castle"),
      (scene_set_day_time, 18),
      (set_skybox, 6, 7), #skybox_cloud_1
      (set_fog_distance, 1200, 0xFF957757),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,620,484,216),
      (set_startup_ambient_light,90,105,123),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
      (eq, ":cur_scene", "scn_mp_arena"),
 #     (scene_set_day_w
 #     (set_skybox, 7, 8), #skybox_cloud_1
 #     (set_fog_distance, 700, 0xFFa49684),
 #     (set_fixed_point_multiplier,255),
 #     (set_startup_sun_light,1020,864,468),
 #     (set_startup_ambient_light,43,33,10),
 #     (set_startup_ground_ambient_light,80,70,50),
	(else_try),
      (eq, ":cur_scene", "scn_mp_swamp_delta"),
      (scene_set_day_time, 15),
      (set_skybox, 6, 7), #skybox_cloud_1
      (set_fog_distance, 300, 0xFFa7a190),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,420,330,276),
      (set_startup_ambient_light,68,78,62),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_polya"),
      (scene_set_day_time, 15),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 1400, 0xFF9a7533),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,414,358,196),
      (set_startup_ambient_light,83,64,52),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_hillroad"),
#      (scene_set_day_time, 10),
#      (set_skybox, 5,6), #skybox_cloud_1
#	  (set_rain, 1,100),
#      (set_fog_distance, 500, 0xFF947f54),
#      (set_fixed_point_multiplier,255),
#      (set_startup_sun_light,312,272,108),
#      (set_startup_ambient_light,146,119,90),
#      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_hutor"),
      (scene_set_day_time, 7),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 1400, 0xFF978d78),
      (set_fixed_point_multiplier,250),
      (set_startup_sun_light,432,322,150),
      (set_startup_ambient_light,58,49,37),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_marketplace"),
      (scene_set_day_time, 11),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 1800, 0xFF967049),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,256,196,102),
      (set_startup_ambient_light,30,25,32),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_forest_edge"),
      (scene_set_day_time, 13),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 1300, 0xFFafaf95),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,320,228,136),
      (set_startup_ambient_light,77,54,12),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_forest_road"),
      (scene_set_day_time, 10),
      (set_skybox, 6, 7), #skybox_cloud_1
      (set_fog_distance, 1000, 0xa88848),
      (set_fixed_point_multiplier,200),
      (set_startup_sun_light,620,440,240),
      (set_startup_ambient_light,58,76,101),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_river_village"),
      (scene_set_day_time, 10),
      (set_skybox, 6, 7), #skybox_cloud_1
      (set_fog_distance, 700, 0xFF969866),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,564,470,396),
      (set_startup_ambient_light,45,60,53),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_nomad_camp"),
      (scene_set_day_time, 15),
      (set_skybox, 14,15), #skybox_cloud_1
      (set_fog_distance, 250, 0xFF928054),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,412,328,188),
      (set_startup_ambient_light,62,37,12),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_swed_zamok"),
      (scene_set_day_time, 15),
      (set_skybox, 10, 11), #skybox_cloud_1
      (set_fog_distance, 170, 0xFFaa9c86),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,48,56,40),
      (set_startup_ambient_light,31,31,31),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_novgorod_fortress"),
      (scene_set_day_time, 15),
      (set_skybox, 10, 11), #skybox_cloud_1
      (set_fog_distance, 1400, 0xFF92774a),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,272,180,124),
      (set_startup_ambient_light,23,14,0),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_rus_fortress"),
      (scene_set_day_time, 15),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 1200, 0xFF867361),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,628,548,428),
      (set_startup_ambient_light,88,66,41),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_mosk_monastyr"),
      (scene_set_day_time, 15),
      (set_skybox, 10, 11), #skybox_cloud_1
      (set_fog_distance, 1200, 0xFF46371b),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,624,544,328),
      (set_startup_ambient_light,29,33,41),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_new_1"),
      (scene_set_day_time, 15),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 800, 0xFF9a8f5e),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,372,272,84),
      (set_startup_ambient_light,49,45,34),
      (set_startup_ground_ambient_light,80,70,50),
	(else_try),
	  (eq, ":cur_scene", "scn_mp_new_2"),
      (scene_set_day_time, 17),
      (set_skybox, 8, 9), #skybox_cloud_1
      (set_fog_distance, 1200, 0xFFaf9067),
      (set_fixed_point_multiplier,255),
      (set_startup_sun_light,460,304,56),
      (set_startup_ambient_light,29,25,10),
      (set_startup_ground_ambient_light,80,70,50),
	  
	  
	  
	  
	  
	  #(set_fog_distance, 3000, 0xFFFFFFFF),
      #(set_fixed_point_multiplier, 255),
      #(set_startup_sun_light, 200, 200, 200), #NOTE: IN EDIT MODE "SunLight" PARAMETER RANGE IS [0-4] (eg. valueof(200) = (200/255)*4 )! 
      #(set_startup_ambient_light, 10, 10, 10),
      #(set_startup_ground_ambient_light, 30, 0, 0),
    (try_end),
    ])



multiplayer_server_check_belfry_movement = (
  1, 0, 0, [],
  [
    (multiplayer_is_server),
    (set_fixed_point_multiplier, 100),

    (try_for_range, ":belfry_kind", 0, 2),
      (try_begin),
        (eq, ":belfry_kind", 0),
        (assign, ":belfry_body_scene_prop", "spr_belfry_a"),
      (else_try),
        (assign, ":belfry_body_scene_prop", "spr_belfry_b"),
      (try_end),
    
      (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
      (try_for_range, ":belfry_no", 0, ":num_belfries"),
        (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
        (prop_instance_get_position, pos1, ":belfry_scene_prop_id"), #pos1 holds position of current belfry 
        (prop_instance_get_starting_position, pos11, ":belfry_scene_prop_id"),

        (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
        (try_begin),
          (eq, ":belfry_kind", 1),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
        (try_end),        
                
        (val_mul, ":belfry_first_entry_point_id", 10),
        (store_add, ":belfry_last_entry_point_id", ":belfry_first_entry_point_id", 10),
    
        (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id"),
          (entry_point_is_auto_generated, ":entry_point_id"),
          (assign, ":belfry_last_entry_point_id", ":entry_point_id"),
        (try_end),
        
        (assign, ":belfry_last_entry_point_id_plus_one", ":belfry_last_entry_point_id"),
        (val_sub, ":belfry_last_entry_point_id", 1),
        (assign, reg0, ":belfry_last_entry_point_id"),
        (neg|entry_point_is_auto_generated, ":belfry_last_entry_point_id"),

        (try_begin),
          (get_sq_distance_between_positions, ":dist_between_belfry_and_its_destination", pos1, pos11),
          (ge, ":dist_between_belfry_and_its_destination", 4), #0.2 * 0.2 * 100 = 4 (if distance between belfry and its destination already less than 20cm no need to move it anymore)

          (assign, ":max_dist_between_entry_point_and_belfry_destination", -1), #should be lower than 0 to allow belfry to go last entry point
          (assign, ":belfry_next_entry_point_id", -1),
          (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id_plus_one"),
            (entry_point_get_position, pos4, ":entry_point_id"),
            (get_sq_distance_between_positions, ":dist_between_entry_point_and_belfry_destination", pos11, pos4),
            (lt, ":dist_between_entry_point_and_belfry_destination", ":dist_between_belfry_and_its_destination"),
            (gt, ":dist_between_entry_point_and_belfry_destination", ":max_dist_between_entry_point_and_belfry_destination"),
            (assign, ":max_dist_between_entry_point_and_belfry_destination", ":dist_between_entry_point_and_belfry_destination"),
            (assign, ":belfry_next_entry_point_id", ":entry_point_id"),
          (try_end),

          (try_begin),
            (ge, ":belfry_next_entry_point_id", 0),
            (entry_point_get_position, pos5, ":belfry_next_entry_point_id"), #pos5 holds belfry next entry point target during its path
          (else_try),
            (copy_position, pos5, pos11),    
          (try_end),
        
          (get_distance_between_positions, ":belfry_next_entry_point_distance", pos1, pos5),
        
          #collecting scene prop ids of belfry parts
          (try_begin),
            (eq, ":belfry_kind", 0),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
            #belfry platform_b
            (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
          (else_try),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),
    
          #belfry wheel_1
          (store_mul, ":wheel_no", ":belfry_no", 3),
          (try_begin),
            (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
            (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
            (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
            (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
          (try_end),
          (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_2
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_3
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),

          (init_position, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos18, pos1, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos19, pos1, pos17),

          (assign, ":number_of_agents_around_belfry", 0),
          (get_max_players, ":num_players"),
          (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":agent_id", ":player_no"),
            (ge, ":agent_id", 0),
            (agent_get_team, ":agent_team", ":agent_id"),
            (eq, ":agent_team", 1), #only team2 players allowed to move belfry (team which spawns outside the castle (team1 = 0, team2 = 1))
            (agent_get_horse, ":agent_horse_id", ":agent_id"),
            (eq, ":agent_horse_id", -1),
            (agent_get_position, pos2, ":agent_id"),
            (get_sq_distance_between_positions_in_meters, ":dist_between_agent_and_belfry", pos18, pos2),

            (lt, ":dist_between_agent_and_belfry", multi_distance_sq_to_use_belfry), #must be at most 10m * 10m = 100m away from the player
            (neg|scene_prop_has_agent_on_it, ":belfry_scene_prop_id", ":agent_id"),
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_a_scene_prop_id", ":agent_id"),

            (this_or_next|eq, ":belfry_kind", 1), #there is this_or_next here because belfry_b has no platform_b
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_b_scene_prop_id", ":agent_id"),
    
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_1_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_2_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_3_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|position_is_behind_position, pos2, pos19),
            (position_is_behind_position, pos2, pos1),
            (val_add, ":number_of_agents_around_belfry", 1),        
          (try_end),

          (val_min, ":number_of_agents_around_belfry", 16),

          (try_begin),
            (scene_prop_get_slot, ":pre_number_of_agents_around_belfry", ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing),
            (scene_prop_get_slot, ":next_entry_point_id", ":belfry_scene_prop_id", scene_prop_next_entry_point_id),
            (this_or_next|neq, ":pre_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),
            (neq, ":next_entry_point_id", ":belfry_next_entry_point_id"),

            (try_begin),
              (eq, ":next_entry_point_id", ":belfry_next_entry_point_id"), #if we are still targetting same entry point subtract 
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              (store_mul, ":sqrt_number_of_agents_around_belfry", "$g_last_number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (assign, ":distance", ":belfry_next_entry_point_distance"),
              (val_mul, ":distance", ":sqrt_number_of_agents_around_belfry"),
              (val_div, ":distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":distance", 4), #multiplying with 4 to make belfry pushing process slower, 
                                                                 #with 16 agents belfry will go with 4 / 4 = 1 speed (max), with 1 agent belfry will go with 1 / 4 = 0.25 speed (min)    
            (try_end),

            (try_begin),
              (ge, ":belfry_next_entry_point_id", 0),

              #up down rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), 
              (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry
      
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, 300), #go 3.0 meters right
              (position_transform_position_to_parent, pos10, pos5, pos9), 
              (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
              (init_position, pos20),    
              (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos23, pos5, pos20),

              #right left rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),    
              (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees. 
              (val_mul, ":rotate_angle_of_next_entry_point", -1),

              (init_position, pos20),
              (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos22, pos23, pos20),
            (else_try),
              (copy_position, pos22, pos5),      
            (try_end),
              
            (try_begin),
              (ge, ":number_of_agents_around_belfry", 1), #if there is any agents pushing belfry

              (store_mul, ":sqrt_number_of_agents_around_belfry", ":number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (val_mul, ":belfry_next_entry_point_distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":belfry_next_entry_point_distance", 3), #multiplying with 3 to make belfry pushing process slower, 
                                                                 #with 9 agents belfry will go with 3 / 3 = 1 speed (max), with 1 agent belfry will go with 1 / 3 = 0.33 speed (min)    
              (val_div, ":belfry_next_entry_point_distance", ":sqrt_number_of_agents_around_belfry"),
              #calculating destination coordinates of belfry parts
              #belfry platform_a
              (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos1, pos6),
              (position_transform_position_to_parent, pos8, pos22, pos7),
              (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),    
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
                (position_transform_position_to_local, pos7, pos1, pos6),
                (position_transform_position_to_parent, pos8, pos22, pos7),
                (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              (try_end),
              #wheel rotation
              (store_mul, ":belfry_wheel_rotation", ":belfry_next_entry_point_distance", -25),
              #(val_add, "$g_belfry_wheel_rotation", ":belfry_wheel_rotation"),
              (assign, "$g_last_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),

              #belfry wheel_1
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_1_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),
      
              #belfry wheel_2
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_2_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),
      
              #belfry wheel_3
              (prop_instance_get_position, pos13, ":belfry_wheel_3_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_3_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry main body
              (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos22, ":belfry_next_entry_point_distance"),    
            (else_try),
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              #belfry platform_a
              (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
              (try_end),
              #belfry wheel_1
              (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
              #belfry wheel_2
              (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
              #belfry wheel_3
              (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
              #belfry main body
              (prop_instance_stop_animating, ":belfry_scene_prop_id"),
            (try_end),
        
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, ":number_of_agents_around_belfry"),    
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, ":belfry_next_entry_point_id"),
          (try_end),
        (else_try),
          (le, ":dist_between_belfry_and_its_destination", 4),
          (scene_prop_slot_eq, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
      
          (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),    

          (try_begin),
            (eq, ":belfry_kind", 0),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
          (else_try),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),
    
          (prop_instance_get_starting_position, pos0, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos0, 400),    
        (try_end),
      (try_end),
    (try_end),
    ])

multiplayer_server_spawn_bots = (
  0, 0, 0, [],
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
    (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"),
    (try_begin),
      (gt, ":total_req", 0),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
##        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_siege),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

        (team_get_score, ":team_1_score", 0),
        (team_get_score, ":team_2_score", 1),

        (store_add, ":current_round", ":team_1_score", ":team_2_score"),
        (eq, ":current_round", 0),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),
        (lt, ":round_time", 20),

        (assign, ":rounded_game_first_round_time_limit_past", 0),
      (else_try),
        (assign, ":rounded_game_first_round_time_limit_past", 1),
      (try_end),
    
      (eq, ":rounded_game_first_round_time_limit_past", 1),
    
      (store_random_in_range, ":random_req", 0, ":total_req"),
      (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),
      (try_begin),
        (lt, ":random_req", 0),
        #add to team 1
        (assign, ":selected_team", 0),
      (else_try),
        #add to team 2
        (assign, ":selected_team", 1),
      (try_end),

      (try_begin),
##        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
##        (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),
    
      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),

      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (player_get_team_no, ":player_team_no", ":player_no"),
        (eq, ":selected_team", ":player_team_no"),

        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
          (player_slot_ge, ":player_no", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0), 
        (try_end),

        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),

      (try_begin),
        (this_or_next|ge, ":selected_group", 0),
        (eq, ":number_of_active_players_wanted_bot", 0),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
          (assign, ":is_horseman", 1),
        (else_try),
          (assign, ":is_horseman", 0),
        (try_end),

        (try_begin),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_siege),
          (             eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

          (store_mission_timer_a, ":round_time"),
          (val_sub, ":round_time", "$g_round_start_time"),

          (try_begin),
            (lt, ":round_time", 20), #at start of game spawn at base entry point
            (try_begin),
              (eq, ":selected_team", 0),
              (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 1, ":is_horseman"), 
            (else_try),
              (assign, reg0, multi_initial_spawn_point_team_2),
            (try_end),
          (else_try),
            (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"), 
          (try_end),
        (else_try),
##          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
##          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
      
          (try_begin),
            (eq, ":selected_team", 0),
            (assign, reg0, 0),
          (else_try),
            (assign, reg0, 32),
          (try_end),
        (else_try),
          (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"), 
        (try_end),
      
        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

        (try_begin),
          (eq, ":selected_team", 0),
          (val_sub, "$g_multiplayer_num_bots_required_team_1", 1),
        (else_try),
          (eq, ":selected_team", 1),
          (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
        (try_end),
      (try_end),
    (try_end),    
    ])

multiplayer_server_manage_bots = (
  3, 0, 0, [],
  [
    (multiplayer_is_server),
    (try_for_agents, ":cur_agent"),
      (agent_is_non_player, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_get_group, ":agent_group", ":cur_agent"),
      (try_begin),
        (neg|player_is_active, ":agent_group"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (else_try),
        (player_get_team_no, ":leader_team_no", ":agent_group"),
        (agent_get_team, ":agent_team", ":cur_agent"),
        (neq, ":leader_team_no", ":agent_team"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (try_end),
    (try_end),
    ])

multiplayer_server_check_polls = (
  1, 5, 0,
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_poll_running", 1),
    (eq, "$g_multiplayer_poll_ended", 0),
    (store_mission_timer_a, ":mission_timer"),
    (store_add, ":total_votes", "$g_multiplayer_poll_no_count", "$g_multiplayer_poll_yes_count"),
    (this_or_next|eq, ":total_votes", "$g_multiplayer_poll_num_sent"),
    (gt, ":mission_timer", "$g_multiplayer_poll_end_time"),
    (call_script, "script_cf_multiplayer_evaluate_poll"),
    ],
  [
    (assign, "$g_multiplayer_poll_running", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_poll_to_show", 0), #change map
      (eq, "$g_multiplayer_poll_to_show", 3), #change map with factions
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_poll_value_to_show", 1),
      (call_script, "script_game_set_multiplayer_mission_end"),
    (try_end),
    ])
    
multiplayer_server_check_end_map = ( 
  1, 0, 0, [],
  [
    (multiplayer_is_server),
    #checking for restarting the map
    (assign, ":end_map", 0),
	(try_begin),
	  (eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_coop),
	  (try_begin),
		(eq, "$g_round_ended", 1),
		(assign, ":end_map", 1),
	  (try_end),
	(else_try),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_battle),
##      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_siege),
      (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
    
      (try_begin),
        (eq, "$g_round_ended", 1),

        (store_mission_timer_a, ":seconds_past_till_round_ended"),
        (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
        (store_sub, ":multiplayer_respawn_period_minus_one", "$g_multiplayer_respawn_period", 1),
        (ge, ":seconds_past_till_round_ended", ":multiplayer_respawn_period_minus_one"),
  
        (store_mission_timer_a, ":mission_timer"),    
        (try_begin),
##          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
##          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_captain_battle),
          (assign, ":reduce_amount", 90),
        (else_try),
          (assign, ":reduce_amount", 120),
        (try_end),
    
        (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
        (store_sub, ":game_max_seconds_min_n_seconds", ":game_max_seconds", ":reduce_amount"), #when round ends if there are 60 seconds to map change time then change map without completing exact map time.
        (gt, ":mission_timer", ":game_max_seconds_min_n_seconds"),
        (assign, ":end_map", 1),
      (try_end),
      
      (eq, ":end_map", 1),
    (else_try),
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #battle mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_captain_battle), #captain battle mod has different end map condition by time
##      (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #fight and destroy mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_captain_siege), #siege mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege), #siege mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #in headquarters mod game cannot limited by time, only can be limited by score.
      (store_mission_timer_a, ":mission_timer"),
      (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
      (gt, ":mission_timer", ":game_max_seconds"),
      (assign, ":end_map", 1),
    (else_try),
      #assuming only 2 teams in scene
      (team_get_score, ":team_1_score", 0),
      (team_get_score, ":team_2_score", 1),
      (try_begin),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #for not-headquarters mods
        (try_begin),
          (this_or_next|ge, ":team_1_score", "$g_multiplayer_game_max_points"),
          (ge, ":team_2_score", "$g_multiplayer_game_max_points"),
          (assign, ":end_map", 1),
        (try_end),
      (else_try),
        (assign, ":at_least_one_player_is_at_game", 0),
        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 0, ":num_players"),
          (player_is_active, ":player_no"),
          (player_get_agent_id, ":agent_id", ":player_no"),
          (ge, ":agent_id", 0),
          (neg|agent_is_non_player, ":agent_id"),
          (assign, ":at_least_one_player_is_at_game", 1),
          (assign, ":num_players", 0),
        (try_end),
    
        (eq, ":at_least_one_player_is_at_game", 1),

        (this_or_next|le, ":team_1_score", 0), #in headquarters game ends only if one team has 0 score.
        (le, ":team_2_score", 0),
        (assign, ":end_map", 1),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":end_map", 1),
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 0),
      (call_script, "script_game_set_multiplayer_mission_end"),           
    (try_end),
    ])

multiplayer_once_at_the_first_frame = (
  0, 0, ti_once, [], [
    (start_presentation, "prsnt_multiplayer_welcome_message"),
    ])

multiplayer_battle_window_opened = (
  ti_battle_window_opened, 0, 0, [], [
    (start_presentation, "prsnt_multiplayer_team_score_display"),
    ])


common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

common_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (eq, "$g_battle_won", 1),
      (call_script, "script_count_mission_casualties_from_agents"),
      (finish_mission,0),
    (else_try),
      (call_script, "script_cf_check_enemies_nearby"),
      (question_box,"str_do_you_want_to_retreat"),
    (else_try),
      (display_message,"str_can_not_retreat"),
    (try_end),
    ])

common_battle_init_banner = (
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":agent_no"),
    (agent_get_troop_id, ":troop_no", ":agent_no"),
    (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),
  ])


common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_fight"),
    ])

common_custom_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (neq, "$g_battle_result", 0),
      (call_script, "script_custom_battle_end"),
      (finish_mission),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ])

custom_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 2),
    (neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign, "$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission, 1),
    ])

custom_battle_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen),
    (assign,"$g_battle_result",-1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission),
    ])

common_battle_victory_display = (
  10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$pin_player_fallen", 0),
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":agent_team", ":player_agent"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15, 0),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20, 0),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_custom_battle_question_answered = (
   ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$g_battle_result", -1),
     (call_script, "script_custom_battle_end"),
     (finish_mission),
     ])

common_custom_siege_init = (
  0, 0, ti_once, [],
  [
    (assign, "$g_battle_result", 0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign,"$g_battle_won",0),
    (assign,"$defender_reinforcement_stage",0),
    (assign,"$attacker_reinforcement_stage",0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_music_situation_update = (
  30, 0, 0, [],
  [
    (call_script, "script_combat_music_set_situation_with_culture"),
    ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_2 = (
  0, 0, ti_once,
  [
    (set_show_messages, 0),
    (entry_point_get_position, pos10, 10),
    (try_for_range, ":cur_group", 0, grc_everyone),
      (neq, ":cur_group", grc_archers),
      (team_give_order, "$defender_team", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
    (try_end),
    (team_give_order, "$defender_team", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team", grc_everyone, pos10),
    (team_give_order, "$defender_team_2", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team_2", grc_everyone, pos10),
    (set_show_messages, 1),
    ], [])

common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

common_siege_defender_reinforcement_check = (
  3, 0, 5, [],
  [(lt, "$defender_reinforcement_stage", 20),
   (store_mission_timer_a,":mission_time"),
   (ge,":mission_time",10),
   (store_normalized_team_count,":num_defenders",0),
   (lt,":num_defenders",8),
   (add_reinforcements_to_entry,4, 7),
   (val_add,"$defender_reinforcement_stage",1),
   (try_begin),
     #(gt, ":mission_time", 100), #5 minutes, don't let small armies charge
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":player_team", ":player_agent"),
     (neq, ":player_team", "$defender_team"), #player should be the attacker
     (neq, ":player_team", "$defender_team_2"), #player should be the attacker
     (ge, "$defender_reinforcement_stage", 2),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     (team_give_order, "$defender_team_2", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
     (set_show_messages, 1),
     (ge, "$defender_reinforcement_stage", 4),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (set_show_messages, 1),
   (try_end),
   ])

common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

common_siege_attacker_reinforcement_check = (
  1, 0, 5,
  [
    (lt,"$attacker_reinforcement_stage",15),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
    (lt,":num_attackers",6)
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])

common_siege_attacker_do_not_stall = (
  5, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),
      (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
    (try_end),
    ])

common_battle_check_friendly_kills = (
  2, 0, 0, [],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
    (neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign,"$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission, 1),
    ])

common_battle_victory_display = (
  10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_refill_ammo = (
  120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    (get_player_agent_no, ":player_agent"),
    (try_for_agents,":cur_agent"),
      (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
##      (agent_is_defender, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
    (try_end),
    ])

common_siege_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen)
    ],
  [
    (assign, "$pin_player_fallen", 1),
    (get_player_agent_no, ":player_agent"),
    (agent_get_team, ":agent_team", ":player_agent"),
    (try_begin),
      (neq, "$attacker_team", ":agent_team"),
      (neq, "$attacker_team_2", ":agent_team"),
      (str_store_string, s5, "str_siege_continues"),
      (call_script, "script_simulate_retreat", 8, 15, 0),
    (else_try),
      (str_store_string, s5, "str_retreat"),
      (call_script, "script_simulate_retreat", 5, 20, 0),
    (try_end),
    (assign, "$g_battle_result", -1),
    (set_mission_result,-1),
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission,0),
    ])

common_battle_order_panel = (
  0, 0, 0, [],
  [
    (game_key_clicked, gk_view_orders),
    (neg|is_presentation_active, "prsnt_battle"),
    (start_presentation, "prsnt_battle"),
    ])

common_battle_order_panel_tick = (
  0.1, 0, 0, [],
  [
    (is_presentation_active, "prsnt_battle"),
    (call_script, "script_update_order_panel_statistics_and_map"),
    ])

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (display_message,"str_use_baggage_for_inventory"),
    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now"),
    ], [])

common_siege_init_ai_and_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_init_ai_and_belfry"),
    ], [])

common_siege_move_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_belfry"),
    ], [])

common_siege_rotate_belfry = (
  0, 2, ti_once,
  [
    (call_script, "script_cf_siege_rotate_belfry_platform"),
    ],
  [
    (assign, "$belfry_positioned", 3),
    ])

common_siege_assign_men_to_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_assign_men_to_belfry"),
    ], [])

#OiM code
common_siege_attacker_reinforcement_check_modify = (
  1, 0, 5,
  [ 
    (lt,"$attacker_reinforcement_stage",5),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
	(store_normalized_team_count,":num_defender",0),
    (lt,":num_attackers",6),
	(lt,":num_defender","$g_enemy_count"),
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])
	
common_horse_death_init = (
  0, 0, ti_once,
  [  ], 
	[  
	##(assign,"$before_defender_reinforcement_stage", "$defender_reinforcement_stage"),
    ##(assign,"$before_attacker_reinforcement_stage", "$attacker_reinforcement_stage"),
	##(assign, "$g_agent_max_index", 0),
	##(try_for_agents,":cur_agent"),
	##	(agent_is_alive, ":cur_agent"),
    ##    (agent_is_human, ":cur_agent"),
	##	(troop_set_slot, "trp_array_agents", "$g_agent_max_index", ":cur_agent"),
	##	(agent_get_horse, ":horse_agent", ":cur_agent"),
	##	(troop_set_slot, "trp_array_agents_horses", "$g_agent_max_index", ":horse_agent"),
	##	(val_add, "$g_agent_max_index", 1),
	##(try_end),
	
	])	

common_horse_death_run = (
  0.1, 0, 0,
  [
        ], 
	[
	])	

common_check_ladders_and_go_to = (
  0, 0,  ti_once,
  [
         ], 
	 [
	(assign, "$g_archers_must_go", 0),
	(assign, ":ladder_index", 0),
	(assign, "$g_ladder_count", 0),
	(try_for_range, ":ind", 0, 2),
		(try_begin),
			(eq, ":ind", 0),
			(assign, ":ladder_type", "spr_siege_ladder_14m"),
		(else_try),
			(assign, ":ladder_type", "spr_siege_ladder_12m"),
		(try_end),
		(scene_prop_get_num_instances, ":prop_count", ":ladder_type"),
		(try_for_range, ":cur_inst", 0, ":prop_count"),
			(scene_prop_get_instance, ":prop", ":ladder_type", ":cur_inst"),
			(prop_instance_get_position, pos0, ":prop"),
			(position_get_x, ":pos_x_prop", pos0),
			(position_get_y, ":pos_y_prop", pos0),
			(position_get_z, ":pos_z_prop", pos0),
			(try_begin),
				(gt, ":pos_z_prop", 453),
				##(val_add, ":pos_z_prop", 100),
					(entry_point_get_position, pos1, 10),
					(get_distance_between_positions,":min_distance", pos0, pos1),
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":prop"),
					(val_add, ":ladder_index", 1),
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_x_prop"),
					(val_add, ":ladder_index", 1),
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_y_prop"),
					(val_add, ":ladder_index", 1),
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_z_prop"),
					(val_add, ":ladder_index", 1),
					(entry_point_get_position, pos1, 0),
					(position_get_x, ":pos_x_start", pos1),
					(position_get_y, ":pos_y_start", pos1),
					(store_sub, ":difer_x", ":pos_x_start", ":pos_x_prop"),
					(val_abs, ":difer_x"),
					(store_sub, ":difer_y", ":pos_y_start", ":pos_y_prop"),
					(val_abs, ":difer_y"),
					(assign, ":k_x", 600),
					(assign, ":k_y", 600),
					(try_begin),
						(ge, ":difer_x", ":difer_y"),
						(val_mul, ":k_y", ":difer_y"),
						(val_div, ":k_y", ":difer_x"),
					(else_try),
						(val_mul, ":k_x", ":difer_x"),
						(val_div, ":k_x", ":difer_y"),
					(try_end),
					(store_mul, ":k_s_x", ":k_x", 3),
					(store_mul, ":k_s_y", ":k_y", 3),
					(try_begin),
						(ge, ":pos_x_prop", ":pos_x_start"),
						(store_sub, ":pos_x_s_prop", ":pos_x_prop", ":k_s_x"),
						(val_sub, ":pos_x_prop", ":k_x"),
					(else_try),
						(store_add, ":pos_x_s_prop", ":pos_x_prop", ":k_s_x"),
						(val_add, ":pos_x_prop", ":k_x"),
					(try_end),
					(try_begin),
						(ge, ":pos_y_prop", ":pos_y_start"),
						(store_sub, ":pos_y_s_prop", ":pos_y_prop", ":k_s_y"),
						(val_sub, ":pos_y_prop", ":k_y"),
					(else_try),
						(store_add, ":pos_y_s_prop", ":pos_y_prop", ":k_s_y"),
						(val_add, ":pos_y_prop", ":k_y"),
					(try_end),
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_x_prop"),
				(val_add, ":ladder_index", 1),	
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_y_prop"),
				(val_add, ":ladder_index", 1),	
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_x_s_prop"),
				(val_add, ":ladder_index", 1),	
					(troop_set_slot, "trp_ladder_array", ":ladder_index", ":pos_y_s_prop"),
				(val_add, ":ladder_index", 1),	
					(troop_set_slot, "trp_ladder_array", ":ladder_index", pos10),
					(try_for_range, ":cur_point", 40, 50),
						(entry_point_get_position,  pos6, ":cur_point"),
						(get_distance_between_positions, ":min_distance_new", pos0, pos6),
						(try_begin),
							(le, ":min_distance_new", ":min_distance"),
							(assign, ":min_distance", ":min_distance_new"),
							(troop_set_slot, "trp_ladder_array", ":ladder_index", ":cur_point"),
						(try_end),
					(try_end),
				(val_add, ":ladder_index", 1),
				
				(val_add, "$g_ladder_count", 1),
			(try_end),
		(try_end),
	(try_end),	
		
		
	(assign, "$g_infantry_count", 0),
	(assign, "$g_archers_count", 0),
	(get_player_agent_no,":player_agent"),
	(try_for_agents,":cur_agent"),
		(neg|eq, ":cur_agent", ":player_agent"),
		(agent_is_alive, ":cur_agent"),
		(agent_is_human, ":cur_agent"),
		(neg|agent_is_defender, ":cur_agent"),
		(agent_get_class , ":cur_class", ":cur_agent"),
		(agent_set_slot, ":cur_agent", slot_agent_is_old, 1),
		(try_begin),
          (eq, ":cur_class", grc_infantry),
          (troop_set_slot, "trp_ladder_infantry_array", "$g_infantry_count", ":cur_agent"),
		  (troop_set_slot, "trp_ladder_infantry_state_array", "$g_infantry_count", 0),
		  (val_add, "$g_infantry_count", 1),
        (else_try),
          (eq, ":cur_class", grc_archers),
          (troop_set_slot, "trp_ladder_archers_array", "$g_archers_count", ":cur_agent"),
		  (troop_set_slot, "trp_ladder_archers_state_array", "$g_archers_count", 0),
		  (val_add, "$g_archers_count", 1),
        (try_end),
	(try_end),	
	
	(assign, "$g_infantry_is", 0),
	(assign, "$g_archers_is", 0),
	(try_begin),
		(gt, "$g_infantry_count", 0),
		(assign, "$g_infantry_is", 1),
		(assign, ":l_index", 0),
		(try_for_range, ":i_agent", 0, "$g_infantry_count"),
			(try_begin),
				(eq, ":l_index", "$g_ladder_count"),
				(assign, ":l_index", 0),
			(try_end),
			(store_mul, ":cur_in_index", ":l_index", 9),
			(val_add, ":cur_in_index", 4),
			(troop_get_slot,":new_pos_x", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":new_pos_y", "trp_ladder_array", ":cur_in_index"),
			(troop_get_slot,":cur_i_agent", "trp_ladder_infantry_array", ":i_agent"),
			(init_position, pos0),
            (position_set_x, pos0, ":new_pos_x"),
			(position_set_y, pos0, ":new_pos_y"),
			(position_set_z_to_ground_level, pos0), #here we set the pos for infantry
			(agent_set_scripted_destination, ":cur_i_agent", pos0, 0),
			(troop_set_slot, "trp_ladder_infantry_state_array", ":i_agent", 1),
			(val_add, ":l_index", 1),
		(try_end),
		(store_mul, ":infantry_limit", 2, "$g_ladder_count"),
		(try_begin),
			(le, "$g_infantry_count", ":infantry_limit"),
			(assign, "$g_archers_must_go", 1),
		(try_end),
	(else_try),
		(assign, "$g_archers_must_go", 1),
	(try_end),	
	
	(try_begin),
		(gt, "$g_archers_count", 0),
		(assign, "$g_archers_is", 1),
		(assign, ":l_index", 0),
		(try_for_range, ":i_agent", 0, "$g_archers_count"),
			(try_begin),
				(eq, ":l_index", "$g_ladder_count"),
				(assign, ":l_index", 0),
			(try_end),
			(store_mul, ":cur_in_index", ":l_index", 9),
			(val_add, ":cur_in_index", 6),
			(troop_get_slot,":new_pos_x", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":new_pos_y", "trp_ladder_array", ":cur_in_index"),
			(troop_get_slot,":cur_i_agent", "trp_ladder_archers_array", ":i_agent"),
			(init_position, pos0),
            (position_set_x, pos0, ":new_pos_x"),
			(position_set_y, pos0, ":new_pos_y"),
			(position_set_z_to_ground_level, pos0), #here we set the pos for archers
			(agent_set_scripted_destination, ":cur_i_agent", pos0, 0),
			(troop_set_slot, "trp_ladder_archers_state_array", ":i_agent", 1),
			(val_add, ":l_index", 1),
		(try_end),
	(try_end),
	
	
	(set_show_messages, 0),
	(assign, ":cur_team_next", "$defender_team"),
	(try_for_agents, ":cur_agent"),
		(neg|eq, ":cur_agent", ":player_agent"),
		(agent_is_alive, ":cur_agent"),
		(agent_is_human, ":cur_agent"),
		(agent_is_defender, ":cur_agent"),
		(agent_get_team, ":cur_team", ":cur_agent"),
		(try_begin),
			(eq, ":cur_team", "$defender_team"),
			(agent_get_entry_no, ":entry_no", ":cur_agent"),
			(agent_get_position, pos0, ":cur_agent"),
			(entry_point_get_position, pos1,":entry_no"),
			(get_distance_between_positions, ":dist", pos1, pos0),
			(le, ":dist", 300),
			(try_begin),
				(eq, ":entry_no", 10),
				(assign, ":cur_team_next", 7),
			(else_try),
				(eq, ":entry_no", 41),
				(assign, ":cur_team_next", 8),
			(else_try),
				(eq, ":entry_no", 42),
				(assign, ":cur_team_next", 9),
			(else_try),
				(eq, ":entry_no", 43),
				(assign, ":cur_team_next", 10),
			(else_try),
				(eq, ":entry_no", 44),
				(assign, ":cur_team_next", 11),
			(try_end),
			(agent_set_team  , ":cur_agent", ":cur_team_next"),
			(agent_set_slot, ":cur_agent", slot_agent_is_old, 1),
		(try_end),
	(try_end),
	
	(try_for_range, ":cur_ladder", 0, "$g_ladder_count"),
		(try_begin),
			(eq, ":cur_ladder", 0),
			(assign, ":cur_team_next", 7),
			(assign, ":entry_no", 10),
		(else_try),
			(eq, ":cur_ladder", 1),
			(assign, ":cur_team_next", 8),
			(assign, ":entry_no", 41),
		(else_try),
			(eq, ":cur_ladder", 2),
			(assign, ":cur_team_next", 9),
			(assign, ":entry_no", 42),
		(else_try),
			(eq, ":cur_ladder", 3),
			(assign, ":cur_team_next", 10),
			(assign, ":entry_no", 43),
		(else_try),
			(eq, ":cur_ladder", 4),
			(assign, ":cur_team_next", 11),
			(assign, ":entry_no", 44),
		(try_end),
		(entry_point_get_position,  pos0, ":entry_no"),
		(team_give_order, ":cur_team_next", grc_infantry, mordr_hold),
		(team_give_order, ":cur_team_next", grc_infantry, mordr_stand_closer),
		(team_give_order, ":cur_team_next", grc_infantry, mordr_stand_closer),
		(team_give_order, ":cur_team_next", grc_archers, mordr_stand_ground),
		(team_set_relation, ":cur_team_next","$attacker_team", -1), 
		(team_set_order_position, ":cur_team_next", grc_everyone, pos0),
	(try_end),
			
    (set_show_messages, 1),
	])	
			
common_check_to_ladders = (
  0, 0, 0,
  [
        ], 
	[	
		(try_begin),
			(eq, "$g_infantry_is", 1),
			(assign, ":alive_count", 0),
			(assign, ":one_state_count", 0),
			(assign, ":l_index", 0),
			(try_for_range, ":i_agent", 0, "$g_infantry_count"),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(troop_get_slot,":cur_i_agent", "trp_ladder_infantry_array", ":i_agent"),
				(try_begin),
					(agent_is_alive, ":cur_i_agent"),
					(val_add, ":alive_count", 1),
					(try_begin),
						(troop_slot_eq, "trp_ladder_infantry_state_array", ":i_agent", 1),
						(store_mul, ":cur_in_index", ":l_index", 9),
						(val_add, ":cur_in_index", 4),
						(troop_get_slot,":old_pos_x", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_y", "trp_ladder_array", ":cur_in_index"),
						(init_position, pos3),
						(position_set_x, pos3, ":old_pos_x"),
						(position_set_y, pos3, ":old_pos_y"),
						(agent_get_position, pos4, ":cur_i_agent"),
						(get_distance_between_positions, ":dist", pos3, pos4),
						(val_sub, ":cur_in_index", 4),
						(troop_get_slot,":ladder_pos_x", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":ladder_pos_y", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":ladder_pos_z", "trp_ladder_array", ":cur_in_index"),
						(store_div, ":koef", ":ladder_pos_z", 8),
						(assign, ":limit", 1104),
						(try_begin),
							(gt, ":koef", 0),
							(val_mul, ":limit", ":koef"),
						(try_end),
						(try_begin),
							(le, ":dist", ":limit"),
							(init_position, pos5),
							(position_set_x, pos5, ":ladder_pos_x"),
							(position_set_y, pos5, ":ladder_pos_y"),
							(position_set_z, pos5, ":ladder_pos_z"),
							(agent_set_scripted_destination, ":cur_i_agent", pos5, 0),
							(troop_set_slot, "trp_ladder_infantry_state_array", ":i_agent", 2),
						(else_try),
							(val_add, ":one_state_count", 1),
						(try_end),
					(try_end),
				(try_end),
				(val_add, ":l_index", 1),
			(try_end),
			(try_begin),
				(eq, ":alive_count", 0),
				(assign, "$g_infantry_is", 0),
			(try_end),
			(try_begin),
				(eq, ":one_state_count", 0),
				(assign, "$g_infantry_is", 2),
			(try_end),
		(try_end),
		
		
		(try_begin),
			(eq, "$g_archers_is", 1),
			(eq, "$g_archers_must_go", 1),
			(assign, ":alive_count", 0),
			(assign, ":one_state_count", 0),
			(assign, ":l_index", 0),
			(try_for_range, ":i_agent", 0, "$g_archers_count"),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(troop_get_slot,":cur_i_agent", "trp_ladder_archers_array", ":i_agent"),
				(try_begin),
					(agent_is_alive, ":cur_i_agent"),
					(val_add, ":alive_count", 1),
					(try_begin),
						(troop_slot_eq, "trp_ladder_archers_state_array", ":i_agent", 1),
						(store_mul, ":cur_in_index", ":l_index", 9),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":ladder_pos_x", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":ladder_pos_y", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":ladder_pos_z", "trp_ladder_array", ":cur_in_index"),
						(init_position, pos5),
						(position_set_x, pos5, ":ladder_pos_x"),
						(position_set_y, pos5, ":ladder_pos_y"),
						(position_set_z, pos5, ":ladder_pos_z"),
						(agent_set_scripted_destination, ":cur_i_agent", pos5, 0),
						(troop_set_slot, "trp_ladder_archers_state_array", ":i_agent", 2),
						(assign, "$g_archers_is", 2),
					(try_end),
				(try_end),
				(val_add, ":l_index", 1),
			(try_end),
			(try_begin),
				(eq, ":alive_count", 0),
				(assign, "$g_archers_is", 0),
			(try_end),
			#(try_begin),
			#	(eq, ":one_state_count", 0),
			#	(assign, "$g_archers_is", 2),
	# (try_end),
		(try_end),
	
		(try_for_agents,":cur_agent"),
			(agent_is_alive, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(neg|agent_is_defender, ":cur_agent"),
			(agent_slot_eq, ":cur_agent", slot_agent_is_old, 2),
			(agent_get_slot, ":l_index", ":cur_agent", slot_agent_ladder),
			(store_mul, ":cur_in_index", ":l_index", 9),
			(val_add, ":cur_in_index", 4),
			(troop_get_slot,":old_pos_x", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":old_pos_y", "trp_ladder_array", ":cur_in_index"),
			(init_position, pos3),
			(position_set_x, pos3, ":old_pos_x"),
			(position_set_y, pos3, ":old_pos_y"),
			(agent_get_position, pos4, ":cur_agent"),
			(get_distance_between_positions, ":dist", pos3, pos4),
			(val_sub, ":cur_in_index", 4),
			(troop_get_slot,":ladder_pos_x", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":ladder_pos_y", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":ladder_pos_z", "trp_ladder_array", ":cur_in_index"),
			(store_div, ":koef", ":ladder_pos_z", 9),
			(assign, ":limit", 1104),
			(try_begin),
				(gt, ":koef", 0),
				(val_mul, ":limit", ":koef"),
			(try_end),
			(try_begin),
				(le, ":dist", ":limit"),
				(init_position, pos5),
				(position_set_x, pos5, ":ladder_pos_x"),
				(position_set_y, pos5, ":ladder_pos_y"),
				(position_set_z, pos5, ":ladder_pos_z"),
				(agent_set_scripted_destination, ":cur_agent", pos5, 0),
				(agent_set_slot, ":cur_agent", slot_agent_is_old, 3),
			(try_end),
		(try_end),
		
	])	
	
common_check_to_last_point = (
  0, 0, 0,
  [
        ], 
	[	
		
		(try_begin),
			(ge, "$g_infantry_is", 1),
			(assign, ":alive_count", 0),
			(assign, ":two_state_count", 0),
			(assign, ":l_index", 0),
			(try_for_range, ":i_agent", 0, "$g_infantry_count"),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(troop_get_slot,":cur_i_agent", "trp_ladder_infantry_array", ":i_agent"),
				(try_begin),
					(agent_is_alive, ":cur_i_agent"),
					(val_add, ":alive_count", 1),
					(try_begin),
						(troop_slot_eq, "trp_ladder_infantry_state_array", ":i_agent", 2),
						(store_mul, ":cur_in_index", ":l_index", 9),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_x", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_y", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_z", "trp_ladder_array", ":cur_in_index"),
						(init_position, pos3),
						(position_set_x, pos3, ":old_pos_x"),
						(position_set_y, pos3, ":old_pos_y"),
						(position_set_z, pos3, ":old_pos_z"),
						(agent_get_position, pos4, ":cur_i_agent"),
						(get_distance_between_positions, ":dist", pos3, pos4),
						(try_begin),
							(le, ":dist", 335),
							(assign, "$g_archers_must_go", 1),
							(val_add, ":cur_in_index", 5),
							(troop_get_slot, ":entry_no", "trp_ladder_array", ":cur_in_index"),
							(init_position, pos5),
							(entry_point_get_position,  pos5, ":entry_no"),
							(agent_set_scripted_destination, ":cur_i_agent", pos5, 0),
							(try_begin), 
								(eq, ":l_index", 1), 
								(scene_prop_get_instance, ":cur_instance_id", "spr_apple_b", 0),
								(prop_instance_set_position, ":cur_instance_id", pos5),
							(end_try), 	
							##(try_begin), 
							##	(eq, ":l_index", 1), 
							##	(scene_prop_get_instance, ":cur_instance_id", "spr_apple_b",1),
							##	(prop_instance_set_position, ":cur_instance_id", pos5),				
							##(end_try), 	
							##(try_begin), 
							##	(eq, ":l_index", 2), 
							##	(scene_prop_get_instance, ":cur_instance_id", "spr_spoon", 1),
							##	(prop_instance_set_position, ":cur_instance_id", pos5),				
							##(end_try), 	
							(troop_set_slot, "trp_ladder_infantry_state_array", ":i_agent", 3),
						(else_try),
							(val_add, ":two_state_count", 1),
						(try_end),
					(try_end),
				(try_end),
				(val_add, ":l_index", 1),
			(try_end),
			(try_begin),
				(eq, ":alive_count", 0),
				(eq, "$g_infantry_is", 2),
				(assign, "$g_infantry_is", 0),
			(try_end),
			(try_begin),
				(eq, ":two_state_count", 0),
				(eq, "$g_infantry_is", 2),
				(assign, "$g_infantry_is", 3),
			(try_end),
		(else_try),
			(assign, "$g_archers_must_go", 1),
		(try_end),
		
		
		(try_begin),
			(ge, "$g_archers_is", 1),
			(assign, ":alive_count", 0),
			(assign, ":two_state_count", 0),
			(assign, ":l_index", 0),
			(try_for_range, ":i_agent", 0, "$g_archers_count"),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(troop_get_slot,":cur_i_agent", "trp_ladder_archers_array", ":i_agent"),
				(try_begin),
					(agent_is_alive, ":cur_i_agent"),
					(val_add, ":alive_count", 1),
					(try_begin),
						(troop_slot_eq, "trp_ladder_archers_state_array", ":i_agent", 2),
						(store_mul, ":cur_in_index", ":l_index", 9),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_x", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_y", "trp_ladder_array", ":cur_in_index"),
						(val_add, ":cur_in_index", 1),
						(troop_get_slot,":old_pos_z", "trp_ladder_array", ":cur_in_index"),
						(init_position, pos3),
						(position_set_x, pos3, ":old_pos_x"),
						(position_set_y, pos3, ":old_pos_y"),
						(position_set_z, pos3, ":old_pos_z"),
						(agent_get_position, pos4, ":cur_i_agent"),
						(get_distance_between_positions, ":dist", pos3, pos4),
						(try_begin),
							(le, ":dist", 337),
							(val_add, ":cur_in_index", 5),
							(troop_get_slot, ":entry_no", "trp_ladder_array", ":cur_in_index"),
							(init_position, pos5),
							(entry_point_get_position,  pos5, ":entry_no"),
							(agent_set_scripted_destination, ":cur_i_agent", pos5, 0),
							(troop_set_slot, "trp_ladder_archers_state_array", ":i_agent", 3),
						(else_try),
							(val_add, ":two_state_count", 1),
						(try_end),
					(try_end),
				(try_end),
				(val_add, ":l_index", 1),
			(try_end),
			(try_begin),
				(eq, ":alive_count", 0),
				(eq, "$g_archers_is", 2),
				(assign, "$g_archers_is", 0),
			(try_end),
			(try_begin),
				(eq, ":two_state_count", 0),
				(eq, "$g_archers_is", 2),
				(assign, "$g_archers_is", 3),
			(try_end),
		(try_end),
		
		
		(try_for_agents,":cur_agent"),
			(agent_is_alive, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(neg|agent_is_defender, ":cur_agent"),
			(agent_slot_eq, ":cur_agent", slot_agent_is_old, 3),
			(agent_get_slot, ":l_index", ":cur_agent", slot_agent_ladder),
			(store_mul, ":cur_in_index", ":l_index", 9),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":old_pos_x", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":old_pos_y", "trp_ladder_array", ":cur_in_index"),
			(val_add, ":cur_in_index", 1),
			(troop_get_slot,":old_pos_z", "trp_ladder_array", ":cur_in_index"),
			(init_position, pos3),
			(position_set_x, pos3, ":old_pos_x"),
			(position_set_y, pos3, ":old_pos_y"),
			(position_set_z, pos3, ":old_pos_z"),
			(agent_get_position, pos4, ":cur_agent"),
			(get_distance_between_positions, ":dist", pos3, pos4),
			(try_begin),
				(le, ":dist", 335),
				(val_add, ":cur_in_index", 5),
				(troop_get_slot, ":entry_no", "trp_ladder_array", ":cur_in_index"),
				(init_position, pos5),
				(entry_point_get_position,  pos5, ":entry_no"),
				(agent_set_scripted_destination, ":cur_agent", pos5, 0),
				(agent_set_slot, ":cur_agent", slot_agent_is_old, 4),
			(try_end),
		(try_end),
			
	])	
	
	
common_check_last_point_to_free = (
  0, 0, 0,
  [
        ], 
	[	
		(try_begin),
			(ge, "$g_infantry_is", 1),
			(assign, ":l_index", 0),
			(try_for_range, ":i_agent", 0, "$g_infantry_count"),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(troop_get_slot,":cur_i_agent", "trp_ladder_infantry_array", ":i_agent"),
				(try_begin),
					(agent_is_alive, ":cur_i_agent"),
					(troop_slot_eq, "trp_ladder_infantry_state_array", ":i_agent", 3),
					(store_mul, ":cur_in_index", ":l_index", 9),
					(val_add, ":cur_in_index", 8),
					(troop_get_slot,":point", "trp_ladder_array", ":cur_in_index"),
					(entry_point_get_position,  pos5, ":point"),
					(agent_get_position, pos4, ":cur_i_agent"),
					(get_distance_between_positions, ":dist", pos5, pos4),
					(try_begin),
						(le, ":dist", 335),
						(troop_set_slot, "trp_ladder_infantry_state_array", ":i_agent", 4),
						(agent_clear_scripted_mode, ":cur_i_agent"),	
					(try_end),
				(try_end),
				(val_add, ":l_index", 1),
			(try_end),
		(try_end),
		
		(try_begin),
			(ge, "$g_archers_is", 1),
			(assign, ":l_index", 0),
			(try_for_range, ":i_agent", 0, "$g_archers_count"),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(troop_get_slot,":cur_i_agent", "trp_ladder_archers_array", ":i_agent"),
				(try_begin),
					(agent_is_alive, ":cur_i_agent"),
					(troop_slot_eq, "trp_ladder_archers_state_array", ":i_agent", 3),
					(store_mul, ":cur_in_index", ":l_index", 9),
					(val_add, ":cur_in_index", 8),
					(troop_get_slot,":point", "trp_ladder_array", ":cur_in_index"),
					(entry_point_get_position,  pos5, ":point"),
					(agent_get_position, pos4, ":cur_i_agent"),
					(get_distance_between_positions, ":dist", pos5, pos4),
					(try_begin),
						(le, ":dist", 337),
						(troop_set_slot, "trp_ladder_archers_state_array", ":i_agent", 4),
						(agent_clear_scripted_mode, ":cur_i_agent"),	
					(try_end),
				(try_end),
				(val_add, ":l_index", 1),
			(try_end),
		(try_end),
		
		(try_for_agents,":cur_agent"),
			(agent_is_alive, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(neg|agent_is_defender, ":cur_agent"),
			(agent_slot_eq, ":cur_agent", slot_agent_is_old, 4),
			(agent_get_slot, ":l_index", ":cur_agent", slot_agent_ladder),
			(store_mul, ":cur_in_index", ":l_index", 9),
			(val_add, ":cur_in_index", 8),
			(troop_get_slot,":point", "trp_ladder_array", ":cur_in_index"),
			(entry_point_get_position,  pos5, ":point"),
			(agent_get_position, pos4, ":cur_agent"),
			(get_distance_between_positions, ":dist", pos5, pos4),
			(try_begin),
				(le, ":dist", 335),
				(agent_clear_scripted_mode, ":cur_agent"),	
				(agent_set_slot, ":cur_agent", slot_agent_is_old, 5),
			(try_end),
		(try_end),
		
	])	
	
common_free_to_order = (
  0, 0, 0, [],
  [
    (try_begin),
		(this_or_next|game_key_clicked, gk_order_1),
		(this_or_next|game_key_clicked, gk_order_2),
		(this_or_next|game_key_clicked, gk_order_3),
		(this_or_next|game_key_clicked, gk_order_4),
		(this_or_next|game_key_clicked, gk_order_5),
		(             game_key_clicked, gk_order_6),
		(get_player_agent_no, ":player_agent"),
		(agent_get_team, ":player_team", ":player_agent"),
		(try_begin),
			(class_is_listening_order, ":player_team", grc_infantry),
			(call_script, "script_clear_scripted", grc_infantry),
		(try_end),
		(try_begin),
			(class_is_listening_order, ":player_team", grc_archers),
			(call_script, "script_clear_scripted", grc_archers),
		(try_end),
	(try_end),
	
	
    
	 
    ])
		
common_check_for_new_agents = (
  0, 0, 0,
  [
        ], 
	[	
			(get_player_agent_no,":player_agent"),
			(assign, ":l_index", 0),
			(try_for_agents,":cur_agent"),
				(neg|eq, ":cur_agent", ":player_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(neg|agent_is_defender, ":cur_agent"),
				(agent_slot_eq, ":cur_agent", slot_agent_is_old, 0),
				(try_begin),
					(eq, ":l_index", "$g_ladder_count"),
					(assign, ":l_index", 0),
				(try_end),
				(agent_set_slot, ":cur_agent", slot_agent_ladder, ":l_index"),
				(store_mul, ":cur_in_index", ":l_index", 9),
				(val_add, ":cur_in_index", 4),
				(troop_get_slot,":new_pos_x", "trp_ladder_array", ":cur_in_index"),
				(val_add, ":cur_in_index", 1),
				(troop_get_slot,":new_pos_y", "trp_ladder_array", ":cur_in_index"),
				(init_position, pos0),
				(position_set_x, pos0, ":new_pos_x"),
				(position_set_y, pos0, ":new_pos_y"),
				(agent_set_scripted_destination, ":cur_agent", pos0, 0),
				(agent_set_slot, ":cur_agent", slot_agent_is_old, 2),
				(val_add, ":l_index", 1),
			(try_end),	
		
	])	
	

#OiM code end  
  
  
mission_templates = [
  (
    "town_default",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),
	 (9,mtef_scene_source,af_override_horse,0,1,[]),
	 (10,mtef_scene_source,af_override_horse,0,1,[]),
	 (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),
	 (13,mtef_scene_source,0,0,1,[]),
	 (14,mtef_scene_source,0,0,1,[]),
	 (15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),
	 (17,mtef_visitor_source,af_override_horse,0,1,[]),
	 (18,mtef_visitor_source,af_override_horse,0,1,[]),
	 (19,mtef_visitor_source,af_override_horse,0,1,[]),
	 (20,mtef_visitor_source,af_override_horse,0,1,[]),
	 (21,mtef_visitor_source,af_override_horse,0,1,[]),
	 (22,mtef_visitor_source,af_override_horse,0,1,[]),
	 (23,mtef_visitor_source,af_override_horse,0,1,[]),
	 (24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),
	 (26,mtef_visitor_source,af_override_horse,0,1,[]),
	 (27,mtef_visitor_source,af_override_horse,0,1,[]),
	 (28,mtef_visitor_source,af_override_horse,0,1,[]),
	 (29,mtef_visitor_source,af_override_horse,0,1,[]),
	 (30,mtef_visitor_source,af_override_horse,0,1,[]),
	 (31,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (try_begin),
            (eq, "$sneaked_into_town", 1),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
          (else_try),
            (eq, "$talk_context", tc_tavern_talk),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
          (else_try),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
          (try_end),
        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),

    ],
  ),

# This template is used in party encounters and such.
# 
  (
    "conversation_encounter",0,-1,
    "Conversation_encounter",
    [( 0,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 1,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ( 2,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 3,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 4,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 5,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 6,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ( 7,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 8,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 9,mtef_visitor_source,af_override_fullhelm,0,1,[]),(10,mtef_visitor_source,af_override_fullhelm,0,1,[]),(11,mtef_visitor_source,af_override_fullhelm,0,1,[]),
    #prisoners now...
     (12,mtef_visitor_source,af_override_fullhelm,0,1,[]),(13,mtef_visitor_source,af_override_fullhelm,0,1,[]),(14,mtef_visitor_source,af_override_fullhelm,0,1,[]),(15,mtef_visitor_source,af_override_fullhelm,0,1,[]),(16,mtef_visitor_source,af_override_fullhelm,0,1,[]),
    #Other party
     (17,mtef_visitor_source,af_override_fullhelm,0,1,[]),(18,mtef_visitor_source,af_override_fullhelm,0,1,[]),(19,mtef_visitor_source,af_override_fullhelm,0,1,[]),(20,mtef_visitor_source,af_override_fullhelm,0,1,[]),(21,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     (22,mtef_visitor_source,af_override_fullhelm,0,1,[]),(23,mtef_visitor_source,af_override_fullhelm,0,1,[]),(24,mtef_visitor_source,af_override_fullhelm,0,1,[]),(25,mtef_visitor_source,af_override_fullhelm,0,1,[]),(26,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     (27,mtef_visitor_source,af_override_fullhelm,0,1,[]),(28,mtef_visitor_source,af_override_fullhelm,0,1,[]),(29,mtef_visitor_source,af_override_fullhelm,0,1,[]),(30,mtef_visitor_source,af_override_fullhelm,0,1,[]),(31,mtef_visitor_source,af_override_fullhelm,0,1,[]),
     ],
    [],
  ),
  
#----------------------------------------------------------------
#mission templates before this point are hardwired into the game.
#-----------------------------------------------------------------

  (
    "town_center",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     
     (8,mtef_scene_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_scene_source,0,0,1,[]),(14,mtef_scene_source,0,0,1,[]),(15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),(47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      (ti_on_agent_spawn, 0, 0, [],
      [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
	  ]),


		 
        
        (1, 0, ti_once, [],
      [
        (try_begin),
          (eq, "$g_mt_mode", tcm_default),
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
        (try_end),
        (call_script, "script_init_town_walker_agents"),
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
             (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (try_end),
      ]),
        (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0,
      [
        (try_begin),
          (eq, "$g_mt_mode", tcm_default),
          (set_trigger_result,1),
        (else_try),
          (eq, "$g_mt_mode", tcm_disguised),
          (display_message,"str_cant_use_inventory_disguised"),
        (else_try),
          (display_message, "str_cant_use_inventory_now"),
        (try_end),
           ], []),
        (ti_tab_pressed, 0, 0,
         [
           (try_begin),
             (this_or_next|eq, "$g_mt_mode", tcm_default),
             (eq, "$g_mt_mode", tcm_disguised),
             (set_trigger_result,1),
           (else_try),
             (display_message, "@Cannot leave now."),
           (try_end),
           ], []),
      (ti_on_leave_area, 0, 0,
      [
        (try_begin),
          (eq, "$g_defending_against_siege", 0),
          (assign,"$g_leave_town",1),
        (try_end),			
            ], []),

        (0, 0, ti_once, [], [(party_slot_eq, "$current_town", slot_party_type, spt_town),
       (call_script, "script_town_init_doors", 0),
       (try_begin),
         (eq, "$town_nighttime", 0),
         (play_sound, "snd_town_ambiance", sf_looping),
       (try_end),
     ]),
        (3, 0, 0, [(call_script, "script_tick_town_walkers")], []),
        (2, 0, 0, [(call_script, "script_center_ambiance_sounds")], []),
	], 
    ),
  

  (
    "village_center",0,-1,
    "village center",
    [(0,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (call_script, "script_init_town_walker_agents"),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(try_begin),
                                (check_quest_active, "qst_hunt_down_fugitive"),
                                (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                                (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                                (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                                (try_begin),
                                  (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                                  (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
                                (else_try),
                                  (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
                                (try_end),
                              (try_end),
                              (set_trigger_result,1)], []),
      (ti_on_leave_area, 0, 0, [
          (try_begin),
            (assign,"$g_leave_town",1),
          (try_end),
          ], []),
      (3, 0, 0, [(call_script, "script_tick_town_walkers")], []),
      (2, 0, 0, [(call_script, "script_center_ambiance_sounds")], []),

      (1, 0, ti_once, [(check_quest_active, "qst_hunt_down_fugitive"),
                       (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                       (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                       (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_current_state, 1),
                       (assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_fugitive"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_village_hunt_down_fugitive_defeated"),
          (call_script, "script_fail_quest", "qst_hunt_down_fugitive"),
          (finish_mission, 4),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$current_town", -2),
          (call_script, "script_succeed_quest", "qst_hunt_down_fugitive"),
        (try_end),
        ]),
    ],
  ),

  (
    "bandits_at_night",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0, af_override_horse, aif_start_alarmed, 1, pilgrim_disguise),
     (1,mtef_visitor_source|mtef_team_1,0,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,0,1,[]),
     (4,mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
     (5,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),     
     (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (10,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	 (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	 (15,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (33,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (34,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (35,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (36,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (37,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (38,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (39,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (48,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (49,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (50,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (51,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (52,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (53,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (54,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (55,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (56,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (57,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (58,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (59,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (60,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (61,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (62,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	 (63,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
         (neq, ":troop_no", "trp_player"),
         #(agent_set_team, ":agent_no", 1),
         ]),

      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),]),

	  (ti_after_mission_start, 0, 0, [], [	  
        (assign, "$num_center_bandits", 3),
		(store_character_level, ":level", "trp_player"),
        (try_for_range, ":unused", 0, 20),
          (try_begin),
            (store_random_in_range, ":random_no", 0, 100),
            (lt, ":random_no", ":level"),
            (val_add, "$num_center_bandits", 1),
          (try_end),
        (try_end),

		(try_begin),
          (neq, "$town_nighttime", 0),
          (check_quest_active,"qst_oim_hunt_down_thieves"),
	      (check_quest_active,"qst_oim_hunt_down_thieves"),
          (eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)
          (eq, "$sneaked_into_town", 0),#Skip if sneaked
	  
	      (neg|check_quest_failed, "qst_oim_hunt_down_thieves"),
	      (neg|check_quest_succeeded, "qst_oim_hunt_down_thieves"),

		  (assign, ":bandit_troop", "trp_bandit"),
		(else_try),
	      (party_get_slot, ":bandit_troop", "$current_town", slot_center_has_bandits),
        (try_end),
	    #(assign, ":bandit_troop", "trp_bandit"),
        (entry_point_get_position, pos0, 2),
	    (assign, reg5, "$num_center_bandits"),
	    #(display_message, "@OZANDEBUG : number of bandits : {reg5}"),
		(try_for_range, ":unused", 0, "$num_center_bandits"),
		  (assign, ":best_entry", -1),
		  (try_for_range, ":unused_2", 0, 100),
		    (eq, ":best_entry", -1),
            (store_random_in_range, ":entry_no", 0, 64),		    
		    (neq, ":entry_no", 0),
		    (neq, ":entry_no", 1),
			(neq, ":entry_no", 2),
			(neg|entry_point_is_auto_generated, ":entry_no"),
		    (entry_point_get_position, pos1, ":entry_no"),
			(position_get_distance_to_terrain, ":height_to_terrain", ":entry_no"),
			(get_distance_between_positions, ":dist", pos0, pos1),
			(assign, reg3, ":entry_no"),
			(assign, reg4, ":dist"),
			(assign, reg5, ":height_to_terrain"),
			#(display_message, "@OZANDEBUG : distance between 2 and {reg3} is {reg4}, distance to terrain : {reg5}"),
			(ge, ":dist", 1500),
			(le, ":dist", 7500),
			(assign, ":best_entry", ":entry_no"),
          (try_end),

		  (ge, ":entry_no", 0),          
          (store_current_scene, ":cur_scene"),
          (modify_visitors_at_site, ":cur_scene"),
          (add_visitors_to_current_scene, ":best_entry", ":bandit_troop", 1),		  
        (try_end),
	  ]),

      common_inventory_not_available,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
      
      (ti_tab_pressed, 0, 0,
       [
         (display_message, "str_cannot_leave_now"),
         ], []),
      (ti_on_leave_area, 0, 0,
       [
         (try_begin),
           (eq, "$g_defending_against_siege", 0),
           (assign,"$g_leave_town",1),
         (try_end),
         ], []),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         (set_party_battle_mode),
         (party_slot_eq, "$current_town", slot_party_type, spt_town),
         (call_script, "script_town_init_doors", 0),
        ]),

      (2, 4, ti_once,
       [
         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le,1)
         ],
       [
         (try_begin),
           (main_hero_fallen),
           (jump_to_menu, "mnu_town_bandits_failed"),
         (else_try),
           (jump_to_menu, "mnu_town_bandits_succeeded"),
         (try_end),
         (finish_mission),
         ]),
      ],
    ),

  
  (
    "village_training", mtf_arena_fight, -1,
    "village_training",
    [(2,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_practice_staff, itm_practice_boots]),
     (4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff, itm_practice_boots]),
     ],
    [
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_train_peasants_against_bandits_training_succeeded", 0),
         (call_script, "script_change_banners_and_chest"),
         ]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (finish_mission),
         ]),
      
      common_inventory_not_available,

      (1, 4, ti_once,
       [
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_train_peasants_against_bandits_training_succeeded", 1),
         (try_end),
         (finish_mission),
         ]),
      ],
    ),
    
  (
    "visit_town_castle",0,-1,
    "You enter the halls of the lord.",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), 
	 (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]), #for doors
     (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (6,mtef_visitor_source,af_override_horse,0,1,[]),
	 (7,mtef_visitor_source,af_override_horse,0,1,[]),
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
	 (9,mtef_visitor_source,af_override_horse,0,1,[]),
	 (10,mtef_scene_source,af_override_horse,0,1,[]),
	 (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_visitor_source,af_override_horse,0,1,[]),
	 (13,mtef_visitor_source,0,0,1,[]),
	 (14,mtef_visitor_source,0,0,1,[]),
	 (15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_castle_lord,0,1,[]),(17,mtef_visitor_source,af_castle_lord,0,1,[]),(18,mtef_visitor_source,af_castle_lord,0,1,[]),(19,mtef_visitor_source,af_castle_lord,0,1,[]),(20,mtef_visitor_source,af_castle_lord,0,1,[]),(21,mtef_visitor_source,af_castle_lord,0,1,[]),(22,mtef_visitor_source,af_castle_lord,0,1,[]),(23,mtef_visitor_source,af_castle_lord,0,1,[]),(24,mtef_visitor_source,af_castle_lord,0,1,[]),
     (25,mtef_visitor_source,af_castle_lord,0,1,[]),(26,mtef_visitor_source,af_castle_lord,0,1,[]),(27,mtef_visitor_source,af_castle_lord,0,1,[]),(28,mtef_visitor_source,af_castle_lord,0,1,[]),(29,mtef_visitor_source,af_castle_lord,0,1,[]),(30,mtef_visitor_source,af_castle_lord,0,1,[]),(31,mtef_visitor_source,af_castle_lord,0,1,[])
     ],
    [
      (ti_on_agent_spawn, 0, 0, [],
      [
        (store_trigger_param_1, ":agent_no"),
        (call_script, "script_init_town_agent", ":agent_no"),
      ]),
      (ti_before_mission_start, 0, 0, [],
      [
        (call_script, "script_change_banners_and_chest"),
      ]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
      (0, 0, ti_once, [], [
        #(set_fog_distance, 150, 0xFF736252)
        (try_begin),
          (eq, "$talk_context", tc_court_talk),
            #(call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", 0), #prison
        (try_end),
        ]),

      
    ],
  ),

  (
    "back_alley_kill_local_merchant",mtf_arena_fight,-1,
    "You enter the back alley",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
         ]),

      (0, 0, ti_once, [
          (store_mission_timer_a,":cur_time"),
          (ge,":cur_time",1), 
          (assign, ":merchant_hp", 0),
          (assign, ":player_hp", 0),
          (assign, ":merchant_hp", 0),
          (assign, ":merchant_agent", -1),
          (assign, ":player_agent", -1),
          (try_for_agents, ":agent_no"),
            (agent_get_troop_id, ":troop_id", ":agent_no"),
            (try_begin),
              (eq, ":troop_id", "trp_local_merchant"),
              (store_agent_hit_points, ":merchant_hp", ":agent_no"),
              (assign, ":merchant_agent", ":agent_no"),
            (else_try),
              (eq, ":troop_id", "trp_player"),
              (store_agent_hit_points, ":player_hp",":agent_no"),
              (assign, ":player_agent", ":agent_no"),
            (try_end),
          (try_end),
          (ge, ":player_agent", 0),
          (ge, ":merchant_agent", 0),
          (agent_is_alive, ":player_agent"),
          (agent_is_alive, ":merchant_agent"),
          (is_between, ":merchant_hp", 1, 30),
          (gt, ":player_hp", 50),
          (start_mission_conversation, "trp_local_merchant"),
          ], []),
      
      (1, 4, ti_once, [(assign, ":not_alive", 0),
                       (try_begin),
                         (call_script, "script_cf_troop_agent_is_alive", "trp_local_merchant"),
                       (else_try),
                         (assign, ":not_alive", 1),
                       (try_end),
                       (this_or_next|main_hero_fallen),
                       (eq, ":not_alive", 1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_kill_local_merchant"),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -4),
             (call_script, "script_succeed_quest", "qst_kill_local_merchant"),
           (try_end),
           (finish_mission),
           ]),

      
    ],
  ),

  (
    "back_alley_revolt",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [(0,mtef_team_0|mtef_use_exact_number,af_override_horse|af_override_weapons|af_override_head,aif_start_alarmed,4,[itm_quarter_staff]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      common_inventory_not_available,

      common_battle_init_banner,

      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_want_to_retreat"),
        ]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (jump_to_menu, "mnu_collect_taxes_failed"),
        (finish_mission),]),

      (ti_tab_pressed, 0, 0, [(display_message,"str_cannot_leave_now")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (jump_to_menu, "mnu_collect_taxes_failed"),
           (else_try),
             (jump_to_menu, "mnu_collect_taxes_rebels_killed"),
           (try_end),
           (finish_mission),
           ]),

      
    ],
  ),

  (
    "lead_charge",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (1,mtef_defenders|mtef_team_0,0,aif_start_alarmed,12,[]),
     (0,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [
      
      
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),

         (assign, ":initial_courage_score", 5000),
                  
         (agent_get_troop_id, ":troop_id", ":agent_no"),
         (store_character_level, ":troop_level", ":troop_id"),
         (val_mul, ":troop_level", 35),
         (val_add, ":initial_courage_score", ":troop_level"), #average : 20 * 35 = 700
         
         (store_random_in_range, ":randomized_addition_courage", 0, 3000), #average : 1500
         (val_add, ":initial_courage_score", ":randomized_addition_courage"), 
                   
         (agent_get_party_id, ":agent_party", ":agent_no"),         
         (party_get_morale, ":cur_morale", ":agent_party"),
         
         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
         (val_mul, ":morale_effect_on_courage", 30), #this can effect morale with -2100..900
         (val_add, ":initial_courage_score", ":morale_effect_on_courage"), 
         
         #average = 5000 + 700 + 1500 = 7200; min : 5700, max : 8700
         #morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
         #min starting : 3600, max starting  : 9600, average starting : 7200
         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"), 
		 (agent_set_slot, ":agent_no", slot_agent_courage_score_fading_out, 0), 
         ]),

      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  #custom_oim_horse_dim_test, 
	  oim_on_horse_dismount,
		 
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
##          (str_store_troop_name, s6, ":dead_agent_troop_id"),
##          (assign, reg0, ":dead_agent_no"),
##          (assign, reg1, ":killer_agent_no"),
##          (assign, reg2, ":is_wounded"),
##          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),

        (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
       ]),

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20, 1),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

         (party_clear, "p_routed_enemies"),

         (assign, "$g_latest_order_1", 1), 
         (assign, "$g_latest_order_2", 1), 
         (assign, "$g_latest_order_3", 0), 
         (assign, "$g_latest_order_4", 3), 
		 (assign, "$g_latest_order_5", 3), 
         ]),

      
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_place_player_banner_near_inventory"),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           (assign, "$g_defender_reinforcement_limit", 7),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [
                              
      #new (25.11.09) starts (TODO : make a similar code to also helping ally encounters)
      #count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
      (assign, ":total_enemy_soldiers", reg0),
      
      #decrease number of agents already in battle area to find all number of reinforcement enemies
      (assign, ":enemy_soldiers_in_battle_area", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_party_id, ":agent_party", ":cur_agent"),
        (try_begin),
          (neq, ":agent_party", "p_main_party"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":enemy_soldiers_in_battle_area", 1),
        (try_end),
      (try_end),
      (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers", ":enemy_soldiers_in_battle_area"),

      (try_begin),
        (lt, ":total_enemy_reinforcements", 15),
        (ge, "$defender_reinforcement_stage", 2),
        (eq, "$defender_reinforcement_limit_increased", 0),
        (val_add, "$g_defender_reinforcement_limit", 1),                    
        (assign, "$defender_reinforcement_limit_increased", 1),
      (try_end),    
      #new (25.11.09) ends
      
      
      
      
      
      
      (lt,"$defender_reinforcement_stage","$g_defender_reinforcement_limit"),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,7),(assign, "$defender_reinforcement_limit_increased", 0),(val_add,"$defender_reinforcement_stage",1)]),
      
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",7),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,7),(val_add,"$attacker_reinforcement_stage",1)]),

      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)]),

      common_battle_inventory,


      #AI Triggers
      (0, 0, ti_once, [
          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          ],
       [(call_script, "script_select_battle_tactic"),
        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        ]),
      
      (3, 0, 0, [
          (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
              ], []), #calculating and applying effect of people on others courage scores

      (3, 0, 0, [
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),          
            (store_mission_timer_a,":mission_time"),
            (ge,":mission_time",3),          
            (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
          (try_end),          
              ], []), #controlling courage score and if needed deciding to run away for each agent

      (2, 0, 0, [
          (store_mission_timer_a,":mission_time"),

          (ge,":mission_time",3),
          
          (call_script, "script_battle_tactic_apply"),
          ], []), #applying battle tactic

      common_battle_order_panel,
      common_battle_order_panel_tick,

    ],
  ),

  (
    "village_attack_bandits",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           (try_begin),
                             (eq, "$g_mt_mode", vba_after_training),
                             (add_reinforcements_to_entry, 1, 6),
                           (else_try),
                             (add_reinforcements_to_entry, 1, 29),
                           (try_end),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result, -1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission, 0)]),

      common_battle_inventory,      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      
    ],
  ),



  (
    "village_raid",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (1,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [
      
      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20, 1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [(lt,"$defender_reinforcement_stage",7),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,6),(val_add,"$defender_reinforcement_stage",1)]),
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",7),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,6),(val_add,"$attacker_reinforcement_stage",1)]),

      (1, 60, ti_once,
       [
         (store_mission_timer_a,reg(1)),
         (ge,reg(1),10),
         (all_enemies_defeated, 5),
         (neg|main_hero_fallen, 0),
         (set_mission_result,1),
         (display_message,"str_msg_battle_won"),
         (assign,"$g_battle_won",1),
         (assign, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_village_raid_evil", 0),
           (call_script, "script_play_victorious_sound"),
         (else_try),
           (play_track, "track_victorious_evil", 1),
         (try_end),
         ],
       [
         (call_script, "script_count_mission_casualties_from_agents"),
         (finish_mission, 1),
         ]),

      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)]),

      common_battle_inventory,
      common_battle_order_panel,
      common_battle_order_panel_tick,

##      #AI Tiggers
##      (0, 0, ti_once, [
##          (store_mission_timer_a,reg(1)),(ge,reg(1),4),
##          (call_script, "script_select_battle_tactic"),
##          (call_script, "script_battle_tactic_init"),
##          ], []),
##      (1, 0, 0, [
##          (store_mission_timer_a,reg(1)),(ge,reg(1),4),
##          (call_script, "script_battle_tactic_apply"),
##          ], []),
    ],
  ),



##  (
##    "charge_with_allies",mtf_battle_mode,charge_with_ally,
##    "Taking a handful of fighters with you, you set off to patrol the area.",
##    [
##     (1,mtef_defenders,0,0|aif_start_alarmed,8,[]),
##     (0,mtef_defenders,0,0|aif_start_alarmed,0,[]),
##     (4,mtef_attackers,0,aif_start_alarmed,8,[]),
##     (4,mtef_attackers,0,aif_start_alarmed,0,[]),
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$g_battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),
##        (eq,":answer",0),
##        (assign, "$pin_player_fallen", 0),
##        (str_store_string, s5, "str_retreat"),
##        (call_script, "script_simulate_retreat", 10, 30),
##        (finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),(assign,"$defender_reinforcement_stage",0),(assign,"$attacker_reinforcement_stage",0)]),
##      (1, 0, 5, [(lt,"$defender_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_defender_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,0,4),(val_add,"$defender_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_attacker_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,3,4),(val_add,"$attacker_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),(all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$g_battle_won",1)],
##           [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$g_battle_won",1),(display_message,"str_msg_battle_won")]),
##
##      (1, 4, ti_once, [(main_hero_fallen)],
##          [
##              (assign, "$pin_player_fallen", 1),
##              (str_store_string, s5, "str_retreat"),
##              (call_script, "script_simulate_retreat", 20, 30),
##              (assign, "$g_battle_result", -1),
##              (set_mission_result,-1),(finish_mission,0)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),

##  (
##    "charge_with_allies_old",mtf_battle_mode,charge_with_ally,
##    "Taking a handful of fighters with you, you set off to patrol the area.",
##    [(1,mtef_leader_only,0,0,1,[]),
##     (1,mtef_no_leader,0,0|aif_start_alarmed,2,[]),
##     (1,mtef_reverse_order|mtef_ally_party,0,0|aif_start_alarmed,3,[]),
##     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
##     (0,mtef_reverse_order|mtef_ally_party,0,0|aif_start_alarmed,0,[]),
##     (3,mtef_reverse_order|mtef_enemy_party,0,aif_start_alarmed,6,[]),
##     (4,mtef_reverse_order|mtef_enemy_party,0,aif_start_alarmed,0,[])],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$g_battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),(eq,":answer",0),(finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),(assign,"$enemy_reinforcement_stage",0),(assign,"$friend_reinforcement_stage",0),(assign,"$ally_reinforcement_stage",0)]),
##      
##      (1, 0, 5, [(lt,"$enemy_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_enemy_count,reg(2)),(lt,reg(2),3)],
##       [(add_reinforcements_to_entry,6,3),(val_add,"$enemy_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$friend_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_friend_count,reg(2)),(lt,reg(2),2)],
##       [(add_reinforcements_to_entry,3,1),(val_add,"$friend_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$ally_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_ally_count,reg(2)),  (lt,reg(2),2)],
##       [(add_reinforcements_to_entry,4,2),(val_add,"$ally_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),
##                        (all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$g_battle_won",1),
##                        ],
##       [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$g_battle_won",1),(display_message,"str_msg_battle_won")]),
##      (1, 4, ti_once, [(main_hero_fallen,0)],
##       [(set_mission_result,-1),(finish_mission,1)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),
##  (
##    "lead_charge_old",mtf_battle_mode,charge,
##    "You lead your men to battle.",
##    [
##     (1,mtef_leader_only,0,0,1,[]),
##     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
##     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
##     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
##     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
##     ],
##    [
##      (ti_tab_pressed, 0, 0, [],
##       [
##           (try_begin),
##             (eq, "$g_battle_won", 1),
##             (finish_mission,0),
##           (else_try),
##             (call_script, "script_cf_check_enemies_nearby"),
##             (question_box,"str_do_you_want_to_retreat"),
##           (else_try),
##             (display_message,"str_can_not_retreat"),
##           (try_end),
##        ]),
##      (ti_question_answered, 0, 0, [],
##       [(store_trigger_param_1,":answer"),(eq,":answer",0),(finish_mission,0),]),
##
##      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),(assign,"$enemy_reinforcement_stage",0),(assign,"$friend_reinforcement_stage",0)]),
##      (1, 0, 5, [(lt,"$enemy_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_enemy_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,4,3),(val_add,"$enemy_reinforcement_stage",1)]),
##      (1, 0, 5, [(lt,"$friend_reinforcement_stage",2),(store_mission_timer_a,reg(1)),(ge,reg(1),10),(store_friend_count,reg(2)),(lt,reg(2),3)],
##           [(add_reinforcements_to_entry,2,3),(val_add,"$friend_reinforcement_stage",1)]),
##      (1, 60, ti_once, [(store_mission_timer_a,reg(1)),
##                        (ge,reg(1),10),(all_enemies_defeated,2),
##                        (neg|main_hero_fallen,0),
##                        (set_mission_result,1),
##                        (assign, "$g_battle_result", 1),
##                        (display_message,"str_msg_battle_won"),
##                        (assign,"$g_battle_won",1)],
##           [(finish_mission,1)]),
##      (10, 0, 0, [], [(eq,"$g_battle_won",1),(display_message,"str_msg_battle_won")]),
##      (1, 4, ti_once, [(main_hero_fallen)],
##          [
##              (assign, "$g_battle_result", -1),
##              (set_mission_result,-1),(finish_mission,1)]),
##      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_use_baggage_for_inventory")], []),
##    ],
##  ),



  (
    "besiege_inner_battle_castle",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (17, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (18, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (19, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (20, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,


      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),
        
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ]),
      
      #AI Tiggers
      (0, 0, ti_once, [
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (assign, "$defender_team_2", 2),
          (assign, "$attacker_team_2", 3),
          ], []),

      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 5, 20, 0),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)
              ]),
      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,
    ],
  ),

  (
    "besiege_inner_battle_town_center",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_use_exact_number|mtef_team_1,af_override_horse,aif_start_alarmed,4,[]),
     (2, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (23, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (24, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (25, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (26, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (27, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (28, mtef_defenders|mtef_use_exact_number|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,


      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (assign, "$g_battle_result", -1),
        (set_mission_result,-1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),
        ]),
        
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
                           ]),
      
      #AI Tiggers
      (0, 0, ti_once, [
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (assign, "$defender_team_2", 2),
          (assign, "$attacker_team_2", 3),
          ], []),

      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 5, 20, 0),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)
              ]),

      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,
    ],
  ),

  (
    "castle_attack_walls_defenders_sally",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (3,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     ],
    [
      
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),
         ]),
      
      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_change_banners_and_chest"),
         (call_script, "script_remove_siege_objects"),
         ]),

      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,


      (ti_on_agent_killed_or_wounded, 0, 0, [], #new
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
       ]),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 5, 20, 0),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),
        
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),
      
      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 60, ti_once, [(store_mission_timer_a, reg(1)),
                        (ge, reg(1), 10),
                        (all_enemies_defeated, 2),
                        (neg|main_hero_fallen,0),
                        (set_mission_result,1),
                        (display_message,"str_msg_battle_won"),
                        (assign, "$g_battle_won", 1),
                        (assign, "$g_battle_result", 1),
                        (assign, "$g_siege_sallied_out_once", 1),
                        (assign, "$g_siege_method", 1), #reset siege timer
                        (call_script, "script_play_victorious_sound"),
                        ],
           [(call_script, "script_count_mission_casualties_from_agents"),
            (finish_mission,1)]),

      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 5, 20, 0),
              (assign, "$g_battle_result", -1),
              (set_mission_result, -1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)]),

      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_battle_inventory,
    ],
  ),


  (
    "castle_attack_walls_belfry",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (47,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,

      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,

      (0, 0, ti_once,
       [
         (set_show_messages, 0),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (team_give_order, "$attacker_team", grc_everyone, mordr_spread_out),
         (set_show_messages, 1),
         ], []),
      
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
       ]),

      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,
    ],
  ),

  (
    "castle_attack_walls_ladder",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
       ]),
    ],
  ),
  

   (
    "castle_visit",0,-1,
    "Castle visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (10,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (11,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (12,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (13,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (14,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (15,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (16,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (17,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (18,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (19,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (20,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (21,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (22,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (23,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (24,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (25,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (26,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (27,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (28,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (29,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (30,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (31,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (32,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (33,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (34,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (35,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (36,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (37,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (38,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
	 (39,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     # Party members
     (40,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (41,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (42,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (43,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (44,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (45,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     (46,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
     ],
    [
      
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_init_town_agent", ":agent_no"),
         ]),
      (ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
                                           (call_script, "script_remove_siege_objects"),
                                           ]),

      (0, 0, ti_once, [],
       [
#         (call_script, "script_music_set_situation_with_culture", mtf_sit_lords_hall),
         ]),

#      (ti_before_mission_start, 0, 0, [],
#          [(scene_prop_disable,"spr_ramp_12m"),(scene_prop_disable,"spr_portcullis")]),
    ],
  ),


  (
    "training_ground_trainer_talk", 0, -1,
    "Training.",
    [
      (0,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (1,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (2,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (3,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (4,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (5,mtef_scene_source|mtef_team_0,af_override_horse|af_override_weapons,0,1,[]),
      (6,mtef_scene_source|mtef_team_0,0,0,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
         ]),
      (ti_inventory_key_pressed, 0, 0,
       [
         (set_trigger_result,1),
         ], []),
      (ti_tab_pressed, 0, 0,
       [
         (set_trigger_result,1),
         ], []),
     (0.0, 1.0, 2.0,
      [(lt, "$trainer_help_message", 2),
        ],
      [(try_begin),
         (eq, "$trainer_help_message", 0),
#         (tutorial_box, "str_trainer_help_1", "@Tutorial"),
       (else_try),
#         (tutorial_box, "str_trainer_help_2", "@Tutorial"),
       (try_end),
       (val_add, "$trainer_help_message", 1),
          ]),
      
    ],
  ),

  (
    "training_ground_trainer_training",mtf_arena_fight,-1,
    "You will fight a match in the arena.",
    [
      (16, mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_practice_shield,itm_practice_sword,itm_practice_boots]),
      (17, mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff,itm_practice_boots]),
      (18, mtef_visitor_source|mtef_team_2,af_override_everything,aif_start_alarmed,1,[itm_practice_staff,itm_practice_boots]),
      (19, mtef_visitor_source|mtef_team_3,af_override_everything,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_boots]),
      (20, mtef_visitor_source,0,0,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1, ":answer"),
         (eq, ":answer", 0),
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (1, 3, ti_once, [(main_hero_fallen,0)],
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (1, 3, ti_once,
       [
         (store_mission_timer_a, reg1),
         (ge, reg1, 1),
         (num_active_teams_le, 1),
         (neg|main_hero_fallen),
         (assign, "$training_fight_won", 1),
         ],
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         ]),
      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
    ],
  ),


  (
    "training_ground_training", mtf_arena_fight, -1,
    "Training.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (1,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (2,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (3,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (8,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (9,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (10,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (11,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (12,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (13,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (14,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (15,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_last_destroyed_gourds", 0),
         (call_script, "script_change_banners_and_chest")]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (assign, "$g_training_ground_training_success_ratio", 0),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),
      
      common_inventory_not_available,

      (0, 0, ti_once,
       [
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (set_fixed_point_multiplier, 100),
           (entry_point_get_position, pos1, 0),
           (init_position, pos2),
           (position_set_y, pos2, "$g_training_ground_ranged_distance"),
           (position_transform_position_to_parent, pos3, pos1, pos2),
           (copy_position, pos1, pos3),
           (assign, ":end_cond", 10),
           (assign, ":shift_value", 0),
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_sub, ":cur_instance", ":cur_i", ":shift_value"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_instance"),
             (copy_position, pos2, pos1),
             (init_position, pos0),
             (store_random_in_range, ":random_no", 0, 360),
             (position_rotate_z, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 50, 600),
             (position_move_x, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 0, 360),
             (position_transform_position_to_local, pos3, pos1, pos2),
             (position_rotate_z, pos0, ":random_no"),
             (position_transform_position_to_parent, pos4, pos0, pos3),
             (position_transform_position_to_parent, pos2, pos1, pos4),
             (position_set_z_to_ground_level, pos2),
             (position_move_z, pos2, 150),
             (assign, ":valid", 1),
             (try_for_range, ":cur_instance_2", 0, 10),
               (eq, ":valid", 1),
               (neq, ":cur_instance", ":cur_instance_2"),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd", ":cur_instance_2"),
               (prop_instance_get_position, pos3, ":target_object_2"),
               (get_distance_between_positions, ":dist", pos2, pos3),
               (lt, ":dist", 100),
               (assign, ":valid", 0),
             (try_end),
             (try_begin),
               (eq, ":valid", 0),
               (val_add, ":end_cond", 1),
               (val_add, ":shift_value", 1),
             (else_try),
               (prop_instance_set_position, ":target_object", pos2),
               (prop_instance_animate_to_position, ":target_object", pos2, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_instance"),
               (position_move_z, pos2, -150), #moving back to ground level
               (prop_instance_set_position, ":target_object_2", pos2),
               (prop_instance_animate_to_position, ":target_object_2", pos2, 1),
             (try_end),
           (try_end),
         (else_try),
           (eq, "$g_mt_mode", ctm_mounted),
           (assign, ":num_gourds", 0),
           #First, placing gourds on the spikes
           (try_for_range, ":cur_i", 0, 100),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_i"),
             (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_i"),
             (ge, ":target_object", 0),
             (ge, ":target_object_2", 0),
             (val_add, ":num_gourds", 1),
             (prop_instance_get_position, pos0, ":target_object_2"),
             (position_move_z, pos0, 150),
             (prop_instance_set_position, ":target_object", pos0),
             (prop_instance_animate_to_position, ":target_object", pos0, 1),
           (try_end),
           (store_sub, ":end_cond", ":num_gourds", "$g_training_ground_training_num_gourds_to_destroy"),
           #Second, removing gourds and their spikes randomly
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_random_in_range, ":random_instance", 0, ":num_gourds"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":random_instance"),
             (prop_instance_get_position, pos0, ":target_object"),
             (position_get_z, ":pos_z", pos0),
             (try_begin),
               (lt, ":pos_z", -50000),
#               (val_add, ":end_cond", 1), #removed already, try again
             (else_try),
               (position_set_z, pos0, -100000),
               (prop_instance_set_position, ":target_object", pos0),
               (prop_instance_animate_to_position, ":target_object", pos0, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":random_instance"),
               (prop_instance_set_position, ":target_object_2", pos0),
               (prop_instance_animate_to_position, ":target_object_2", pos0, 1),
             (try_end),
           (try_end),
         (try_end),
         ],
       []),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_melee),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_training_ground_training_success_ratio", 100),
         (else_try),
           (assign, ":alive_enemies", 0),
           (try_for_agents, ":agent_no"),
             (agent_is_alive, ":agent_no"),
             (agent_is_human, ":agent_no"),
             (agent_get_team, ":team_no", ":agent_no"),
             (eq, ":team_no", 1),
             (val_add, ":alive_enemies", 1),
           (try_end),
           (store_sub, ":dead_enemies", "$g_training_ground_training_num_enemies", ":alive_enemies"),
           (store_mul, "$g_training_ground_training_success_ratio", ":dead_enemies", 100),
           (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_enemies"),
         (try_end),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_ranged),
         (get_player_agent_no, ":player_agent"),
         (agent_get_ammo, ":ammo", ":player_agent"),
         (store_mission_timer_a, ":cur_seconds"),
         (this_or_next|main_hero_fallen),
         (this_or_next|eq, ":ammo", 0),
         (gt, ":cur_seconds", 116), 
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 10),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_mounted),
         (get_player_agent_no, ":player_agent"),
         (agent_get_horse, ":player_horse", ":player_agent"),
         (store_mission_timer_a, ":cur_seconds"),
         (this_or_next|lt, ":player_horse", 0),
         (this_or_next|main_hero_fallen),
         (this_or_next|ge, "$scene_num_total_gourds_destroyed", "$g_training_ground_training_num_gourds_to_destroy"),
         (gt, ":cur_seconds", 120),
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 100),
         (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_gourds_to_destroy"),
         (jump_to_menu, "mnu_training_ground_training_result"),
         (finish_mission),
         ]),

      (0, 0, 0,
       [
         (gt, "$g_last_destroyed_gourds", 0),
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (entry_point_get_position, pos1, 0),
           (position_move_y, pos1, 100, 0),
           (get_player_agent_no, ":player_agent"),
           (agent_get_position, pos2, ":player_agent"),
           (try_begin),
             (position_is_behind_position, pos2, pos1),
             (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
           (else_try),
             (display_message, "@You must stay behind the line on the ground! Point is not counted."),
           (try_end),
         (else_try),
           (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
         (try_end),
         (assign, "$g_last_destroyed_gourds", 0),
         ],
       []),
    ],
  ),

  (
    "sneak_caught_fight",mtf_arena_fight,-1,
    "You must fight your way out!",
    [
     (0,mtef_scene_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (5,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (6,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (7,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (10,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (15,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (33,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (34,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (35,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (36,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (37,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (38,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (39,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (40,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (48,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (49,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (50,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (51,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (52,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (53,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (54,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (55,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (56,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (57,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (58,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (59,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (60,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (61,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (62,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (63,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (64,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     
     # (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
     # (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     # (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [], 
      [
        (call_script, "script_change_banners_and_chest"),
      ]),

	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
      
      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),
       
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),(eq,":answer",0),(jump_to_menu,"mnu_captivity_start_castle_defeat"),(finish_mission,0),]),
      
      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
         
      (0, 3, 0,
       [
          (main_hero_fallen,0),
        ],
       [
         (jump_to_menu,"mnu_captivity_start_castle_defeat"),
         (finish_mission,0),
       ]),
       
      (1, 0, 0, [], 
       [
	    (get_player_agent_no, ":player_agent"),
	    (agent_get_position, pos0, ":player_agent"),
	    	    
        (try_for_agents, ":agent_no"),
          (neq, ":agent_no", ":player_agent"),
          (agent_is_alive, ":agent_no"),
          (agent_get_team, ":agent_team", ":agent_no"),
          (eq, ":agent_team", 1),
          
          (agent_get_position, pos1, ":agent_no"),
        
          (get_distance_between_positions, ":dist", pos0, pos1),
         
          (try_begin),
            (le, ":dist", 800),
            (agent_clear_scripted_mode, ":agent_no"),
          (else_try),  
            (agent_set_scripted_destination, ":agent_no", pos0, 0),
          (try_end),
        (try_end),                  	      
       ]), 

	   (5, 1, ti_once, 
	   [
	     (num_active_teams_le,1),
	     (neg|main_hero_fallen),

         (store_mission_timer_a,":cur_time"),
         (ge, ":cur_time", 5),
	   ],
       [
         (assign,"$auto_menu",-1),
         (jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),
         (finish_mission,1),
       ]),
       
	   (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
      
    ],
  ),

   (
    "ai_training",0,-1,
    "You start training.",
    [
#     (0,0,af_override_horse,aif_start_alarmed,1,[]),
     (0,0,0,aif_start_alarmed,30,[]),
#     (1,mtef_no_leader,0,0|aif_start_alarmed,5,[]),
#     (0,mtef_no_leader,0,0|aif_start_alarmed,0,[]),
#     (3,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,6,[]),
#     (4,mtef_enemy_party|mtef_reverse_order,0,aif_start_alarmed,0,[]),
     ],
    [
      
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),

      common_battle_order_panel,
      common_battle_order_panel_tick,
    ],
  ),
   (
    "camera_test",0,-1,
    "camera Test.",
    [
#     (0,mtef_attackers,0,aif_start_alarmed,5,[]),
     ],
    [
      
      (1, 0, 0, [(mission_cam_set_mode,1),
          (entry_point_get_position, pos3, 3),
          (mission_cam_set_position, pos3)], []),
#      (ti_before_mission_start, 0, 0, [], [(set_rain, 1,100)]),
      (ti_tab_pressed, 0, 0, [],
       [(finish_mission,0)]),
    ],
  ),

  (
    "arena_melee_fight",mtf_arena_fight,-1,
    "You enter a melee fight in the arena.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_red, itm_red_tourney_helmet]),
      (1,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword, itm_arena_tunic_red]),
      (2,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_red, itm_red_tourney_helmet]),
      (3,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_red, itm_red_tourney_helmet]),
      (4,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows, itm_practice_dagger, itm_arena_tunic_red]),
      (5,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_red]),
      (6,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_red]),
      (7,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_red, itm_red_tourney_helmet]),

      (8,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_dagger, itm_arena_tunic_blue]),
      (9,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_blue,itm_blue_tourney_helmet]),
      (10,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_arena_tunic_blue]),
      (11,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_blue, itm_blue_tourney_helmet]),
      (12,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_blue]),
      (13,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_blue,itm_blue_tourney_helmet]),
      (14,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_arena_tunic_blue]),
      (15,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_blue]),

      (16,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_green, itm_green_tourney_helmet]),
      (17,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_arena_tunic_green, itm_green_tourney_helmet]),
      (18,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_green, itm_green_tourney_helmet]),
      (19,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_green, itm_green_tourney_helmet]),
      (20,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_dagger, itm_arena_tunic_green, itm_green_tourney_helmet]),
      (21,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_green]),
      (22,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_green]),
      (23,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_green, itm_green_tourney_helmet]),

      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (25,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (26,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (27,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (28,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_dagger, itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (29,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_yellow]),
      (30,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_yellow]),
      (31,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
#32
      (32, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword]),
      (33,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
      (34,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword, itm_practice_shield]),
      (35,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
      (36, mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows, itm_practice_dagger]),
      (37,mtef_visitor_source|mtef_team_2,af_override_all,aif_start_alarmed,1,[itm_practice_sword, itm_practice_shield]),
      (38,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword]),
      (39,mtef_visitor_source|mtef_team_4,af_override_all,aif_start_alarmed,1,[itm_practice_staff]),
#40-49 not used yet
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_dagger, itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_sword,itm_practice_shield,itm_arena_tunic_yellow]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_heavy_practice_sword,itm_practice_horse,itm_arena_tunic_yellow]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_lance,itm_practice_shield,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),
      (24,mtef_visitor_source|mtef_team_3,af_override_all,aif_start_alarmed,1,[itm_practice_bow,itm_practice_arrows,itm_practice_horse,itm_arena_tunic_yellow, itm_gold_tourney_helmet]),

      (50, mtef_scene_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (51, mtef_visitor_source,af_override_horse|af_override_weapons|af_override_head,0,1,[]),
      (52, mtef_scene_source,af_override_horse,0,1,[]),
#not used yet:
      (53, mtef_scene_source,af_override_horse,0,1,[]),(54, mtef_scene_source,af_override_horse,0,1,[]),(55, mtef_scene_source,af_override_horse,0,1,[]),
#used for torunament master scene

      (56, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_padded_cloth, itm_segmented_helmet]),
      (57, mtef_visitor_source|mtef_team_0, af_override_all, aif_start_alarmed, 1, [itm_practice_sword, itm_practice_shield, itm_padded_cloth, itm_segmented_helmet]),
    ],
    []
  ),

  (
    "arena_challenge_fight",mtf_arena_fight|mtf_commit_casualties,-1,
    "You enter a melee fight in the arena.",
    [
      (56, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 1, []),
      (58, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 1, []),
    ],
    [
      
      common_inventory_not_available,
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
             (call_script, "script_fail_quest", "qst_duel_for_lady"),
           (else_try),
             (call_script, "script_succeed_quest", "qst_duel_for_lady"),
		   (try_end),
           (finish_mission),
           ]),
    ],
  ),

  (
    "tutorial_training_ground",mtf_arena_fight,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "tutorial_1",0,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "tutorial_2",mtf_arena_fight,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "tutorial_3",mtf_arena_fight,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "tutorial_3_2",mtf_arena_fight,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "tutorial_4",mtf_arena_fight,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "tutorial_5",mtf_arena_fight,-1,
    "You enter the training ground.",
    [], [],
  ),

  (
    "quick_battle_battle",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,

      (ti_before_mission_start, 0, 0, [],
       [
         (scene_set_day_time, 15),
         ]),

      common_battle_init_banner,
      
      (0, 0, ti_once, [],
        [
          (assign, "$g_battle_result", 0),
          (call_script, "script_combat_music_set_situation_with_culture"),
         ]),

      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
    ],
  ),

  (
    "quick_battle_siege", mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_init_banner,

      (0, 0, ti_once,
       [
         (assign, "$defender_team", 0),
         (assign, "$attacker_team", 1),
         (assign, "$defender_team_2", 2),
         (assign, "$attacker_team_2", 3),
         ], []),

      (ti_before_mission_start, 0, 0, [],
       [
         (scene_set_day_time, 15),
         ]),

      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,
      common_custom_siege_init,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,
      common_siege_ai_trigger_init_2,
	  custom_oim_replace_items_begin,
      ],
    ),

    (
    "multiplayer_dm",mtf_battle_mode,-1, #deathmatch mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      #multiplayer_server_check_belfry_movement,      
     
      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         ]),
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (multiplayer_make_everyone_enemy),

         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"), # close this line and open map in deathmatch mod and use all ladders firstly 
         ]),                                                            # to be able to edit maps without damaging any headquarters flags ext. 

      (ti_after_mission_start, 0, 0, [], 
       [
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),

         (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
           (call_script, "script_multiplayer_event_mission_end"),

           (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
           (start_presentation, "prsnt_multiplayer_stats_chart_deathmatch"),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"), 
         (store_trigger_param_2, ":killer_agent_no"), 
         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
         ]),
      
      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),

           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),

           (player_get_agent_id, ":player_agent", ":player_no"),
           (assign, ":spawn_new", 0),
           (try_begin),
             (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
             (eq, ":player_first_spawn", 1),
             (assign, ":spawn_new", 1),
             (player_set_slot, ":player_no", slot_player_first_spawn, 0),
           (else_try),
             (try_begin),
               (lt, ":player_agent", 0),
               (assign, ":spawn_new", 1),
             (else_try),
               (neg|agent_is_alive, ":player_agent"),
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
               (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
               (assign, ":spawn_new", 1),
             (try_end),             
           (try_end),
           (eq, ":spawn_new", 1),
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (troop_get_inventory_slot, ":has_item", ":player_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),
         
           (call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":is_horseman"), 
           (player_spawn_new_agent, ":player_no", reg0),
         (try_end),
         ]),

      (1, 0, 0, [ (multiplayer_is_server),
                  (this_or_next|gt,"$g_multiplayer_num_bots_team_1",0),
                  (gt,"$g_multiplayer_num_bots_team_2",0), # are there any bots?
                ], #do this in every new frame, but not at the same time
       [
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), 
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),

      (0, 0, 0, [],
       [
         (multiplayer_is_server),
         (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
         (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"),
         (try_begin),
           (gt, ":total_req", 0),
           (store_random_in_range, ":random_req", 0, ":total_req"),
           (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),
           (try_begin),
             (lt, ":random_req", 0),
             #add to team 1
             (assign, ":selected_team", 0),
             (val_sub, "$g_multiplayer_num_bots_required_team_1", 1),
           (else_try),
             #add to team 2
             (assign, ":selected_team", 1),
             (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
           (try_end),

           (team_get_faction, ":team_faction_no", ":selected_team"),
           (assign, ":available_troops_in_faction", 0),

           (try_for_range, ":troop_no", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
             (store_troop_faction, ":troop_faction", ":troop_no"),
             (eq, ":troop_faction", ":team_faction_no"),
             (val_add, ":available_troops_in_faction", 1),
           (try_end),

           (store_random_in_range, ":random_troop_index", 0, ":available_troops_in_faction"),
           (assign, ":end_cond", multiplayer_ai_troops_end),
           (try_for_range, ":troop_no", multiplayer_ai_troops_begin, ":end_cond"),
             (store_troop_faction, ":troop_faction", ":troop_no"),
             (eq, ":troop_faction", ":team_faction_no"),
             (val_sub, ":random_troop_index", 1),
             (lt, ":random_troop_index", 0),
             (assign, ":end_cond", 0),
             (assign, ":selected_troop", ":troop_no"),
           (try_end),
         
           (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),

           (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"), 
           (store_current_scene, ":cur_scene"),
           (modify_visitors_at_site, ":cur_scene"),
           (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", -1),
           (assign, "$g_multiplayer_ready_for_spawning_agent", 0),
         (try_end),
         ]),

      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         #checking for restarting the map
         (assign, ":end_map", 0),
         (try_begin),
           (store_mission_timer_a, ":mission_timer"),
           (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
           (gt, ":mission_timer", ":game_max_seconds"),
           (assign, ":end_map", 1),
         (try_end),
         (try_begin),
           (eq, ":end_map", 1),
           (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
           (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 0),
           (call_script, "script_game_set_multiplayer_mission_end"),
         (try_end),
         ]),
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart_deathmatch"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,
      
      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart_deathmatch"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),

    (
    "multiplayer_tdm",mtf_battle_mode,-1, #team_deathmatch mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         ]),
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
		 
		 # clear squad info
		 (call_script, "script_mp_clear_squad_info", ":player_no"),
      ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),

         (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"), 
         (store_trigger_param_2, ":killer_agent_no"), 
         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
         #adding 1 score points to killer agent's team. (special for "headquarters" and "team deathmatch" mod)
         (try_begin), 
           (ge, ":killer_agent_no", 0),
           (agent_is_human, ":dead_agent_no"),
           (agent_is_human, ":killer_agent_no"),
           (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
           (le, ":killer_agent_team", 1), #0 or 1 is ok
           (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
           (neq, ":killer_agent_team", ":dead_agent_team"),
           (team_get_score, ":team_score", ":killer_agent_team"),
           (val_add, ":team_score", 1),
           (team_set_score, ":killer_agent_team", ":team_score"),
         (try_end),
         ]),
	
      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),

           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),

           (player_get_agent_id, ":player_agent", ":player_no"),
           (assign, ":spawn_new", 0),
           (try_begin),
             (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
             (eq, ":player_first_spawn", 1),
             (assign, ":spawn_new", 1),
             (player_set_slot, ":player_no", slot_player_first_spawn, 0),
           (else_try),
             (try_begin),
               (lt, ":player_agent", 0),
               (assign, ":spawn_new", 1),
             (else_try),
               (neg|agent_is_alive, ":player_agent"),
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
               (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
               (assign, ":spawn_new", 1),
             (try_end),             
           (try_end),
           (eq, ":spawn_new", 1),
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (troop_get_inventory_slot, ":has_item", ":player_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),

           (call_script, "script_multiplayer_find_spawn_point", ":player_team", 1, ":is_horseman"), 
           (player_spawn_new_agent, ":player_no", reg0),
         (try_end),
         ]),

      (1, 0, 0, [ (multiplayer_is_server),
                  (this_or_next|gt,"$g_multiplayer_num_bots_team_1",0),
                  (gt,"$g_multiplayer_num_bots_team_2",0), # are there any bots?
                ], #do this in every new frame, but not at the same time
       [
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), 
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),
      
      multiplayer_server_spawn_bots,
      multiplayer_server_manage_bots,

      (20, 0, 0, [],
       [
         (multiplayer_is_server),
         #auto team balance control in every 20 seconds (tdm)
         (call_script, "script_check_team_balance"),
         ]),

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,
      multiplayer_battle_window_opened,

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),
  
  (
    "multiplayer_hq", mtf_battle_mode,-1, #headquarters mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         ]),
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (store_mul, ":initial_hq_score", "$g_multiplayer_game_max_points", 10000),
         
         (assign, "$g_score_team_1", ":initial_hq_score"),
         (assign, "$g_score_team_2", ":initial_hq_score"),

         (try_for_range, ":cur_flag_slot", multi_data_flag_owner_begin, multi_data_flag_owner_end),
           (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", -1),
         (try_end),
           
         (try_begin),
           (multiplayer_is_server),
           (try_for_range, ":cur_flag_slot", multi_data_flag_pull_code_begin, multi_data_flag_pull_code_end),
             (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", -1),
           (try_end),
         (try_end),

         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),

         (try_begin),
           (multiplayer_is_server),
           (team_set_score, 0, "$g_multiplayer_game_max_points"),
           (team_set_score, 1, "$g_multiplayer_game_max_points"),
         (try_end),
         ]),

      (ti_after_mission_start, 0, 0, [],
       [
         (call_script, "script_determine_team_flags", 0),
         (call_script, "script_determine_team_flags", 1),
         (set_spawn_effector_scene_prop_kind, 0, "$team_1_flag_scene_prop"), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to $team_1_flag_scene_prop
         (set_spawn_effector_scene_prop_kind, 1, "$team_2_flag_scene_prop"), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to $team_2_flag_scene_prop
         
         (try_begin),
           (multiplayer_is_server),

           (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         
           (assign, "$g_number_of_flags", 0),
         
           #place base flags
           (entry_point_get_position, pos1, multi_base_point_team_1),
           (entry_point_get_position, pos3, multi_base_point_team_1),

           (set_spawn_position, pos3),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),
           (set_spawn_position, pos3),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
           (set_spawn_position, pos3),
           (spawn_scene_prop, "$team_2_flag_scene_prop", 0),
           (set_spawn_position, pos3),
           (spawn_scene_prop, "spr_headquarters_flag_gray_code_only", 0),
         
           (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, "$g_number_of_flags"),
           (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 1),
           (val_add, "$g_number_of_flags", 1),

           (entry_point_get_position, pos2, multi_base_point_team_2),
           (entry_point_get_position, pos3, multi_base_point_team_2),
         
           (set_spawn_position, pos3),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),
           (set_spawn_position, pos3),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
           (set_spawn_position, pos3),
           (spawn_scene_prop, "$team_2_flag_scene_prop", 0),
           (set_spawn_position, pos3),
           (spawn_scene_prop, "spr_headquarters_flag_gray_code_only", 0),
           (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, "$g_number_of_flags"),
           (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 2),
           (val_add, "$g_number_of_flags", 1),

           (scene_prop_get_num_instances, ":num_instances_of_red_headquarters_flag", "spr_headquarters_flag_red"),
           (scene_prop_get_num_instances, ":num_instances_of_blue_headquarters_flag", "spr_headquarters_flag_blue"),
           (scene_prop_get_num_instances, ":num_instances_of_gray_headquarters_flag", "spr_headquarters_flag_gray"),

           (store_add, ":end_cond", "spr_headquarters_flag_gray", 1),
           (try_for_range, ":headquarters_flag_no", "spr_headquarters_flag_red", ":end_cond"),
             (try_begin),
               (eq, ":headquarters_flag_no", "spr_headquarters_flag_red"),
               (assign, ":num_instances_of_headquarters_flag", ":num_instances_of_red_headquarters_flag"),
             (else_try),
               (eq, ":headquarters_flag_no", "spr_headquarters_flag_blue"),
               (assign, ":num_instances_of_headquarters_flag", ":num_instances_of_blue_headquarters_flag"),
             (else_try),
               (eq, ":headquarters_flag_no", "spr_headquarters_flag_gray"),
               (assign, ":num_instances_of_headquarters_flag", ":num_instances_of_gray_headquarters_flag"),
             (try_end),
             (gt, ":num_instances_of_headquarters_flag", 0),
             (try_for_range, ":instance_no", 0, ":num_instances_of_headquarters_flag"),
               (scene_prop_get_instance, ":flag_id", ":headquarters_flag_no", ":instance_no"),
               (prop_instance_get_position, pos0, ":flag_id"),
        
               (set_spawn_position, pos0),
               (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),
         
               #place other flags
               (try_for_range, ":headquarters_flag_no_will_be_added", "spr_headquarters_flag_red", ":end_cond"),
                 (set_spawn_position, pos0),             
                 (try_begin),
                   (eq, ":headquarters_flag_no_will_be_added", "spr_headquarters_flag_red"),
                   (spawn_scene_prop, "$team_1_flag_scene_prop"),
                 (else_try),
                   (eq, ":headquarters_flag_no_will_be_added", "spr_headquarters_flag_blue"),
                   (spawn_scene_prop, "$team_2_flag_scene_prop"),
                 (else_try),
                   (eq, ":headquarters_flag_no_will_be_added", "spr_headquarters_flag_gray"),
                   (spawn_scene_prop, "spr_headquarters_flag_gray_code_only"),
                 (try_end),        
               (try_end),

               #assign who owns this flag values
               (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, "$g_number_of_flags"),
               (try_begin),
                 (eq, ":headquarters_flag_no", "spr_headquarters_flag_red"),
                 (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 1),
               (else_try),
                 (eq, ":headquarters_flag_no", "spr_headquarters_flag_blue"),
                 (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 2),
               (else_try),
                 (eq, ":headquarters_flag_no", "spr_headquarters_flag_gray"),
                 (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 0),
               (try_end),
               (val_add, "$g_number_of_flags", 1),         
             (try_end),
           (try_end),

           (assign, "$g_number_of_initial_team_1_flags", 0),
           (assign, "$g_number_of_initial_team_2_flags", 0),

           (try_for_range, ":place_no", 0, "$g_number_of_flags"),
             (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":place_no"),
             (troop_get_slot, ":current_owner", "trp_multiplayer_data", ":cur_flag_slot"),
         
             (try_begin),
               (eq, ":place_no", 0),
               (entry_point_get_position, pos0, multi_base_point_team_1),
               (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":place_no"),
               (assign, "$g_base_flag_team_1", ":flag_id"),
             (else_try),
               (eq, ":place_no", 1),
               (entry_point_get_position, pos0, multi_base_point_team_2),
               (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":place_no"),
               (assign, "$g_base_flag_team_2", ":flag_id"),
             (else_try),
               (assign, ":flag_start_red", 2),
               (scene_prop_get_num_instances, ":num_initial_red_flags", "spr_headquarters_flag_red"),
               (store_add, ":flag_start_blue", ":flag_start_red", ":num_initial_red_flags"),
               (scene_prop_get_num_instances, ":num_initial_blue_flags", "spr_headquarters_flag_blue"),
               (store_add, ":flag_start_gray", ":flag_start_blue", ":num_initial_blue_flags"),
               (scene_prop_get_num_instances, ":num_initial_gray_flags", "spr_headquarters_flag_gray"),         
               (try_begin),
                 (ge, ":place_no", ":flag_start_red"),
                 (gt, ":num_initial_red_flags", 0),         
                 (store_sub, ":flag_no", ":place_no", ":flag_start_red"),
                 (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_red", ":flag_no"),
               (else_try),
                 (ge, ":place_no", ":flag_start_blue"),
                 (gt, ":num_initial_blue_flags", 0),         
                 (store_sub, ":flag_no", ":place_no", ":flag_start_blue"),
                 (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_blue", ":flag_no"),
               (else_try),
                 (ge, ":place_no", ":flag_start_gray"),
                 (gt, ":num_initial_gray_flags", 0),         
                 (store_sub, ":flag_no", ":place_no", ":flag_start_gray"),
                 (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray", ":flag_no"),
               (try_end),             
               (prop_instance_get_position, pos0, ":flag_id"),
             (try_end),

             (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":place_no"),
             (prop_instance_set_position, ":pole_id", pos0),
         
             (position_move_z, pos0, multi_headquarters_pole_height),           
             (try_begin),
               (eq, ":current_owner", 0),
               (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 0),
               (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 0),
               (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 1),
             (else_try),
               (eq, ":current_owner", 1),
               (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 1),
               (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 0),
               (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 0),
               (val_add, "$g_number_of_initial_team_1_flags", 1),
             (else_try),
               (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 0),
               (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 1),
               (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":place_no"),
               (prop_instance_set_position, ":flag_id", pos0),
               (scene_prop_set_visibility, ":flag_id", 0),
               (val_add, "$g_number_of_initial_team_2_flags", 1),
             (try_end),
           (try_end),
         (else_try),
           #these three lines both used in calculation of $g_number_of_flags and below part removing of initially placed flags
           (scene_prop_get_num_instances, ":num_instances_of_red_headquarters_flag", "spr_headquarters_flag_red"),
           (scene_prop_get_num_instances, ":num_instances_of_blue_headquarters_flag", "spr_headquarters_flag_blue"),
           (scene_prop_get_num_instances, ":num_instances_of_gray_headquarters_flag", "spr_headquarters_flag_gray"),

           (assign, "$g_number_of_flags", 2),
           (val_add, "$g_number_of_flags", ":num_instances_of_red_headquarters_flag"),
           (val_add, "$g_number_of_flags", ":num_instances_of_blue_headquarters_flag"),
           (val_add, "$g_number_of_flags", ":num_instances_of_gray_headquarters_flag"),         
         (try_end),

         #remove initially placed flags
         (try_for_range, ":flag_no", 0, ":num_instances_of_red_headquarters_flag"),
           (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_red", ":flag_no"),
           (scene_prop_set_visibility, ":flag_id", 0),
         (try_end),
         (try_for_range, ":flag_no", 0, ":num_instances_of_blue_headquarters_flag"),
           (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_blue", ":flag_no"),
           (scene_prop_set_visibility, ":flag_id", 0),
         (try_end),
         (try_for_range, ":flag_no", 0, ":num_instances_of_gray_headquarters_flag"),
           (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray", ":flag_no"),
           (scene_prop_set_visibility, ":flag_id", 0),
         (try_end),

         (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
           (store_add, ":cur_flag_owned_seconds_counts_slot", multi_data_flag_owned_seconds_begin, ":flag_no"),
           (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owned_seconds_counts_slot", 0),
         (try_end),

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
       ]),         

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),

         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"), 
         (store_trigger_param_2, ":killer_agent_no"), 
         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),

         #adding 1 score points to killer agent's team. (special for "headquarters" and "team deathmatch" mod)
         (try_begin), 
           (gt, ":dead_agent_no", -1),
           (gt, ":killer_agent_no", -1),
           (agent_is_active,":dead_agent_no"),
           (agent_is_active,":killer_agent_no"),
           (agent_is_human, ":dead_agent_no"),
           (agent_is_human, ":killer_agent_no"),
           (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
           (lt, ":killer_agent_team", multi_team_spectator), #0 or 1 is ok
           (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
           (lt, ":dead_agent_team", multi_team_spectator), #0 or 1 is ok
           
           (team_get_score, ":team_score", ":dead_agent_team"),
           (val_sub, ":team_score", 1),
           (call_script, "script_team_set_score", ":dead_agent_team", ":team_score"),
           
           # The rest only for the server
           (multiplayer_is_server),

           (try_begin),
             (eq, ":dead_agent_team", 0),
             (val_sub, "$g_score_team_1", 10000), 
           (else_try),
             (val_sub, "$g_score_team_2", 10000), 
           (try_end),
         (try_end),
         ]),

      (1, 0, 0, [],
      [
        (multiplayer_is_server),
        #trigger for (a) counting seconds of flags being owned by their owners & (b) to calculate seconds past after that flag's pull message has shown          
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          #part a: counting seconds of flags being owned by their owners
          (store_add, ":cur_flag_owned_seconds_counts_slot", multi_data_flag_owned_seconds_begin, ":flag_no"),
          (troop_get_slot, ":cur_flag_owned_seconds", "trp_multiplayer_data", ":cur_flag_owned_seconds_counts_slot"),
          (val_add, ":cur_flag_owned_seconds", 1),
          (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owned_seconds_counts_slot", ":cur_flag_owned_seconds"),
          #part b: to calculate seconds past after that flag's pull message has shown
          (store_add, ":cur_flag_pull_code_slot", multi_data_flag_pull_code_begin, ":flag_no"),
          (troop_get_slot, ":cur_flag_pull_code", "trp_multiplayer_data", ":cur_flag_pull_code_slot"),
          (store_mod, ":cur_flag_pull_message_seconds_past", ":cur_flag_pull_code", 100),
          (try_begin),
            (ge, ":cur_flag_pull_code", 100),
            (lt, ":cur_flag_pull_message_seconds_past", 25),
            (val_add, ":cur_flag_pull_code", 1),
            (troop_set_slot, "trp_multiplayer_data", ":cur_flag_pull_code_slot", ":cur_flag_pull_code"),
          (try_end),
        (try_end),        
      ]),               
       
      # Put this to once per second to increase server performance dramatically.
      (1, 0, 0, [],
      [
        (multiplayer_is_server),
        #main trigger which controls which agent is moving/near which flag.
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
          (troop_get_slot, ":current_owner_code", "trp_multiplayer_data", ":cur_flag_owner_counts_slot"),
          (store_div, ":old_team_1_agent_count", ":current_owner_code", 100),
          (store_mod, ":old_team_2_agent_count", ":current_owner_code", 100),
        
          (assign, ":number_of_agents_around_flag_team_1", 0),
          (assign, ":number_of_agents_around_flag_team_2", 0),

          (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"), 
          (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.

          (get_max_players, ":num_players"),
            (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":cur_agent", ":player_no"),
            (ge, ":cur_agent", 0),
            (agent_is_alive, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (agent_get_position, pos1, ":cur_agent"), #pos1 holds agent's position.
            (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
            (get_sq_distance_between_position_heights, ":squared_height_dist", pos0, pos1),
            (val_add, ":squared_dist", ":squared_height_dist"),
            (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
            (try_begin),
              (eq, ":cur_agent_team", 0),
              (val_add, ":number_of_agents_around_flag_team_1", 1),
            (else_try),
              (eq, ":cur_agent_team", 1),
              (val_add, ":number_of_agents_around_flag_team_2", 1),
            (try_end),
          (try_end),

          (try_begin),
            (this_or_next|neq, ":old_team_1_agent_count", ":number_of_agents_around_flag_team_1"),
            (neq, ":old_team_2_agent_count", ":number_of_agents_around_flag_team_2"),

            (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
            (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),

            (store_add, ":cur_flag_pull_code_slot", multi_data_flag_pull_code_begin, ":flag_no"),
            (troop_get_slot, ":cur_flag_pull_code", "trp_multiplayer_data", ":cur_flag_pull_code_slot"),
            (store_mod, ":cur_flag_pull_message_seconds_past", ":cur_flag_pull_code", 100),
            (store_div, ":cur_flag_puller_team_last", ":cur_flag_pull_code", 100),

            (try_begin),        
              (assign, ":continue", 0),
              (try_begin),
                (neq, ":cur_flag_owner", 1),
                (eq, ":old_team_1_agent_count", 0),
                (gt, ":number_of_agents_around_flag_team_1", 0),
                (eq, ":number_of_agents_around_flag_team_2", 0),
                (assign, ":puller_team", 1),
                (assign, ":continue", 1),
              (else_try),
                (neq, ":cur_flag_owner", 2),
                (eq, ":old_team_2_agent_count", 0),
                (eq, ":number_of_agents_around_flag_team_1", 0),
                (gt, ":number_of_agents_around_flag_team_2", 0),
                (assign, ":puller_team", 2),
                (assign, ":continue", 1),
              (try_end),
 
              (eq, ":continue", 1),

              (store_mul, ":puller_team_multiplied_by_100", ":puller_team", 100),
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_pull_code_slot", ":puller_team_multiplied_by_100"),

              (this_or_next|neq, ":cur_flag_puller_team_last", ":puller_team"),
              (ge, ":cur_flag_pull_message_seconds_past", 25),

              (store_mul, ":flag_code", ":puller_team", 100),
              (val_add, ":flag_code", ":flag_no"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_show_multiplayer_message", multiplayer_message_type_flag_is_pulling, ":flag_code"), 
              #for only server itself-----------------------------------------------------------------------------------------------     
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_flag_is_pulling, ":flag_code"),
              (try_end),
            (try_end),

            (try_begin),
              (store_mul, ":current_owner_code", ":number_of_agents_around_flag_team_1", 100),
              (val_add, ":current_owner_code", ":number_of_agents_around_flag_team_2"),        
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owner_counts_slot", ":current_owner_code"),

              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_set_num_agents_around_flag", ":flag_no", ":current_owner_code"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (get_max_players, ":num_players"),
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_num_agents_around_flag, ":flag_no", ":current_owner_code"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),

        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (assign, ":new_flag_owner", -1),

          (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"), 
          (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.            

          (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
          (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),

          (try_begin),
            (try_begin),
              (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
              (scene_prop_get_visibility, ":flag_visibility", ":flag_id"),
              (assign, ":cur_shown_flag", 1),
              (eq, ":flag_visibility", 0),
              (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
              (scene_prop_get_visibility, ":flag_visibility", ":flag_id"),
              (assign, ":cur_shown_flag", 2),
              (eq, ":flag_visibility", 0),                    
              (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
              (scene_prop_get_visibility, ":flag_visibility", ":flag_id"),        
              (assign, ":cur_shown_flag", 0),
            (try_end),

            #flag_id holds shown flag after this point
            (prop_instance_get_position, pos1, ":flag_id"), #pos1 holds gray/red/blue (current shown) flag position.

            (try_begin),
              (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),        
              (lt, ":squared_dist", multi_headquarters_distance_sq_to_change_flag), #if distance is less than 2 meters

              (store_add, ":cur_flag_players_around_slot", multi_data_flag_players_around_begin, ":flag_no"),
              (troop_get_slot, ":cur_flag_players_around", "trp_multiplayer_data", ":cur_flag_players_around_slot"),
              (store_div, ":number_of_agents_around_flag_team_1", ":cur_flag_players_around", 100),
              (store_mod, ":number_of_agents_around_flag_team_2", ":cur_flag_players_around", 100),

              (try_begin),
                (gt, ":number_of_agents_around_flag_team_1", 0),
                (eq, ":number_of_agents_around_flag_team_2", 0),
                (assign, ":new_flag_owner", 0),
                (assign, ":new_shown_flag", 1),
              (else_try),
                (eq, ":number_of_agents_around_flag_team_1", 0),
                (gt, ":number_of_agents_around_flag_team_2", 0),
                (assign, ":new_flag_owner", 0),
                (assign, ":new_shown_flag", 2),
              (else_try),
                (eq, ":number_of_agents_around_flag_team_1", 0),
                (eq, ":number_of_agents_around_flag_team_2", 0),
                (neq, ":cur_shown_flag", 0),
                (assign, ":new_flag_owner", 0),
                (assign, ":new_shown_flag", 0),
              (try_end),
            (else_try),
              (neq, ":cur_flag_owner", ":cur_shown_flag"),      
              (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),        
              (ge, ":squared_dist", multi_headquarters_distance_sq_to_set_flag), #if distance is more equal than 9 meters

              (store_add, ":cur_flag_players_around_slot", multi_data_flag_players_around_begin, ":flag_no"),
              (troop_get_slot, ":cur_flag_players_around", "trp_multiplayer_data", ":cur_flag_players_around_slot"),
              (store_div, ":number_of_agents_around_flag_team_1", ":cur_flag_players_around", 100),
              (store_mod, ":number_of_agents_around_flag_team_2", ":cur_flag_players_around", 100),

              (try_begin),
                (eq, ":cur_shown_flag", 1),
                (assign, ":new_flag_owner", 1),
                (assign, ":new_shown_flag", 1),
              (else_try),
                (eq, ":cur_shown_flag", 2),
                (assign, ":new_flag_owner", 2),
                (assign, ":new_shown_flag", 2),
              (try_end),        
            (try_end),
          (try_end),
        
          (try_begin),
            (ge, ":new_flag_owner", 0),
            (this_or_next|neq, ":new_flag_owner", ":cur_flag_owner"),
            (neq, ":cur_shown_flag", ":new_shown_flag"),

            (try_begin),
              (neq, ":cur_flag_owner", 0),
              (eq, ":new_flag_owner", 0),
              (try_begin),
                (eq, ":cur_flag_owner", 1),
                (assign, ":neutralizer_team", 2),
              (else_try),
                (eq, ":cur_flag_owner", 2),
                (assign, ":neutralizer_team", 1),
              (try_end),
              (store_mul, ":flag_code", ":neutralizer_team", 100),
              (val_add, ":flag_code", ":flag_no"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_show_multiplayer_message", multiplayer_message_type_flag_neutralized, ":flag_code"), 
              #for only server itself-----------------------------------------------------------------------------------------------     
              (get_max_players, ":num_players"),        
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_flag_neutralized, ":flag_code"),
              (try_end),              
            (try_end),
        
            (try_begin),
              (neq, ":cur_flag_owner", ":new_flag_owner"),
              (neq, ":new_flag_owner", 0),
              (store_mul, ":flag_code", ":new_flag_owner", 100),
              (val_add, ":flag_code", ":flag_no"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_show_multiplayer_message", multiplayer_message_type_flag_captured, ":flag_code"), 
              #for only server itself-----------------------------------------------------------------------------------------------     
              (get_max_players, ":num_players"),        
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_flag_captured, ":flag_code"),
              (try_end),              
            (try_end),

            #for only server itself-----------------------------------------------------------------------------------------------
            (call_script, "script_set_num_agents_around_flag", ":flag_no", ":cur_flag_players_around"),
            #for only server itself-----------------------------------------------------------------------------------------------
            (assign, ":number_of_total_players", 0),
            (get_max_players, ":num_players"),        
            (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
              (player_is_active, ":player_no"),
              (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_num_agents_around_flag, ":flag_no", ":cur_flag_players_around"),
              (val_add, ":number_of_total_players", 1),
            (try_end),

            (store_mul, ":owner_code", ":new_flag_owner", 100),
            (val_add, ":owner_code", ":new_shown_flag"),
            #for only server itself-----------------------------------------------------------------------------------------------
            (call_script, "script_change_flag_owner", ":flag_no", ":owner_code"),
            #for only server itself-----------------------------------------------------------------------------------------------
            (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
              (player_is_active, ":player_no"),
              (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_change_flag_owner, ":flag_no", ":owner_code"),          
            (try_end),

            (try_begin),
              (neq, ":new_flag_owner", 0),

              (try_begin),
                (eq, ":new_flag_owner", 1),
                (assign, ":number_of_players_around_flag", ":number_of_agents_around_flag_team_1"),
              (else_try),
                (assign, ":number_of_players_around_flag", ":number_of_agents_around_flag_team_2"),
              (try_end),

              (store_add, ":cur_flag_owned_seconds_counts_slot", multi_data_flag_owned_seconds_begin, ":flag_no"),
              (troop_get_slot, ":current_flag_owned_seconds", "trp_multiplayer_data", ":cur_flag_owned_seconds_counts_slot"),              
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owned_seconds_counts_slot", 0),

              (val_min, ":current_flag_owned_seconds", 360), #360 seconds is max time for hq, this will limit money awarding by (180 x total_number_of_players)

              (scene_prop_get_instance, ":flag_of_team_1", "$team_1_flag_scene_prop", ":flag_no"),
              (scene_prop_get_instance, ":flag_of_team_2", "$team_2_flag_scene_prop", ":flag_no"),

              (try_begin),
                (this_or_next|eq, "$g_base_flag_team_1", ":flag_of_team_1"),
                (eq, "$g_base_flag_team_2", ":flag_of_team_2"),
                (assign, ":flag_value", 2),
              (else_try),
                (assign, ":flag_value", 1),
              (try_end),

              (try_begin),                                #score awarding in flag capturing is changed in hq. If only one player captured flag he get 3 points,
                (le, ":number_of_players_around_flag", 1),   #if 2 player captured they get 2 points, if <=6 players get flag all get 1 points. There is no importance of flag value at scoring.
                (assign, ":score_award_per_player", 3),
              (else_try),
                (eq, ":number_of_players_around_flag", 2),
                (assign, ":score_award_per_player", 2),
              (else_try),
                (le, ":number_of_players_around_flag", 6),
                (assign, ":score_award_per_player", 1),
              (else_try),
                (assign, ":score_award_per_player", 0),
              (try_end),
              
              (store_mul, ":total_money_award", ":current_flag_owned_seconds", ":number_of_total_players"), #total money will be shared after a flag capturing is (0.50 * seconds * number_of_players)         
              (val_mul, ":total_money_award", ":flag_value"),                                               #example: if 15 players is playing and 120 seconds past before flag captured, award is 900 golds.
              (val_div, ":total_money_award", 2),

              (try_begin),
                (gt, ":number_of_players_around_flag", 0), #if there are still any living agents around flag.
                (store_div, ":money_award_per_player", ":total_money_award", ":number_of_players_around_flag"),
              (try_end),
        
              (get_max_players, ":num_players"),
                (try_for_range, ":player_no", 0, ":num_players"),
                (player_is_active, ":player_no"),
                (player_get_agent_id, ":cur_agent", ":player_no"),
                (ge, ":cur_agent", 0),
                (agent_get_team, ":cur_agent_team", ":cur_agent"),
                (val_add, ":cur_agent_team", 1),
                (eq, ":cur_agent_team", ":new_flag_owner"),
                (agent_get_position, pos1, ":cur_agent"), 
                (prop_instance_get_position, pos0, ":pole_id"), 
                (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
                (get_sq_distance_between_position_heights, ":squared_height_dist", pos0, pos1),
                (val_add, ":squared_dist", ":squared_height_dist"),
                (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),                
                (player_get_score, ":player_score", ":player_no"), #give score to player which helped flag to be owned by new_flag_owner team 
                (val_add, ":player_score", ":score_award_per_player"),
                (player_set_score, ":player_no", ":player_score"),                
                (player_get_gold, ":player_gold", ":player_no"), #give money to player which helped flag to be owned by new_flag_owner team 
                (val_add, ":player_gold", ":money_award_per_player"),
                (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),              
              (try_end),
            (try_end),
          (try_end),
        (try_end),
        ]),

      (1, 0, 0, [],
       [
         (multiplayer_is_server),
        #trigger for increasing score in each second.
        (assign, ":number_of_team_1_flags", 0),
        (assign, ":number_of_team_2_flags", 0),

        (assign, ":owned_flag_value", 0),        
        (assign, ":not_owned_flag_value", 0),
        
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
          (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),

          (scene_prop_get_instance, ":flag_of_team_1", "$team_1_flag_scene_prop", ":flag_no"),
          (scene_prop_get_instance, ":flag_of_team_2", "$team_2_flag_scene_prop", ":flag_no"),
        
          (try_begin),
            (this_or_next|eq, "$g_base_flag_team_1", ":flag_of_team_1"),
            (eq, "$g_base_flag_team_2", ":flag_of_team_2"),
            (assign, ":flag_value", 2),
          (else_try),
            (assign, ":flag_value", 1),
          (try_end),
        
          (try_begin),
            (eq, ":cur_flag_owner", 1),
            (val_add, ":number_of_team_1_flags", ":flag_value"),
            (val_add, ":owned_flag_value", ":flag_value"),
          (else_try),
            (eq, ":cur_flag_owner", 2),
            (val_add, ":number_of_team_2_flags", ":flag_value"),
            (val_add, ":owned_flag_value", ":flag_value"),
          (else_try),
            (val_add, ":not_owned_flag_value", ":flag_value"),
          (try_end),
        (try_end),
        
        (store_add, ":all_flag_value", ":owned_flag_value", ":not_owned_flag_value"),
        (store_sub, ":cur_flag_difference", ":number_of_team_1_flags", ":number_of_team_2_flags"),
        (store_mul, ":cur_flag_difference_mul_2", ":cur_flag_difference", 2),
        (store_sub, ":initial_flag_difference", "$g_number_of_initial_team_1_flags", "$g_number_of_initial_team_2_flags"),

        (assign, ":number_of_active_players", 0),
        (get_max_players, ":end_cond"),
        (try_for_range, ":player_no", 0, ":end_cond"),
          (player_is_active, ":player_no"),
          (val_add, ":number_of_active_players", 1),
          (assign, ":end_cond", 0),
        (try_end),

        (try_begin),
          (ge, ":cur_flag_difference_mul_2", ":initial_flag_difference"),
          (store_sub, ":difference", ":cur_flag_difference_mul_2", ":initial_flag_difference"),
          (store_mul, ":score_addition_winner", ":difference", 125),
          (val_add, ":score_addition_winner", 500),
          (store_div, ":score_addition_loser", 250000, ":score_addition_winner"),
          
          (try_begin), #if number of owned flag values < all flag values give only a percentage of score to teams
            (lt, ":owned_flag_value", ":all_flag_value"),
            (val_mul, ":score_addition_loser", ":owned_flag_value"),
            (val_div, ":score_addition_loser", ":all_flag_value"),
            (val_mul, ":score_addition_winner", ":owned_flag_value"),
            (val_div, ":score_addition_winner", ":all_flag_value"),
          (try_end),

          (call_script, "script_find_number_of_agents_constant"),        
          (val_mul, ":score_addition_winner", reg0),
          (val_div, ":score_addition_winner", 100),
          (val_mul, ":score_addition_loser", reg0),
          (val_div, ":score_addition_loser", 100),
          
          (val_mul, ":score_addition_winner", "$g_multiplayer_point_gained_from_flags"),
          (val_div, ":score_addition_winner", 100),
          (val_mul, ":score_addition_loser", "$g_multiplayer_point_gained_from_flags"),
          (val_div, ":score_addition_loser", 100),

          (try_begin),
            (ge, ":number_of_active_players", 1),
            (val_sub, "$g_score_team_2", ":score_addition_winner"),
            (try_begin),
              (ge, ":number_of_team_2_flags", 1),
              (val_sub, "$g_score_team_1", ":score_addition_loser"),
            (else_try),
              (val_sub, "$g_score_team_2", ":score_addition_loser"),
            (try_end),
          (try_end),
        (else_try),
          (store_sub, ":difference", ":initial_flag_difference", ":cur_flag_difference_mul_2"),
          (store_mul, ":score_addition_winner", ":difference", 125),
          (val_add, ":score_addition_winner", 500),
          (store_div, ":score_addition_loser", 250000, ":score_addition_winner"),
          
          (try_begin), #if number of owned flag values < all flag values give only a percentage of score to teams
            (lt, ":owned_flag_value", ":all_flag_value"),
            (val_mul, ":score_addition_loser", ":owned_flag_value"),
            (val_div, ":score_addition_loser", ":all_flag_value"),
            (val_mul, ":score_addition_winner", ":owned_flag_value"),
            (val_div, ":score_addition_winner", ":all_flag_value"),
          (try_end),

          (call_script, "script_find_number_of_agents_constant"),
          (val_mul, ":score_addition_winner", reg0),
          (val_div, ":score_addition_winner", 100),
          (val_mul, ":score_addition_loser", reg0),
          (val_div, ":score_addition_loser", 100),
        
          (val_mul, ":score_addition_winner", "$g_multiplayer_point_gained_from_flags"),
          (val_div, ":score_addition_winner", 100),
          (val_mul, ":score_addition_loser", "$g_multiplayer_point_gained_from_flags"),
          (val_div, ":score_addition_loser", 100),

          (try_begin),
            (ge, ":number_of_active_players", 1),
            (try_begin),
              (ge, ":number_of_team_1_flags", 1),
              (val_sub, "$g_score_team_2", ":score_addition_loser"),
            (else_try),
              (val_sub, "$g_score_team_1", ":score_addition_loser"),
            (try_end),
            (val_sub, "$g_score_team_1", ":score_addition_winner"),
          (try_end),
        (try_end),

        (team_get_score, ":team_score_1", 0),
        (try_begin),
          (store_div, ":team_new_score_1", "$g_score_team_1", 10000),
          (neq, ":team_new_score_1", ":team_score_1"),
          (get_max_players, ":num_players"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_team_set_score", 0, ":team_new_score_1"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 0, ":team_new_score_1"),
          (try_end),
        (try_end),

        (team_get_score, ":team_score_2", 1),
        (try_begin),
          (store_div, ":team_new_score_2", "$g_score_team_2", 10000),
          (neq, ":team_new_score_2", ":team_score_2"),
          (get_max_players, ":num_players"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_team_set_score", 1, ":team_new_score_2"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 1, ":team_new_score_2"),
          (try_end),
        (try_end),
      ]),

      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),

           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),

           (player_get_agent_id, ":player_agent", ":player_no"),
           (assign, ":spawn_new", 0),
           (try_begin),
             (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
             (eq, ":player_first_spawn", 1),
             (assign, ":spawn_new", 1),
             (player_set_slot, ":player_no", slot_player_first_spawn, 0),
           (else_try),
             (try_begin),
               (lt, ":player_agent", 0),
               (assign, ":spawn_new", 1),
             (else_try),
               (neg|agent_is_alive, ":player_agent"),
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
               (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
               (assign, ":spawn_new", 1),
             (try_end),             
           (try_end),
           (eq, ":spawn_new", 1),
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),
         
           (troop_get_inventory_slot, ":has_item", ":player_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),

           (call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":is_horseman"), 
           (player_spawn_new_agent, ":player_no", reg0),
         (try_end),
         ]),

      (1, 0, 0, [ (multiplayer_is_server),
                  (this_or_next|gt,"$g_multiplayer_num_bots_team_1",0),
                  (gt,"$g_multiplayer_num_bots_team_2",0), # are there any bots?
                ], #do this in every new frame, but not at the same time
       [
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), #new died (< g_multiplayer_respawn_period) so will be counted too
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),

      multiplayer_server_spawn_bots,
      multiplayer_server_manage_bots,

      (20, 0, 0, [],
       [
         (multiplayer_is_server),
         #auto team balance control in every 10 seconds (hq)
         (call_script, "script_check_team_balance"),
         ]),

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,
      multiplayer_battle_window_opened,

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),

    (
    "multiplayer_cf",mtf_battle_mode,-1, #capture_the_flag mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      
      (64,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (65,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         ]),

      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (try_begin),
           (multiplayer_is_server),
           (store_current_scene, ":cur_scene"),
           (this_or_next|eq, ":cur_scene", "scn_random_multi_plain_medium"),
           (this_or_next|eq, ":cur_scene", "scn_random_multi_plain_large"),
           (this_or_next|eq, ":cur_scene", "scn_random_multi_steppe_medium"),
           (eq, ":cur_scene", "scn_random_multi_steppe_large"),
           (entry_point_get_position, pos0, 0),
           (entry_point_set_position, 64, pos0),
           (entry_point_get_position, pos1, 32),
           (entry_point_set_position, 65, pos1),
         (try_end),

         (assign, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (assign, "$flag_1_at_ground_timer", 0),
         (assign, "$flag_2_at_ground_timer", 0),
         
         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [],
       [
         (call_script, "script_determine_team_flags", 0),
         (call_script, "script_determine_team_flags", 1),
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)
       
         (try_begin),
           (multiplayer_is_server),

           (assign, "$g_multiplayer_ready_for_spawning_agent", 1),

           (entry_point_get_position, pos0, multi_base_point_team_1),
           (set_spawn_position, pos0),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
         
           (entry_point_get_position, pos0, multi_base_point_team_2),
           (set_spawn_position, pos0),
           (spawn_scene_prop, "$team_2_flag_scene_prop", 0),
         (try_end),

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
         ]),         

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"), 
         (store_trigger_param_2, ":killer_agent_no"), 

         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),

         (try_begin),                                 #when an agent dies which carrying a flag, assign flag position to current position with
           (agent_is_human, ":dead_agent_no"),        #ground level z and do not change it again according to dead agent's any coordinate/rotation.
           (agent_get_attached_scene_prop, ":attached_scene_prop", ":dead_agent_no"),
           (try_begin),
             (try_begin),
               (multiplayer_is_server),
  
               (ge, ":attached_scene_prop", 0), #moved from above after auto-set position

               (multiplayer_get_my_player, ":my_player_no"),
               (get_max_players, ":num_players"),
               #for only server itself-----------------------------------------------------------------------------------------------
               (call_script, "script_set_attached_scene_prop", ":dead_agent_no", -1),
               (agent_set_horse_speed_factor, ":dead_agent_no", 100),
               #for only server itself-----------------------------------------------------------------------------------------------
               (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                 (player_is_active, ":player_no"),
                 (neq, ":my_player_no", ":player_no"),
                 (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_attached_scene_prop, ":dead_agent_no", -1),
               (try_end),

               (prop_instance_get_position, pos0, ":attached_scene_prop"), #moved from above to here after auto-set position
               (position_set_z_to_ground_level, pos0), #moved from above to here after auto-set position
               (prop_instance_set_position, ":attached_scene_prop", pos0), #moved from above to here after auto-set position

               (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
               (try_begin),
                 (eq, ":dead_agent_team", 0),
                 (assign, ":dead_agent_rival_team", 1),
               (else_try),
                 (assign, ":dead_agent_rival_team", 0),
               (try_end),
               (team_set_slot, ":dead_agent_rival_team", slot_team_flag_situation, 2), #2-flag at ground
               (multiplayer_get_my_player, ":my_player_no"),
               (get_max_players, ":num_players"),
               #for only server itself-----------------------------------------------------------------------------------------------
               (call_script, "script_set_team_flag_situation", ":dead_agent_rival_team", 2),
               #for only server itself-----------------------------------------------------------------------------------------------         
               (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                 (player_is_active, ":player_no"),
                 (neq, ":my_player_no", ":player_no"),
                 (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, ":dead_agent_rival_team", 2), #flag at ground
               (try_end),
             (try_end),
           (try_end),         
         (try_end),
         ]),

      (1, 0, 0, [], #returning flag if it is not touched by anyone in 60 seconds
       [
         (multiplayer_is_server),
         (try_for_range, ":team_no", 0, 2),           
           (try_begin),
             (team_slot_eq, ":team_no", slot_team_flag_situation, 2),

             (assign, ":flag_team_no", -1),
         
             (try_begin),
               (eq, ":team_no", 0),
               (val_add, "$flag_1_at_ground_timer", 1),
               (ge, "$flag_1_at_ground_timer", multi_max_seconds_flag_can_stay_in_ground),
               (assign, ":flag_team_no", 0),
             (else_try),
               (val_add, "$flag_2_at_ground_timer", 1),
               (ge, "$flag_2_at_ground_timer", multi_max_seconds_flag_can_stay_in_ground), 
               (assign, ":flag_team_no", 1),
             (try_end),

             (try_begin),
               (ge, ":flag_team_no", 0),

               (try_begin),
                 (eq, ":flag_team_no", 0),
                 (assign, "$flag_1_at_ground_timer", 0),
               (else_try),
                 (eq, ":flag_team_no", 1),
                 (assign, "$flag_2_at_ground_timer", 0),
               (try_end),
         
               #cur agent returned his own flag to its default position!
               (team_set_slot, ":flag_team_no", slot_team_flag_situation, 0), #0-flag at base

               #return team flag to its starting position.
               #for only server itself-----------------------------------------------------------------------------------------------
               (call_script, "script_set_team_flag_situation", ":flag_team_no", 0),
               #for only server itself-----------------------------------------------------------------------------------------------         
               (multiplayer_get_my_player, ":my_player_no"),
               (get_max_players, ":num_players"),
               (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                 (player_is_active, ":player_no"),
                 (neq, ":my_player_no", ":player_no"),
                 (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, ":flag_team_no", 0),
               (try_end),

               (scene_prop_get_instance, ":flag_red_id", "$team_1_flag_scene_prop", 0),
               (scene_prop_get_instance, ":flag_blue_id", "$team_2_flag_scene_prop", 0),

               (assign, ":team_1_flag_id", ":flag_red_id"),
               (assign, ":team_1_base_entry_id", multi_base_point_team_1),

               (assign, ":team_2_flag_id", ":flag_blue_id"),
               (assign, ":team_2_base_entry_id", multi_base_point_team_2),

               #return team flag to its starting position.
               (try_begin),
                 (eq, ":flag_team_no", 0),
                 (entry_point_get_position, pos5, ":team_1_base_entry_id"), #moved from above to here after auto-set position
                 (prop_instance_set_position, ":team_1_flag_id", pos5), #moved from above to here after auto-set position
               (else_try),
                 (entry_point_get_position, pos5, ":team_2_base_entry_id"), #moved from above to here after auto-set position
                 (prop_instance_set_position, ":team_2_flag_id", pos5), #moved from above to here after auto-set position
               (try_end),

               #(team_get_faction, ":team_faction", ":flag_team_no"),
               #(str_store_faction_name, s1, ":team_faction"),
               #(tutorial_message_set_position, 500, 500),
               #(tutorial_message_set_size, 30, 30),
               #(tutorial_message_set_center_justify, 1),
               #(tutorial_message, "str_s1_returned_flag", 0xFFFFFFFF, 5),

               (store_mul, ":minus_flag_team_no", ":flag_team_no", -1),
               (val_sub, ":minus_flag_team_no", 1),

               #for only server itself
               (call_script, "script_show_multiplayer_message", multiplayer_message_type_flag_returned_home, ":minus_flag_team_no"), 
 
               #no need to send also server here
               (try_for_range, ":player_no", 0, ":num_players"),
                 (player_is_active, ":player_no"),
                 (neq, ":my_player_no", ":player_no"),
                 (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_flag_returned_home, ":minus_flag_team_no"),
               (try_end),
             (try_end),
           (else_try),
             (try_begin),
               (eq, ":team_no", 0),
               (assign, "$flag_1_at_ground_timer", 0),
             (else_try),
               (assign, "$flag_2_at_ground_timer", 0),         
             (try_end),
           (try_end),
         (try_end),           
         ]),
         
      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),

           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),

           (player_get_agent_id, ":player_agent", ":player_no"),
           (assign, ":spawn_new", 0),
           (try_begin),
             (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
             (eq, ":player_first_spawn", 1),
             (assign, ":spawn_new", 1),
             (player_set_slot, ":player_no", slot_player_first_spawn, 0),
           (else_try),
             (try_begin),
               (lt, ":player_agent", 0),
               (assign, ":spawn_new", 1),
             (else_try),
               (neg|agent_is_alive, ":player_agent"),
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
               (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
               (assign, ":spawn_new", 1),
             (try_end),             
           (try_end),
           (eq, ":spawn_new", 1),
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (troop_get_inventory_slot, ":has_item", ":player_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),

           (call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":is_horseman"), 
           (player_spawn_new_agent, ":player_no", reg0),
         (try_end),
         ]),

      (1, 0, 0, [ (multiplayer_is_server),
                  (this_or_next|gt,"$g_multiplayer_num_bots_team_1",0),
                  (gt,"$g_multiplayer_num_bots_team_2",0), # are there any bots?
                ], #do this in every new frame, but not at the same time
       [
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), #new died (< g_multiplayer_respawn_period) so will be counted too
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),

      multiplayer_server_spawn_bots,
      multiplayer_server_manage_bots,
      
      (1, 0, 0, [], #control any agent captured flag or made score.
       [
         (multiplayer_is_server),
         (scene_prop_get_instance, ":flag_red_id", "$team_1_flag_scene_prop", 0),
         (prop_instance_get_position, pos1, ":flag_red_id"), #hold position of flag of team 1 (red flag) at pos1

         (scene_prop_get_instance, ":flag_blue_id", "$team_2_flag_scene_prop", 0),
         (prop_instance_get_position, pos2, ":flag_blue_id"), #hold position of flag of team 2 (blue flag) at pos2

         (multiplayer_get_my_player, ":my_player_no"),
         (get_max_players, ":num_players"),                               

         (try_for_agents, ":cur_agent"),
           (agent_is_human, ":cur_agent"), #horses cannot take flag
           (agent_is_alive, ":cur_agent"),
           (neg|agent_is_non_player, ":cur_agent"), #for now bots cannot take flag or return flags to home.
           (agent_get_horse, ":cur_agent_horse", ":cur_agent"),
           (eq, ":cur_agent_horse", -1), #horseman cannot take flag
           (agent_get_attached_scene_prop, ":attached_scene_prop", ":cur_agent"),
         
           (agent_get_team, ":cur_agent_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_agent_team", 0),
             (assign, ":cur_agent_rival_team", 1),
           (else_try),
             (assign, ":cur_agent_rival_team", 0),
           (try_end),

           (try_begin),
             (eq, ":cur_agent_team", 0), 
             (assign, ":our_flag_id", ":flag_red_id"),
             (assign, ":our_base_entry_id", multi_base_point_team_1),
           (else_try), 
             (assign, ":our_flag_id", ":flag_blue_id"),
             (assign, ":our_base_entry_id", multi_base_point_team_2),
           (try_end),

           (agent_get_position, pos3, ":cur_agent"),
           (prop_instance_get_position, pos4, ":our_flag_id"),
           (get_distance_between_positions, ":dist", pos3, pos4),
           (team_get_slot, ":cur_agent_flag_situation", ":cur_agent_team", slot_team_flag_situation),
         
           (try_begin), #control if agent can return his own flag to default position
             (eq, ":cur_agent_flag_situation", 2), #if our flag is at ground
             (lt, ":dist", 100), #if this agent is near to his team's own flag

             #cur agent returned his own flag to its default position!
             (team_set_slot, ":cur_agent_team", slot_team_flag_situation, 0), #0-flag at base

             #return team flag to its starting position.
             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_set_team_flag_situation", ":cur_agent_team", 0),
             #for only server itself-----------------------------------------------------------------------------------------------         
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, ":cur_agent_team", 0),
             (try_end),

             #return team flag to its starting position.
             (entry_point_get_position, pos5, ":our_base_entry_id"), #moved from above to here after auto-set position
             (prop_instance_set_position, ":our_flag_id", pos5), #moved from above to here after auto-set position

             (try_begin), #give 1 score points to player which returns his/her flag to team base
               (multiplayer_is_server),
               (neg|agent_is_non_player, ":cur_agent"),
               (agent_get_player_id, ":cur_agent_player_id", ":cur_agent"),
               (player_get_score, ":cur_agent_player_score", ":cur_agent_player_id"),
               (val_add, ":cur_agent_player_score", multi_capture_the_flag_score_flag_returning),
               (player_set_score, ":cur_agent_player_id", ":cur_agent_player_score"),
             (try_end),

             #(team_get_faction, ":cur_agent_faction", ":cur_agent_team"),
             #(str_store_faction_name, s1, ":cur_agent_faction"),
             #(tutorial_message_set_position, 500, 500),
             #(tutorial_message_set_size, 30, 30),
             #(tutorial_message_set_center_justify, 1),
             #(tutorial_message, "str_s1_returned_flag", 0xFFFFFFFF, 5),

             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_flag_returned_home, ":cur_agent"), 

             #no need to send also server here
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_flag_returned_home, ":cur_agent"),
             (try_end),         
           (try_end),
                   
           (try_begin), #control if agent carries flag and made score
             (neq, ":attached_scene_prop", -1), #if not agent is carrying anything
         
             (try_begin),
               (eq, ":cur_agent_team", 0), 
               (assign, ":rival_flag_id", ":flag_blue_id"),
               (assign, ":rival_base_entry_id", multi_base_point_team_2),
             (else_try), 
               (assign, ":rival_flag_id", ":flag_red_id"),
               (assign, ":rival_base_entry_id", multi_base_point_team_1),
             (try_end),
             
             (eq, ":attached_scene_prop", ":rival_flag_id"), #if agent is carrying rival flag
             (eq, ":cur_agent_flag_situation", 0), #if our flag is at home position         
             (lt, ":dist", 100), #if this agent (carrying rival flag) is near to his team's own

             #cur_agent's team is scored!#
             (team_get_score, ":cur_agent_team_score", ":cur_agent_team"), #this agent's team scored
             (val_add, ":cur_agent_team_score", 1),
             (team_set_score, ":cur_agent_team", ":cur_agent_team_score"),

             (try_begin), #give 5 score points to player which connects two flag and make score to his/her team
               (multiplayer_is_server),
               (neg|agent_is_non_player, ":cur_agent"),
               (agent_get_player_id, ":cur_agent_player_id", ":cur_agent"),
               (player_get_score, ":cur_agent_player_score", ":cur_agent_player_id"),
               (val_add, ":cur_agent_player_score", "$g_multiplayer_point_gained_from_capturing_flag"),
               (player_set_score, ":cur_agent_player_id", ":cur_agent_player_score"),
             (try_end),
         
             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_team_set_score", ":cur_agent_team", ":cur_agent_team_score"),
             #for only server itself-----------------------------------------------------------------------------------------------
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, ":cur_agent_team", ":cur_agent_team_score"),
             (try_end),

             (agent_set_attached_scene_prop, ":cur_agent", -1),             
             (team_set_slot, ":cur_agent_rival_team", slot_team_flag_situation, 0), #0-flag at base

             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_set_attached_scene_prop", ":cur_agent", -1),
             (agent_set_horse_speed_factor, ":cur_agent", 100),
             #for only server itself-----------------------------------------------------------------------------------------------
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_attached_scene_prop, ":cur_agent", -1),
             (try_end),

             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_set_team_flag_situation", ":cur_agent_rival_team", 0),
             #for only server itself-----------------------------------------------------------------------------------------------         
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, ":cur_agent_rival_team", 0),
             (try_end),

             #return rival flag to its starting position
             (entry_point_get_position, pos5, ":rival_base_entry_id"), #moved from above to here after auto-set position
             (prop_instance_set_position, ":rival_flag_id", pos5), #moved from above to here after auto-set position

             #(team_get_faction, ":cur_agent_faction", ":cur_agent_team"),
             #(str_store_faction_name, s1, ":cur_agent_faction"),
             #(player_get_agent_id, ":my_player_agent", ":my_player_no"),
             #(try_begin),
             #  (ge, ":my_player_agent", 0),
             #  (agent_get_team, ":my_player_team", ":my_player_agent"),
             #  (try_begin),
             #    (eq, ":my_player_team", ":cur_agent_team"),
             #    (assign, ":text_font_color", 0xFF33DDFF),
             #  (else_try),
             #    (assign, ":text_font_color", 0xFFFF0000),
             #  (try_end),
             #(else_try),
             #  (assign, ":text_font_color", 0xFFFFFFFF),
             #(try_end),    
             #(tutorial_message_set_position, 500, 500),
             #(tutorial_message_set_size, 30, 30),
             #(tutorial_message_set_center_justify, 1),
             #(tutorial_message, "str_s1_captured_flag", ":text_font_color", 5),

             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_capture_the_flag_score, ":cur_agent"), 
             
             #no need to send to also server here
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_capture_the_flag_score, ":cur_agent"),
             (try_end),
           (try_end),
         
           (eq, ":attached_scene_prop", -1), #agents carrying other scene prop cannot take flag.
           (agent_get_position, pos3, ":cur_agent"),
           (agent_get_team, ":cur_agent_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_agent_team", 0), #if this agent is from team 1, look its distance to blue flag.
             (get_distance_between_positions, ":dist", pos2, pos3),
             (assign, ":rival_flag_id", ":flag_blue_id"),
           (else_try), #if this agent is from team 2, look its distance to red flag.
             (get_distance_between_positions, ":dist", pos1, pos3),
             (assign, ":rival_flag_id", ":flag_red_id"),
           (try_end),

           (try_begin),  #control if agent stole enemy flag
             (le, ":dist", 100),
             (neg|team_slot_eq, ":cur_agent_rival_team", slot_team_flag_situation, 1), #if flag is not already stolen.
             
             (agent_set_attached_scene_prop, ":cur_agent", ":rival_flag_id"),
             (agent_set_attached_scene_prop_x, ":cur_agent", 20),
             (agent_set_attached_scene_prop_z, ":cur_agent", 50),

             (try_begin),
               (eq, ":cur_agent_team", 0),
               (assign, "$flag_1_at_ground_timer", 0),
             (else_try),
               (eq, ":cur_agent_team", 1),
               (assign, "$flag_2_at_ground_timer", 0),
             (try_end),

             #cur_agent stole rival team's flag!
             (team_set_slot, ":cur_agent_rival_team", slot_team_flag_situation, 1), #1-stolen flag
                      
             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_set_attached_scene_prop", ":cur_agent", ":rival_flag_id"),
             (agent_set_horse_speed_factor, ":cur_agent", 75),
             #for only server itself-----------------------------------------------------------------------------------------------
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_attached_scene_prop, ":cur_agent", ":rival_flag_id"),
             (try_end),
         
             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_set_team_flag_situation", ":cur_agent_rival_team", 1),
             #for only server itself-----------------------------------------------------------------------------------------------
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, ":cur_agent_rival_team", 1),
             (try_end),

             #(team_get_faction, ":cur_agent_faction", ":cur_agent_team"),
             #(str_store_faction_name, s1, ":cur_agent_faction"),
             #(tutorial_message_set_position, 500, 500),
             #(tutorial_message_set_size, 30, 30),
             #(tutorial_message_set_center_justify, 1),
             #(tutorial_message, "str_s1_taken_flag", 0xFFFFFFFF, 5), 

             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_capture_the_flag_stole, ":cur_agent"), 

             #no need to send also server here
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_capture_the_flag_stole, ":cur_agent"),
             (try_end),         
           (try_end),
         (try_end),         
         ]),

      (20, 0, 0, [],
       [
         (multiplayer_is_server),
         #auto team balance control in every 10 seconds (cf)
         (call_script, "script_check_team_balance"),
         ]),

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,

      (ti_battle_window_opened, 0, 0, [], [
        (start_presentation, "prsnt_multiplayer_team_score_display"),
        (start_presentation, "prsnt_multiplayer_flag_projection_display"),
        ]),

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),

    (
    "multiplayer_sg",mtf_battle_mode,-1, #siege
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),
     ],
    [
      
      multiplayer_server_check_belfry_movement,      

      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),

         (try_begin),
           (multiplayer_is_server),
           (this_or_next|player_is_active, ":player_no"),
           (eq, ":player_no", 0),
           (store_mission_timer_a, ":round_time"),
           (val_sub, ":round_time", "$g_round_start_time"),
           # for each 20 % of round time spend loose 1 life.
           (try_begin),
             (store_mul,":spend_time","$g_multiplayer_round_max_seconds",20), 
             (val_div,":spend_time",100), # 20% of default roundtime of 300 sec = 60 so first 60 seconds loose no life.
             (lt, ":round_time", ":spend_time"),
             (assign, ":number_of_respawns_spent", 0),
           (else_try),
             (store_mul,":spend_time","$g_multiplayer_round_max_seconds",40), 
             (val_div,":spend_time",100), # 40% of default roundtime 300 sec = 120 so between 60 and 120 seconds loose 1 life.
             (lt, ":round_time", ":spend_time"),
             (assign, ":number_of_respawns_spent", 1),
           (else_try),
             (store_mul,":spend_time","$g_multiplayer_round_max_seconds",60),
             (val_div,":spend_time",100), # 60% of default roundtime 300 sec = 180 so between 120 and 180 seconds loose 2 lifes.
             (lt, ":round_time", ":spend_time"),
             (assign, ":number_of_respawns_spent", 2),
           (else_try),
             (store_mul,":spend_time","$g_multiplayer_round_max_seconds",80),
             (val_div,":spend_time",100), # 80% of default roundtime 300 sec = 240 so between 180 and 240 seconds loose 3 lifes.
             (lt, ":round_time", ":spend_time"),
             (assign, ":number_of_respawns_spent", 3),
           (else_try),  # for anything above the 80% (>240 sec default round time) of the round spend give no more lifes.
             (assign, ":number_of_respawns_spent", "$g_multiplayer_number_of_respawn_count"), 
           (try_end),
           (player_set_slot, ":player_no", slot_player_spawn_count, ":number_of_respawns_spent"),             
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_spent, ":number_of_respawns_spent"),
         (try_end),         
       ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_siege),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (try_begin),
           (multiplayer_is_server),
           (try_for_range, ":cur_flag_slot", multi_data_flag_pull_code_begin, multi_data_flag_pull_code_end),
             (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", -1),
           (try_end),
           (assign, "$g_round_start_time", 0),
         (try_end),
         
         (assign, "$g_my_spawn_count", 0),
      
         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
         (assign, "$g_round_ended", 0),

         (assign, "$my_team_at_start_of_round", -1),

         (assign, "$g_flag_is_not_ready", 0),

         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (call_script, "script_determine_team_flags", 0),
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         
         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),

         (assign, "$g_number_of_flags", 0),
         (try_begin),
           (multiplayer_is_server),
           (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         
           #place base flags
           (entry_point_get_position, pos1, multi_siege_flag_point),
           (set_spawn_position, pos1),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),         
           (position_move_z, pos1, multi_headquarters_pole_height),         
           (set_spawn_position, pos1),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
           (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, "$g_number_of_flags"),
           (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 1),
         (try_end),
         (val_add, "$g_number_of_flags", 1),

         (try_begin),
           (multiplayer_is_server),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),
           (try_end),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),
           (try_end),

           (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_a"),
           (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_b"),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
           (try_end),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
           (try_end),

           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
           (try_end),

           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
           (try_end),
         (try_end),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),

         (try_begin), #if my initial team still not initialized, find and assign its value.
           (neg|multiplayer_is_dedicated_server),
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (eq, ":my_agent_id", ":agent_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),

         (try_begin),
           (neg|multiplayer_is_server),
           (try_begin),
             (eq, "$g_round_ended", 1),
             (assign, "$g_round_ended", 0),
             (assign, "$g_my_spawn_count", 0),

             #initialize scene object slots at start of new round at clients.
             (call_script, "script_initialize_all_scene_prop_slots"),

             #these lines are done in only clients at start of each new round.
             (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
             (call_script, "script_initialize_objects_clients"),
             #end of lines
           (try_end),  
         (try_end),         

         (try_begin),
           (neg|multiplayer_is_dedicated_server),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (eq, ":my_agent_id", ":agent_no"),

           (val_add, "$g_my_spawn_count", 1),
         
           (try_begin),
             (ge, "$g_my_spawn_count", "$g_multiplayer_number_of_respawn_count"),
             (gt, "$g_multiplayer_number_of_respawn_count", 0),
             (multiplayer_get_my_player, ":my_player_no"),
             (player_get_team_no, ":my_player_team_no", ":my_player_no"),
             (eq, ":my_player_team_no", 0),
             (assign, "$g_my_spawn_count", 999),
           (try_end),
         (try_end),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (store_trigger_param_2, ":killer_agent_no"),

         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
         
         (try_begin), #if my initial team still not initialized, find and assign its value.
           (neg|multiplayer_is_dedicated_server),
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),         
         
         (try_begin),
           (multiplayer_is_server),
           (agent_is_human, ":dead_agent_no"),
           (neg|agent_is_non_player, ":dead_agent_no"),
           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
           (player_set_slot, ":dead_agent_player_id", slot_player_spawned_this_round, 0),
         (try_end),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),
      
      # Running this trigger not every frame is quite important for server performance
      # It reduces the amount of messages send to clients by a lot plus loops per second.
      (1, 0, 0, [],
      [
        (multiplayer_is_server),
        (eq, "$g_round_ended", 0),
        #main trigger which controls which agent is moving/near which flag.
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
          (troop_get_slot, ":current_owner_code", "trp_multiplayer_data", ":cur_flag_owner_counts_slot"),
          (store_div, ":old_team_1_agent_count", ":current_owner_code", 100),
          (store_mod, ":old_team_2_agent_count", ":current_owner_code", 100),
        
          (assign, ":number_of_agents_around_flag_team_1", 0),
          (assign, ":number_of_agents_around_flag_team_2", 0),

          (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"), 
          (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.

          (get_max_players, ":num_players"),
            (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":cur_agent", ":player_no"),            
            (ge, ":cur_agent", 0),
            (agent_is_alive, ":cur_agent"),
            (agent_get_position, pos1, ":cur_agent"), #pos1 holds agent's position.
            (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
            (get_sq_distance_between_position_heights, ":squared_height_dist", pos0, pos1),
            (val_add, ":squared_dist", ":squared_height_dist"),
            (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (try_begin),
              (eq, ":cur_agent_team", 0),
              (val_add, ":number_of_agents_around_flag_team_1", 1),
            (else_try),
              (eq, ":cur_agent_team", 1),
              (val_add, ":number_of_agents_around_flag_team_2", 1),
            (try_end),
          (try_end),

          (try_begin),
            (this_or_next|neq, ":old_team_1_agent_count", ":number_of_agents_around_flag_team_1"),
            (neq, ":old_team_2_agent_count", ":number_of_agents_around_flag_team_2"),

            (store_add, ":cur_flag_pull_code_slot", multi_data_flag_pull_code_begin, ":flag_no"),
            (troop_get_slot, ":cur_flag_pull_code", "trp_multiplayer_data", ":cur_flag_pull_code_slot"),
            (store_mod, ":cur_flag_pull_message_seconds_past", ":cur_flag_pull_code", 100),
            (store_div, ":cur_flag_puller_team_last", ":cur_flag_pull_code", 100),

            (try_begin),        
              (eq, ":old_team_2_agent_count", 0),
              (gt, ":number_of_agents_around_flag_team_2", 0),
              (eq, ":number_of_agents_around_flag_team_1", 0),
              (assign, ":puller_team", 2),

              (store_mul, ":puller_team_multiplied_by_100", ":puller_team", 100),
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_pull_code_slot", ":puller_team_multiplied_by_100"),

              (this_or_next|neq, ":cur_flag_puller_team_last", ":puller_team"),
              (ge, ":cur_flag_pull_message_seconds_past", 25),

              (store_mul, ":flag_code", ":puller_team", 100),
              (val_add, ":flag_code", ":flag_no"),
            (try_end),

            (try_begin),
              (store_mul, ":current_owner_code", ":number_of_agents_around_flag_team_1", 100),
              (val_add, ":current_owner_code", ":number_of_agents_around_flag_team_2"),        
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owner_counts_slot", ":current_owner_code"),
              (get_max_players, ":num_players"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_set_num_agents_around_flag", ":flag_no", ":current_owner_code"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_num_agents_around_flag, ":flag_no", ":current_owner_code"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),

        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (eq, "$g_round_ended", 0), #if round still continues and any team did not sucseed yet
          (eq, "$g_flag_is_not_ready", 0), #if round still continues and any team did not sucseed yet
        
          (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"), 
          (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.            

          (try_begin),
            (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),

            #flag_id holds shown flag after this point
            (prop_instance_get_position, pos1, ":flag_id"), #pos1 holds gray/red/blue (current shown) flag position.
            (try_begin),
              (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),        
              (lt, ":squared_dist", multi_headquarters_distance_sq_to_change_flag), #if distance is less than 2 meters
              
              (prop_instance_is_animating, ":is_animating", ":flag_id"),
              (eq, ":is_animating", 1),

              #end of round, attackers win
              (assign, "$g_winner_team", 1),
              (prop_instance_stop_animating, ":flag_id"),        
        
              (get_max_players, ":num_players"), 
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_draw_this_round", "$g_winner_team"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
              (try_end),

              (assign, "$g_flag_is_not_ready", 1),
            (try_end),        
          (try_end),
        (try_end),
        ]),

      (0, 0, 0, [(neg|multiplayer_is_dedicated_server)], #if there is nobody in any teams do not reduce round time.
       [
         (store_mission_timer_a, ":seconds_past_since_round_started"),
         (val_sub, ":seconds_past_since_round_started", "$g_round_start_time"),
         (le, ":seconds_past_since_round_started", 2),

         (assign, ":human_agents_spawned_at_team_1", "$g_multiplayer_num_bots_team_1"),
         (assign, ":human_agents_spawned_at_team_2", "$g_multiplayer_num_bots_team_2"),
         
         (get_max_players, ":end_cond"),
         (try_for_range, ":player_no", 0, ":end_cond"),
           (player_is_active, ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"), 
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":human_agents_spawned_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":human_agents_spawned_at_team_2", 1),
           (try_end),
           (gt, ":human_agents_spawned_at_team_1", 0),
           (gt, ":human_agents_spawned_at_team_2", 0),
           (assign, ":end_cond", 0),
         (try_end),

         (try_begin),
           (this_or_next|eq, ":human_agents_spawned_at_team_1", 0),
           (eq, ":human_agents_spawned_at_team_2", 0),
                  
           (store_mission_timer_a, "$g_round_start_time"),
         (try_end),
       ]),

      # copied this for server with less checks.
      (1, 0, 0, [(multiplayer_is_dedicated_server)], #if there is nobody in any teams do not reduce round time.
       [
         (store_mission_timer_a, ":seconds_past_since_round_started"),
         (val_sub, ":seconds_past_since_round_started", "$g_round_start_time"),
         (le, ":seconds_past_since_round_started", 2),
       
         (assign, ":human_agents_spawned_at_team_1", "$g_multiplayer_num_bots_team_1"),
         (assign, ":human_agents_spawned_at_team_2", "$g_multiplayer_num_bots_team_2"),
         
         (get_max_players,":end_cond"),
         (try_for_range, ":player_no", 0, ":end_cond"),
           (player_is_active, ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"), 
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":human_agents_spawned_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":human_agents_spawned_at_team_2", 1),
           (try_end),
           (gt, ":human_agents_spawned_at_team_1", 0),
           (gt, ":human_agents_spawned_at_team_2", 0),
           (assign, ":end_cond", 0),
         (try_end),

         (try_begin),
           (this_or_next|eq, ":human_agents_spawned_at_team_1", 0),
           (eq, ":human_agents_spawned_at_team_2", 0),

           (store_mission_timer_a, "$g_round_start_time"),
         (try_end),
       ]),
      

      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0),
                 (eq, "$g_flag_is_not_ready", 0),
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (ge, ":seconds_past_in_round", "$g_multiplayer_round_max_seconds")],
       [
         (assign, ":flag_no", 0),
         (store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
         (troop_get_slot, ":current_owner_code", "trp_multiplayer_data", ":cur_flag_owner_counts_slot"),
         (store_mod, ":team_2_agent_count_around_flag", ":current_owner_code", 100),

         (try_begin),
           (eq, ":team_2_agent_count_around_flag", 0),
         
           (store_mission_timer_a, "$g_round_finish_time"),
           (assign, "$g_round_ended", 1),
           (assign, "$g_flag_is_not_ready", 1),
        
           (assign, "$g_winner_team", 0),

           (get_max_players, ":num_players"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_draw_this_round", "$g_winner_team"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
           (try_end),
         (try_end),
         ]),          

      (1, 0, 0, [],
      [
        (multiplayer_is_server),
        #trigger for calculating seconds past after that flag's pull message has shown          
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (store_add, ":cur_flag_pull_code_slot", multi_data_flag_pull_code_begin, ":flag_no"),
          (troop_get_slot, ":cur_flag_pull_code", "trp_multiplayer_data", ":cur_flag_pull_code_slot"),
          (store_mod, ":cur_flag_pull_message_seconds_past", ":cur_flag_pull_code", 100),
          (try_begin),
            (ge, ":cur_flag_pull_code", 100),
            (lt, ":cur_flag_pull_message_seconds_past", 25),
            (val_add, ":cur_flag_pull_code", 1),
            (troop_set_slot, "trp_multiplayer_data", ":cur_flag_pull_code_slot", ":cur_flag_pull_code"),
          (try_end),
        (try_end),        
      ]),               

      (10, 0, 0, [(multiplayer_is_server)],
       [
         #auto team balance control during the round         
         (assign, ":number_of_players_at_team_1", 0),
         (assign, ":number_of_players_at_team_2", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 0, ":num_players"),
           (player_is_active, ":cur_player"),
           (player_get_team_no, ":player_team", ":cur_player"),
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":number_of_players_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":number_of_players_at_team_2", 1),
           (try_end),         
         (try_end),
         #end of counting active players per team.
         (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
         (assign, ":number_of_players_will_be_moved", 0),
         (try_begin),
           (try_begin),
             (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
             (le, ":difference_of_number_of_players", ":checked_value"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
           (else_try),
             (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
           (try_end),          
         (try_end),         
         #number of players will be moved calculated. (it is 0 if no need to make team balance)
         (try_begin),
		   (neq, "$g_multiplayer_game_type", multiplayer_game_type_captain_coop), # disable auto team balance in captain coop
           (gt, ":number_of_players_will_be_moved", 0),
           (try_begin),
             (eq, "$g_team_balance_next_round", 0),
         
             (assign, "$g_team_balance_next_round", 1),

             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
             #for only server itself-----------------------------------------------------------------------------------------------     
             (get_max_players, ":num_players"),                               
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
             (try_end),
             
             (call_script, "script_warn_player_about_auto_team_balance"),
           (try_end),
         (try_end),           
         #team balance check part finished
         ]),          

      (1, 0, 3, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 1),
                 (store_mission_timer_a, ":seconds_past_till_round_ended"),
                 (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
                 (ge, ":seconds_past_till_round_ended", "$g_multiplayer_respawn_period")],
       [
         #auto team balance control at the end of round         
         (assign, ":number_of_players_at_team_1", 0),
         (assign, ":number_of_players_at_team_2", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 0, ":num_players"),
           (player_is_active, ":cur_player"),
           (player_get_team_no, ":player_team", ":cur_player"),
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":number_of_players_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":number_of_players_at_team_2", 1),
           (try_end),         
         (try_end),
         #end of counting active players per team.
         (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
         (assign, ":number_of_players_will_be_moved", 0),
         (try_begin),
           (try_begin),
             (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
             (le, ":difference_of_number_of_players", ":checked_value"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
             (assign, ":team_with_more_players", 1),
             (assign, ":team_with_less_players", 0),
           (else_try),
             (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
             (assign, ":team_with_more_players", 0),
             (assign, ":team_with_less_players", 1),
           (try_end),          
         (try_end),         
         #number of players will be moved calculated. (it is 0 if no need to make team balance)
         (try_begin),
           (gt, ":number_of_players_will_be_moved", 0),
           (try_begin),
             (try_for_range, ":unused", 0, ":number_of_players_will_be_moved"), 
               (assign, ":max_player_join_time", 0),
               (assign, ":latest_joined_player_no", -1),
               (get_max_players, ":num_players"),                               
               (try_for_range, ":player_no", 0, ":num_players"),
                 (player_is_active, ":player_no"),
                 (player_get_team_no, ":player_team", ":player_no"),
                 (eq, ":player_team", ":team_with_more_players"),
                 (player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
                 (try_begin),
                   (gt, ":player_join_time", ":max_player_join_time"),
                   (assign, ":max_player_join_time", ":player_join_time"),
                   (assign, ":latest_joined_player_no", ":player_no"),
                 (try_end),
               (try_end),
               (try_begin),
                 (ge, ":latest_joined_player_no", 0),
                 (try_begin),
                   #if player is living add +1 to his kill count because he will get -1 because of team change while living.
                   (player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"), 
                   (ge, ":latest_joined_agent_id", 0),
                   (agent_is_alive, ":latest_joined_agent_id"),

                   (player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
                   (val_add, ":player_kill_count", 1),
                   (player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),

                   (player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
                   (val_sub, ":player_death_count", 1),
                   (player_set_death_count, ":latest_joined_player_no", ":player_death_count"),

                   (player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
                   (val_add, ":player_score", 1),
                   (player_set_score, ":latest_joined_player_no", ":player_score"),

                   (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                     (player_is_active, ":player_no"),
                     (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
                   (try_end),         

                   (player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
                   (player_get_gold, ":player_gold", ":latest_joined_player_no"),
                   (val_add, ":player_gold", ":old_items_value"),
                   (player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
                 (end_try),

				 (call_script, "script_mp_set_player_team_no", ":latest_joined_player_no", ":team_with_less_players", 0),
                 (multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
               (try_end),
             (try_end),
             #tutorial message (after team balance)
             
             #(tutorial_message_set_position, 500, 500),
             #(tutorial_message_set_size, 30, 30),
             #(tutorial_message_set_center_justify, 1),
             #(tutorial_message, "str_auto_team_balance_done", 0xFFFFFFFF, 5),
             
             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), 

             #no need to send also server here
             (multiplayer_get_my_player, ":my_player_no"),
             (get_max_players, ":num_players"),                               
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
             (try_end),
             (assign, "$g_team_balance_next_round", 0),
           (try_end),
         (try_end),           
         #team balance check part finished
         (assign, "$g_team_balance_next_round", 0),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
           (player_set_slot, ":player_no", slot_player_spawned_at_siege_round, 0),           
           (player_get_agent_id, ":player_agent", ":player_no"),
           (ge, ":player_agent", 0),
           (agent_is_alive, ":player_agent"),
           (player_save_picked_up_items_for_next_spawn, ":player_no"),
           (player_get_value_of_original_items, ":old_items_value", ":player_no"),
           (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, ":old_items_value"),
         (try_end),

         #money management
         (assign, ":per_round_gold_addition", multi_battle_round_team_money_add),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_gold, ":player_gold", ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"),
         
           (try_begin),
             (this_or_next|eq, ":player_team", 0),
             (eq, ":player_team", 1),
             (val_add, ":player_gold", ":per_round_gold_addition"), 
           (try_end),

           #(below lines added new at 25.11.09 after Armagan decided new money system)
           (try_begin),
             (player_get_slot, ":old_items_value", ":player_no", slot_player_last_rounds_used_item_earnings),
             (store_add, ":player_total_potential_gold", ":player_gold", ":old_items_value"),
             (store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
             (lt, ":player_total_potential_gold", ":minimum_gold"),
             (store_sub, ":additional_gold", ":minimum_gold", ":player_total_potential_gold"),
             (val_add, ":player_gold", ":additional_gold"),
           (try_end),
           #new money system addition end

           (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
         (try_end),

         #initialize my team at start of round (it will be assigned again at next round's first death)
         (assign, "$my_team_at_start_of_round", -1),

         #clear scene and end round
         (multiplayer_clear_scene),
         
         #assigning everbody's spawn counts to 0
         (assign, "$g_my_spawn_count", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_set_slot, ":player_no", slot_player_spawn_count, 0),
         (try_end),

         #(call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_initialize_objects"),

         #initialize moveable object positions
         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_close_gate_if_it_is_open"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
         (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_a"),
         (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_b"),
         
         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
         (try_end),

         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
         (try_end),

         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
         (try_end),

         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
         (try_end),

         #initialize flag coordinates (move up the flag at pole)
         (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
           (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
           (prop_instance_get_position, pos1, ":pole_id"),
           (position_move_z, pos1, multi_headquarters_pole_height),
           (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
           (prop_instance_stop_animating, ":flag_id"),
           (prop_instance_set_position, ":flag_id", pos1),
         (try_end),
         
         (assign, "$g_round_ended", 0),
         
         (store_mission_timer_a, "$g_round_start_time"),
         (call_script, "script_initialize_all_scene_prop_slots"),

         #initialize round start time for clients
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, -9999),
         (try_end),         

         (assign, "$g_flag_is_not_ready", 0),
       ]),
           
      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0)],
       [
         (store_mission_timer_a, ":current_time"),
         (store_sub, ":round_time", ":current_time", "$g_round_start_time"),
        
         (assign, ":attacker_respawn_period", "$g_multiplayer_respawn_period"), 
         (store_add, ":defender_respawn_period",":attacker_respawn_period", multiplayer_siege_mod_defender_team_extra_respawn_time), 
 
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
           (player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),
          
           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),
           
           (assign, ":continue", 1),
           (player_get_slot, ":spawn_count", ":player_no", slot_player_spawn_count),
           (try_begin),
             (gt, "$g_multiplayer_number_of_respawn_count", 0),
             (try_begin),
               (eq, ":player_team", 0),
               (ge, ":spawn_count", "$g_multiplayer_number_of_respawn_count"),
               (assign, ":continue", 0),
             (else_try),
               (eq, ":player_team", 1),      
               (ge, ":spawn_count", 999),
               (assign, ":continue", 0),
             (try_end),
           (try_end),
           (eq, ":continue", 1),
           
           (try_begin),
             (eq, ":player_team", 0), # defender
             (assign,":player_team_respawn_period",":defender_respawn_period"),
           (else_try),
             (assign,":player_team_respawn_period",":attacker_respawn_period"),
           (try_end),
           
           (player_get_agent_id, ":player_agent", ":player_no"), #new added for siege mod
           (assign, ":spawn_new", 0), 
           (try_begin), #addition for siege mod to allow players spawn more than once (begin)
             (lt, ":player_agent", 0), 

             (try_begin), #new added begin, to avoid siege-crack (rejoining of defenders when they die)
               (eq, ":player_team", 0), 
               (player_get_slot, ":player_last_team_select_time", ":player_no", slot_player_last_team_select_time),
               (store_sub, ":elapsed_time", ":current_time", ":player_last_team_select_time"),
               
               (lt, ":elapsed_time", ":player_team_respawn_period"),
               (ge, ":round_time", multiplayer_new_agents_finish_spawning_time), # Do nothing he must wait.
             (else_try), #new added end         
               (assign, ":spawn_new", 1),
             (try_end),
           (else_try), 
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"), 
             (this_or_next|gt, ":elapsed_time", ":player_team_respawn_period"), 
             (player_slot_eq, ":player_no", slot_player_spawned_at_siege_round, 0), 
             (assign, ":spawn_new", 1),
           (try_end), #addition for siege mod to allow players spawn more than once (end)

           (eq, ":spawn_new", 1),
           
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (val_add, ":spawn_count", 1),
           (player_set_slot, ":player_no", slot_player_spawn_count, ":spawn_count"),

           (try_begin),
             (ge, ":spawn_count", "$g_multiplayer_number_of_respawn_count"),
             (gt, "$g_multiplayer_number_of_respawn_count", 0),
             (eq, ":player_team", 0),
             (player_set_slot, ":player_no", slot_player_spawn_count, 999),
           (try_end),

           (assign, ":player_is_horseman", 0),
           (player_get_item_id, ":item_id", ":player_no", ek_horse),
           (try_begin),
             (this_or_next|is_between, ":item_id", horses_begin, horses_end),
             (             is_between, ":item_id", oim_horses_begin, oim_horses_end),
             (assign, ":player_is_horseman", 1),
           (try_end),
		   
           (try_begin),
             (lt, ":round_time", 20), #at start of game spawn at base entry point (only enemies)
             (try_begin),         
               (eq, ":player_team", 0), #defenders in siege mod at start of round
               (call_script, "script_multiplayer_find_spawn_point", ":player_team", 1, ":player_is_horseman"),
               (assign, ":entry_no", reg0),             
             (else_try),
               (eq, ":player_team", 1), #attackers in siege mod at start of round
               (assign, ":entry_no", multi_initial_spawn_point_team_2), #change later
             (try_end),
           (else_try),
             (call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":player_is_horseman"),
             (assign, ":entry_no", reg0),             
           (try_end),
         
           (player_spawn_new_agent, ":player_no", ":entry_no"),
           (player_set_slot, ":player_no", slot_player_spawned_this_round, 1),
           (player_set_slot, ":player_no", slot_player_spawned_at_siege_round, 1),         
         (try_end),
         ]),

      (1, 0, 0, [ (multiplayer_is_server),
                  (this_or_next|gt,"$g_multiplayer_num_bots_team_1",0),
                  (gt,"$g_multiplayer_num_bots_team_2",0),# are there any bots?
                  (store_mission_timer_a, ":mission_timer"),
                  (ge, ":mission_timer", 2)                
                ], #do this in every new frame, but not at the same time
       [
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), 
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),

      multiplayer_server_spawn_bots, 
      multiplayer_server_manage_bots, 

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,

      (ti_battle_window_opened, 0, 0, [], [
        (start_presentation, "prsnt_multiplayer_round_time_counter"),
        (start_presentation, "prsnt_multiplayer_team_score_display"),
        ]),

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),

   (
    "multiplayer_bt",mtf_battle_mode,-1, #battle mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_battle),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
         (assign, "$g_round_ended", 0),
         (assign, "$g_battle_death_mode_started", 0),
         (assign, "$g_reduced_waiting_seconds", 0),

         (try_begin),
           (multiplayer_is_server),
           (assign, "$server_mission_timer_while_player_joined", 0),
           (assign, "$g_round_start_time", 0),
         (try_end),
         (assign, "$my_team_at_start_of_round", -1),

         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (call_script, "script_determine_team_flags", 0),
         (call_script, "script_determine_team_flags", 1),
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)

         (try_begin),
           (multiplayer_is_server),

           (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         
           (entry_point_get_position, pos0, multi_death_mode_point),
           (position_set_z_to_ground_level, pos0),
           (position_move_z, pos0, -2000),

           (position_move_x, pos0, 100), 
           (set_spawn_position, pos0),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),

           (position_move_x, pos0, -200), 
           (set_spawn_position, pos0),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),

           (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
           (prop_instance_get_position, pos0, ":pole_1_id"),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
           (position_move_z, pos0, multi_headquarters_flag_initial_height),
           (prop_instance_set_position, reg0, pos0),
         
           (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
           (prop_instance_get_position, pos0, ":pole_2_id"),
           (spawn_scene_prop, "$team_2_flag_scene_prop", 0),
           (position_move_z, pos0, multi_headquarters_flag_initial_height),
           (prop_instance_set_position, reg0, pos0),

           (assign, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1"), 
           (assign, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2"), 
         (try_end),

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
		 
		 (set_cheer_at_no_enemy, 0),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         
         (try_begin), #if my initial team still not initialized, find and assign its value.
           (neg|multiplayer_is_dedicated_server),
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (eq, ":my_agent_id", ":agent_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),
         
         (call_script, "script_calculate_new_death_waiting_time_at_death_mod"),
 
         (try_begin),
           (neg|multiplayer_is_server),
           (eq, "$g_round_ended", 1),
           (assign, "$g_round_ended", 0),

           #initialize scene object slots at start of new round at clients.
           (call_script, "script_initialize_all_scene_prop_slots"),

           #these lines are done in only clients at start of each new round.
           (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
           (call_script, "script_initialize_objects_clients"),
           #end of lines
           (try_begin),
             (eq, "$g_team_balance_next_round", 1),
             (assign, "$g_team_balance_next_round", 0),
           (try_end),
         (try_end),         
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (store_trigger_param_2, ":killer_agent_no"),

         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),

         (try_begin), #if my initial team still not initialized, find and assign its value.
           (neg|multiplayer_is_dedicated_server),
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),         
         
         (try_begin), #count players and if round ended understand this.
           (agent_is_human, ":dead_agent_no"),
           (assign, ":team1_living_players", 0),
           (assign, ":team2_living_players", 0),
           (assign,":continue_loop",1),
           (try_for_agents, ":cur_agent"),
             (eq,":continue_loop",1),
             (agent_is_human, ":cur_agent"),         
             (agent_is_alive, ":cur_agent"),  
             (agent_get_team, ":cur_agent_team", ":cur_agent"),
             (try_begin),
               (eq, ":cur_agent_team", 0),
               (val_add, ":team1_living_players", 1),
             (else_try),
               (eq, ":cur_agent_team", 1),
               (val_add, ":team2_living_players", 1),
             (try_end),
             # Break loop.
             (gt, ":team1_living_players", 0),
             (gt, ":team2_living_players", 0),
             (assign,":continue_loop",0),
           (try_end),  
           
           (try_begin),         
             (eq, "$g_round_ended", 0),
             (this_or_next|eq, ":team1_living_players", 0),
             (eq, ":team2_living_players", 0),
             (assign, "$g_winner_team", -1),
             (assign, reg0, "$g_multiplayer_respawn_period"),
             (try_begin),
               (eq, ":team1_living_players", 0),
               (try_begin),
                 (neq, ":team2_living_players", 0),
                 (team_get_score, ":team_2_score", 1),
                 (val_add, ":team_2_score", 1),
                 (team_set_score, 1, ":team_2_score"),
                 (assign, "$g_winner_team", 1),
               (try_end),
             (else_try),
               (neq, ":team1_living_players", 0),
               (team_get_score, ":team_1_score", 0),
               (val_add, ":team_1_score", 1),
               (team_set_score, 0, ":team_1_score"),
               (assign, "$g_winner_team", 0),
             (try_end),
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, "$g_winner_team"),

             (store_mission_timer_a, "$g_round_finish_time"),
             (assign, "$g_round_ended", 1),
           (try_end),
         (try_end),

         (try_begin),
           (multiplayer_is_server),
           (agent_is_human, ":dead_agent_no"),
           (neg|agent_is_non_player, ":dead_agent_no"),

           (ge, ":dead_agent_no", 0),
           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
           (ge, ":dead_agent_player_id", 0),

           (set_fixed_point_multiplier, 100),

           (agent_get_position, pos0, ":dead_agent_no"),

           (position_get_x, ":x_coor", pos0),
           (position_get_y, ":y_coor", pos0),
           (position_get_z, ":z_coor", pos0),
         
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_x, ":x_coor"),
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_y, ":y_coor"),
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_z, ":z_coor"),
         (try_end),    
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),
      
      (1, 0, 0, [(multiplayer_is_server), 
                 (eq, "$g_round_ended", 0),
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (ge, ":seconds_past_in_round", "$g_multiplayer_round_max_seconds"),

                 (assign, ":overtime_needed", 0), #checking for if overtime is needed. Overtime happens when lower heighted flag is going up
                 (try_begin),
                   (eq, "$g_battle_death_mode_started", 2), #if death mod is currently open
                    
                   (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
                   (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
                   (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
                   (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

                   (prop_instance_get_position, pos1, ":pole_1_id"),
                   (prop_instance_get_position, pos2, ":pole_2_id"),
                   (prop_instance_get_position, pos3, ":flag_1_id"),
                   (prop_instance_get_position, pos4, ":flag_2_id"),

                   (get_distance_between_positions, ":height_of_flag_1", pos1, pos3),
                   (get_distance_between_positions, ":height_of_flag_2", pos2, pos4),
                   (store_add, ":height_of_flag_1_plus", ":height_of_flag_1", min_allowed_flag_height_difference_to_make_score),
                   (store_add, ":height_of_flag_2_plus", ":height_of_flag_2", min_allowed_flag_height_difference_to_make_score),

                   (try_begin),
                     (le, ":height_of_flag_1", ":height_of_flag_2_plus"),
                     (prop_instance_is_animating, ":is_animating", ":flag_1_id"),
                     (eq, ":is_animating", 1),
                     (prop_instance_get_animation_target_position, pos5, ":flag_1_id"),
                     (position_get_z, ":flag_2_animation_target_z", pos5),
                     (position_get_z, ":flag_1_cur_z", pos3),
                     (ge, ":flag_2_animation_target_z", ":flag_1_cur_z"),
                     (assign, ":overtime_needed", 1),
                   (try_end),
                   
                   (try_begin),
                     (le, ":height_of_flag_2", ":height_of_flag_1_plus"),
                     (prop_instance_is_animating, ":is_animating", ":flag_2_id"),
                     (eq, ":is_animating", 1),
                     (prop_instance_get_animation_target_position, pos5, ":flag_2_id"),
                     (position_get_z, ":flag_2_animation_target_z", pos5),
                     (position_get_z, ":flag_2_cur_z", pos4),
                     (ge, ":flag_2_animation_target_z", ":flag_2_cur_z"),
                     (assign, ":overtime_needed", 1),
                   (try_end),
                 (try_end),
                 (eq, ":overtime_needed", 0),
                 ],
       [ #round time is up
         (store_mission_timer_a, "$g_round_finish_time"),                          
         (assign, "$g_round_ended", 1),
         (assign, "$g_winner_team", -1),
         
         (try_begin), #checking for winning by death mod
           (eq, "$g_battle_death_mode_started", 2), #if death mod is currently open

           (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
           (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
           (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
           (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

           (prop_instance_get_position, pos1, ":pole_1_id"),
           (prop_instance_get_position, pos2, ":pole_2_id"),
           (prop_instance_get_position, pos3, ":flag_1_id"),
           (prop_instance_get_position, pos4, ":flag_2_id"),

           (get_distance_between_positions, ":height_of_flag_1", pos1, pos3),
           (get_distance_between_positions, ":height_of_flag_2", pos2, pos4),

           (try_begin),
             (ge, ":height_of_flag_1", ":height_of_flag_2"), #if flag_1 is higher than flag_2
             (store_sub, ":difference_of_heights", ":height_of_flag_1", ":height_of_flag_2"), 
             (ge, ":difference_of_heights", min_allowed_flag_height_difference_to_make_score), #if difference between flag heights is greater than 
             (assign, "$g_winner_team", 0),                                                    #"min_allowed_flag_height_difference_to_make_score" const value
           (else_try), #if flag_2 is higher than flag_1
             (store_sub, ":difference_of_heights", ":height_of_flag_2", ":height_of_flag_1"),
             (ge, ":difference_of_heights", min_allowed_flag_height_difference_to_make_score), #if difference between flag heights is greater than 
             (assign, "$g_winner_team", 1),                                                    #"min_allowed_flag_height_difference_to_make_score" const value
           (try_end),
         (try_end),
    
         (multiplayer_get_my_player, ":my_player_no"), #send all players draw information of round.
         #for only server itself-----------------------------------------------------------------------------------------------
         (call_script, "script_draw_this_round", "$g_winner_team"),
         #for only server itself-----------------------------------------------------------------------------------------------
         (get_max_players, ":num_players"), 
         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
           (player_is_active, ":player_no"),
           (neq, ":player_no", ":my_player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
         (try_end),
        ]),          

      (10, 0, 0, [(multiplayer_is_server)],
       [
         #auto team balance control during the round
	     (call_script, "script_multiplayer_get_balance_dif", 0, 0),
         (assign, ":number_of_players_will_be_moved", reg0),
         (neq, ":number_of_players_will_be_moved", 0),
         (try_begin),
           (eq, "$g_team_balance_next_round", 0),
           (assign, "$g_team_balance_next_round", 1),

           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
           #for only server itself-----------------------------------------------------------------------------------------------     
           (get_max_players, ":num_players"),                               
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
           (try_end),
           (call_script, "script_warn_player_about_auto_team_balance"),
         (try_end),
         #team balance check part finished
         ]),

      #checking for starting "death mode part 1"
      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0),
                 (eq, "$g_battle_death_mode_started", 0),
                 (store_mission_timer_a, ":seconds_past_till_round_started"),
                 (val_sub, ":seconds_past_till_round_started", "$g_round_start_time"),
                 (store_div, "$g_multiplayer_round_max_seconds_div_2", "$g_multiplayer_round_max_seconds", 2),
                 (ge, ":seconds_past_till_round_started", "$g_multiplayer_round_max_seconds_div_2")],
       [
         (call_script, "script_calculate_new_death_waiting_time_at_death_mod"),
         (assign, "$g_battle_death_mode_started", 1),
         ]),

      #checking during "death mode part 1" for entering "death mode part 2"
      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0),
                 (eq, "$g_battle_death_mode_started", 1),
                 (store_mission_timer_a, ":seconds_past_till_death_mode_part_1_started"),
                 (val_sub, ":seconds_past_till_death_mode_part_1_started", "$g_death_mode_part_1_start_time"),
                 (store_add, ":g_battle_waiting_seconds_plus_reduced_waiting_seconds", "$g_battle_waiting_seconds", "$g_reduced_waiting_seconds"),
                 (ge, ":seconds_past_till_death_mode_part_1_started", ":g_battle_waiting_seconds_plus_reduced_waiting_seconds"), #death mod start if anybody did not dies in "$g_battle_waiting_seconds" seconds
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (store_sub, ":g_multiplayer_round_max_seconds_sub_15", "$g_multiplayer_round_max_seconds", 15),
                 (lt, ":seconds_past_in_round", ":g_multiplayer_round_max_seconds_sub_15")], #death mod cannot start at last 15 seconds
       [
         (assign, "$g_battle_death_mode_started", 2),
         #for only server itself-----------------------------------------------------------------------------------------------
         (call_script, "script_start_death_mode"),
         #for only server itself-----------------------------------------------------------------------------------------------
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
           (player_is_active, ":player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_start_death_mode),
         (try_end),

         (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
         (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
         (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
         (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

         #death mode started make 4 item related to death mode visible.
         (store_random_in_range, "$g_random_entry_point", 0, 3),
         (val_add, "$g_random_entry_point", multi_death_mode_point),

         (entry_point_get_position, pos0, "$g_random_entry_point"),
         (position_set_z_to_ground_level, pos0),
         
         (position_move_x, pos0, 100), 
         (prop_instance_set_position, ":pole_1_id", pos0),

         (position_move_x, pos0, -200), 
         (prop_instance_set_position, ":pole_2_id", pos0),

         (prop_instance_get_position, pos0, ":pole_1_id"),
         (position_move_z, pos0, multi_headquarters_flag_initial_height),
         (prop_instance_set_position, ":flag_1_id", pos0),
         
         (prop_instance_get_position, pos0, ":pole_2_id"),
         (position_move_z, pos0, multi_headquarters_flag_initial_height),
         (prop_instance_set_position, ":flag_2_id", pos0),

         (start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
         ]),

      (3, 0, 0, [(multiplayer_is_server),  #this trigger is to reduce "$g_battle_waiting_seconds" at between last 66th and last 24th seconds 1 per 3 seconds, total 14 seconds.
                 (eq, "$g_round_ended", 0),                 
                 (eq, "$g_battle_death_mode_started", 1),
                 
                 (store_mission_timer_a, ":seconds_past_till_death_mode_part_1_started"),
                 (val_sub, ":seconds_past_till_death_mode_part_1_started", "$g_death_mode_part_1_start_time"),
                 (store_add, ":g_battle_waiting_seconds_plus_reduced_waiting_seconds", "$g_battle_waiting_seconds", "$g_reduced_waiting_seconds"),
                 (val_sub, ":g_battle_waiting_seconds_plus_reduced_waiting_seconds", 20), #in last 20 seconds to master of field below code effects
                 (ge, ":seconds_past_till_death_mode_part_1_started", ":g_battle_waiting_seconds_plus_reduced_waiting_seconds"),], #death mod start if anybody did not dies in "$g_battle_waiting_seconds" seconds            
        [
                 (assign, ":there_are_fighting_agents", 0),

                 (try_for_agents, ":agent_no_1"),
                   (eq, ":there_are_fighting_agents", 0),
                   (agent_is_human, ":agent_no_1"),
                   (agent_get_team, ":agent_no_1_team", ":agent_no_1"),
                   (agent_get_position, pos1, ":agent_no_1"),
                   (try_for_agents, ":agent_no_2"),
                     (eq, ":there_are_fighting_agents", 0),
                     (agent_is_human, ":agent_no_2"),
                     (neq, ":agent_no_1", ":agent_no_2"),

                     (agent_get_team, ":agent_no_2_team", ":agent_no_2"),

                     (neq, ":agent_no_1_team", ":agent_no_2_team"),
                 
                     (agent_get_position, pos2, ":agent_no_2"),

                     (get_sq_distance_between_positions_in_meters, ":sq_dist_in_meters", pos1, pos2),

                     (le, ":sq_dist_in_meters", multi_max_sq_dist_between_agents_to_longer_mof_time),

                     (assign, ":there_are_fighting_agents", 1),
                   (try_end),   
                 (try_end),

                 (try_begin),
                   (eq, ":there_are_fighting_agents", 1),
                   (val_add, "$g_reduced_waiting_seconds", 3),
                   #(display_message, "@{!}DEBUG : there are fighting agents"),
                 (try_end),
        ]),

      (3, 0, 0, [(multiplayer_is_server),  #this trigger is to reduce "$g_battle_waiting_seconds" at between last 66th and last 24th seconds 1 per 3 seconds, total 14 seconds.
                 (eq, "$g_round_ended", 0),                 
                 (eq, "$g_battle_death_mode_started", 1),
                 
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (store_sub, ":g_multiplayer_round_max_seconds_sub_60", "$g_multiplayer_round_max_seconds", 66),
                 (ge, ":seconds_past_in_round", ":g_multiplayer_round_max_seconds_sub_60"),
                 (store_sub, ":g_multiplayer_round_max_seconds_sub_20", "$g_multiplayer_round_max_seconds", 24),
                 (le, ":seconds_past_in_round", ":g_multiplayer_round_max_seconds_sub_20"),
                 ],
       [
         (val_add, "$g_reduced_waiting_seconds", 1),
         ]),

      # change interval, this saves a lot of server performance,
      (1, 0, 0, [(multiplayer_is_server),  
                 (eq, "$g_round_ended", 0),                 
                 (eq, "$g_battle_death_mode_started", 2)],
       [
         (set_fixed_point_multiplier, 100),
         (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
         (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
         (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
         (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

         (prop_instance_get_position, pos1, ":pole_1_id"),
         (prop_instance_get_position, pos2, ":pole_2_id"),
         (prop_instance_get_position, pos3, ":flag_1_id"),
         (prop_instance_get_position, pos4, ":flag_2_id"),

         (copy_position, pos7, pos1),
         (position_move_z, pos7, multi_headquarters_flag_initial_height),
         (copy_position, pos8, pos2),
         (position_move_z, pos8, multi_headquarters_flag_initial_height),

         (get_distance_between_positions, ":dist_1", pos1, pos3),
         (get_distance_between_positions, ":dist_2", pos2, pos4),

         (assign, ":there_are_agents_from_only_team_1_around_their_flag", 0),
         (assign, ":there_are_agents_from_only_team_2_around_their_flag", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_agent_id, ":agent_id", ":player_no"),
           (ge, ":agent_id", 0),
           (agent_is_human, ":agent_id"),
           (agent_is_alive, ":agent_id"),
           (agent_get_team, ":agent_team", ":agent_id"),
           (agent_get_position, pos0, ":agent_id"),

           (agent_get_horse, ":agent_horse", ":agent_id"),
           (eq, ":agent_horse", -1), #horseman cannot move flag
         
           (try_begin),
             (eq, ":agent_team", 0),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_1 agent in the flag_1 area, so flag_1 situation can be 1 or -2
                 (this_or_next|eq, ":there_are_agents_from_only_team_1_around_their_flag", 0),
                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", 1), #there are agents from only our team
               (else_try),                 
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos2),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_1 agent in the flag_2 area, so flag_2 situation can be -1 or -2
                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 0),
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -1), #there are agents from only rival team
               (else_try),
                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
           (else_try),
             (eq, ":agent_team", 1),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos2),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_2 agent in the flag 2 area, so flag_2 situation can be 1 or -2
                 (this_or_next|eq, ":there_are_agents_from_only_team_2_around_their_flag", 0),
                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", 1), #there are agents from only our team
               (else_try),                 
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_2 agent in the flag_1 area, so flag_1 situation can be -1 or -2
                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 0),
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -1), #there are agents from only rival team
               (else_try),
                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
           (try_end),
         (try_end),

         #controlling battle win by death mode conditions
         (try_begin),
           (ge, ":dist_1", multi_headquarters_flag_height_to_win),           
           (assign, "$g_winner_team", 0),

           (get_max_players, ":num_players"), 
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_draw_this_round", "$g_winner_team"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
           (try_end),

           (team_get_score, ":team_1_score", 0),
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_team_set_score", 0, ":team_1_score"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 0, ":team_1_score"),             
           (try_end),

           (store_mission_timer_a, "$g_round_finish_time"),
           (assign, "$g_round_ended", 1),
         (else_try),
           (ge, ":dist_2", multi_headquarters_flag_height_to_win),
           (assign, "$g_winner_team", 1),

           (get_max_players, ":num_players"), 
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_draw_this_round", "$g_winner_team"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
           (try_end),

           (team_get_score, ":team_2_score", 1),
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_team_set_score", 1, ":team_2_score"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 1, ":team_2_score"),             
           (try_end),

           (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, 0), #0 is winner team

           (store_mission_timer_a, "$g_round_finish_time"),
           (assign, "$g_round_ended", 1),
         (try_end),

         (try_begin),
           (eq, "$g_round_ended", 0),

           (position_get_z, ":flag_1_cur_z", pos3),       
           (prop_instance_is_animating, ":is_animating", ":flag_1_id"),         
           (try_begin), #if flag_1 is going down or up and there are agents from both teams
             (eq, ":there_are_agents_from_only_team_1_around_their_flag", -2), #if there are agents from both teams
             (eq, ":is_animating", 1),
             (prop_instance_stop_animating, ":flag_1_id"), #stop flag_1
           (else_try), #if flag_1 is going down
             (this_or_next|eq, ":there_are_agents_from_only_team_1_around_their_flag", 0), #if there is no one
             (eq, ":there_are_agents_from_only_team_1_around_their_flag", -1), #if there are agents from only team_2 (enemy of team_1)
             (prop_instance_get_animation_target_position, pos9, ":flag_1_id"),
             (position_get_z, ":flag_1_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_1 is stopping
             (gt, ":flag_1_animation_target_z", ":flag_1_cur_z"), #if flag_1 is going up         
             (get_distance_between_positions, ":time_1", pos3, pos7),
             (gt, ":time_1", 0),
             (val_mul, ":time_1", 16),
             (prop_instance_animate_to_position, ":flag_1_id", pos7, ":time_1"), #move flag_1 down
           (else_try), #if flag_1 is going down or stopping
             (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1), #if there is agents from only team_1 (current team)
             (prop_instance_get_animation_target_position, pos9, ":flag_1_id"),
             (position_get_z, ":flag_1_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_1 is stopping
             (lt, ":flag_1_animation_target_z", ":flag_1_cur_z"), #if flag_1 is going down
             (copy_position, pos5, pos1),
             (position_move_z, pos5, multi_headquarters_flag_height_to_win),
             (get_distance_between_positions, ":time_1", pos3, pos5),
             (gt, ":time_1", 0),
             (val_mul, ":time_1", 8),
             (prop_instance_animate_to_position, ":flag_1_id", pos5, ":time_1"), #move flag_1 up
           (try_end),

           (position_get_z, ":flag_2_cur_z", pos4),       
           (prop_instance_is_animating, ":is_animating", ":flag_2_id"),         
           (try_begin), #if flag is going down or up and there are agents from both teams
             (eq, ":there_are_agents_from_only_team_2_around_their_flag", -2), #if there are agents from both teams
             (eq, ":is_animating", 1),
             (prop_instance_stop_animating, ":flag_2_id"), #stop flag_2
           (else_try), #if flag_2 is going down
             (this_or_next|eq, ":there_are_agents_from_only_team_2_around_their_flag", 0), #if there is no one
             (eq, ":there_are_agents_from_only_team_2_around_their_flag", -1), #if there are agents from only team_1 (enemy of team_1)
             (prop_instance_get_animation_target_position, pos9, ":flag_2_id"),
             (position_get_z, ":flag_2_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_2 is stopping
             (gt, ":flag_2_animation_target_z", ":flag_2_cur_z"), #if flag_2 is going up         
             (get_distance_between_positions, ":time_2", pos4, pos8),
             (gt, ":time_2", 0),
             (val_mul, ":time_2", 16),
             (prop_instance_animate_to_position, ":flag_2_id", pos8, ":time_2"), #move flag_2 down
           (else_try), #if flag_2 is going down or stopping
             (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1), #if there is agents from only team_2 (current team)
             (prop_instance_get_animation_target_position, pos9, ":flag_2_id"),
             (position_get_z, ":flag_2_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_2 is stopping
             (lt, ":flag_2_animation_target_z", ":flag_2_cur_z"), #if flag_2 is going down
             (copy_position, pos6, pos2),
             (position_move_z, pos6, multi_headquarters_flag_height_to_win),
             (get_distance_between_positions, ":time_2", pos4, pos6),
             (gt, ":time_2", 0),
             (val_mul, ":time_2", 8),
             (prop_instance_animate_to_position, ":flag_2_id", pos6, ":time_2"), #move flag_2 up
           (try_end),
         (try_end),
         ]),
                
      (1, 0, 3, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 1),
                 (store_mission_timer_a, ":seconds_past_till_round_ended"),
                 (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
                 (ge, ":seconds_past_till_round_ended", "$g_multiplayer_respawn_period")],
       [
         #auto team balance control at the end of round
         (call_script, "script_multiplayer_get_balance_dif", 0, 0),
         (assign, ":number_of_players_will_be_moved", reg0),
         #number of players will be moved calculated. (it is 0 if no need to make team balance)
         (try_begin),
           (neq, ":number_of_players_will_be_moved", 0),
           (try_begin),
             (le, ":number_of_players_will_be_moved", 0),
             (val_mul, ":number_of_players_will_be_moved", -1),
             (assign, ":team_with_more_players", 1),
             (assign, ":team_with_less_players", 0),
           (else_try),
             (assign, ":team_with_more_players", 0),
             (assign, ":team_with_less_players", 1),
           (try_end),
           (try_begin),
             #(eq, "$g_team_balance_next_round", 1), #control if at pre round players are warned about team change.

             (try_for_range, ":unused", 0, ":number_of_players_will_be_moved"), 
               (assign, ":max_player_join_time", 0),
               (assign, ":latest_joined_player_no", -1),
               (get_max_players, ":num_players"),                               
               (try_for_range, ":player_no", 0, ":num_players"),
                 (player_is_active, ":player_no"),
                 (player_get_team_no, ":player_team", ":player_no"),
                 (eq, ":player_team", ":team_with_more_players"),
                 (player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
                 (try_begin),
                   (gt, ":player_join_time", ":max_player_join_time"),
                   (assign, ":max_player_join_time", ":player_join_time"),
                   (assign, ":latest_joined_player_no", ":player_no"),
                 (try_end),
               (try_end),
               (try_begin),
                 (ge, ":latest_joined_player_no", 0),
                 (try_begin),
                   #if player is living add +1 to his kill count because he will get -1 because of team change while living.
                   (player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"), 
                   (ge, ":latest_joined_agent_id", 0),
                   (agent_is_alive, ":latest_joined_agent_id"),

                   (player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
                   (val_add, ":player_kill_count", 1),
                   (player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),

                   (player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
                   (val_sub, ":player_death_count", 1),
                   (player_set_death_count, ":latest_joined_player_no", ":player_death_count"),

                   (player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
                   (val_add, ":player_score", 1),
                   (player_set_score, ":latest_joined_player_no", ":player_score"),

                   (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                     (player_is_active, ":player_no"),
                     (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
                   (try_end),         

                   (player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
                   (player_get_gold, ":player_gold", ":latest_joined_player_no"),
                   (val_add, ":player_gold", ":old_items_value"),
                   (player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
                 (end_try),

				 (call_script, "script_mp_set_player_team_no", ":latest_joined_player_no", ":team_with_less_players", 0),
                 (multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
               (try_end),
             (try_end),

             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), 

             #no need to send also server here
             (multiplayer_get_my_player, ":my_player_no"),
             (get_max_players, ":num_players"),                               
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
             (try_end),
             (assign, "$g_team_balance_next_round", 0),
           (try_end),
         (try_end),           
         #team balance check part finished
         (assign, "$g_team_balance_next_round", 0),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_agent_id, ":player_agent", ":player_no"),
           (ge, ":player_agent", 0),
           (agent_is_alive, ":player_agent"),
           (player_save_picked_up_items_for_next_spawn, ":player_no"),
           (player_get_value_of_original_items, ":old_items_value", ":player_no"),
           (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, ":old_items_value"),
         (try_end),

         #money management
         (assign, ":per_round_gold_addition", multi_battle_round_team_money_add),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
		   (player_slot_eq, ":player_no", slot_player_spawned_this_round, 1),
           (player_get_gold, ":player_gold", ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"),

           (try_begin),
             (this_or_next|eq, ":player_team", 0),
             (eq, ":player_team", 1),
             (val_add, ":player_gold", ":per_round_gold_addition"), 
           (try_end),

           #(below lines added new at 25.11.09 after Armagan decided new money system)
           (try_begin),
             (player_get_slot, ":old_items_value", ":player_no", slot_player_last_rounds_used_item_earnings),
             (store_add, ":player_total_potential_gold", ":player_gold", ":old_items_value"),
             (store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
             (lt, ":player_total_potential_gold", ":minimum_gold"),
             (store_sub, ":additional_gold", ":minimum_gold", ":player_total_potential_gold"),
             (val_add, ":player_gold", ":additional_gold"),
           (try_end),
           #new money system addition end
         
           (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
         (try_end),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
         (try_end),

         #initialize my team at start of round (it will be assigned again at next round's first death)
         (assign, "$my_team_at_start_of_round", -1),

         #clear scene and end round
         (multiplayer_clear_scene),

         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),

         (try_begin),
           (eq, "$g_battle_death_mode_started", 2),
           (call_script, "script_move_death_mode_flags_down"),
         (try_end),

         (assign, "$g_battle_death_mode_started", 0),
         (assign, "$g_reduced_waiting_seconds", 0),
         
         #initialize moveable object positions
         (call_script, "script_multiplayer_close_gate_if_it_is_open"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
                  
         (assign, "$g_round_ended", 0), 

         (assign, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1"), 
         (assign, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2"), 

         (store_mission_timer_a, "$g_round_start_time"),
         (call_script, "script_initialize_all_scene_prop_slots"),

         #initialize round start times for clients
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, -9999), #this will also initialize moveable object slots.
         (try_end),         
       ]),

      (0, 0, 0, [], #if there is nobody in any teams do not reduce round time.
       [
         (store_mission_timer_a, ":seconds_past_since_round_started"),
         (val_sub, ":seconds_past_since_round_started", "$g_round_start_time"),
         (le, ":seconds_past_since_round_started", 3),

         (assign, ":human_agents_spawned_at_team_1", "$g_multiplayer_num_bots_team_1"),
         (assign, ":human_agents_spawned_at_team_2", "$g_multiplayer_num_bots_team_2"),
         
         (get_max_players, ":end_cond"),
         (try_for_range, ":player_no", 0, ":end_cond"),
           (player_is_active, ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"), 
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":human_agents_spawned_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":human_agents_spawned_at_team_2", 1),
           (try_end),
           
           (gt, ":human_agents_spawned_at_team_1", 0),
           (gt, ":human_agents_spawned_at_team_2", 0),
           (assign, ":end_cond", 0),
         (try_end),

         (try_begin),
           (this_or_next|eq, ":human_agents_spawned_at_team_1", 0),
           (eq, ":human_agents_spawned_at_team_2", 0),

           (store_mission_timer_a, "$g_round_start_time"),
         (try_end),
       ]),
      
      (1, 0, 0, [(multiplayer_is_server),
                 ],
       [
         (store_add, ":total_bots", "$g_multiplayer_num_bots_team_1", "$g_multiplayer_num_bots_team_2"),
         (store_mission_timer_a, ":round_time"),
         (val_sub, ":round_time", "$g_round_start_time"),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
           (try_begin),
             (player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),

             (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
             (lt, ":player_team", multi_team_spectator),

             (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
             (ge, ":player_troop", 0),

             (assign, ":spawn_new", 0), 
             (assign, ":num_active_players_in_team_0", 0),
             (assign, ":num_active_players_in_team_1", 0),
             (try_begin),
               (assign, ":num_active_players", 0),
               (get_max_players, ":num_players"),
               (try_for_range, ":player_no_2", 0, ":num_players"),
                 (player_is_active, ":player_no_2"),
                 (val_add, ":num_active_players", 1),
                 (player_get_team_no, ":player_team_2", ":player_no_2"),
                 (try_begin),
                   (eq, ":player_team_2", 0),
                   (val_add, ":num_active_players_in_team_0", 1),
                 (else_try),
                   (eq, ":player_team_2", 1),
                   (val_add, ":num_active_players_in_team_1", 1),
                 (try_end),
               (try_end),

               (store_mul, ":multipication_of_num_active_players_in_teams", ":num_active_players_in_team_0", ":num_active_players_in_team_1"),

               (this_or_next|lt, ":round_time", multiplayer_new_agents_finish_spawning_time),
               (this_or_next|le, ":num_active_players", 2),
               (eq, ":multipication_of_num_active_players_in_teams", 0),
         
               (eq, "$g_round_ended", 0),
               (assign, ":spawn_new", 1),
             (try_end),
             (eq, ":spawn_new", 1),
             (try_begin),
               (eq, ":player_team", 0),
               (assign, ":entry_no", multi_initial_spawn_point_team_1),
             (else_try),
               (eq, ":player_team", 1),
               (assign, ":entry_no", multi_initial_spawn_point_team_2),
             (try_end),
             (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),
             (player_spawn_new_agent, ":player_no", ":entry_no"),
             (player_set_slot, ":player_no", slot_player_spawned_this_round, 1),
           (else_try), #spawning as a bot (if option ($g_multiplayer_player_respawn_as_bot) is 1)
             (eq, "$g_multiplayer_player_respawn_as_bot", 1),
             (gt,":total_bots",0),
             
             (player_get_agent_id, ":player_agent", ":player_no"),
             (ge, ":player_agent", 0),
             (neg|agent_is_alive, ":player_agent"),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
             (gt, ":elapsed_time", "$g_multiplayer_respawn_period"), # Only respawn as bot after respawntime

             (call_script, "script_find_most_suitable_bot_to_control", ":player_no"),
             (assign,":bot_agent",reg0),
             (gt,":bot_agent",-1), # We found a bot to control lets control him.
             
             (player_control_agent, ":player_no", ":bot_agent"),

             (player_get_slot, ":num_spawns", ":player_no", slot_player_spawned_this_round),
             (val_add, ":num_spawns", 1),
             (player_set_slot, ":player_no", slot_player_spawned_this_round, ":num_spawns"),
           (try_end),
         (try_end),
         ]),

      multiplayer_server_spawn_bots, 
      multiplayer_server_manage_bots, 

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,

      (ti_battle_window_opened, 0, 0, [], [
        (start_presentation, "prsnt_multiplayer_round_time_counter"),
        (start_presentation, "prsnt_multiplayer_team_score_display"),
        (try_begin),
          (eq, "$g_battle_death_mode_started", 2),
          (start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
        (try_end),
        ]),

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),
  
  (
    "multiplayer_cbt",mtf_battle_mode,-1, #captain_battle mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,

      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_captain_battle),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
         (assign, "$g_round_ended", 0),
         (assign, "$g_battle_death_mode_started", 0),
         (assign, "$g_reduced_waiting_seconds", 0),

         (try_begin),
           (multiplayer_is_server),
           (assign, "$server_mission_timer_while_player_joined", 0),
           (assign, "$g_round_start_time", 0),
         (try_end),
         (assign, "$my_team_at_start_of_round", -1),

         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (call_script, "script_determine_team_flags", 0),
         (call_script, "script_determine_team_flags", 1),
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)

         (try_begin),
           (multiplayer_is_server),

           (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         
           (entry_point_get_position, pos0, multi_death_mode_point),
           (position_set_z_to_ground_level, pos0),
           (position_move_z, pos0, -2000),

           (position_move_x, pos0, 100), 
           (set_spawn_position, pos0),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),

           (position_move_x, pos0, -200), 
           (set_spawn_position, pos0),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),

           (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
           (prop_instance_get_position, pos0, ":pole_1_id"),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
           (position_move_z, pos0, multi_headquarters_flag_initial_height),
           (prop_instance_set_position, reg0, pos0),
         
           (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
           (prop_instance_get_position, pos0, ":pole_2_id"),
           (spawn_scene_prop, "$team_2_flag_scene_prop", 0),
           (position_move_z, pos0, multi_headquarters_flag_initial_height),
           (prop_instance_set_position, reg0, pos0),
         (try_end),

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
		 
		 (set_cheer_at_no_enemy, 0),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         
         (try_begin), #if my initial team still not initialized, find and assign its value.
           (neg|multiplayer_is_dedicated_server),
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (eq, ":my_agent_id", ":agent_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),
         
         (call_script, "script_calculate_new_death_waiting_time_at_death_mod"),
 
         (try_begin),
           (neg|multiplayer_is_server),
           (eq, "$g_round_ended", 1),
           (assign, "$g_round_ended", 0),

           #initialize scene object slots at start of new round at clients.
           (call_script, "script_initialize_all_scene_prop_slots"),

           #these lines are done in only clients at start of each new round.
           (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
           (call_script, "script_initialize_objects_clients"),
           #end of lines
           (try_begin),
             (eq, "$g_team_balance_next_round", 1),
             (assign, "$g_team_balance_next_round", 0),
           (try_end),
         (try_end),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (store_trigger_param_2, ":killer_agent_no"),

         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),

         (try_begin), #if my initial team still not initialized, find and assign its value.
           (neg|multiplayer_is_dedicated_server),
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),         
         
         (try_begin), #count players and if round ended understand this.
           (agent_is_human, ":dead_agent_no"),
           (assign, ":team1_living_players", 0),
           (assign, ":team2_living_players", 0),
           (assign,":continue_loop",1),
           (try_for_agents, ":cur_agent"),
             (eq,":continue_loop",1),
             (agent_is_human, ":cur_agent"),         
             (agent_is_alive, ":cur_agent"),
             (agent_get_team, ":cur_agent_team", ":cur_agent"),
             (try_begin),
               (eq, ":cur_agent_team", 0),
               (val_add, ":team1_living_players", 1),
             (else_try),
               (eq, ":cur_agent_team", 1),
               (val_add, ":team2_living_players", 1),
             (try_end),
             # Break loop.
             (gt, ":team1_living_players", 0),
             (gt, ":team2_living_players", 0),
             (assign,":continue_loop",0),
           (try_end),  
           
           (try_begin),         
             (eq, "$g_round_ended", 0),
             (this_or_next|eq, ":team1_living_players", 0),
             (eq, ":team2_living_players", 0),
             (assign, "$g_winner_team", -1),
             (assign, reg0, "$g_multiplayer_respawn_period"),
             (try_begin),
               (eq, ":team1_living_players", 0),
               (try_begin),
                 (neq, ":team2_living_players", 0),
                 (team_get_score, ":team_2_score", 1),
                 (val_add, ":team_2_score", 1),
                 (team_set_score, 1, ":team_2_score"),
                 (assign, "$g_winner_team", 1),
               (try_end),
             (else_try),
               (neq, ":team1_living_players", 0),
               (team_get_score, ":team_1_score", 0),
               (val_add, ":team_1_score", 1),
               (team_set_score, 0, ":team_1_score"),
               (assign, "$g_winner_team", 0),
             (try_end),
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, "$g_winner_team"),

             (store_mission_timer_a, "$g_round_finish_time"),
             (assign, "$g_round_ended", 1),
           (try_end),
         (try_end),

         (try_begin),
           (multiplayer_is_server),
           (agent_is_human, ":dead_agent_no"),
           (neg|agent_is_non_player, ":dead_agent_no"),

           (ge, ":dead_agent_no", 0),
           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
           (ge, ":dead_agent_player_id", 0),

           (set_fixed_point_multiplier, 100),

           (agent_get_position, pos0, ":dead_agent_no"),

           (position_get_x, ":x_coor", pos0),
           (position_get_y, ":y_coor", pos0),
           (position_get_z, ":z_coor", pos0),

           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_x, ":x_coor"),
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_y, ":y_coor"),
           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_z, ":z_coor"),
         (try_end),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),
		 
	  (ti_on_player_exit, 0, 0, [],
		[
		 # force kill all squad agents of the existing player
		 (store_trigger_param_1, ":exiting_player_no"),
		 (call_script, "script_cf_multiplayer_event_team_change", ":exiting_player_no"),
		 ]),
		 
		 # one time execute
		(0, 0, ti_once, [],
		[
			(try_begin),
				(assign, "$g_multiplayer_squad_size_calc", "$g_multiplayer_squad_size"),
			
				(neg|multiplayer_is_server),
				# clear squad info
				(multiplayer_get_my_player, ":my_player_no"),
				(call_script, "script_mp_clear_squad_info", ":my_player_no"),
			(try_end),
		]),

      (1, 0, 0, [(multiplayer_is_server), 
                 (eq, "$g_round_ended", 0),
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (ge, ":seconds_past_in_round", "$g_multiplayer_round_max_seconds"),

                 (assign, ":overtime_needed", 0), #checking for if overtime is needed. Overtime happens when lower heighted flag is going up
                 (try_begin),
                   (eq, "$g_battle_death_mode_started", 2), #if death mod is currently open
                    
                   (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
                   (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
                   (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
                   (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

                   (prop_instance_get_position, pos1, ":pole_1_id"),
                   (prop_instance_get_position, pos2, ":pole_2_id"),
                   (prop_instance_get_position, pos3, ":flag_1_id"),
                   (prop_instance_get_position, pos4, ":flag_2_id"),

                   (get_distance_between_positions, ":height_of_flag_1", pos1, pos3),
                   (get_distance_between_positions, ":height_of_flag_2", pos2, pos4),
                   (store_add, ":height_of_flag_1_plus", ":height_of_flag_1", min_allowed_flag_height_difference_to_make_score),
                   (store_add, ":height_of_flag_2_plus", ":height_of_flag_2", min_allowed_flag_height_difference_to_make_score),

                   (try_begin),
                     (le, ":height_of_flag_1", ":height_of_flag_2_plus"),
                     (prop_instance_is_animating, ":is_animating", ":flag_1_id"),
                     (eq, ":is_animating", 1),
                     (prop_instance_get_animation_target_position, pos5, ":flag_1_id"),
                     (position_get_z, ":flag_2_animation_target_z", pos5),
                     (position_get_z, ":flag_1_cur_z", pos3),
                     (ge, ":flag_2_animation_target_z", ":flag_1_cur_z"),
                     (assign, ":overtime_needed", 1),
                   (try_end),
                   
                   (try_begin),
                     (le, ":height_of_flag_2", ":height_of_flag_1_plus"),
                     (prop_instance_is_animating, ":is_animating", ":flag_2_id"),
                     (eq, ":is_animating", 1),
                     (prop_instance_get_animation_target_position, pos5, ":flag_2_id"),
                     (position_get_z, ":flag_2_animation_target_z", pos5),
                     (position_get_z, ":flag_2_cur_z", pos4),
                     (ge, ":flag_2_animation_target_z", ":flag_2_cur_z"),
                     (assign, ":overtime_needed", 1),
                   (try_end),
                 (try_end),
                 (eq, ":overtime_needed", 0),
                 ],
       [ #round time is up
         (store_mission_timer_a, "$g_round_finish_time"),                          
         (assign, "$g_round_ended", 1),
         (assign, "$g_winner_team", -1),
         
         (try_begin), #checking for winning by death mod
           (eq, "$g_battle_death_mode_started", 2), #if death mod is currently open

           (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
           (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
           (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
           (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

           (prop_instance_get_position, pos1, ":pole_1_id"),
           (prop_instance_get_position, pos2, ":pole_2_id"),
           (prop_instance_get_position, pos3, ":flag_1_id"),
           (prop_instance_get_position, pos4, ":flag_2_id"),

           (get_distance_between_positions, ":height_of_flag_1", pos1, pos3),
           (get_distance_between_positions, ":height_of_flag_2", pos2, pos4),

           (try_begin),
             (ge, ":height_of_flag_1", ":height_of_flag_2"), #if flag_1 is higher than flag_2
             (store_sub, ":difference_of_heights", ":height_of_flag_1", ":height_of_flag_2"), 
             (ge, ":difference_of_heights", min_allowed_flag_height_difference_to_make_score), #if difference between flag heights is greater than 
             (assign, "$g_winner_team", 0),                                                    #"min_allowed_flag_height_difference_to_make_score" const value
           (else_try), #if flag_2 is higher than flag_1
             (store_sub, ":difference_of_heights", ":height_of_flag_2", ":height_of_flag_1"),
             (ge, ":difference_of_heights", min_allowed_flag_height_difference_to_make_score), #if difference between flag heights is greater than 
             (assign, "$g_winner_team", 1),                                                    #"min_allowed_flag_height_difference_to_make_score" const value
           (try_end),
         (try_end),
    
         (multiplayer_get_my_player, ":my_player_no"), #send all players draw information of round.
         #for only server itself-----------------------------------------------------------------------------------------------
         (call_script, "script_draw_this_round", "$g_winner_team"),
         #for only server itself-----------------------------------------------------------------------------------------------
         (get_max_players, ":num_players"), 
         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
           (player_is_active, ":player_no"),
           (neq, ":player_no", ":my_player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
         (try_end),
        ]),          

      (10, 0, 0, [(multiplayer_is_server)],
       [
         #auto team balance control during the round
	     (call_script, "script_multiplayer_get_balance_dif", 0, 0),
         (assign, ":number_of_players_will_be_moved", reg0),
         (neq, ":number_of_players_will_be_moved", 0),
         (try_begin),
           (eq, "$g_team_balance_next_round", 0),
           (assign, "$g_team_balance_next_round", 1),

           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
           #for only server itself-----------------------------------------------------------------------------------------------     
           (get_max_players, ":num_players"),                               
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
           (try_end),
           (call_script, "script_warn_player_about_auto_team_balance"),
         (try_end),
         #team balance check part finished
         ]),

      #checking for starting "death mode part 1"
      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0),
                 (eq, "$g_battle_death_mode_started", 0),
                 (store_mission_timer_a, ":seconds_past_till_round_started"),
                 (val_sub, ":seconds_past_till_round_started", "$g_round_start_time"),
                 (store_div, "$g_multiplayer_round_max_seconds_div_2", "$g_multiplayer_round_max_seconds", 2),
                 (ge, ":seconds_past_till_round_started", "$g_multiplayer_round_max_seconds_div_2")],
       [
         (call_script, "script_calculate_new_death_waiting_time_at_death_mod"),
         (assign, "$g_battle_death_mode_started", 1),
         ]),

      #checking during "death mode part 1" for entering "death mode part 2"
      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0),
                 (eq, "$g_battle_death_mode_started", 1),
                 (store_mission_timer_a, ":seconds_past_till_death_mode_part_1_started"),
                 (val_sub, ":seconds_past_till_death_mode_part_1_started", "$g_death_mode_part_1_start_time"),
                 (store_add, ":g_battle_waiting_seconds_plus_reduced_waiting_seconds", "$g_battle_waiting_seconds", "$g_reduced_waiting_seconds"),
                 (ge, ":seconds_past_till_death_mode_part_1_started", ":g_battle_waiting_seconds_plus_reduced_waiting_seconds"), #death mod start if anybody did not dies in "$g_battle_waiting_seconds" seconds
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (store_sub, ":g_multiplayer_round_max_seconds_sub_15", "$g_multiplayer_round_max_seconds", 15),
                 (lt, ":seconds_past_in_round", ":g_multiplayer_round_max_seconds_sub_15")], #death mod cannot start at last 15 seconds
       [
         (assign, "$g_battle_death_mode_started", 2),
         #for only server itself-----------------------------------------------------------------------------------------------
         (call_script, "script_start_death_mode"),
         #for only server itself-----------------------------------------------------------------------------------------------
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
           (player_is_active, ":player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_start_death_mode),
         (try_end),

         (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
         (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
         (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
         (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

         #death mode started make 4 item related to death mode visible.
         (store_random_in_range, "$g_random_entry_point", 0, 3),
         (val_add, "$g_random_entry_point", multi_death_mode_point),

         (entry_point_get_position, pos0, "$g_random_entry_point"),
         (position_set_z_to_ground_level, pos0),
         
         (position_move_x, pos0, 100), 
         (prop_instance_set_position, ":pole_1_id", pos0),

         (position_move_x, pos0, -200), 
         (prop_instance_set_position, ":pole_2_id", pos0),

         (prop_instance_get_position, pos0, ":pole_1_id"),
         (position_move_z, pos0, multi_headquarters_flag_initial_height),
         (prop_instance_set_position, ":flag_1_id", pos0),
         
         (prop_instance_get_position, pos0, ":pole_2_id"),
         (position_move_z, pos0, multi_headquarters_flag_initial_height),
         (prop_instance_set_position, ":flag_2_id", pos0),

         (start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
         ]),

      (3, 0, 0, [(multiplayer_is_server),  #this trigger is to reduce "$g_battle_waiting_seconds" at between last 66th and last 24th seconds 1 per 3 seconds, total 14 seconds.
                 (eq, "$g_round_ended", 0),                 
                 (eq, "$g_battle_death_mode_started", 1),
                 
                 (store_mission_timer_a, ":seconds_past_till_death_mode_part_1_started"),
                 (val_sub, ":seconds_past_till_death_mode_part_1_started", "$g_death_mode_part_1_start_time"),
                 (store_add, ":g_battle_waiting_seconds_plus_reduced_waiting_seconds", "$g_battle_waiting_seconds", "$g_reduced_waiting_seconds"),
                 (val_sub, ":g_battle_waiting_seconds_plus_reduced_waiting_seconds", 20), #in last 20 seconds to master of field below code effects
                 (ge, ":seconds_past_till_death_mode_part_1_started", ":g_battle_waiting_seconds_plus_reduced_waiting_seconds"),], #death mod start if anybody did not dies in "$g_battle_waiting_seconds" seconds            
        [
                 (assign, ":there_are_fighting_agents", 0),

                 (try_for_agents, ":agent_no_1"),
                   (eq, ":there_are_fighting_agents", 0),
                   (agent_is_human, ":agent_no_1"),
                   (agent_get_team, ":agent_no_1_team", ":agent_no_1"),
                   (agent_get_position, pos1, ":agent_no_1"),
                   (try_for_agents, ":agent_no_2"),
                     (eq, ":there_are_fighting_agents", 0),
                     (agent_is_human, ":agent_no_2"),
                     (neq, ":agent_no_1", ":agent_no_2"),

                     (agent_get_team, ":agent_no_2_team", ":agent_no_2"),

                     (neq, ":agent_no_1_team", ":agent_no_2_team"),
                 
                     (agent_get_position, pos2, ":agent_no_2"),

                     (get_sq_distance_between_positions_in_meters, ":sq_dist_in_meters", pos1, pos2),

                     (le, ":sq_dist_in_meters", multi_max_sq_dist_between_agents_to_longer_mof_time),

                     (assign, ":there_are_fighting_agents", 1),
                   (try_end),   
                 (try_end),

                 (try_begin),
                   (eq, ":there_are_fighting_agents", 1),
                   (val_add, "$g_reduced_waiting_seconds", 3),
                   #(display_message, "@{!}DEBUG : there are fighting agents"),
                 (try_end),
        ]),

      (3, 0, 0, [(multiplayer_is_server),  #this trigger is to reduce "$g_battle_waiting_seconds" at between last 66th and last 24th seconds 1 per 3 seconds, total 14 seconds.
                 (eq, "$g_round_ended", 0),                 
                 (eq, "$g_battle_death_mode_started", 1),
                 
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (store_sub, ":g_multiplayer_round_max_seconds_sub_60", "$g_multiplayer_round_max_seconds", 66),
                 (ge, ":seconds_past_in_round", ":g_multiplayer_round_max_seconds_sub_60"),
                 (store_sub, ":g_multiplayer_round_max_seconds_sub_20", "$g_multiplayer_round_max_seconds", 24),
                 (le, ":seconds_past_in_round", ":g_multiplayer_round_max_seconds_sub_20"),
                 ],
       [
         (val_add, "$g_reduced_waiting_seconds", 1),
         ]),

      # change interval, this saves a lot of server performance,
      (1, 0, 0, [(multiplayer_is_server),  
                 (eq, "$g_round_ended", 0),                 
                 (eq, "$g_battle_death_mode_started", 2)],
       [
         (set_fixed_point_multiplier, 100),
         (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
         (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
         (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
         (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),

         (prop_instance_get_position, pos1, ":pole_1_id"),
         (prop_instance_get_position, pos2, ":pole_2_id"),
         (prop_instance_get_position, pos3, ":flag_1_id"),
         (prop_instance_get_position, pos4, ":flag_2_id"),

         (copy_position, pos7, pos1),
         (position_move_z, pos7, multi_headquarters_flag_initial_height),
         (copy_position, pos8, pos2),
         (position_move_z, pos8, multi_headquarters_flag_initial_height),

         (get_distance_between_positions, ":dist_1", pos1, pos3),
         (get_distance_between_positions, ":dist_2", pos2, pos4),

         (assign, ":there_are_agents_from_only_team_1_around_their_flag", 0),
         (assign, ":there_are_agents_from_only_team_2_around_their_flag", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_agent_id, ":agent_id", ":player_no"),
           (ge, ":agent_id", 0),
           (agent_is_human, ":agent_id"),
           (agent_is_alive, ":agent_id"),
           (agent_get_team, ":agent_team", ":agent_id"),
           (agent_get_position, pos0, ":agent_id"),

           (agent_get_horse, ":agent_horse", ":agent_id"),
           (eq, ":agent_horse", -1), #horseman cannot move flag
         
           (try_begin),
             (eq, ":agent_team", 0),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_1 agent in the flag_1 area, so flag_1 situation can be 1 or -2
                 (this_or_next|eq, ":there_are_agents_from_only_team_1_around_their_flag", 0),
                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", 1), #there are agents from only our team
               (else_try),                 
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos2),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_1 agent in the flag_2 area, so flag_2 situation can be -1 or -2
                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 0),
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -1), #there are agents from only rival team
               (else_try),
                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
           (else_try),
             (eq, ":agent_team", 1),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos2),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_2 agent in the flag 2 area, so flag_2 situation can be 1 or -2
                 (this_or_next|eq, ":there_are_agents_from_only_team_2_around_their_flag", 0),
                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", 1), #there are agents from only our team
               (else_try),                 
                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
             (try_begin),
               (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
               (try_begin), #we found a team_2 agent in the flag_1 area, so flag_1 situation can be -1 or -2
                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 0),
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -1), #there are agents from only rival team
               (else_try),
                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1),
                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -2), #there are agents from both teams
               (try_end),
             (try_end),
           (try_end),
         (try_end),

         #controlling battle win by death mode conditions
         (try_begin),
           (ge, ":dist_1", multi_headquarters_flag_height_to_win),           
           (assign, "$g_winner_team", 0),

           (get_max_players, ":num_players"), 
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_draw_this_round", "$g_winner_team"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
           (try_end),

           (team_get_score, ":team_1_score", 0),
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_team_set_score", 0, ":team_1_score"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 0, ":team_1_score"),             
           (try_end),

           (store_mission_timer_a, "$g_round_finish_time"),
           (assign, "$g_round_ended", 1),
         (else_try),
           (ge, ":dist_2", multi_headquarters_flag_height_to_win),
           (assign, "$g_winner_team", 1),

           (get_max_players, ":num_players"), 
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_draw_this_round", "$g_winner_team"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
           (try_end),

           (team_get_score, ":team_2_score", 1),
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_team_set_score", 1, ":team_2_score"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 1, ":team_2_score"),             
           (try_end),

           (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, 0), #0 is winner team

           (store_mission_timer_a, "$g_round_finish_time"),
           (assign, "$g_round_ended", 1),
         (try_end),

         (try_begin),
           (eq, "$g_round_ended", 0),

           (position_get_z, ":flag_1_cur_z", pos3),       
           (prop_instance_is_animating, ":is_animating", ":flag_1_id"),         
           (try_begin), #if flag_1 is going down or up and there are agents from both teams
             (eq, ":there_are_agents_from_only_team_1_around_their_flag", -2), #if there are agents from both teams
             (eq, ":is_animating", 1),
             (prop_instance_stop_animating, ":flag_1_id"), #stop flag_1
           (else_try), #if flag_1 is going down
             (this_or_next|eq, ":there_are_agents_from_only_team_1_around_their_flag", 0), #if there is no one
             (eq, ":there_are_agents_from_only_team_1_around_their_flag", -1), #if there are agents from only team_2 (enemy of team_1)
             (prop_instance_get_animation_target_position, pos9, ":flag_1_id"),
             (position_get_z, ":flag_1_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_1 is stopping
             (gt, ":flag_1_animation_target_z", ":flag_1_cur_z"), #if flag_1 is going up         
             (get_distance_between_positions, ":time_1", pos3, pos7),
             (gt, ":time_1", 0),
             (val_mul, ":time_1", 16),
             (prop_instance_animate_to_position, ":flag_1_id", pos7, ":time_1"), #move flag_1 down
           (else_try), #if flag_1 is going down or stopping
             (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1), #if there is agents from only team_1 (current team)
             (prop_instance_get_animation_target_position, pos9, ":flag_1_id"),
             (position_get_z, ":flag_1_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_1 is stopping
             (lt, ":flag_1_animation_target_z", ":flag_1_cur_z"), #if flag_1 is going down
             (copy_position, pos5, pos1),
             (position_move_z, pos5, multi_headquarters_flag_height_to_win),
             (get_distance_between_positions, ":time_1", pos3, pos5),
             (gt, ":time_1", 0),
             (val_mul, ":time_1", 8),
             (prop_instance_animate_to_position, ":flag_1_id", pos5, ":time_1"), #move flag_1 up
           (try_end),

           (position_get_z, ":flag_2_cur_z", pos4),       
           (prop_instance_is_animating, ":is_animating", ":flag_2_id"),         
           (try_begin), #if flag is going down or up and there are agents from both teams
             (eq, ":there_are_agents_from_only_team_2_around_their_flag", -2), #if there are agents from both teams
             (eq, ":is_animating", 1),
             (prop_instance_stop_animating, ":flag_2_id"), #stop flag_2
           (else_try), #if flag_2 is going down
             (this_or_next|eq, ":there_are_agents_from_only_team_2_around_their_flag", 0), #if there is no one
             (eq, ":there_are_agents_from_only_team_2_around_their_flag", -1), #if there are agents from only team_1 (enemy of team_1)
             (prop_instance_get_animation_target_position, pos9, ":flag_2_id"),
             (position_get_z, ":flag_2_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_2 is stopping
             (gt, ":flag_2_animation_target_z", ":flag_2_cur_z"), #if flag_2 is going up         
             (get_distance_between_positions, ":time_2", pos4, pos8),
             (gt, ":time_2", 0),
             (val_mul, ":time_2", 16),
             (prop_instance_animate_to_position, ":flag_2_id", pos8, ":time_2"), #move flag_2 down
           (else_try), #if flag_2 is going down or stopping
             (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1), #if there is agents from only team_2 (current team)
             (prop_instance_get_animation_target_position, pos9, ":flag_2_id"),
             (position_get_z, ":flag_2_animation_target_z", pos9),
             (this_or_next|eq, ":is_animating", 0), #if flag_2 is stopping
             (lt, ":flag_2_animation_target_z", ":flag_2_cur_z"), #if flag_2 is going down
             (copy_position, pos6, pos2),
             (position_move_z, pos6, multi_headquarters_flag_height_to_win),
             (get_distance_between_positions, ":time_2", pos4, pos6),
             (gt, ":time_2", 0),
             (val_mul, ":time_2", 8),
             (prop_instance_animate_to_position, ":flag_2_id", pos6, ":time_2"), #move flag_2 up
           (try_end),
         (try_end),
         ]),
                
      (1, 0, 3, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 1),
                 (store_mission_timer_a, ":seconds_past_till_round_ended"),
                 (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
                 (ge, ":seconds_past_till_round_ended", "$g_multiplayer_respawn_period")],
       [
         #auto team balance control at the end of round
         (call_script, "script_multiplayer_get_balance_dif", 0, 0),
         (assign, ":number_of_players_will_be_moved", reg0),
         #number of players will be moved calculated. (it is 0 if no need to make team balance)
         (try_begin),
           (neq, ":number_of_players_will_be_moved", 0),
           (try_begin),
             (le, ":number_of_players_will_be_moved", 0),
             (val_mul, ":number_of_players_will_be_moved", -1),
             (assign, ":team_with_more_players", 1),
             (assign, ":team_with_less_players", 0),
           (else_try),
             (assign, ":team_with_more_players", 0),
             (assign, ":team_with_less_players", 1),
           (try_end),
           (try_begin),
             #(eq, "$g_team_balance_next_round", 1), #control if at pre round players are warned about team change.

             (try_for_range, ":unused", 0, ":number_of_players_will_be_moved"), 
               (assign, ":max_player_join_time", 0),
               (assign, ":latest_joined_player_no", -1),
               (get_max_players, ":num_players"),                               
               (try_for_range, ":player_no", 0, ":num_players"),
                 (player_is_active, ":player_no"),
                 (player_get_team_no, ":player_team", ":player_no"),
                 (eq, ":player_team", ":team_with_more_players"),
                 (player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
                 (try_begin),
                   (gt, ":player_join_time", ":max_player_join_time"),
                   (assign, ":max_player_join_time", ":player_join_time"),
                   (assign, ":latest_joined_player_no", ":player_no"),
                 (try_end),
               (try_end),
               (try_begin),
                 (ge, ":latest_joined_player_no", 0),
                 (try_begin),
                   #if player is living add +1 to his kill count because he will get -1 because of team change while living.
                   (player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"), 
                   (ge, ":latest_joined_agent_id", 0),
                   (agent_is_alive, ":latest_joined_agent_id"),

                   (player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
                   (val_add, ":player_kill_count", 1),
                   (player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),

                   (player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
                   (val_sub, ":player_death_count", 1),
                   (player_set_death_count, ":latest_joined_player_no", ":player_death_count"),

                   (player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
                   (val_add, ":player_score", 1),
                   (player_set_score, ":latest_joined_player_no", ":player_score"),

                   (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                     (player_is_active, ":player_no"),
                     (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
                   (try_end),         

                   (player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
                   (player_get_gold, ":player_gold", ":latest_joined_player_no"),
                   (val_add, ":player_gold", ":old_items_value"),
                   (player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
                 (end_try),

				 (call_script, "script_mp_set_player_team_no", ":latest_joined_player_no", ":team_with_less_players", 0),
                 (multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
               (try_end),
             (try_end),

             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), 

             #no need to send also server here
             (multiplayer_get_my_player, ":my_player_no"),
             (get_max_players, ":num_players"),                               
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
             (try_end),
             (assign, "$g_team_balance_next_round", 0),
           (try_end),
         (try_end),           
         #team balance check part finished
         (assign, "$g_team_balance_next_round", 0),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_agent_id, ":player_agent", ":player_no"),
           (ge, ":player_agent", 0),
           (agent_is_alive, ":player_agent"),
           (player_save_picked_up_items_for_next_spawn, ":player_no"),
           (player_get_value_of_original_items, ":old_items_value", ":player_no"),
           (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, ":old_items_value"),
         (try_end),
		 
		 (call_script, "script_mp_add_players_last_rounds_alive_squad_earnings"),

         #money management
         (assign, ":per_round_gold_addition", multi_battle_round_team_money_add),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
		   (player_slot_eq, ":player_no", slot_player_spawned_this_round, 1),
           (player_get_gold, ":player_gold", ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"),

           (try_begin),
             (this_or_next|eq, ":player_team", 0),
             (eq, ":player_team", 1),
             (val_add, ":player_gold", ":per_round_gold_addition"), 
			 (try_begin),
			   (eq, ":player_team", 0),
			   (store_mul, ":newly_added_player_gold", ":per_round_gold_addition", "$g_multiplayer_squad_size_calc"),
			   (val_div, ":newly_added_player_gold", 10),
			   (val_add, ":player_gold", ":newly_added_player_gold"),
			 (try_end),
           (try_end),

           #(below lines added new at 25.11.09 after Armagan decided new money system)
           (try_begin),
             (player_get_slot, ":old_items_value", ":player_no", slot_player_last_rounds_used_item_earnings),
             (store_add, ":player_total_potential_gold", ":player_gold", ":old_items_value"),
             (store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
             (lt, ":player_total_potential_gold", ":minimum_gold"),
             (store_sub, ":additional_gold", ":minimum_gold", ":player_total_potential_gold"),
             (val_add, ":player_gold", ":additional_gold"),
           (try_end),
           #new money system addition end
         
           (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
         (try_end),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
         (try_end),

         #initialize my team at start of round (it will be assigned again at next round's first death)
         (assign, "$my_team_at_start_of_round", -1),

         #clear scene and end round
         (multiplayer_clear_scene),

         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),

         (try_begin),
           (eq, "$g_battle_death_mode_started", 2),
           (call_script, "script_move_death_mode_flags_down"),
         (try_end),

         (assign, "$g_battle_death_mode_started", 0),
         (assign, "$g_reduced_waiting_seconds", 0),
         
         #initialize moveable object positions
         (call_script, "script_multiplayer_close_gate_if_it_is_open"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
                  
         (assign, "$g_round_ended", 0), 
         (store_mission_timer_a, "$g_round_start_time"),
         (call_script, "script_initialize_all_scene_prop_slots"),

         #initialize round start times for clients
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, -9999), #this will also initialize moveable object slots.
         (try_end),         
       ]),

      (0, 0, 0, [], #if there is nobody in any teams do not reduce round time.
       [
         (store_mission_timer_a, ":seconds_past_since_round_started"),
         (val_sub, ":seconds_past_since_round_started", "$g_round_start_time"),
         (le, ":seconds_past_since_round_started", 3),

         (assign, ":human_agents_spawned_at_team_1", "$g_multiplayer_num_bots_team_1"),
         (assign, ":human_agents_spawned_at_team_2", "$g_multiplayer_num_bots_team_2"),
         
         (get_max_players, ":end_cond"),
         (try_for_range, ":player_no", 0, ":end_cond"),
           (player_is_active, ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"), 
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":human_agents_spawned_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":human_agents_spawned_at_team_2", 1),
           (try_end),
           
           (gt, ":human_agents_spawned_at_team_1", 0),
           (gt, ":human_agents_spawned_at_team_2", 0),
           (assign, ":end_cond", 0),
         (try_end),

         (try_begin),
           (this_or_next|eq, ":human_agents_spawned_at_team_1", 0),
           (eq, ":human_agents_spawned_at_team_2", 0),

           (store_mission_timer_a, "$g_round_start_time"),
         (try_end),
       ]),
      
      (1, 0, 0, [(multiplayer_is_server),
                 ],
       [
         (store_mission_timer_a, ":round_time"),
         (val_sub, ":round_time", "$g_round_start_time"),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
           (try_begin),
             (player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),

             (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
             (lt, ":player_team", multi_team_spectator),
             (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
             (ge, ":player_troop", 0),

             (assign, ":spawn_new", 0), 
             (assign, ":num_active_players_in_team_0", 0),
             (assign, ":num_active_players_in_team_1", 0),
             (try_begin),
               (assign, ":num_active_players", 0),
               (get_max_players, ":num_players"),
               (try_for_range, ":player_no_2", 0, ":num_players"),
                 (player_is_active, ":player_no_2"),
                 (val_add, ":num_active_players", 1),
                 (player_get_team_no, ":player_team_2", ":player_no_2"),
                 (try_begin),
                   (eq, ":player_team_2", 0),
                   (val_add, ":num_active_players_in_team_0", 1),
                 (else_try),
                   (eq, ":player_team_2", 1),
                   (val_add, ":num_active_players_in_team_1", 1),
                 (try_end),
               (try_end),

               (store_mul, ":multipication_of_num_active_players_in_teams", ":num_active_players_in_team_0", ":num_active_players_in_team_1"),

               (this_or_next|lt, ":round_time", multiplayer_new_agents_finish_spawning_time),
               (this_or_next|le, ":num_active_players", 2),
               (eq, ":multipication_of_num_active_players_in_teams", 0),
         
               (eq, "$g_round_ended", 0),
               (assign, ":spawn_new", 1),
             (try_end),
             (eq, ":spawn_new", 1),
             (try_begin),
               (eq, ":player_team", 0),
               (assign, ":entry_no", multi_initial_spawn_point_team_1),
             (else_try),
               (eq, ":player_team", 1),
               (assign, ":entry_no", multi_initial_spawn_point_team_2),
             (try_end),
             (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),
             (player_spawn_new_agent, ":player_no", ":entry_no"),
			 (try_begin),
			   (eq, ":player_team", 0),
			   (call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":player_no", ":player_team", ":entry_no"), 
			 (try_end),

             (player_set_slot, ":player_no", slot_player_spawned_this_round, 1),
           (else_try), #spawning as a bot (if option ($g_multiplayer_player_respawn_as_bot) is 1)
             (eq, "$g_multiplayer_player_respawn_as_bot", 1),
#must be on team 1
			 (player_get_team_no, ":team_no", ":player_no"),
			 (eq, ":team_no", 0),

             (player_get_agent_id, ":player_agent", ":player_no"),
             (ge, ":player_agent", 0),
             (neg|agent_is_alive, ":player_agent"),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
             (gt, ":elapsed_time", "$g_multiplayer_respawn_period"), # Only respawn as bot after respawntime

             (call_script, "script_find_most_suitable_bot_to_control", ":player_no"),
             (assign,":bot_agent",reg0),
             (gt,":bot_agent",-1), # We found a bot to control lets control him.
             
             (player_control_agent, ":player_no", ":bot_agent"),

             (player_get_slot, ":num_spawns", ":player_no", slot_player_spawned_this_round),
             (val_add, ":num_spawns", 1),
             (player_set_slot, ":player_no", slot_player_spawned_this_round, ":num_spawns"),
           (try_end),
         (try_end),
         ]),

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,

      (ti_battle_window_opened, 0, 0, [], [
        (start_presentation, "prsnt_multiplayer_round_time_counter"),
        (start_presentation, "prsnt_multiplayer_team_score_display"),
        (try_begin),
          (eq, "$g_battle_death_mode_started", 2),
          (start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
        (try_end),
        ]),

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),



##    (
##    "multiplayer_fd",mtf_battle_mode,-1, #fight and destroy mode
##    "You lead your men to battle.",
##    [
##      (0,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
##      (1,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
##      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##
##      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##
##      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##
##      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##
##      (32,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
##      (33,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
##      (34,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (35,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (36,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (37,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (38,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (39,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##
##      (40,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (41,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (42,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (43,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (44,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (45,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (46,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##      (47,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
##
##      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##
##      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
##     ],
##    [
##      common_battle_init_banner,
##
##      multiplayer_server_check_polls,
##      multiplayer_set_map_weather,
##	  
##      (ti_server_player_joined, 0, 0, [],
##       [
##         (store_trigger_param_1, ":player_no"),
##         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
##         ]),
##
##      (ti_before_mission_start, 0, 0, [],
##       [
##         (assign, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
##         (call_script, "script_multiplayer_server_before_mission_start_common"),
##
##         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
##         (assign, "$g_round_ended", 0),
##         (assign, "$g_reduced_waiting_seconds", 0),
##
##         (try_begin),
##           (multiplayer_is_server),
##           (assign, "$g_round_start_time", 0),
##         (try_end),
##         (assign, "$my_team_at_start_of_round", -1),
##
##         (call_script, "script_multiplayer_init_mission_variables"),
##         (call_script, "script_multiplayer_remove_headquarters_flags"),         
##         ]),
##
##      (ti_after_mission_start, 0, 0, [], 
##       [
##         (call_script, "script_determine_team_flags", 0),
##         (call_script, "script_determine_team_flags", 1),
##         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
##         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)
##
##         (call_script, "script_initialize_all_scene_prop_slots"),
##         
##         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
##         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
##
##         (assign, "$g_destructible_target_1", "spr_catapult_destructible"),
##         (assign, "$g_destructible_target_2", "spr_trebuchet_destructible"),
##
##         #assigning destructible object team nos to 0. (0 is also used for showing defender team in siege mode)
##         (scene_prop_get_num_instances, ":num_destructible_target_1", "$g_destructible_target_1"),
##         (try_for_range, ":destructible_target_1_no", 0, ":num_destructible_target_1"),
##           (scene_prop_get_instance, ":destructible_target_1_id", "$g_destructible_target_1", ":destructible_target_1_no"),
##           (ge, ":destructible_target_1_id", 0),
##           (scene_prop_set_team, ":destructible_target_1_id", 0),
##         (try_end),
##
##         (scene_prop_get_num_instances, ":num_destructible_target_2", "$g_destructible_target_2"),
##         (try_for_range, ":destructible_target_2_no", 0, ":num_destructible_target_2"),
##           (scene_prop_get_instance, ":destructible_target_2_id", "$g_destructible_target_2", ":destructible_target_2_no"),
##           (ge, ":destructible_target_2_id", 0),
##           (scene_prop_set_team, ":destructible_target_2_id", 0),
##         (try_end),
##
##         (try_begin),
##           (scene_prop_get_num_instances, ":num_catapults", "spr_catapult_destructible"),
##           (ge, ":num_catapults", 1),
##           (scene_prop_get_instance, ":catapult_scene_prop_id", "spr_catapult_destructible", 0),
##           (scene_prop_get_team, "$g_defender_team", ":catapult_scene_prop_id"),
##         (else_try),         
##           (scene_prop_get_num_instances, ":num_trebuchets", "spr_trebuchet_destructible"),
##           (ge, ":num_trebuchets", 1),
##           (scene_prop_get_instance, ":trebuchet_scene_prop_id", "spr_trebuchet_destructible", 0),
##           (scene_prop_get_team, "$g_defender_team", ":trebuchet_scene_prop_id"),
##         (try_end),
##
##         (assign, "$g_number_of_targets_destroyed", 0),
##
##         (try_begin),
##           (assign, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1"), 
##           (assign, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2"), 
##         (try_end),
##
##         (start_presentation, "prsnt_multiplayer_destructible_targets_display"),
##
##         (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
##        ]),
##
##      (ti_on_agent_spawn, 0, 0, [],
##       [
##         (store_trigger_param_1, ":agent_no"),
##         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
##         
##         (try_begin), #if my initial team still not initialized, find and assign its value.
##           (neg|multiplayer_is_dedicated_server),
##           (lt, "$my_team_at_start_of_round", 0),
##           (multiplayer_get_my_player, ":my_player_no"),
##           (ge, ":my_player_no", 0),
##           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
##           (eq, ":my_agent_id", ":agent_no"),
##           (ge, ":my_agent_id", 0),
##           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
##         (try_end),         
##          
##         (try_begin),
##           (neg|multiplayer_is_server),
##           (try_begin),
##             (eq, "$g_round_ended", 1),
##             (assign, "$g_round_ended", 0),
##
##             #initialize scene object slots at start of new round at clients.
##             (call_script, "script_initialize_all_scene_prop_slots"),
##
##             #these lines are done in only clients at start of each new round.
##             (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
##             (call_script, "script_initialize_objects_clients"),
##             #end of lines
##        
##             (start_presentation, "prsnt_multiplayer_destructible_targets_display"),
##             (try_begin),
##               (eq, "$g_team_balance_next_round", 1),
##               (assign, "$g_team_balance_next_round", 0),
##             (try_end),
##           (try_end),  
##         (try_end),         
##         ]),
##
##      (ti_on_agent_killed_or_wounded, 0, 0, [],
##       [
##         (store_trigger_param_1, ":dead_agent_no"),
##         (store_trigger_param_2, ":killer_agent_no"),
##
##         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
##         
##         (try_begin), #if my initial team still not initialized, find and assign its value.
##           (neg|multiplayer_is_dedicated_server),
##           (lt, "$my_team_at_start_of_round", 0),
##           (multiplayer_get_my_player, ":my_player_no"),
##           (ge, ":my_player_no", 0),
##           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
##           (ge, ":my_agent_id", 0),
##           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
##         (try_end),         
##         
##         (try_begin), #count players and if round ended understand this.
##           (agent_is_human, ":dead_agent_no"),
##           (assign, ":team1_living_players", 0),
##           (assign, ":team2_living_players", 0),
##           (try_for_agents, ":cur_agent"),
##             (agent_is_human, ":cur_agent"),         
##             (try_begin),
##               (agent_is_alive, ":cur_agent"),  
##               (agent_get_team, ":cur_agent_team", ":cur_agent"),
##               (try_begin),
##                 (eq, ":cur_agent_team", 0),
##               (val_add, ":team1_living_players", 1),
##               (else_try),
##                 (eq, ":cur_agent_team", 1),
##                 (val_add, ":team2_living_players", 1),
##               (try_end),
##             (try_end),
##           (try_end),                    
##           (try_begin),         
##             (eq, "$g_round_ended", 0),
##             (try_begin),
##               (this_or_next|eq, ":team1_living_players", 0),
##               (eq, ":team2_living_players", 0),                
##               (assign, "$g_winner_team", -1),
##               (assign, reg0, "$g_multiplayer_respawn_period"),
##               (try_begin),
##                 (eq, ":team1_living_players", 0),
##                 (try_begin),
##                   (neq, ":team2_living_players", 0),
##                   (assign, "$g_winner_team", 1),
##                 (try_end),
##
##                 (try_begin),
##                   (eq, "$g_winner_team", -1),
##                 (else_try),
##                   (eq, "$g_defender_team", 1), #if defender team killed all attackers
##                   (try_begin),
##                     (neg|multiplayer_is_server),
##                     (call_script, "script_calculate_number_of_targets_destroyed"),
##                   (try_end),
##                   (store_sub, ":num_targets_saved", 2, "$g_number_of_targets_destroyed"),
##                   (call_script, "script_show_multiplayer_message", multiplayer_message_type_defenders_saved_n_targets, ":num_targets_saved"), #1 or -1 is winner team
##                 (else_try),
##                   (call_script, "script_show_multiplayer_message", multiplayer_message_type_attackers_won_the_round, 0), #1 or -1 is winner team
##                 (try_end),        
##               (else_try),
##                 (try_begin),
##                   (neq, ":team1_living_players", 0),
##                   (assign, "$g_winner_team", 0),
##                 (try_end),
##
##                 (try_begin),
##                   (eq, "$g_winner_team", -1),         
##                 (else_try),
##                   (eq, "$g_defender_team", 0), #if defender team killed all attackers
##                   (try_begin),
##                     (neg|multiplayer_is_server),
##                     (call_script, "script_calculate_number_of_targets_destroyed"),
##                   (try_end),
##                   (store_sub, ":num_targets_saved", 2, "$g_number_of_targets_destroyed"),
##                   (call_script, "script_show_multiplayer_message", multiplayer_message_type_defenders_saved_n_targets, ":num_targets_saved"), #0 or -1 is winner team
##                 (else_try),
##                   (call_script, "script_show_multiplayer_message", multiplayer_message_type_attackers_won_the_round, 0), #0 or -1 is winner team
##                 (try_end),         
##               (try_end),
##               (store_mission_timer_a, "$g_round_finish_time"),
##               (assign, "$g_round_ended", 1),
##
##
##               (try_begin), #destroy score (condition : remained no one)
##                 (multiplayer_is_server),
##                 (ge, "$g_winner_team", 0),
##                 (lt, "$g_winner_team", 2),
##                 (neq, "$g_winner_team", -1),
##
##                 (team_get_score, ":team_score", "$g_winner_team"),
##                 (store_sub, ":num_targets_remained", 2, "$g_number_of_targets_destroyed"),
##                 (val_add, ":team_score", ":num_targets_remained"),
##
##                 #for only server itself-----------------------------------------------------------------------------------------------
##                 (call_script, "script_team_set_score", "$g_winner_team", ":team_score"),
##                 #for only server itself-----------------------------------------------------------------------------------------------
##                 (get_max_players, ":num_players"),
##                 (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##                   (player_is_active, ":player_no"),
##                   (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, "$g_winner_team", ":team_score"),
##                 (try_end),
##               (try_end), #destroy score end
##
##         
##               (try_begin),
##                 (neq, "$g_defender_team", "$g_winner_team"),
##                 (neq, "$g_winner_team", -1),
##                 (assign, "$g_number_of_targets_destroyed", 2),              
##               (try_end),
##             (try_end),
##           (try_end),
##         (try_end),
##
##         (try_begin),
##           (multiplayer_is_server),
##           (agent_is_human, ":dead_agent_no"),
##           (neg|agent_is_non_player, ":dead_agent_no"),
##
##           (ge, ":dead_agent_no", 0),
##           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
##           (ge, ":dead_agent_player_id", 0),
##
##           (set_fixed_point_multiplier, 100),
##
##           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
##           (agent_get_position, pos0, ":dead_agent_no"),
##
##           (position_get_x, ":x_coor", pos0),
##           (position_get_y, ":y_coor", pos0),
##           (position_get_z, ":z_coor", pos0),
##         
##           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_x, ":x_coor"),
##           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_y, ":y_coor"),
##           (player_set_slot, ":dead_agent_player_id", slot_player_death_pos_z, ":z_coor"),
##         (try_end),    
##         ]),
##
##      (ti_on_multiplayer_mission_end, 0, 0, [],
##       [
##         (call_script, "script_multiplayer_event_mission_end"),
##         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
##         (start_presentation, "prsnt_multiplayer_stats_chart"),
##         ]),
##
##      
##      (1, 0, 0, [(multiplayer_is_server), 
##                 (eq, "$g_round_ended", 0),
##                 (eq, "$g_number_of_targets_destroyed", 2),
##                 ],
##       [
##         (store_mission_timer_a, "$g_round_finish_time"),
##         (assign, "$g_round_ended", 1),         
##
##         (multiplayer_get_my_player, ":my_player_no"), #send all players draw information of round.
##         #for only server itself-----------------------------------------------------------------------------------------------
##         (call_script, "script_draw_this_round", -9),
##         #for only server itself-----------------------------------------------------------------------------------------------
##         (get_max_players, ":num_players"), 
##         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##           (player_is_active, ":player_no"),
##           (neq, ":player_no", ":my_player_no"),
##           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, -9),
##         (try_end),
##         ]),
##      
##      (1, 0, 0, [(multiplayer_is_server), 
##                 (eq, "$g_round_ended", 0),
##                 (store_mission_timer_a, ":current_time"),
##                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
##                 (ge, ":seconds_past_in_round", "$g_multiplayer_round_max_seconds"),
##                 ],
##       [ #round time is up
##         (store_mission_timer_a, "$g_round_finish_time"),                          
##         (assign, "$g_round_ended", 1),
##         (assign, "$g_winner_team", -9),
##         
##         (multiplayer_get_my_player, ":my_player_no"), #send all players draw information of round.
##
##         (store_sub, ":num_targets_saved", 2, "$g_number_of_targets_destroyed"),
##         #for only server itself-----------------------------------------------------------------------------------------------
##         (call_script, "script_show_multiplayer_message", multiplayer_message_type_defenders_saved_n_targets, ":num_targets_saved"), 
##         #for only server itself-----------------------------------------------------------------------------------------------     
##         (get_max_players, ":num_players"),
##         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##           (player_is_active, ":player_no"),
##           (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_defenders_saved_n_targets, ":num_targets_saved"),
##         (try_end),
##
##         #for only server itself-----------------------------------------------------------------------------------------------
##         (call_script, "script_draw_this_round", "$g_winner_team"),
##         #for only server itself-----------------------------------------------------------------------------------------------
##         (get_max_players, ":num_players"), 
##         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##           (player_is_active, ":player_no"),
##           (neq, ":player_no", ":my_player_no"),
##           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
##         (try_end),
##                         
##         (try_begin), #destroy score (condition : time is up)
##           (multiplayer_is_server),
##           (assign, "$g_winner_team", "$g_defender_team"),         
##         
##           (team_get_score, ":team_score", "$g_winner_team"),
##           (store_sub, ":num_targets_remained", 2, "$g_number_of_targets_destroyed"),
##           (val_add, ":team_score", ":num_targets_remained"),
##
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (call_script, "script_team_set_score", "$g_winner_team", ":team_score"),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##             (player_is_active, ":player_no"),
##             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, "$g_winner_team", ":team_score"),
##           (try_end),
##         (try_end), #destroy score end        
##        ]),          
##
##      (10, 0, 0, [(multiplayer_is_server)],
##       [
##         #auto team balance control during the round         
##         (assign, ":number_of_players_at_team_1", 0),
##         (assign, ":number_of_players_at_team_2", 0),
##         (get_max_players, ":num_players"),
##         (try_for_range, ":cur_player", 0, ":num_players"),
##           (player_is_active, ":cur_player"),
##           (player_get_team_no, ":player_team", ":cur_player"),
##           (try_begin),
##             (eq, ":player_team", 0),
##             (val_add, ":number_of_players_at_team_1", 1),
##           (else_try),
##             (eq, ":player_team", 1),
##             (val_add, ":number_of_players_at_team_2", 1),
##           (try_end),         
##         (try_end),
##         #end of counting active players per team.
##         (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
##         (assign, ":number_of_players_will_be_moved", 0),
##         (try_begin),
##           (try_begin),
##             (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
##             (le, ":difference_of_number_of_players", ":checked_value"),
##             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
##           (else_try),
##             (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
##             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
##           (try_end),          
##         (try_end),         
##         #number of players will be moved calculated. (it is 0 if no need to make team balance)
##         (try_begin),
##           (gt, ":number_of_players_will_be_moved", 0),
##           (try_begin),
##             (eq, "$g_team_balance_next_round", 0),
##         
##             (assign, "$g_team_balance_next_round", 1),
##
##             #for only server itself-----------------------------------------------------------------------------------------------
##             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
##             #for only server itself-----------------------------------------------------------------------------------------------     
##             (get_max_players, ":num_players"),                               
##             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##               (player_is_active, ":player_no"),
##               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
##             (try_end),
##             
##             (call_script, "script_warn_player_about_auto_team_balance"),
##           (try_end),
##         (try_end),           
##         #team balance check part finished
##         ]),
##
##      (0, 0, 0, [(multiplayer_is_server),  
##                 (eq, "$g_round_ended", 0),                 
##                 (eq, "$g_battle_death_mode_started", 2)],
##       [
##         (set_fixed_point_multiplier, 100),
##         (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
##         (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
##         (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
##         (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),
##
##         (prop_instance_get_position, pos1, ":pole_1_id"),
##         (prop_instance_get_position, pos2, ":pole_2_id"),
##         (prop_instance_get_position, pos3, ":flag_1_id"),
##         (prop_instance_get_position, pos4, ":flag_2_id"),
##
##         (copy_position, pos7, pos1),
##         (position_move_z, pos7, multi_headquarters_flag_initial_height),
##         (copy_position, pos8, pos2),
##         (position_move_z, pos8, multi_headquarters_flag_initial_height),
##
##         (get_distance_between_positions, ":dist_1", pos1, pos3),
##         (get_distance_between_positions, ":dist_2", pos2, pos4),
##
##         (assign, ":there_are_agents_from_only_team_1_around_their_flag", 0),
##         (assign, ":there_are_agents_from_only_team_2_around_their_flag", 0),
##         (get_max_players, ":num_players"),
##         (try_for_range, ":player_no", 0, ":num_players"),
##           (player_is_active, ":player_no"),
##           (player_get_agent_id, ":agent_id", ":player_no"),
##           (ge, ":agent_id", 0),
##           (agent_is_human, ":agent_id"),
##           (agent_is_alive, ":agent_id"),
##           (agent_get_team, ":agent_team", ":agent_id"),
##           (agent_get_position, pos0, ":agent_id"),
##
##           (agent_get_horse, ":agent_horse", ":agent_id"),
##           (eq, ":agent_horse", -1), #horseman cannot move flag
##         
##           (try_begin),
##             (eq, ":agent_team", 0),
##             (try_begin),
##               (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
##               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
##               (try_begin), #we found a team_1 agent in the flag_1 area, so flag_1 situation can be 1 or -2
##                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 0),
##                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", 1), #there are agents from only our team
##               (else_try),
##                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", -1),
##                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -2), #there are agents from both teams
##               (try_end),
##             (try_end),
##             (try_begin),
##               (get_sq_distance_between_positions, ":squared_dist", pos0, pos2),
##               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
##               (try_begin), #we found a team_1 agent in the flag_2 area, so flag_2 situation can be -1 or -2
##                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 0),
##                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -1), #there are agents from only rival team
##               (else_try),
##                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1),
##                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -2), #there are agents from both teams
##               (try_end),
##             (try_end),
##           (else_try),
##             (eq, ":agent_team", 1),
##             (try_begin),
##               (get_sq_distance_between_positions, ":squared_dist", pos0, pos2),
##               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
##               (try_begin), #we found a team_2 agent in the flag 2 area, so flag_2 situation can be 1 or -2
##                 (eq, ":there_are_agents_from_only_team_2_around_their_flag", 0),
##                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", 1), #there are agents from only our team
##               (else_try),
##                 (assign, ":there_are_agents_from_only_team_2_around_their_flag", -2), #there are agents from both teams
##               (try_end),
##             (try_end),
##             (try_begin),
##               (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
##               (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
##               (try_begin), #we found a team_2 agent in the flag_1 area, so flag_1 situation can be -1 or -2
##                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 0),
##                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -1), #there are agents from only rival team
##               (else_try),
##                 (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1),
##                 (assign, ":there_are_agents_from_only_team_1_around_their_flag", -2), #there are agents from both teams
##               (try_end),
##             (try_end),
##           (try_end),
##         (try_end),
##
##         #controlling battle win by death mode conditions
##         (try_begin),
##           (ge, ":dist_1", multi_headquarters_flag_height_to_win),           
##           (assign, "$g_winner_team", 0),
##
##           (get_max_players, ":num_players"), 
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (call_script, "script_draw_this_round", "$g_winner_team"),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##             (player_is_active, ":player_no"),
##             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
##           (try_end),
##
##           (team_get_score, ":team_1_score", 0),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (call_script, "script_team_set_score", 0, ":team_1_score"),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##             (player_is_active, ":player_no"),
##             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 0, ":team_1_score"),             
##           (try_end),
##
##           (store_mission_timer_a, "$g_round_finish_time"),
##           (assign, "$g_round_ended", 1),
##         (else_try),
##           (ge, ":dist_2", multi_headquarters_flag_height_to_win),
##           (assign, "$g_winner_team", 1),
##
##           (get_max_players, ":num_players"), 
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (call_script, "script_draw_this_round", "$g_winner_team"),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##             (player_is_active, ":player_no"),
##             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
##           (try_end),
##
##           (team_get_score, ":team_2_score", 1),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (call_script, "script_team_set_score", 1, ":team_2_score"),
##           #for only server itself-----------------------------------------------------------------------------------------------
##           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##             (player_is_active, ":player_no"),
##             (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_score, 1, ":team_2_score"),             
##           (try_end),
##
##           (call_script, "script_show_multiplayer_message", multiplayer_message_type_round_result_in_battle_mode, 0), #0 is winner team         
##
##           (store_mission_timer_a, "$g_round_finish_time"),
##           (assign, "$g_round_ended", 1),
##         (try_end),
##
##         (try_begin),
##           (eq, "$g_round_ended", 0),
##
##           (position_get_z, ":flag_1_cur_z", pos3),       
##           (prop_instance_is_animating, ":is_animating", ":flag_1_id"),         
##           (try_begin), #if flag_1 is going down or up and there are agents from both teams
##             (eq, ":there_are_agents_from_only_team_1_around_their_flag", -2), #if there are agents from both teams
##             (eq, ":is_animating", 1),
##             (prop_instance_stop_animating, ":flag_1_id"), #stop flag_1
##           (else_try), #if flag_1 is going down
##             (this_or_next|eq, ":there_are_agents_from_only_team_1_around_their_flag", 0), #if there is no one
##             (eq, ":there_are_agents_from_only_team_1_around_their_flag", -1), #if there are agents from only team_2 (enemy of team_1)
##             (prop_instance_get_animation_target_position, pos9, ":flag_1_id"),
##             (position_get_z, ":flag_1_animation_target_z", pos9),
##             (this_or_next|eq, ":is_animating", 0), #if flag_1 is stopping
##             (gt, ":flag_1_animation_target_z", ":flag_1_cur_z"), #if flag_1 is going up         
##             (get_distance_between_positions, ":time_1", pos3, pos7),
##             (gt, ":time_1", 0),
##             (val_mul, ":time_1", 16),
##             (prop_instance_animate_to_position, ":flag_1_id", pos7, ":time_1"), #move flag_1 down
##           (else_try), #if flag_1 is going down or stopping
##             (eq, ":there_are_agents_from_only_team_1_around_their_flag", 1), #if there is agents from only team_1 (current team)
##             (prop_instance_get_animation_target_position, pos9, ":flag_1_id"),
##             (position_get_z, ":flag_1_animation_target_z", pos9),
##             (this_or_next|eq, ":is_animating", 0), #if flag_1 is stopping
##             (lt, ":flag_1_animation_target_z", ":flag_1_cur_z"), #if flag_1 is going down
##             (copy_position, pos5, pos1),
##             (position_move_z, pos5, multi_headquarters_flag_height_to_win),
##             (get_distance_between_positions, ":time_1", pos3, pos5),
##             (gt, ":time_1", 0),
##             (val_mul, ":time_1", 8),
##             (prop_instance_animate_to_position, ":flag_1_id", pos5, ":time_1"), #move flag_1 up
##           (try_end),
##
##           (position_get_z, ":flag_2_cur_z", pos4),       
##           (prop_instance_is_animating, ":is_animating", ":flag_2_id"),         
##           (try_begin), #if flag is going down or up and there are agents from both teams
##             (eq, ":there_are_agents_from_only_team_2_around_their_flag", -2), #if there are agents from both teams
##             (eq, ":is_animating", 1),
##             (prop_instance_stop_animating, ":flag_2_id"), #stop flag_2
##           (else_try), #if flag_2 is going down
##             (this_or_next|eq, ":there_are_agents_from_only_team_2_around_their_flag", 0), #if there is no one
##             (eq, ":there_are_agents_from_only_team_2_around_their_flag", -1), #if there are agents from only team_1 (enemy of team_1)
##             (prop_instance_get_animation_target_position, pos9, ":flag_2_id"),
##             (position_get_z, ":flag_2_animation_target_z", pos9),
##             (this_or_next|eq, ":is_animating", 0), #if flag_2 is stopping
##             (gt, ":flag_2_animation_target_z", ":flag_2_cur_z"), #if flag_2 is going up         
##             (get_distance_between_positions, ":time_2", pos4, pos8),
##             (gt, ":time_2", 0),
##             (val_mul, ":time_2", 16),
##             (prop_instance_animate_to_position, ":flag_2_id", pos8, ":time_2"), #move flag_2 down
##           (else_try), #if flag_2 is going down or stopping
##             (eq, ":there_are_agents_from_only_team_2_around_their_flag", 1), #if there is agents from only team_2 (current team)
##             (prop_instance_get_animation_target_position, pos9, ":flag_2_id"),
##             (position_get_z, ":flag_2_animation_target_z", pos9),
##             (this_or_next|eq, ":is_animating", 0), #if flag_2 is stopping
##             (lt, ":flag_2_animation_target_z", ":flag_2_cur_z"), #if flag_2 is going down
##             (copy_position, pos6, pos2),
##             (position_move_z, pos6, multi_headquarters_flag_height_to_win),
##             (get_distance_between_positions, ":time_2", pos4, pos6),
##             (gt, ":time_2", 0),
##             (val_mul, ":time_2", 8),
##             (prop_instance_animate_to_position, ":flag_2_id", pos6, ":time_2"), #move flag_2 up
##           (try_end),
##         (try_end),
##         ]),
##                
##      (1, 0, 3, [(multiplayer_is_server),
##                 (eq, "$g_round_ended", 1),
##                 (store_mission_timer_a, ":seconds_past_till_round_ended"),
##                 (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
##                 (ge, ":seconds_past_till_round_ended", "$g_multiplayer_respawn_period")],
##       [
##         #auto team balance control at the end of round         
##         (assign, ":number_of_players_at_team_1", 0),
##         (assign, ":number_of_players_at_team_2", 0),
##         (get_max_players, ":num_players"),
##         (try_for_range, ":cur_player", 0, ":num_players"),
##           (player_is_active, ":cur_player"),
##           (player_get_team_no, ":player_team", ":cur_player"),
##           (try_begin),
##             (eq, ":player_team", 0),
##             (val_add, ":number_of_players_at_team_1", 1),
##           (else_try),
##             (eq, ":player_team", 1),
##             (val_add, ":number_of_players_at_team_2", 1),
##           (try_end),         
##         (try_end),
##         #end of counting active players per team.
##         (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
##         (assign, ":number_of_players_will_be_moved", 0),
##         (try_begin),
##           (try_begin),
##             (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
##             (le, ":difference_of_number_of_players", ":checked_value"),
##             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
##             (assign, ":team_with_more_players", 1),
##             (assign, ":team_with_less_players", 0),
##           (else_try),
##             (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
##             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
##             (assign, ":team_with_more_players", 0),
##             (assign, ":team_with_less_players", 1),
##           (try_end),          
##         (try_end),         
##         #number of players will be moved calculated. (it is 0 if no need to make team balance)
##         (try_begin),
##           (gt, ":number_of_players_will_be_moved", 0),
##           (try_begin),
##             #(eq, "$g_team_balance_next_round", 1), #control if at pre round players are warned about team change.
##
##             (try_for_range, ":unused", 0, ":number_of_players_will_be_moved"), 
##               (assign, ":max_player_join_time", 0),
##               (assign, ":latest_joined_player_no", -1),
##               (get_max_players, ":num_players"),                               
##               (try_for_range, ":player_no", 0, ":num_players"),
##                 (player_is_active, ":player_no"),
##                 (player_get_team_no, ":player_team", ":player_no"),
##                 (eq, ":player_team", ":team_with_more_players"),
##                 (player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
##                 (try_begin),
##                   (gt, ":player_join_time", ":max_player_join_time"),
##                   (assign, ":max_player_join_time", ":player_join_time"),
##                   (assign, ":latest_joined_player_no", ":player_no"),
##                 (try_end),
##               (try_end),
##               (try_begin),
##                 (ge, ":latest_joined_player_no", 0),
##                 (try_begin),
##                   #if player is living add +1 to his kill count because he will get -1 because of team change while living.
##                   (player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"), 
##                   (ge, ":latest_joined_agent_id", 0),
##                   (agent_is_alive, ":latest_joined_agent_id"),
##
##                   (player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
##                   (val_add, ":player_kill_count", 1),
##                   (player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),
##
##                   (player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
##                   (val_sub, ":player_death_count", 1),
##                   (player_set_death_count, ":latest_joined_player_no", ":player_death_count"),
##
##                   (player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
##                   (val_add, ":player_score", 1),
##                   (player_set_score, ":latest_joined_player_no", ":player_score"),
##
##                   (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##                     (player_is_active, ":player_no"),
##                     (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
##                   (try_end),         
##
##                   (player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
##                   (player_get_gold, ":player_gold", ":latest_joined_player_no"),
##                   (val_add, ":player_gold", ":old_items_value"),
##                   (player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
##                 (end_try),
##
##                 (player_set_troop_id, ":latest_joined_player_no", -1),
##                 (player_set_team_no, ":latest_joined_player_no", ":team_with_less_players"),
##                 (multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
##               (try_end),
##             (try_end),
##             #tutorial message (after team balance)
##             
##             #(tutorial_message_set_position, 500, 500),
##             #(tutorial_message_set_size, 30, 30),
##             #(tutorial_message_set_center_justify, 1),
##             #(tutorial_message, "str_auto_team_balance_done", 0xFFFFFFFF, 5),
##
##             #for only server itself
##             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), 
##
##             #no need to send also server here
##             (multiplayer_get_my_player, ":my_player_no"),
##             (get_max_players, ":num_players"),                               
##             (try_for_range, ":player_no", 0, ":num_players"),
##               (player_is_active, ":player_no"),
##               (neq, ":my_player_no", ":player_no"),
##               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
##             (try_end),
##             (assign, "$g_team_balance_next_round", 0),
##           (try_end),
##         (try_end),           
##         #team balance check part finished
##         (assign, "$g_team_balance_next_round", 0),
##
##         (get_max_players, ":num_players"),
##         (try_for_range, ":player_no", 0, ":num_players"),
##           (player_is_active, ":player_no"),
##           (player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
##           (player_get_agent_id, ":player_agent", ":player_no"),
##           (ge, ":player_agent", 0),
##           (agent_is_alive, ":player_agent"),
##           (player_save_picked_up_items_for_next_spawn, ":player_no"),
##           (player_get_value_of_original_items, ":old_items_value", ":player_no"),
##           (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, ":old_items_value"),
##         (try_end),
##
##         #money management
##         (assign, ":per_round_gold_addition", multi_battle_round_team_money_add),
##         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
##         (val_div, ":per_round_gold_addition", 100),
##         
##         (store_sub, ":num_targets_remained", 2, "$g_number_of_targets_destroyed"),
##         (store_mul, ":defender_money_add", ":num_targets_remained", multi_destroy_save_or_destroy_target_money_add),
##         (store_mul, ":attacker_money_add", "$g_number_of_targets_destroyed", multi_destroy_save_or_destroy_target_money_add),
##         (val_add, ":defender_money_add", 100), #defenders cannot get money from destroying catapult thats why they get more money per round.
##         (val_sub, ":attacker_money_add", 100), #attackers also get money from destroying catapult thats why they get less money per round.
##         (get_max_players, ":num_players"),
##
##         (val_mul, ":defender_money_add", "$g_multiplayer_round_earnings_multiplier"),
##         (val_div, ":defender_money_add", 100),
##         (val_mul, ":attacker_money_add", "$g_multiplayer_round_earnings_multiplier"),
##         (val_div, ":attacker_money_add", 100),
##
##         (try_for_range, ":player_no", 0, ":num_players"),
##           (player_is_active, ":player_no"),
##           (player_get_gold, ":player_gold", ":player_no"),
##           (player_get_team_no, ":player_team", ":player_no"),           
##           (val_add, ":player_gold", ":per_round_gold_addition"), #standard           
##           (try_begin), 
##             (eq, ":player_team", "$g_defender_team"),
##             (val_add, ":player_gold", ":defender_money_add"),
##           (else_try), 
##             (val_add, ":player_gold", ":attacker_money_add"),
##           (try_end),
##         
##           #(below lines added new at 25.11.09 after Armagan decided new money system)
##           (try_begin),
##             (player_get_slot, ":old_items_value", ":player_no", slot_player_last_rounds_used_item_earnings),
##             (store_add, ":player_total_potential_gold", ":player_gold", ":old_items_value"),
##             (store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
##             (lt, ":player_total_potential_gold", ":minimum_gold"),
##             (store_sub, ":additional_gold", ":minimum_gold", ":player_total_potential_gold"),
##             (val_add, ":player_gold", ":additional_gold"),
##           (try_end),
##           #new money system addition end
##
##           (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
##         (try_end),
##
##         #initialize my team at start of round (it will be assigned again at next round's first death)
##         (assign, "$my_team_at_start_of_round", -1),
##
##         #clear scene and end round
##         (multiplayer_clear_scene),
##         
##         (get_max_players, ":num_players"),                               
##         (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
##           (player_is_active, ":player_no"),
##           (player_set_slot, ":player_no", slot_player_damage_given_to_target_1, 0),
##           (player_set_slot, ":player_no", slot_player_damage_given_to_target_2, 0),
##         (try_end),
##         
##         #initialize moveable object positions
##         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
##         (call_script, "script_multiplayer_close_gate_if_it_is_open"),
##         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
##                  
##         (assign, "$g_round_ended", 0),
##
##         (assign, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1"), 
##         (assign, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2"), 
##
##         (start_presentation, "prsnt_multiplayer_destructible_targets_display"),
##
##         #initializing catapult & trebuchet positions and hit points for destroy mod.
##         (call_script, "script_initialize_objects"),
##
##         (store_mission_timer_a, "$g_round_start_time"),
##         (call_script, "script_initialize_all_scene_prop_slots"),
##
##         #initialize round start times for clients
##         (get_max_players, ":num_players"),
##         (try_for_range, ":player_no", 0, ":num_players"),
##           (player_is_active, ":player_no"),
##           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, -9999), #this will also initialize moveable object slots.
##         (try_end),         
##       ]),
##
##      (0, 0, 0, [], #if there is nobody in any teams do not reduce round time.
##       [
##         #(multiplayer_is_server),
##         (assign, ":human_agents_spawned_at_team_1", "$g_multiplayer_num_bots_team_1"),
##         (assign, ":human_agents_spawned_at_team_2", "$g_multiplayer_num_bots_team_2"),
##         
##         (get_max_players, ":num_players"),
##         (try_for_range, ":player_no", 0, ":num_players"),
##           (player_is_active, ":player_no"),
##           (player_get_team_no, ":player_team", ":player_no"), 
##           (try_begin),
##             (eq, ":player_team", 0),
##             (val_add, ":human_agents_spawned_at_team_1", 1),
##           (else_try),
##             (eq, ":player_team", 1),
##             (val_add, ":human_agents_spawned_at_team_2", 1),
##           (try_end),
##         (try_end),
##
##         (try_begin),
##           (this_or_next|eq, ":human_agents_spawned_at_team_1", 0),
##           (eq, ":human_agents_spawned_at_team_2", 0),
##
##           (store_mission_timer_a, ":seconds_past_since_round_started"),
##           (val_sub, ":seconds_past_since_round_started", "$g_round_start_time"),
##           (le, ":seconds_past_since_round_started", 2),
##                  
##           (store_mission_timer_a, "$g_round_start_time"),
##         (try_end),
##       ]),    
##           
##      (1, 0, 0, [],
##       [
##         (multiplayer_is_server),
##         (get_max_players, ":num_players"),
##         (try_for_range, ":player_no", 0, ":num_players"),
##           (player_is_active, ":player_no"),
##           (neg|player_is_busy_with_menus, ":player_no"),
##           (try_begin),
##             (player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),
##
##             (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
##             (lt, ":player_team", multi_team_spectator),
##
##             (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
##             (ge, ":player_troop", 0),
##
##             (assign, ":spawn_new", 0), 
##             (assign, ":num_active_players_in_team_0", 0),
##             (assign, ":num_active_players_in_team_1", 0),
##             (try_begin),
##               (assign, ":num_active_players", 0),
##               (get_max_players, ":num_players"),
##               (try_for_range, ":player_no_2", 0, ":num_players"),
##                 (player_is_active, ":player_no_2"),
##                 (val_add, ":num_active_players", 1),
##                 (player_get_team_no, ":player_team_2", ":player_no_2"),
##                 (try_begin),
##                   (eq, ":player_team_2", 0),
##                   (val_add, ":num_active_players_in_team_0", 1),
##                 (else_try),
##                   (eq, ":player_team_2", 1),
##                   (val_add, ":num_active_players_in_team_1", 1),
##                 (try_end),
##               (try_end),
##
##               (store_mul, ":multipication_of_num_active_players_in_teams", ":num_active_players_in_team_0", ":num_active_players_in_team_1"),
##
##               (store_mission_timer_a, ":round_time"),
##               (val_sub, ":round_time", "$g_round_start_time"),
##
##               (this_or_next|lt, ":round_time", multiplayer_new_agents_finish_spawning_time),
##               (this_or_next|le, ":num_active_players", 2),
##               (eq, ":multipication_of_num_active_players_in_teams", 0),
##         
##               (eq, "$g_round_ended", 0),
##               (assign, ":spawn_new", 1),
##             (try_end),
##             (eq, ":spawn_new", 1),
##             (try_begin),
##               (eq, ":player_team", 0),
##               (assign, ":entry_no", multi_initial_spawn_point_team_1),
##             (else_try),
##               (eq, ":player_team", 1),
##               (assign, ":entry_no", multi_initial_spawn_point_team_2),
##             (try_end),
##             (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),
##             (player_spawn_new_agent, ":player_no", ":entry_no"),
##             (player_set_slot, ":player_no", slot_player_spawned_this_round, 1),
##           (else_try), #spawning as a bot (if option ($g_multiplayer_player_respawn_as_bot) is 1)
##             (eq, "$g_multiplayer_player_respawn_as_bot", 1),
##             (player_get_agent_id, ":player_agent", ":player_no"),
##             (ge, ":player_agent", 0),
##             (neg|agent_is_alive, ":player_agent"),
##             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
##             (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
##
##             (player_get_team_no, ":player_team", ":player_no"),
##             (assign, ":is_found", 0),
##             (try_for_agents, ":cur_agent"),
##               (eq, ":is_found", 0),
##               (agent_is_alive, ":cur_agent"),
##               (agent_is_human, ":cur_agent"),
##               (agent_is_non_player, ":cur_agent"),
##               (agent_get_team ,":cur_team", ":cur_agent"),
##               (eq, ":cur_team", ":player_team"),
##               (assign, ":is_found", 1),
##             (try_end),
##
##             (try_begin),
##               (eq, ":is_found", 1),
##               (call_script, "script_find_most_suitable_bot_to_control", ":player_no"),
##               (player_control_agent, ":player_no", reg0),
##
##               (player_get_slot, ":num_spawns", ":player_no", slot_player_spawned_this_round),
##               (val_add, ":num_spawns", 1),
##               (player_set_slot, ":player_no", slot_player_spawned_this_round, ":num_spawns"),
##             (try_end),
##           (try_end),
##         (try_end),
##         ]),
##
##      multiplayer_server_spawn_bots, 
##      multiplayer_server_manage_bots, 
##      
##      multiplayer_server_check_end_map,
##        
##      (ti_tab_pressed, 0, 0, [],
##       [
##         (try_begin),
##           (eq, "$g_multiplayer_mission_end_screen", 0),
##           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
##           (start_presentation, "prsnt_multiplayer_stats_chart"),
##         (try_end),
##         ]),
##
##      multiplayer_once_at_the_first_frame,
##
##      (ti_battle_window_opened, 0, 0, [], [
##        (start_presentation, "prsnt_multiplayer_round_time_counter"),
##        (start_presentation, "prsnt_multiplayer_team_score_display"),
##        ]),
##
##      (ti_escape_pressed, 0, 0, [],
##       [
##         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
##         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
##         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
##         (start_presentation, "prsnt_multiplayer_escape_menu"),
##         ]),
##      ],
##  ),
  
    (
    "multiplayer_ctdm",mtf_battle_mode,-1, #captain_team_deathmatch mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         ]),
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
		 
		 (call_script, "script_mp_clear_squad_info", ":player_no"),
		 ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_captain_team_deathmatch),		 
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)

         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),

         (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
		 (set_cheer_at_no_enemy, 0),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),
		 
	  (ti_on_player_exit, 0, 0, [],
		[
		 # force kill all squad agents of the exiting player
		 (store_trigger_param_1, ":exiting_player_no"),
		 (call_script, "script_cf_multiplayer_event_team_change", ":exiting_player_no"),
		 ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"), 
         (store_trigger_param_2, ":killer_agent_no"), 
         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
         #adding 1 score points to killer agent's team. (special for "headquarters" and "team deathmatch" mod)
         (try_begin),
           (ge, ":killer_agent_no", 0),
           (agent_is_human, ":dead_agent_no"),
           (agent_is_human, ":killer_agent_no"),
           (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
           (le, ":killer_agent_team", 1), #0 or 1 is ok
           (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
           (neq, ":killer_agent_team", ":dead_agent_team"),
           (team_get_score, ":team_score", ":killer_agent_team"),
		   (try_begin),
		     (agent_is_non_player, ":dead_agent_no"),
             (val_add, ":team_score", 1),
		   (else_try),
             (val_add, ":team_score", 3),
		   (try_end),
           (team_set_score, ":killer_agent_team", ":team_score"),
         (try_end),
         ]),
		 
		 # MCA	
		(0, 0, ti_once, [],
		[
			(try_begin),
				# clear squad info
				(neg|multiplayer_is_server),
				(multiplayer_get_my_player, ":player_no"),
				(call_script, "script_mp_clear_squad_info", ":player_no"),
			(try_end),
		]),
         
      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),

           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),

           (player_get_agent_id, ":player_agent", ":player_no"),
           (assign, ":spawn_new", 0),
           (try_begin),
             (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
             (eq, ":player_first_spawn", 1),
             (assign, ":spawn_new", 1),
             (player_set_slot, ":player_no", slot_player_first_spawn, 0),
           (else_try),
             (try_begin),
               (lt, ":player_agent", 0),
               (assign, ":spawn_new", 1),
             (else_try),
               (neg|agent_is_alive, ":player_agent"),
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
               (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
               (assign, ":spawn_new", 1),
             (try_end),             
           (try_end),
           (eq, ":spawn_new", 1),
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (troop_get_inventory_slot, ":has_item", ":player_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),
		   (call_script, "script_multiplayer_get_bots_count", ":player_no"), 
		   (assign, ":bot_count", reg0),
		   (try_begin),
				(gt, ":bot_count", 0),
				(call_script, "script_multiplayer_get_spawn_point_close_to_bots", ":player_no"), 
				(assign, ":point_no", reg0),
		   (else_try), 
				(call_script, "script_multiplayer_find_spawn_point", ":player_team", 1, ":is_horseman"), 
				(assign, ":point_no", reg0), 
		   (end_try), 
		   (player_spawn_new_agent, ":player_no", ":point_no"),
		   (call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":player_no", ":player_team", ":point_no"), 
         (try_end),
         ]),

      (1, 0, 0, [], #do this in every new frame, but not at the same time
       [
         (multiplayer_is_server),
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), 
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),
      
      (20, 0, 0, [],
       [
         (multiplayer_is_server),
         #auto team balance control in every 20 seconds (tdm)
         (call_script, "script_check_team_balance"),
         ]),

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,
      multiplayer_battle_window_opened,

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),
  
  
  ###############################################
  ####################################  WAVE MODE
  ###############################################
  
  
	( 	"multiplayer_ccoop",mtf_battle_mode,-1, #captain_coop mode, aka "wave mode"
		"You lead your men to battle.",
    [
		(0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

		(8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

		(16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

		(24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
		(31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

		(32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

		(40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

		(48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

		(56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		
		
		(64,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(65,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(66,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(67,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(68,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(69,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		
		# prison cart entry points
		(70,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(71,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(72,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(73,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(74,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),	

		# empty slots
		(75,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(76,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(77,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(78,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(79,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		
		# enemy wave spawn points
		(80,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(81,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(82,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(83,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(84,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),	
		(85,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(86,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
		(87,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),	
	],
	
    [      
		common_battle_init_banner,

		multiplayer_server_check_polls,
		multiplayer_set_map_weather,

		(ti_on_agent_spawn, 0, 0, [],
		[
			(store_trigger_param_1, ":agent_no"),
			(call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
			(agent_get_team, ":agent_team_no", ":agent_no"),
			(try_begin),
				(eq, ":agent_team_no", 1), # enemies
				(gt, "$g_multiplayer_ccoop_wave_no", 20), # wave++
				(agent_set_max_hit_points, ":agent_no", 150),
				(agent_set_damage_modifier, ":agent_no", 130),
			(else_try),
				(eq, ":agent_team_no", 1), # enemies
				(gt, "$g_multiplayer_ccoop_wave_no", 10), # wave+
				(agent_set_max_hit_points, ":agent_no", 175),
				(agent_set_damage_modifier, ":agent_no", 150),
			(try_end),
		]),

		(ti_server_player_joined, 0, 0, [],
		[
			(store_trigger_param_1, ":player_no"),
			(call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
			
			# player has to wait for next round to respawn (make it -1 instead of 0 to prevent the player from spawning from prison cart this round)
			(player_set_slot, ":player_no", slot_player_first_spawn, -1),

			# clear squad info
			(call_script, "script_mp_clear_squad_info", ":player_no"),
			
			(call_script, "script_multiplayer_ccoop_send_troop_data_to_client", ":player_no"),
			
			(try_begin),
				(gt, "$g_multiplayer_ccoop_game_started", 0),
				
				(try_begin),
					(le, "$g_multiplayer_ccoop_enemy_respawn_secs", 45), # if 45 secs left to respawn
					(multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_count_down_visible, "$g_multiplayer_ccoop_enemy_respawn_secs", "$g_multiplayer_ccoop_wave_no"),
				(else_try),
					(multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_count_down_invisible, "$g_multiplayer_ccoop_enemy_respawn_secs", "$g_multiplayer_ccoop_wave_no"),
				(try_end),
			(try_end),			
		]),

		(ti_before_mission_start, 0, 0, [],
		[
			(assign, "$g_multiplayer_game_type", multiplayer_game_type_captain_coop),		  
			(call_script, "script_multiplayer_server_before_mission_start_common"),

			(call_script, "script_multiplayer_init_mission_variables"),
			(call_script, "script_multiplayer_remove_destroy_mod_targets"),
			(call_script, "script_multiplayer_remove_headquarters_flags"),
		]),

		(ti_after_mission_start, 0, 0, [], 
		[
			(set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
			(set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)

			(call_script, "script_initialize_all_scene_prop_slots"),         
			(call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
			
			(try_begin),
				(multiplayer_is_server),

				#(assign, "$g_multiplayer_ccoop_enemy_respawn_secs", multi_captain_coop_round_duration_in_sec), #count down time: 10mins
				(assign, "$g_multiplayer_ccoop_spawn_prison_cart_counter", 0),
				(assign, "$g_multiplayer_ccoop_spawn_player_and_squad_counter", 0),
				(assign, "$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots", -1),
			(try_end),
			
			(assign, "$g_multiplayer_ccoop_wave_no", 0),
			(assign, "$g_multiplayer_ccoop_game_started", 0),
			(assign, "$g_multiplayer_ccoop_enable_count_down", 0),
			(assign, "$g_multiplayer_ccoop_change_map", 0),
			(assign, "$g_multiplayer_squad_size", 6), # constant size for coop
			(assign, "$g_round_ended", 0),

			# destroy prison cart (since it is invisible when mission starts)
			(call_script, "script_multiplayer_ccoop_destroy_prison_cart"),
		]),

		(ti_on_multiplayer_mission_end, 0, 0, [],
		[
			# disable count down
			(assign, "$g_multiplayer_ccoop_enable_count_down", 0),
			(assign, "$g_multiplayer_ccoop_enemy_respawn_secs", 100000),
			(assign, "$g_multiplayer_ccoop_game_started", 0),
			
			
			(assign, "$g_multiplayer_stats_chart_opened_manually", 0),
			(start_presentation, "prsnt_multiplayer_stats_chart_deathmatch"),			
		]),
		
		(ti_on_player_exit, 0, 0, [],
		[
			# force kill all squad agents of the exiting player
			(store_trigger_param_1, ":exiting_player_no"),
			(call_script, "script_cf_multiplayer_event_team_change", ":exiting_player_no"),
		]),

		(ti_on_agent_killed_or_wounded, 0, 0, [],
		[
			(store_trigger_param_1, ":dead_agent_no"), 
			(store_trigger_param_2, ":killer_agent_no"), 
			(call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
			
			(agent_get_team, ":dead_agent_team", ":dead_agent_no"),			
			
			#add 1 score points to killer agent's team.
			(try_begin),
				(ge, ":killer_agent_no", 0),
				(agent_is_human, ":dead_agent_no"),
				(agent_is_human, ":killer_agent_no"),
				(agent_get_team, ":killer_agent_team", ":killer_agent_no"),
				(le, ":killer_agent_team", 1), #0 or 1 is ok
				(team_get_score, ":team_score", ":killer_agent_team"),
				(neq, ":killer_agent_team", ":dead_agent_team"),
				(val_add, ":team_score", 1),
				(team_set_score, ":killer_agent_team", ":team_score"),
			(try_end),
			 
			# if dead agent is in wave team
			(try_begin),
				(multiplayer_is_server),				
				(eq, ":dead_agent_team", 1),  # enemy (wave) side
				
				(call_script, "script_multiplayer_ccoop_check_reinforcement"),
				
				(assign, ":has_agents", 0),
				(try_for_agents, ":cur_agent"),
					(try_begin),
						(agent_is_human, ":cur_agent"),
						(agent_is_alive, ":cur_agent"),
						(agent_get_team, ":cur_agent_team", ":cur_agent"),
						(eq, ":cur_agent_team", 1),
						(val_add, ":has_agents", 1),
					(try_end),
					(gt, ":has_agents", 0), # break
				(try_end),				
				
				(eq, ":has_agents", 0), # if all enemies are dead
				
				(play_sound, "snd_team_scored_a_point"), # play victory sound
				
				# round cleared
				(assign, "$g_multiplayer_ccoop_enemy_respawn_secs", 32), # set 32 secs left for next wave
				
				# refill everyone's health (for refilling players' and squad members' health)
				(try_for_agents, ":cur_agent"),
					(agent_is_alive, ":cur_agent"),
					(agent_is_human, ":cur_agent"),
					
					# refill agent heath and ammo
					(agent_set_hit_points, ":cur_agent", 100),
					(agent_refill_ammo, ":cur_agent"),
					
					(try_begin),
						# if agent has a horse
						(agent_get_horse, ":horse_agent", ":cur_agent"), 
						(gt, ":horse_agent", -1), 
						(agent_is_alive, ":horse_agent"),
						# refill horse health
						(agent_set_hit_points, ":horse_agent", 100),
					#(else_try),
						# if player's horse is dead, we cannot respawn the horse due to restrictions in the engine
					(try_end),
					
				(try_end),
				
			(else_try),				
				(multiplayer_is_server),
				(eq, ":dead_agent_team", 0),  # players side
				
				#(display_debug_message, "@{!}dead agent is on our team!"),
				
				(assign, ":has_agents", 0),
				(try_for_agents, ":cur_agent"),
					(try_begin),
						(agent_is_human, ":cur_agent"),
						(agent_is_alive, ":cur_agent"),
						(agent_get_team, ":cur_agent_team", ":cur_agent"),
						(eq, ":cur_agent_team", 0),
						(val_add, ":has_agents", 1),						
					(try_end),
					(gt, ":has_agents", 0), #break
				(try_end),
				
				(eq, ":has_agents", 0),  # no player and bots left alive								
				
				(assign, "$g_multiplayer_ccoop_change_map", 5), #5 secs
				
			(else_try),	
				(neg|multiplayer_is_server), # client side
				
				(assign, ":has_agents", 0),
				(try_for_agents, ":cur_agent"),
					(try_begin),
						(agent_is_human, ":cur_agent"),
						(agent_is_alive, ":cur_agent"),
						(agent_get_team, ":cur_agent_team", ":cur_agent"),
						(eq, ":cur_agent_team", 1),
						(val_add, ":has_agents", 1),
					(try_end),
					(gt, ":has_agents", 0), # break
				(try_end),				
				
				(eq, ":has_agents", 0), # if all enemies are dead
				
				(play_sound, "snd_team_scored_a_point"), # play victory sound
				
			(try_end),
		]),
		 
		# one time execute
		(0, 0, ti_once, [],
		[
			(set_cheer_at_no_enemy, 0), # no cheer after all enemies are dead

			(try_begin),
				(neg|multiplayer_is_server),
				
				# clear squad info
				(multiplayer_get_my_player, ":player_no"),			
				(call_script, "script_mp_clear_squad_info", ":player_no"),
			(try_end),
		]),

		# if count down is enabled
		(1, 0, 0, [(gt, "$g_multiplayer_ccoop_enable_count_down", 0)],
		[
			(try_begin),
				(gt, "$g_multiplayer_ccoop_change_map", 0),
				
				(try_begin),
					(eq, "$g_multiplayer_ccoop_change_map", 4),
					(call_script, "script_multiplayer_ccoop_destroy_prison_cart"),
				(try_end),
				
				(val_sub, "$g_multiplayer_ccoop_change_map", 1),
				(eq, "$g_multiplayer_ccoop_change_map", 0),				
				(assign, "$g_multiplayer_ccoop_enable_count_down", 0),
				(assign, "$g_round_ended", 1),
			(else_try),
				(gt, "$g_multiplayer_ccoop_enemy_respawn_secs", 0),
				(val_sub, "$g_multiplayer_ccoop_enemy_respawn_secs", 1),

				(try_begin),
					(gt, "$g_multiplayer_ccoop_enemy_respawn_secs", 59),
					(store_mod, ":mod", "$g_multiplayer_ccoop_enemy_respawn_secs", 60),
					(eq, ":mod", 0),
					(store_div, reg0, "$g_multiplayer_ccoop_enemy_respawn_secs", 60),
					(neg|multiplayer_is_dedicated_server),
					(display_message, "str_next_wave_in_reg0_mins", 0xFFDE6300),
				(try_end),
				
				(try_begin),
					(eq, "$g_multiplayer_ccoop_enemy_respawn_secs", 30), #if 30secs left to next wave
					(multiplayer_is_server),

					# give round bonus gold at the start of each wave (whether the previous wave is cleared or it is timed out)
					(call_script, "script_multiplayer_ccoop_give_round_bonus_gold"),
					
					(val_add, "$g_multiplayer_ccoop_wave_no", 1), # increment wave no

					(try_begin),
						(eq, "$g_multiplayer_ccoop_wave_no", 31),
						# game end win condition
						# initiate round end/change map duration
						(assign, "$g_multiplayer_ccoop_change_map", 5), #5 secs
					(try_end),
					
					# destroy prison cart (since current wave is timed out and next wave is coming in 30 seconds) or
					# destroy prison cart (since round is cleared and everyone will respawn automatically)
					(call_script, "script_multiplayer_ccoop_destroy_prison_cart"),
					
					# respawn all dead players (with some delay)
					(call_script, "script_multiplayer_ccoop_start_player_and_squad_respawn_period", 1),
										
					# sync clients count down counter
					(get_max_players, ":max_players"),
					(store_sub, ":respawn_secs", "$g_multiplayer_ccoop_enemy_respawn_secs", 1), # send to clients as 1 sec decreased					
					(try_for_range, ":cur_player", 1, ":max_players"),						
						(player_is_active, ":cur_player"),
						(multiplayer_send_3_int_to_player, ":cur_player", multiplayer_event_other_events, multiplayer_event_other_event_ccoop_count_down_visible, ":respawn_secs", "$g_multiplayer_ccoop_wave_no"),
					(try_end),
					
					(call_script, "script_multiplayer_ccoop_prepare_spawn_wave"),
					
					(store_mission_timer_a, "$g_multiplayer_ccoop_next_wave_start_time"),
					(val_add, "$g_multiplayer_ccoop_next_wave_start_time", "$g_multiplayer_ccoop_enemy_respawn_secs"),
					(start_presentation, "prsnt_multiplayer_ccoop_next_wave_time_counter"),
					(start_presentation, "prsnt_multiplayer_flag_projection_display_ccoop_wave"),
				(else_try),
					(lt, "$g_multiplayer_ccoop_enemy_respawn_secs", 1),
					(multiplayer_is_server),
					
					# generate count down
					(call_script, "script_multiplayer_ccoop_calculate_round_duration"),
					
					# spawn wave
					(call_script, "script_multiplayer_ccoop_spawn_wave", 100),
				(try_end),
				
			(try_end),
		]),
				
		# prison cart and player&bot spawn management
		(1, 0, 0, [(multiplayer_is_server),],		
		[
			(get_max_players, ":max_players"),
			
			# prison cart management
			(try_begin),
				# if move underground is initiated
				(gt, "$g_multiplayer_ccoop_move_prison_cart", 0),  
					
				(store_mission_timer_a, ":current_time"),
				(store_sub, ":time_left", "$g_multiplayer_ccoop_move_prison_cart", ":current_time"),
				
				(try_begin),
					(le, ":time_left", 0),
					
					(display_debug_message, "@{!}sending prisoner cart 6 feet underground!"),
					
					(set_fixed_point_multiplier, 100), 
					
					(scene_prop_get_instance, ":prison_cart", "spr_prison_cart", 0),
					(scene_prop_get_instance, ":prison_cart_door_left", "spr_prison_cart_door_left", 0),
					(scene_prop_get_instance, ":prison_cart_door_right", "spr_prison_cart_door_right", 0),
					
					(prop_instance_get_position, pos1, ":prison_cart"),
					(position_set_z, pos1, -4000), #40m down
					(prop_instance_set_position, ":prison_cart", pos1),	
					(prop_instance_set_position, ":prison_cart_door_left", pos1),
					(prop_instance_set_position, ":prison_cart_door_right", pos1),
					
					(assign, "$g_multiplayer_ccoop_move_prison_cart", 0),
				(try_end),
			
			(else_try),
				(gt, "$g_prison_cart_point", 0), # if visible				
				
				(scene_prop_get_instance, ":prison_cart_door_left", "spr_prison_cart_door_left", 0),
				(scene_prop_get_hit_points, ":left_door", ":prison_cart_door_left"),
				
				(scene_prop_get_instance, ":prison_cart_door_right", "spr_prison_cart_door_right", 0),
				(scene_prop_get_hit_points, ":right_door", ":prison_cart_door_right"),
					
				(try_begin),
					(this_or_next|lt, ":left_door", 1),  # left door's broken
					(lt, ":right_door", 1),  # right door's broken
										
					# destroy prison cart (since doors are cracked)
					(call_script, "script_multiplayer_ccoop_destroy_prison_cart"),
					
					# respawn all dead players (with some delay)
					(call_script, "script_multiplayer_ccoop_start_player_and_squad_respawn_period", 0),
					
				(try_end),
				
				# check if prison cart is spawned and there is no dead player (may occur if dead players quit the game or change their faction to spectator)
				(assign, ":is_anyone_dead", 0),
				(try_for_range, ":cur_player", 0, ":max_players"),
					(eq, ":is_anyone_dead", 0),
					(player_is_active, ":cur_player"),
					(player_get_team_no, ":player_team", ":cur_player"),
					(eq, ":player_team", 0),
					(player_get_agent_id, ":player_agent", ":cur_player"),
					(try_begin),
						(ge, ":player_agent", 0),
						(try_begin),
							(neg|agent_is_alive, ":player_agent"),
							(assign, ":is_anyone_dead", 1),
						(try_end),
					(else_try),
						(assign, ":is_anyone_dead", 1),
					(end_try),
				(try_end),
				(try_begin),
					(eq, ":is_anyone_dead", 0),
					# destroy prison cart (since there is no dead player left in the game)
					(call_script, "script_multiplayer_ccoop_destroy_prison_cart"),
				(try_end),
				
			(else_try),
			
				# if prison cart is not spawned and there is a dead player, then spawn the prison cart
				(assign, ":is_anyone_dead", 0),
				(try_for_range, ":cur_player", 0, ":max_players"),
					(eq, ":is_anyone_dead", 0),				
					(player_is_active, ":cur_player"),
					(player_get_team_no, ":player_team", ":cur_player"),
					(eq, ":player_team", 0),
					(player_get_agent_id, ":player_agent", ":cur_player"),
					(ge, ":player_agent", 0),
					(neg|agent_is_alive, ":player_agent"),
					(assign, ":is_anyone_dead", 1),
				(try_end),
				(try_begin),
					(eq, ":is_anyone_dead", 1),
					(eq, "$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots", 1), # if cart is not spawned before in this round, otherwise that value would be 0
					# spawn prison cart with 5 second delay
					(le, "$g_multiplayer_ccoop_spawn_player_and_squad_counter", 0), # if not in player spawn period
					(eq, "$g_multiplayer_ccoop_spawn_prison_cart_counter", 0), # if not in prison cart spawn period
					(assign, "$g_multiplayer_ccoop_spawn_prison_cart_counter", 5),
					(display_debug_message, "@{!}spawn prison cart 5 secs initiated!"),
				(try_end),
				
				(try_begin),
					(gt, "$g_multiplayer_ccoop_spawn_prison_cart_counter", 0),
					(val_sub, "$g_multiplayer_ccoop_spawn_prison_cart_counter", 1),
					(display_debug_message, "@{!}spawn prison cart!"),
					(try_begin),
						(eq, "$g_multiplayer_ccoop_spawn_prison_cart_counter", 0),
						(call_script, "script_multiplayer_ccoop_spawn_prison_cart"),
					(try_end),
				(try_end),
				
			(try_end),
			
			# player&bot spawn management
			(try_begin),
				(multiplayer_is_server),
				(gt, "$g_multiplayer_ccoop_spawn_player_and_squad_counter", 0),
				(val_sub, "$g_multiplayer_ccoop_spawn_player_and_squad_counter", 1),
				(try_begin),
					(lt, "$g_multiplayer_ccoop_spawn_player_and_squad_counter", 25),
					
					# respawn all dead players
					(get_max_players, ":max_players"),
					(try_for_range, ":cur_player", 0, ":max_players"),
						(player_is_active, ":cur_player"),
						(player_get_team_no, ":player_team", ":cur_player"), # if player is not spectator
						(lt, ":player_team", multi_team_spectator),
						(player_get_agent_id, ":player_agent", ":cur_player"),
						
						(try_begin),
							(this_or_next|lt, ":player_agent", 0), #if not spawned or
							(neg|agent_is_alive, ":player_agent"), #if agent is dead
							
							(try_begin),
								# if first spawn this round
								(player_get_slot, ":player_first_spawn", ":cur_player", slot_player_first_spawn),
								(eq, ":player_first_spawn", 1),
								
								(call_script, "script_multiplayer_ccoop_spawn_player_and_bots", ":cur_player"),
								
								# if spawned
								(try_begin),
									(eq, reg0, 1),
									(player_set_slot, ":cur_player", slot_player_first_spawn, 0),
								(try_end),
								
							(try_end),
							
						(else_try),
							(assign, reg0, "$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots"),
							(display_debug_message, "@{!}g_multiplayer_ccoop_spawn_alive_player_squad: {reg0}"),
						
							(eq, "$g_multiplayer_ccoop_spawn_alive_player_squad_and_minus_one_first_spawn_slots_and_minus_one_first_spawn_slots", 1),
							(neg|player_is_busy_with_menus, ":cur_player"), # if player is not busy with menus
							(player_get_troop_id, ":player_troop", ":cur_player"), # if troop is not selected do not spawn his bots	
							(ge, ":player_troop", 0),
							
							# buy squads of alive player
							(call_script, "script_multiplayer_upgrade_player_equipment", ":cur_player"),
							#(call_script, "script_multiplayer_get_spawn_point_close_to_bots", ":cur_player"),
							(call_script, "script_multiplayer_get_spawn_point_close_to_player", ":cur_player"),
							(call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":cur_player", 0, reg0),
						(try_end),
						
						
					(try_end),
					
					
					
				(try_end),
				
			(try_end),
		]),

				
		# first spawn
		(1, 0, 0, 
		[			
			(eq, "$g_multiplayer_ccoop_game_started", 0),
			(multiplayer_is_server),
		],
		
		[			
			(assign, ":any_player_spawned", 0),
			
			(get_max_players, ":num_players"),
			(try_for_range, ":player_no", 0, ":num_players"),
				(player_is_active, ":player_no"),
				
				(call_script, "script_multiplayer_ccoop_spawn_player_and_bots", ":player_no"),
				
				(try_begin),
					(eq, ":any_player_spawned", 0),
					(gt, reg0, 0),
					(assign, ":any_player_spawned", 1),
				(try_end),
			(try_end),
			
			(try_begin),
				(ge, ":any_player_spawned", 1),
				
				#(display_debug_message, "@{!}first spawn" ),
				(assign, "$g_multiplayer_ccoop_game_started", 1),
				
				(assign, "$g_multiplayer_ccoop_enemy_respawn_secs", 31), # set 31 secs left for next wave
				(assign, "$g_multiplayer_ccoop_enable_count_down", 1), # enable count down
				
				(call_script, "script_multiplayer_ccoop_start_player_and_squad_respawn_period", 1),
			(try_end),
		]),
    
		multiplayer_server_check_end_map,

		(ti_tab_pressed, 0, 0, [],
		[
			(try_begin),
				(eq, "$g_multiplayer_mission_end_screen", 0),
				(assign, "$g_multiplayer_stats_chart_opened_manually", 1),
				(start_presentation, "prsnt_multiplayer_stats_chart_deathmatch"),
			(try_end),
		]),

		multiplayer_once_at_the_first_frame,
		#multiplayer_battle_window_opened,
		(ti_battle_window_opened, 0, 0, [], [
			#(start_presentation, "prsnt_multiplayer_round_time_counter"),
			#(start_presentation, "prsnt_multiplayer_team_score_display"),
			(start_presentation, "prsnt_multiplayer_flag_projection_display_ccoop"),
			(start_presentation, "prsnt_multiplayer_flag_projection_display_ccoop_wave"),
			(start_presentation, "prsnt_multiplayer_ccoop_next_wave_time_counter"),
        ]),

		(ti_escape_pressed, 0, 0, [],
		[
			(neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
			(neg|is_presentation_active, "prsnt_multiplayer_stats_chart_deathmatch"),
			(eq, "$g_waiting_for_confirmation_to_terminate", 0),
			(start_presentation, "prsnt_multiplayer_escape_menu"),
		]),
	]),
  
  
  
  #############################  END OF WAVE MODE
  ###############################################
  
  
  
#OiM captain siege mode:
    (
    "multiplayer_csg",mtf_battle_mode,-1, #siege
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1|mtef_no_auto_reset,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),
     ],
    [
      
      multiplayer_server_check_belfry_movement,      

      common_battle_init_banner,

      multiplayer_server_check_polls,
	  multiplayer_set_map_weather,
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),

         (try_begin),
           (multiplayer_is_server),
           (this_or_next|player_is_active, ":player_no"),
           (eq, ":player_no", 0),
             (store_mission_timer_a, ":round_time"),
             (val_sub, ":round_time", "$g_round_start_time"),
             (try_begin),
               (lt, ":round_time", 25),
               (assign, ":number_of_respawns_spent", 0),
             (else_try),
               (lt, ":round_time", 60),
               (assign, ":number_of_respawns_spent", 1),
             (else_try),
               (lt, ":round_time", 105),
               (assign, ":number_of_respawns_spent", 2),
             (else_try),
               (lt, ":round_time", 160),
               (assign, ":number_of_respawns_spent", 3),
             (else_try),
               (assign, ":number_of_respawns_spent", "$g_multiplayer_number_of_respawn_count"),
             (try_end),
             (player_set_slot, ":player_no", slot_player_spawn_count, ":number_of_respawns_spent"),             
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_spent, ":number_of_respawns_spent"),
           (try_end),         
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_siege),
         (call_script, "script_multiplayer_server_before_mission_start_common"),

         (try_begin),
           (multiplayer_is_server),
           (try_for_range, ":cur_flag_slot", multi_data_flag_pull_code_begin, multi_data_flag_pull_code_end),
             (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", -1),
           (try_end),
           (assign, "$g_my_spawn_count", 0),
         (else_try),
           (assign, "$g_my_spawn_count", 0),
         (try_end),
      
         (assign, "$g_waiting_for_confirmation_to_terminate", 0),
         (assign, "$g_round_ended", 0),
         (try_begin),
           (multiplayer_is_server),
           (assign, "$g_round_start_time", 0),
         (try_end),
         (assign, "$my_team_at_start_of_round", -1),

         (assign, "$g_flag_is_not_ready", 0),

         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"),
         ]),

      (ti_after_mission_start, 0, 0, [], 
       [
         (call_script, "script_determine_team_flags", 0),
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         
         (call_script, "script_initialize_all_scene_prop_slots"),
         
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),

         (assign, "$g_number_of_flags", 0),
         (try_begin),
           (multiplayer_is_server),
           (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         
           #place base flags
           (entry_point_get_position, pos1, multi_siege_flag_point),
           (set_spawn_position, pos1),
           (spawn_scene_prop, "spr_headquarters_pole_code_only", 0),         
           (position_move_z, pos1, multi_headquarters_pole_height),         
           (set_spawn_position, pos1),
           (spawn_scene_prop, "$team_1_flag_scene_prop", 0),
           (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, "$g_number_of_flags"),
           (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", 1),
         (try_end),
         (val_add, "$g_number_of_flags", 1),

         (try_begin),
           (multiplayer_is_server),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),
           (try_end),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),
           (try_end),

           (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_a"),
           (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_b"),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
           (try_end),
         
           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
           (try_end),

           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
           (try_end),

           (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
           (try_for_range, ":belfry_no", 0, ":num_belfries"),
             (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
             (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
           (try_end),
         (try_end),
         ]),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),

         (try_begin), #if my initial team still not initialized, find and assign its value.
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (eq, ":my_agent_id", ":agent_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),

         (try_begin),
           (neg|multiplayer_is_server),
           (try_begin),
             (eq, "$g_round_ended", 1),
             (assign, "$g_round_ended", 0),
             (assign, "$g_my_spawn_count", 0),

             #initialize scene object slots at start of new round at clients.
             (call_script, "script_initialize_all_scene_prop_slots"),

             #these lines are done in only clients at start of each new round.
             (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
             (call_script, "script_initialize_objects_clients"),
             #end of lines
           (try_end),  
         (try_end),         

         (try_begin), 
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (eq, ":my_agent_id", ":agent_no"),

           (val_add, "$g_my_spawn_count", 1),
         
           (try_begin),
             (ge, "$g_my_spawn_count", "$g_multiplayer_number_of_respawn_count"),
             (gt, "$g_multiplayer_number_of_respawn_count", 0),
             (multiplayer_get_my_player, ":my_player_no"),
             (player_get_team_no, ":my_player_team_no", ":my_player_no"),
             (eq, ":my_player_team_no", 0),
             (assign, "$g_my_spawn_count", 999),
           (try_end),
         (try_end),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"),
         (store_trigger_param_2, ":killer_agent_no"),

         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),
         
         (try_begin), #if my initial team still not initialized, find and assign its value.
           (lt, "$my_team_at_start_of_round", 0),
           (multiplayer_get_my_player, ":my_player_no"),
           (ge, ":my_player_no", 0),
           (player_get_agent_id, ":my_agent_id", ":my_player_no"),
           (ge, ":my_agent_id", 0),
           (agent_get_team, "$my_team_at_start_of_round", ":my_agent_id"),
         (try_end),         
         
         (try_begin),
           (multiplayer_is_server),
           (agent_is_human, ":dead_agent_no"),
           (neg|agent_is_non_player, ":dead_agent_no"),
           (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
           (player_set_slot, ":dead_agent_player_id", slot_player_spawned_this_round, 0),
         (try_end),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart"),
         ]),
      
      # Change interval for obvious reasons..
      (1, 0, 0, [], #if this trigger takes lots of time in the future and make server machine runs siege mod
                    #very slow with lots of players make period of this trigger 1 seconds, but best is 0. Currently
                    #we are testing this mod with few players and no speed problem occured.
      [
        (multiplayer_is_server),
        (eq, "$g_round_ended", 0),
        #main trigger which controls which agent is moving/near which flag.
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
          (troop_get_slot, ":current_owner_code", "trp_multiplayer_data", ":cur_flag_owner_counts_slot"),
          (store_div, ":old_team_1_agent_count", ":current_owner_code", 100),
          (store_mod, ":old_team_2_agent_count", ":current_owner_code", 100),
        
          (assign, ":number_of_agents_around_flag_team_1", 0),
          (assign, ":number_of_agents_around_flag_team_2", 0),

          (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"), 
          (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.

          (get_max_players, ":num_players"),
            (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":cur_agent", ":player_no"),            
            (ge, ":cur_agent", 0),
            (agent_is_alive, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (agent_get_position, pos1, ":cur_agent"), #pos1 holds agent's position.
            (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
            (get_sq_distance_between_position_heights, ":squared_height_dist", pos0, pos1),
            (val_add, ":squared_dist", ":squared_height_dist"),
            (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
            (try_begin),
              (eq, ":cur_agent_team", 0),
              (val_add, ":number_of_agents_around_flag_team_1", 1),
            (else_try),
              (eq, ":cur_agent_team", 1),
              (val_add, ":number_of_agents_around_flag_team_2", 1),
            (try_end),
          (try_end),

          (try_begin),
            (this_or_next|neq, ":old_team_1_agent_count", ":number_of_agents_around_flag_team_1"),
            (neq, ":old_team_2_agent_count", ":number_of_agents_around_flag_team_2"),

            (store_add, ":cur_flag_pull_code_slot", multi_data_flag_pull_code_begin, ":flag_no"),
            (troop_get_slot, ":cur_flag_pull_code", "trp_multiplayer_data", ":cur_flag_pull_code_slot"),
            (store_mod, ":cur_flag_pull_message_seconds_past", ":cur_flag_pull_code", 100),
            (store_div, ":cur_flag_puller_team_last", ":cur_flag_pull_code", 100),

            (try_begin),        
              (eq, ":old_team_2_agent_count", 0),
              (gt, ":number_of_agents_around_flag_team_2", 0),
              (eq, ":number_of_agents_around_flag_team_1", 0),
              (assign, ":puller_team", 2),

              (store_mul, ":puller_team_multiplied_by_100", ":puller_team", 100),
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_pull_code_slot", ":puller_team_multiplied_by_100"),

              (this_or_next|neq, ":cur_flag_puller_team_last", ":puller_team"),
              (ge, ":cur_flag_pull_message_seconds_past", 25),

              (store_mul, ":flag_code", ":puller_team", 100),
              (val_add, ":flag_code", ":flag_no"),
            (try_end),

            (try_begin),
              (store_mul, ":current_owner_code", ":number_of_agents_around_flag_team_1", 100),
              (val_add, ":current_owner_code", ":number_of_agents_around_flag_team_2"),        
              (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owner_counts_slot", ":current_owner_code"),
              (get_max_players, ":num_players"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_set_num_agents_around_flag", ":flag_no", ":current_owner_code"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_num_agents_around_flag, ":flag_no", ":current_owner_code"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),

        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (eq, "$g_round_ended", 0), #if round still continues and any team did not sucseed yet
          (eq, "$g_flag_is_not_ready", 0), #if round still continues and any team did not sucseed yet
        
          (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"), 
          (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.            

          (try_begin),
            (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),

            #flag_id holds shown flag after this point
            (prop_instance_get_position, pos1, ":flag_id"), #pos1 holds gray/red/blue (current shown) flag position.
            (try_begin),
              (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),        
              (lt, ":squared_dist", multi_headquarters_distance_sq_to_change_flag), #if distance is less than 2 meters
              
              (prop_instance_is_animating, ":is_animating", ":flag_id"),
              (eq, ":is_animating", 1),

              #end of round, attackers win
              (assign, "$g_winner_team", 1),
              (prop_instance_stop_animating, ":flag_id"),        
        
              (get_max_players, ":num_players"), 
              #for only server itself-----------------------------------------------------------------------------------------------
              (call_script, "script_draw_this_round", "$g_winner_team"),
              #for only server itself-----------------------------------------------------------------------------------------------
              (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                (player_is_active, ":player_no"),
                (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
              (try_end),

              (assign, "$g_flag_is_not_ready", 1),
            (try_end),        
          (try_end),
        (try_end),
        ]),

      (0, 0, 0, [], #if there is nobody in any teams do not reduce round time.
       [
         #(multiplayer_is_server),
         (assign, ":human_agents_spawned_at_team_1", "$g_multiplayer_num_bots_team_1"),
         (assign, ":human_agents_spawned_at_team_2", "$g_multiplayer_num_bots_team_2"),
         
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"), 
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":human_agents_spawned_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":human_agents_spawned_at_team_2", 1),
           (try_end),
         (try_end),

         (try_begin),
           (this_or_next|eq, ":human_agents_spawned_at_team_1", 0),
           (eq, ":human_agents_spawned_at_team_2", 0),

           (store_mission_timer_a, ":seconds_past_since_round_started"),
           (val_sub, ":seconds_past_since_round_started", "$g_round_start_time"),
           (le, ":seconds_past_since_round_started", 2),
                  
           (store_mission_timer_a, "$g_round_start_time"),
         (try_end),
       ]),

      (1, 0, 0, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 0),
                 (eq, "$g_flag_is_not_ready", 0),
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":seconds_past_in_round", ":current_time", "$g_round_start_time"),
                 (ge, ":seconds_past_in_round", "$g_multiplayer_round_max_seconds")],
       [
         (assign, ":flag_no", 0),
         (store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
         (troop_get_slot, ":current_owner_code", "trp_multiplayer_data", ":cur_flag_owner_counts_slot"),
         (store_mod, ":team_2_agent_count_around_flag", ":current_owner_code", 100),

         (try_begin),
           (eq, ":team_2_agent_count_around_flag", 0),
         
           (store_mission_timer_a, "$g_round_finish_time"),
           (assign, "$g_round_ended", 1),
           (assign, "$g_flag_is_not_ready", 1),
        
           (assign, "$g_winner_team", 0),

           (get_max_players, ":num_players"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (call_script, "script_draw_this_round", "$g_winner_team"),
           #for only server itself-----------------------------------------------------------------------------------------------
           (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
             (player_is_active, ":player_no"),
             (multiplayer_send_int_to_player, ":player_no", multiplayer_event_draw_this_round, "$g_winner_team"),
           (try_end),
         (try_end),
         ]),          

      (1, 0, 0, [],
      [
        (multiplayer_is_server),
        #trigger for calculating seconds past after that flag's pull message has shown          
        (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
          (store_add, ":cur_flag_pull_code_slot", multi_data_flag_pull_code_begin, ":flag_no"),
          (troop_get_slot, ":cur_flag_pull_code", "trp_multiplayer_data", ":cur_flag_pull_code_slot"),
          (store_mod, ":cur_flag_pull_message_seconds_past", ":cur_flag_pull_code", 100),
          (try_begin),
            (ge, ":cur_flag_pull_code", 100),
            (lt, ":cur_flag_pull_message_seconds_past", 25),
            (val_add, ":cur_flag_pull_code", 1),
            (troop_set_slot, "trp_multiplayer_data", ":cur_flag_pull_code_slot", ":cur_flag_pull_code"),
          (try_end),
        (try_end),        
      ]),               

      (10, 0, 0, [(multiplayer_is_server)],
       [
         #auto team balance control during the round         
         (assign, ":number_of_players_at_team_1", 0),
         (assign, ":number_of_players_at_team_2", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 0, ":num_players"),
           (player_is_active, ":cur_player"),
           (player_get_team_no, ":player_team", ":cur_player"),
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":number_of_players_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":number_of_players_at_team_2", 1),
           (try_end),         
         (try_end),
         #end of counting active players per team.
         (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
         (assign, ":number_of_players_will_be_moved", 0),
         (try_begin),
           (try_begin),
             (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
             (le, ":difference_of_number_of_players", ":checked_value"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
           (else_try),
             (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
           (try_end),          
         (try_end),         
         #number of players will be moved calculated. (it is 0 if no need to make team balance)
         (try_begin),
           (gt, ":number_of_players_will_be_moved", 0),
           (try_begin),
             (eq, "$g_team_balance_next_round", 0),
         
             (assign, "$g_team_balance_next_round", 1),

             #for only server itself-----------------------------------------------------------------------------------------------
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
             #for only server itself-----------------------------------------------------------------------------------------------     
             (get_max_players, ":num_players"),                               
             (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
               (player_is_active, ":player_no"),
               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
             (try_end),
             
             (call_script, "script_warn_player_about_auto_team_balance"),
           (try_end),
         (try_end),           
         #team balance check part finished
         ]),          

      (1, 0, 3, [(multiplayer_is_server),
                 (eq, "$g_round_ended", 1),
                 (store_mission_timer_a, ":seconds_past_till_round_ended"),
                 (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
                 (ge, ":seconds_past_till_round_ended", "$g_multiplayer_respawn_period")],
       [
         #auto team balance control at the end of round         
         (assign, ":number_of_players_at_team_1", 0),
         (assign, ":number_of_players_at_team_2", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":cur_player", 0, ":num_players"),
           (player_is_active, ":cur_player"),
           (player_get_team_no, ":player_team", ":cur_player"),
           (try_begin),
             (eq, ":player_team", 0),
             (val_add, ":number_of_players_at_team_1", 1),
           (else_try),
             (eq, ":player_team", 1),
             (val_add, ":number_of_players_at_team_2", 1),
           (try_end),         
         (try_end),
         #end of counting active players per team.
         (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
         (assign, ":number_of_players_will_be_moved", 0),
         (try_begin),
           (try_begin),
             (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
             (le, ":difference_of_number_of_players", ":checked_value"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
             (assign, ":team_with_more_players", 1),
             (assign, ":team_with_less_players", 0),
           (else_try),
             (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
             (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
             (assign, ":team_with_more_players", 0),
             (assign, ":team_with_less_players", 1),
           (try_end),          
         (try_end),         
         #number of players will be moved calculated. (it is 0 if no need to make team balance)
         (try_begin),
           (gt, ":number_of_players_will_be_moved", 0),
           (try_begin),
             (try_for_range, ":unused", 0, ":number_of_players_will_be_moved"), 
               (assign, ":max_player_join_time", 0),
               (assign, ":latest_joined_player_no", -1),
               (get_max_players, ":num_players"),                               
               (try_for_range, ":player_no", 0, ":num_players"),
                 (player_is_active, ":player_no"),
                 (player_get_team_no, ":player_team", ":player_no"),
                 (eq, ":player_team", ":team_with_more_players"),
                 (player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
                 (try_begin),
                   (gt, ":player_join_time", ":max_player_join_time"),
                   (assign, ":max_player_join_time", ":player_join_time"),
                   (assign, ":latest_joined_player_no", ":player_no"),
                 (try_end),
               (try_end),
               (try_begin),
                 (ge, ":latest_joined_player_no", 0),
                 (try_begin),
                   #if player is living add +1 to his kill count because he will get -1 because of team change while living.
                   (player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"), 
                   (ge, ":latest_joined_agent_id", 0),
                   (agent_is_alive, ":latest_joined_agent_id"),

                   (player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
                   (val_add, ":player_kill_count", 1),
                   (player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),

                   (player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
                   (val_sub, ":player_death_count", 1),
                   (player_set_death_count, ":latest_joined_player_no", ":player_death_count"),

                   (player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
                   (val_add, ":player_score", 1),
                   (player_set_score, ":latest_joined_player_no", ":player_score"),

                   (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                     (player_is_active, ":player_no"),
                     (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
                   (try_end),         

                   (player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
                   (player_get_gold, ":player_gold", ":latest_joined_player_no"),
                   (val_add, ":player_gold", ":old_items_value"),
                   (player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
                 (end_try),

				 (call_script, "script_mp_set_player_team_no", ":latest_joined_player_no", ":team_with_less_players", 0),
                 (multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
               (try_end),
             (try_end),
             #tutorial message (after team balance)
             
             #(tutorial_message_set_position, 500, 500),
             #(tutorial_message_set_size, 30, 30),
             #(tutorial_message_set_center_justify, 1),
             #(tutorial_message, "str_auto_team_balance_done", 0xFFFFFFFF, 5),
             
             #for only server itself
             (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), 

             #no need to send also server here
             (multiplayer_get_my_player, ":my_player_no"),
             (get_max_players, ":num_players"),                               
             (try_for_range, ":player_no", 0, ":num_players"),
               (player_is_active, ":player_no"),
               (neq, ":my_player_no", ":player_no"),
               (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
             (try_end),
             (assign, "$g_team_balance_next_round", 0),
           (try_end),
         (try_end),           
         #team balance check part finished
         (assign, "$g_team_balance_next_round", 0),

         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
           (player_set_slot, ":player_no", slot_player_spawned_at_siege_round, 0),           
           (player_get_agent_id, ":player_agent", ":player_no"),
           (ge, ":player_agent", 0),
           (agent_is_alive, ":player_agent"),
           (player_save_picked_up_items_for_next_spawn, ":player_no"),
           (player_get_value_of_original_items, ":old_items_value", ":player_no"),
           (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, ":old_items_value"),
         (try_end),

         #money management
         (assign, ":per_round_gold_addition", multi_battle_round_team_money_add),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_get_gold, ":player_gold", ":player_no"),
           (player_get_team_no, ":player_team", ":player_no"),
         
           (try_begin),
             (this_or_next|eq, ":player_team", 0),
             (eq, ":player_team", 1),
             (val_add, ":player_gold", ":per_round_gold_addition"), 
           (try_end),

           #(below lines added new at 25.11.09 after Armagan decided new money system)
           (try_begin),
             (player_get_slot, ":old_items_value", ":player_no", slot_player_last_rounds_used_item_earnings),
             (store_add, ":player_total_potential_gold", ":player_gold", ":old_items_value"),
             (store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
             (lt, ":player_total_potential_gold", ":minimum_gold"),
             (store_sub, ":additional_gold", ":minimum_gold", ":player_total_potential_gold"),
             (val_add, ":player_gold", ":additional_gold"),
           (try_end),
           #new money system addition end

           (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
         (try_end),

         #initialize my team at start of round (it will be assigned again at next round's first death)
         (assign, "$my_team_at_start_of_round", -1),

         #clear scene and end round
         (multiplayer_clear_scene),
         
         #assigning everbody's spawn counts to 0
         (assign, "$g_my_spawn_count", 0),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (player_set_slot, ":player_no", slot_player_spawn_count, 0),
         (try_end),

         #(call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_initialize_objects"),

         #initialize moveable object positions
         (call_script, "script_multiplayer_initialize_belfry_wheel_rotations"),
         (call_script, "script_multiplayer_close_gate_if_it_is_open"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
         (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_a"),
         (call_script, "script_move_belfries_to_their_first_entry_point", "spr_belfry_b"),
         
         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
         (try_end),

         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_a", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
         (try_end),

         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, 0),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, 0),
         (try_end),

         (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
         (try_for_range, ":belfry_no", 0, ":num_belfries"),
           (scene_prop_get_instance, ":belfry_scene_prop_id", "spr_belfry_b", ":belfry_no"),
           (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
         (try_end),

         #initialize flag coordinates (move up the flag at pole)
         (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
           (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
           (prop_instance_get_position, pos1, ":pole_id"),
           (position_move_z, pos1, multi_headquarters_pole_height),
           (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
           (prop_instance_stop_animating, ":flag_id"),
           (prop_instance_set_position, ":flag_id", pos1),
         (try_end),
         
         (assign, "$g_round_ended", 0),
         
         (store_mission_timer_a, "$g_round_start_time"),
         (call_script, "script_initialize_all_scene_prop_slots"),

         #initialize round start time for clients
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, -9999),
         (try_end),         

         (assign, "$g_flag_is_not_ready", 0),
       ]),
           
      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
           (player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),
           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),
           (player_get_agent_id, ":player_agent", ":player_no"), #new added for siege mod
         
           (assign, ":spawn_new", 0), 
           (assign, ":num_active_players_in_team_0", 0),
           (assign, ":num_active_players_in_team_1", 0),
           (try_begin),
             (assign, ":num_active_players", 0),
             (get_max_players, ":num_players"),
             (try_for_range, ":cur_player", 0, ":num_players"),
               (player_is_active, ":cur_player"),

               (player_get_team_no, ":cur_player_team", ":cur_player"),
               (try_begin),
                 (eq, ":cur_player_team", 0),
                 (val_add, ":num_active_players_in_team_0", 1),
               (else_try),
                 (eq, ":cur_player_team", 1),
                 (val_add, ":num_active_players_in_team_1", 1),
               (try_end),

               (val_add, ":num_active_players", 1),
             (try_end),
             (store_mission_timer_a, ":round_time"),
             (val_sub, ":round_time", "$g_round_start_time"),
                  
             (eq, "$g_round_ended", 0),
         
             (try_begin), #addition for siege mod to allow players spawn more than once (begin)
               (lt, ":player_agent", 0), 

               (try_begin), #new added begin, to avoid siege-crack (rejoining of defenders when they die)
                 (eq, ":player_team", 0), 
                 (player_get_slot, ":player_last_team_select_time", ":player_no", slot_player_last_team_select_time),
                 (store_mission_timer_a, ":current_time"),
                 (store_sub, ":elapsed_time", ":current_time", ":player_last_team_select_time"),
                 
                 (assign, ":player_team_respawn_period", "$g_multiplayer_respawn_period"), 
                 (val_add, ":player_team_respawn_period", multiplayer_siege_mod_defender_team_extra_respawn_time), #new added for siege mod
                 (lt, ":elapsed_time", ":player_team_respawn_period"),

                 (store_sub, ":round_time", ":current_time", "$g_round_start_time"),
                 (ge, ":round_time", multiplayer_new_agents_finish_spawning_time),
                 (gt, ":num_active_players", 2),
                 (store_mul, ":multipication_of_num_active_players_in_teams", ":num_active_players_in_team_0", ":num_active_players_in_team_1"),
                 (neq, ":multipication_of_num_active_players_in_teams", 0),
         
                 (assign, ":spawn_new", 0),
               (else_try), #new added end         
                 (assign, ":spawn_new", 1),
               (try_end),
             (else_try), 
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"), 
               (assign, ":player_team_respawn_period", "$g_multiplayer_respawn_period"), 
               (try_begin), 
                 (eq, ":player_team", 0), 
                 (val_add, ":player_team_respawn_period", multiplayer_siege_mod_defender_team_extra_respawn_time), 
               (try_end), 
               (this_or_next|gt, ":elapsed_time", ":player_team_respawn_period"), 
               (player_slot_eq, ":player_no", slot_player_spawned_at_siege_round, 0), 
               (assign, ":spawn_new", 1),
             (try_end), 
           (try_end), #addition for siege mod to allow players spawn more than once (end)

           (player_get_slot, ":spawn_count", ":player_no", slot_player_spawn_count),

           (try_begin),
             (gt, "$g_multiplayer_number_of_respawn_count", 0),
             (try_begin),
               (eq, ":spawn_new", 1),
               (eq, ":player_team", 0),
               (ge, ":spawn_count", "$g_multiplayer_number_of_respawn_count"),
               (assign, ":spawn_new", 0),
             (else_try),
               (eq, ":spawn_new", 1),
               (eq, ":player_team", 1),      
               (ge, ":spawn_count", 999),
               (assign, ":spawn_new", 0),
             (try_end),
           (try_end),

           (eq, ":spawn_new", 1),

           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (player_get_slot, ":spawn_count", ":player_no", slot_player_spawn_count),
           (val_add, ":spawn_count", 1),
           (player_set_slot, ":player_no", slot_player_spawn_count, ":spawn_count"),

           (try_begin),
             (ge, ":spawn_count", "$g_multiplayer_number_of_respawn_count"),
             (gt, "$g_multiplayer_number_of_respawn_count", 0),
             (eq, ":player_team", 0),
             (assign, ":spawn_count", 999),
             (player_set_slot, ":player_no", slot_player_spawn_count, ":spawn_count"),
           (try_end),

           (assign, ":player_is_horseman", 0),
           (player_get_item_id, ":item_id", ":player_no", ek_horse),
           (try_begin),
             (this_or_next|is_between, ":item_id", horses_begin, horses_end),
             (             is_between, ":item_id", oim_horses_begin, oim_horses_end),
             (assign, ":player_is_horseman", 1),
           (try_end),

           (try_begin),
             (lt, ":round_time", 20), #at start of game spawn at base entry point (only enemies)
             (try_begin),         
               (eq, ":player_team", 0), #defenders in siege mod at start of round
               (call_script, "script_multiplayer_find_spawn_point", ":player_team", 1, ":player_is_horseman"),
               (assign, ":entry_no", reg0),             
             (else_try),
               (eq, ":player_team", 1), #attackers in siege mod at start of round
               (assign, ":entry_no", multi_initial_spawn_point_team_2), #change later
             (try_end),
           (else_try),
             (call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":player_is_horseman"),
             (assign, ":entry_no", reg0),             
           (try_end),

		   (call_script, "script_multiplayer_get_bots_count", ":player_no"), 
		   (assign, ":bot_count", reg0), 
		   (try_begin),
			(gt, ":bot_count", 0),
			(player_spawn_new_agent, ":player_no", ":entry_no"),
		   (else_try), 
			#(call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":player_is_horseman"), 
			#(assign, ":entry_no", reg0), 
			(player_spawn_new_agent, ":player_no", ":entry_no"),
			(call_script, "script_multiplayer_spawn_player_bot_squad_at_point", ":player_no", ":player_team", ":entry_no"), 
		   (end_try), 
		   
           (player_set_slot, ":player_no", slot_player_spawned_this_round, 1),
           (player_set_slot, ":player_no", slot_player_spawned_at_siege_round, 1),         
         (try_end),
         ]),

      (1, 0, 0, [], #do this in every new frame, but not at the same time
       [
         (multiplayer_is_server),
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), 
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),

      multiplayer_server_check_end_map,
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,

      (ti_battle_window_opened, 0, 0, [], [
        (start_presentation, "prsnt_multiplayer_round_time_counter"),
        (start_presentation, "prsnt_multiplayer_team_score_display"),
        ]),

      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),
      ],
  ),  

  (
    "custom_battle",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,
      
      (0, 0, ti_once, [],
        [
          (assign, "$g_battle_result", 0),
          (call_script, "script_combat_music_set_situation_with_culture"),
         ]),

      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,

    ],
  ),

  (
    "custom_battle_siege",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,

      (0, 0, ti_once,
       [
         (assign, "$defender_team", 0),
         (assign, "$attacker_team", 1),
         (assign, "$defender_team_2", 2),
         (assign, "$attacker_team_2", 3),
         ], []),

      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_inventory_not_available,
      common_custom_siege_init,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,
      common_siege_init_ai_and_belfry,
      common_siege_move_belfry,
      common_siege_rotate_belfry,
      common_siege_assign_men_to_belfry,
      common_siege_ai_trigger_init_2,
	  custom_oim_replace_items_begin,
	  
      ],
    ),

  (
    "custom_battle_shturm2",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (8,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      
      (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

     ],
    [
      
      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_custom_siege_init,
      common_inventory_not_available,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
	  custom_oim_replace_items_begin,
	  
      
      (0, 0, ti_once,
       [
         (assign, "$defender_team", 1),
         (assign, "$attacker_team", 0),
         (assign, "$defender_team_2", 3),
         (assign, "$attacker_team_2", 2),
         ], []),

      common_siege_ai_trigger_init_2,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,

    ],
  ),


  (
    "custom_battle_5",mtf_battle_mode,-1,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (24,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),

     ],
    [
      
      common_custom_battle_tab_press,
      common_custom_battle_question_answered,
      common_custom_siege_init,
      common_inventory_not_available,
      common_music_situation_update,
      custom_battle_check_victory_condition,
      common_battle_victory_display,
      custom_battle_check_defeat_condition,
	  custom_oim_replace_items_begin,
	  
      
      (0, 0, ti_once,
       [
         (assign, "$defender_team", 1),
         (assign, "$attacker_team", 0),
         (assign, "$defender_team_2", 3),
         (assign, "$attacker_team_2", 2),
         ], []),

      common_siege_ai_trigger_init_2,
      common_siege_attacker_do_not_stall,
      common_siege_refill_ammo,
    ],
  ),

  
   (
    "oim_monfor_challenge_fight", mtf_arena_fight, -1,
    "oim_monfor_challenge_fight",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_sablya_turk_b]),
      (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
	],  
    [
      
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
         ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
      
     
      common_inventory_not_available,
	  

      (1, 4, ti_once,
       [
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1),
         ],
       [
	     (try_begin),
            (main_hero_fallen),
            (assign, "$oim_monfor_ready_to_fight", 3),		 
         (else_try),
            (assign, "$oim_monfor_ready_to_fight", 2),
         (try_end),
         (finish_mission),
        ]
		),
      ],
    ),

(
    "oim_training_ground_training", mtf_arena_fight, -1,
    "Training.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_weapons|af_override_horse,aif_start_alarmed,1, oim_ranged_practice),
      (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[itm_practice_staff]),
      (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[itm_practice_staff]),
      (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[itm_practice_staff]),
      (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[itm_practice_staff]),
      (8,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (9,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (10,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (11,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (12,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (13,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (14,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (15,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_last_destroyed_gourds", 0),
         (call_script, "script_change_banners_and_chest")]),
      
      common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (assign, "$g_training_ground_training_success_ratio", 0),
         (jump_to_menu, "mnu_oim_training_ground_training_result"),
         (finish_mission),
         ]),
      
      common_inventory_not_available,

      (0, 0, ti_once,
       [
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (set_fixed_point_multiplier, 100),
           (entry_point_get_position, pos1, 0),
           (init_position, pos2),
           (position_set_y, pos2, "$g_training_ground_ranged_distance"),
           (position_transform_position_to_parent, pos3, pos1, pos2),
           (copy_position, pos1, pos3),
           (assign, ":end_cond", 10),
           (assign, ":shift_value", 0),
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_sub, ":cur_instance", ":cur_i", ":shift_value"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_instance"),
             (copy_position, pos2, pos1),
             (init_position, pos0),
             (store_random_in_range, ":random_no", 0, 360),
             (position_rotate_z, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 50, 600),
             (position_move_x, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 0, 360),
             (position_transform_position_to_local, pos3, pos1, pos2),
             (position_rotate_z, pos0, ":random_no"),
             (position_transform_position_to_parent, pos4, pos0, pos3),
             (position_transform_position_to_parent, pos2, pos1, pos4),
             (position_set_z_to_ground_level, pos2),
             (position_move_z, pos2, 150),
             (assign, ":valid", 1),
             (try_for_range, ":cur_instance_2", 0, 10),
               (eq, ":valid", 1),
               (neq, ":cur_instance", ":cur_instance_2"),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd", ":cur_instance_2"),
               (prop_instance_get_position, pos3, ":target_object_2"),
               (get_distance_between_positions, ":dist", pos2, pos3),
               (lt, ":dist", 100),
               (assign, ":valid", 0),
             (try_end),
             (try_begin),
               (eq, ":valid", 0),
               (val_add, ":end_cond", 1),
               (val_add, ":shift_value", 1),
             (else_try),
               (prop_instance_set_position, ":target_object", pos2),
               (prop_instance_animate_to_position, ":target_object", pos2, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_instance"),
               (position_move_z, pos2, -150), #moving back to ground level
               (prop_instance_set_position, ":target_object_2", pos2),
               (prop_instance_animate_to_position, ":target_object_2", pos2, 1),
             (try_end),
           (try_end),
         (else_try),
           (eq, "$g_mt_mode", ctm_mounted),
           (assign, ":num_gourds", 0),
           #First, placing gourds on the spikes
           (try_for_range, ":cur_i", 0, 100),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_i"),
             (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_i"),
             (ge, ":target_object", 0),
             (ge, ":target_object_2", 0),
             (val_add, ":num_gourds", 1),
             (prop_instance_get_position, pos0, ":target_object_2"),
             (position_move_z, pos0, 150),
             (prop_instance_set_position, ":target_object", pos0),
             (prop_instance_animate_to_position, ":target_object", pos0, 1),
           (try_end),
           (store_sub, ":end_cond", ":num_gourds", "$g_training_ground_training_num_gourds_to_destroy"),
           #Second, removing gourds and their spikes randomly
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_random_in_range, ":random_instance", 0, ":num_gourds"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":random_instance"),
             (prop_instance_get_position, pos0, ":target_object"),
             (position_get_z, ":pos_z", pos0),
             (try_begin),
               (lt, ":pos_z", -50000),
               (val_add, ":end_cond", 1), #removed already, try again
             (else_try),
               (position_set_z, pos0, -100000),
               (prop_instance_set_position, ":target_object", pos0),
               (prop_instance_animate_to_position, ":target_object", pos0, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":random_instance"),
               (prop_instance_set_position, ":target_object_2", pos0),
               (prop_instance_animate_to_position, ":target_object_2", pos0, 1),
             (try_end),
           (try_end),
         (try_end),
         ],
       []),

      (1, 3, ti_once,
       [
         (eq, "$g_mt_mode", ctm_melee),
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1)
         ],
       [
         (try_begin),
           (neg|main_hero_fallen),
           (assign, "$g_training_ground_training_success_ratio", 100),
         (else_try),
           (assign, ":alive_enemies", 0),
           (try_for_agents, ":agent_no"),
             (agent_is_alive, ":agent_no"),
             (agent_is_human, ":agent_no"),
             (agent_get_team, ":team_no", ":agent_no"),
             (eq, ":team_no", 1),
             (val_add, ":alive_enemies", 1),
           (try_end),
           (store_sub, ":dead_enemies", "$g_training_ground_training_num_enemies", ":alive_enemies"),
           (store_mul, "$g_training_ground_training_success_ratio", ":dead_enemies", 100),
           (val_div, "$g_training_ground_training_success_ratio", "$g_training_ground_training_num_enemies"),
         (try_end),
         (jump_to_menu, "mnu_oim_training_ground_training_result"),
         (finish_mission),
         ]),

      (1, 16, ti_once,
       [
         (eq, "$g_mt_mode", ctm_ranged),
         (get_player_agent_no, ":player_agent"),
         (agent_get_ammo, ":ammo", ":player_agent"),
         (this_or_next|main_hero_fallen),
         (		       eq, ":ammo", 0),
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 10),
         (jump_to_menu, "mnu_oim_training_ground_training_result"),
         (finish_mission),
         ]),

      (0, 0, 0,
       [
         (gt, "$g_last_destroyed_gourds", 0),
         (try_begin),
           (eq, "$g_mt_mode", ctm_ranged),
           (entry_point_get_position, pos1, 0),
           (position_move_y, pos1, 100, 0),
           (get_player_agent_no, ":player_agent"),
           (agent_get_position, pos2, ":player_agent"),
           (try_begin),
             (position_is_behind_position, pos2, pos1),
             (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
           (else_try),
             (display_message, "@You must stay behind the line on the ground! Point is not counted."),
           (try_end),
         (else_try),
           (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
         (try_end),
         (assign, "$g_last_destroyed_gourds", 0),
         ],
       []),
    ],
  ), 
  

  

  (
    "oim_trakai_icon",0,-1,
    "OiM hack tracai icon",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
      
      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
        ]),

      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
		
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [  
							(try_begin),
								(quest_slot_eq, "qst_oim_trakay_icon", slot_quest_current_state, 6),
								(try_begin),
									(try_begin),
										(call_script, "script_cf_oim_trakay_fight_check"),
										(call_script, "script_fail_quest", "qst_oim_trakay_icon"),
										(display_message, "@You run away from the fight"),								  
									(else_try),
										(jump_to_menu, "mnu_oim_monk_is_killed"),
										(call_script, "script_succeed_quest", "qst_oim_trakay_icon"),
										(finish_mission, 4),
									(try_end),
								(try_end),
								(set_trigger_result,1),
							(else_try),
								(set_trigger_result,1),
							(try_end),
							], []),
      (ti_on_leave_area, 0, 0, [
          (try_begin),
            (assign,"$g_leave_town",1),
          (try_end),
          ], []),

		  (1, 0, ti_once, [(check_quest_active, "qst_oim_trakay_icon"),
                        (neg|check_quest_succeeded, "qst_oim_trakay_icon"),
                        (neg|check_quest_failed, "qst_oim_trakay_icon"),
                        (quest_slot_eq, "qst_oim_trakay_icon", slot_quest_current_state, 6),
                        (assign, ":not_alive", 0),
						(try_begin),
							(call_script, "script_cf_oim_trakay_fight_check"),                       
							(assign, ":not_alive", 1),
						(else_try),
							(main_hero_fallen),
							(assign, ":not_alive", 1),
						(try_end),
		                (eq, ":not_alive", 1),
                       ],
       [(try_begin),
          (main_hero_fallen),
          (jump_to_menu, "mnu_oim_defeated_by_monk"),
          (call_script, "script_fail_quest", "qst_oim_trakay_icon"),
          (finish_mission, 4),
        (else_try),
		  (jump_to_menu, "mnu_oim_monk_is_killed"),
          (call_script, "script_succeed_quest", "qst_oim_trakay_icon"),
		  (finish_mission, 4),
        (try_end),
        ]),
    ],
  ),

   (
    "oim_sem_samuraev_fight", mtf_arena_fight, -1,
    "oim_sem_samuraev_fight",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (7,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
      (10,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
	  ],  
	
    [
      
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
         ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
      
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
     
      common_inventory_not_available,

      (1, 4, ti_once,
       [
         (this_or_next|main_hero_fallen),
         (num_active_teams_le, 1),
         ],
       [
	     (try_begin),
            (main_hero_fallen),
            (assign, "$oim_fight_sem_samuraev", 3),		 
         (else_try),
            (assign, "$oim_fight_sem_samuraev", 2),
         (try_end),
         (finish_mission),
        ]
		),
      ],
    ),

  (
    "oim_sem_samuraev_battle",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (3,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     (1,mtef_team_0|mtef_use_exact_number,0,aif_start_alarmed, 7,[]),
     (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_tab_press,
	  
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           #(assign, "$g_presentation_battle_active", 0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20),
              (assign, "$g_battle_result", -1),
              (set_mission_result, -1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission, 0)]),

      common_battle_inventory,      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      
    ],
  ),

  (
    "oim_interior_battle",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
	  (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),	  
	  (3,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (7,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (8,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (9,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
      (10,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (12,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (13,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (14,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  	  
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (16,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (17,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  
	  (18,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	  	  
	  (19,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_tab_press,
	  
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,


      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (str_store_string, s5, "str_retreat"),
        (call_script, "script_simulate_retreat", 10, 20),
        (assign, "$g_battle_result", -1),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (0, 0, ti_once, [], [(assign, "$g_battle_won", 0),
                           (assign, "$defender_reinforcement_stage", 0),
                           (assign, "$attacker_reinforcement_stage", 0),
                           #(assign, "$g_presentation_battle_active", 0),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20),
              (assign, "$g_battle_result", -1),
              (set_mission_result, -1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission, 0)]),

      common_battle_inventory,      
      common_battle_order_panel,
      common_battle_order_panel_tick,
      
    ],
  ),
  

    (
    "oim_steale_horse",0,-1,
    "OiM steal horse mission",
    [
	 (0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     #(1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
	 [
           
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
		 (assign, "$tutorial_4_state", 0),
         (assign, "$tutorial_4_msg_1_displayed", 0),
        ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
           
      common_inventory_not_available,	

	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

	(1, 0, ti_once, [
		#(ge, "$tutorial_4_state", 2), 
		(assign, ":not_alive", 0),
        (try_begin),
			(call_script, "script_cf_check_agent_count"),                       
			(assign, ":not_alive", 1),
		(else_try),
			(main_hero_fallen),
			(assign, ":not_alive", 1),
		(try_end),
        (eq, ":not_alive", 1),
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 4),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 4),
	    (try_end),
    ]),
	
	
	
	
	(0, 0, ti_once, [
		(quest_slot_eq, "qst_oim_potop_kshetuskiy", slot_quest_current_state, 4),
	],
	[
		(tutorial_message, "str_oim_potop_horse_warn_defenders"),
	]), 	
		
      (0, 0, 0, [(try_begin),
                 (eq, "$tutorial_4_state", 0),
                   (try_begin),
                     (eq, "$tutorial_4_msg_1_displayed", 0),
                     (store_mission_timer_a, ":cur_time"),
                     (gt, ":cur_time", 0),
                     (assign, "$tutorial_4_msg_1_displayed", 1),
                     #(tutorial_message, "str_tutorial_4_msg_1"),
                     (entry_point_get_position, pos1, 1),
                     (set_spawn_position, 1),
                     (spawn_horse, "itm_oim_qst_horse"),
                   (try_end),
                   (get_player_agent_no, ":player_agent"),
                   (agent_get_horse, ":horse_agent", ":player_agent"),
                   (ge, ":horse_agent", 0),
                   (val_add, "$tutorial_4_state", 2),
                   (tutorial_message, "str_oim_potop_horse_warn"), 
				   (call_script, "script_cf_set_agent_mode_hostile"), 
                 (try_end),
                 ], []),
	 
	]),
	
(
    "vtorhenie",mtf_battle_mode|mtf_synch_inventory,-1,
    "Vtorzhenie",
     [

     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     #(39,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (4,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,5,[]),
     (5,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,5,[]),
     (6,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,5,[]),
     (7,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,5,[]),
	 
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_defender_reinforcement_check,
      common_siege_attacker_reinforcement_check_modify,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,

	  

    ],
  ),

 (
    "castle_attack_walls_mina",mtf_battle_mode|mtf_synch_inventory,-1,
    "Vzorvat minu",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  custom_oim_replace_items_begin,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  
	  


    ],
  ),

    (
    "oim_simle_fight_interior",0,-1,
    "Simple interrior fight",
    [
	 (0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_visitor_source,af_override_horse,0,1,[]),
     (7,mtef_visitor_source,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
	 [
           
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
        ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
           
      common_inventory_not_available,	
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

	(1, 0, ti_once, [
		#(ge, "$tutorial_4_state", 2), 
		(assign, ":not_alive", 0),
        (try_begin),
			(call_script, "script_cf_check_agent_count"),                       
			(assign, ":not_alive", 1),
		(else_try),
			(main_hero_fallen),
			(assign, ":not_alive", 1),
		(try_end),
        (eq, ":not_alive", 1),
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 4),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 4),
	    (try_end),
    ]),
	

	]),

  (
    "sneak_oim_after_radz",mtf_arena_fight,-1,
    "You must fight your way out!",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (32,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
#      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
	  
	  (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
	  
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  
      
      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
      
	  (0, 3, 0,
       [
           (main_hero_fallen,0),
        ],
       [(jump_to_menu, "$g_next_menu"),(finish_mission,0)]),
      (5, 1, ti_once, [(num_active_teams_le,1),(neg|main_hero_fallen)],
       [(assign,"$auto_menu",-1),(jump_to_menu, "$g_next_menu"),(finish_mission,1)]),
      (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu, "$g_next_menu"),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
    ],
    ),	
    
	
	(
    "oim_dungeon_mission",mtf_battle_mode|mtf_synch_inventory,charge,
    "OiM steal horse mission",
    [
	 (0,mtef_scene_source|mtef_team_0,af_override_head|af_override_body|af_override_foot|af_override_gloves|af_override_horse,0,1, pilgrim_disguise_oim),
     (1,mtef_visitor_source,af_override_horse,0,1,[]),
     (2,mtef_visitor_source,af_override_horse,0,1,[]),
     (3,mtef_visitor_source,af_override_horse,0,1,[]),
     (4,mtef_visitor_source,af_override_horse,0,1,[]),
     (5,mtef_visitor_source,af_override_horse,0,1,[]),
     (6,mtef_visitor_source,af_override_horse,0,1,[]),
     (7,mtef_visitor_source,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
	 [
           
      (ti_before_mission_start, 0, 0, [],
       [
        (call_script, "script_change_banners_and_chest"),
        ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
           
      common_inventory_not_available,		
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

    (0.1, 0, 0, [],
    [
		(call_script, "script_cf_set_nearby_agents_hostile"),
    ]),



    (1, 0, ti_once, [
		#(ge, "$tutorial_4_state", 2), 
		(assign, ":not_alive", 0),
        (try_begin),
			(call_script, "script_cf_check_agent_count"),                       
			(assign, ":not_alive", 1),
		(else_try),
			(main_hero_fallen),
			(assign, ":not_alive", 1),
			
		(try_end),
        (eq, ":not_alive", 1),
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 4),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 4),
	    (try_end),
    ]),

	]),	
	
	(
    "oim_dungeon_mission_msk",mtf_battle_mode|mtf_synch_inventory,charge,
    "OiM steal horse mission",
    [
	 (0,mtef_scene_source|mtef_team_0,af_override_head|af_override_body|af_override_foot|af_override_gloves|af_override_horse,0,1, pilgrim_disguise_oim),
     (1,mtef_visitor_source,af_override_horse,0,1,[]),
     (2,mtef_visitor_source,af_override_horse,0,1,[]),
     (3,mtef_visitor_source,af_override_horse,0,1,[]),
     (4,mtef_visitor_source,af_override_horse,0,1,[]),
     (5,mtef_visitor_source,af_override_horse,0,1,[]),
     (6,mtef_visitor_source,af_override_horse,0,1,[]),
     (7,mtef_visitor_source,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),
	 #(21,mtef_visitor_source,af_override_horse,0,1,[]), its an exit point
	 (22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
	 [
           
      (ti_before_mission_start, 0, 0, [],
       [
        (scene_set_day_time, 3), 
		(call_script, "script_change_banners_and_chest"),
        ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
           
      common_inventory_not_available,	
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

    (0.1, 0, 0, [],
    [
		(call_script, "script_cf_set_nearby_agents_hostile"),
    ]),

    (0.1, 0, ti_once, [
      (set_fixed_point_multiplier, 100),
      (get_player_agent_no, ":player_agent"),
      (agent_get_position, pos2, ":player_agent"),
      (entry_point_get_position, pos1, 21),  
      (get_distance_between_positions, ":cur_distance", pos1, pos2),
	  #(assign, reg0, ":cur_distance"), 
	  #(display_message, "@dist: {reg0}"),
      (le, ":cur_distance", 150), #45 meters
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 1),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 1),
	    (try_end),
    ]),

    (1, 0, ti_once, [
		#(ge, "$tutorial_4_state", 2), 
		(assign, ":not_alive", 0),
        (try_begin),
			(call_script, "script_cf_check_agent_count"),                       
			(assign, ":not_alive", 1),
		(else_try),
			(main_hero_fallen),
			(assign, ":not_alive", 1),
			
		(try_end),
        (eq, ":not_alive", 1),
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 1),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 1),
	    (try_end),
    ]),
	
	(0, 0, 0, [
		(get_player_agent_no, ":agent_no"), 
		(agent_get_position, pos0, ":agent_no"), 
		(entry_point_get_position, pos1, 21),
		(get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1), 
		(le, ":dist", 3),
	],
	[
		(jump_to_menu, "$g_next_menu"),
		(finish_mission, 1),
	]), 

	]),		


	(
    "oim_alevtina_tatar",0,-1,
    "OiM steal horse mission",
    [
	 (0,mtef_scene_source|mtef_team_0, af_override_all,0,1, tatar_disguise_oim),
     (1,mtef_visitor_source,af_override_horse,0,1,[]),
     (2,mtef_visitor_source,af_override_horse,0,1,[]),
     (3,mtef_visitor_source,af_override_horse,0,1,[]),
     (4,mtef_visitor_source,af_override_horse,0,1,[]),
     (5,mtef_visitor_source,af_override_horse,0,1,[]),
     (6,mtef_visitor_source,af_override_horse,0,1,[]),
     (7,mtef_visitor_source,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
	 [
           
      (ti_before_mission_start, 0, 0, [],
       [
        (call_script, "script_change_banners_and_chest"),
        ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
           
      common_inventory_not_available,	
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

    (0.1, 0, 0, [],
    [
		(call_script, "script_cf_set_nearby_agents_hostile"),
    ]),



    (1, 0, ti_once, [
		#(ge, "$tutorial_4_state", 2), 
		(assign, ":not_alive", 0),
        (try_begin),
			(call_script, "script_cf_check_agent_count"),                       
			(assign, ":not_alive", 1),
		(else_try),
			(main_hero_fallen),
			(assign, ":not_alive", 1),
			
		(try_end),
        (eq, ":not_alive", 1),
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 4),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 4),
	    (try_end),
    ]),

	]),		


  (
    "oim_tavern_simple_fight",mtf_arena_fight,charge,
    "You lead your men to battle.",
    [
	 #af_override_weapons
	 (0,mtef_visitor_source|mtef_team_0,af_override_all, aif_start_alarmed,1, oim_hand_to_hand),
     #(3,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,[]),
	 
     (1,mtef_visitor_source|mtef_team_1,af_override_weapons, aif_start_alarmed,1, []),
     (2,mtef_visitor_source|mtef_team_1,af_override_weapons, aif_start_alarmed,1, []),
     (3,mtef_visitor_source|mtef_team_1,af_override_weapons, aif_start_alarmed,1, []),
	 (4,mtef_visitor_source|mtef_team_1,af_override_weapons, aif_start_alarmed,1, []),

     ],
    [
      
      common_inventory_not_available,

      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
		 (get_player_agent_no, ":player_agent"),
		 (agent_set_kick_allowed, ":player_agent", 0),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
			 (assign, "$g_battle_result", -1),
             (jump_to_menu, "mnu_oim_tavern_simple_fight_result"),
           (else_try),
             (jump_to_menu, "mnu_oim_tavern_simple_fight_result"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),	
  
  #oim_tavern_duel_fight
  (
    "oim_tavern_duel_fight", mtf_battle_mode|mtf_synch_inventory, charge,
    "You lead your men to battle.",
    [
	 (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,oim_duel_equip),
     (1,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_npc),
     (2,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_npc),
     (3,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_npc),
	 (4,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_npc),
     ],
    [      
      common_inventory_not_available,

      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),		 
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
			 (assign, "$g_battle_result", -1),
             (jump_to_menu, "mnu_oim_tavern_duel_fight_result"),
           (else_try),
             (jump_to_menu, "mnu_oim_tavern_duel_fight_result"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),
  
  (
    "oim_tavern_duel_fight_swed", mtf_battle_mode|mtf_synch_inventory, charge,
    "You lead your men to battle.",
    [
	 (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,oim_duel_equip_swed),
     (1,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_swed_npc),
     (2,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_swed_npc),
	 (3,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_swed_npc),
     (4,mtef_visitor_source|mtef_team_1,af_override_all,aif_start_alarmed,1,oim_duel_equip_swed_npc),
     ],
    [
      
      common_inventory_not_available,

      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
			 (assign, "$g_battle_result", -1),
             (jump_to_menu, "mnu_oim_tavern_duel_fight_result"),
           (else_try),
             (jump_to_menu, "mnu_oim_tavern_duel_fight_result"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),

  ("oim_tavern_ranged_duel", mtf_arena_fight, -1,
    "Training.",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_weapons|af_override_horse,aif_start_alarmed,1,[itm_practice_staff]),
      (1,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (2,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (3,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (4,mtef_visitor_source|mtef_team_1,af_override_everything,aif_start_alarmed,1,[itm_practice_staff]),
      (8,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (9,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (10,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (11,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (12,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (13,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (14,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
      (15,mtef_visitor_source,af_override_weapons|af_override_horse|af_override_head,0,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_last_destroyed_gourds", 0),
         (call_script, "script_change_banners_and_chest")]),
      
      #common_arena_fight_tab_press,
      
      (ti_question_answered, 0, 0, [],
       [
         (store_trigger_param_1,":answer"),
         (eq,":answer",0),
         (assign, "$g_training_ground_training_success_ratio", 0),
         (jump_to_menu, "mnu_oim_ranged_duel_tavern_result"),
         (finish_mission),
         ]),
      
      common_inventory_not_available,
	  
   (ti_tab_pressed, 0, 0, [],
    [
      (question_box,"str_oim_give_up_fight"),
    ]),
 
   
   (1, 3, ti_once,
       [
         #(eq, "$g_mt_mode", ctm_ranged),
         (get_player_agent_no, ":player_agent"),
         (agent_get_ammo, ":ammo", ":player_agent"),
         #(store_mission_timer_a, ":cur_seconds"),
         #(this_or_next|main_hero_fallen),
         (eq, ":ammo", 0),
         #(gt, ":cur_seconds", 116), 
         ],
       [
         (store_mul, "$g_training_ground_training_success_ratio", "$scene_num_total_gourds_destroyed", 10),
         (jump_to_menu, "mnu_oim_ranged_duel_tavern_result"),
         (finish_mission),
         ]),

      (0, 0, ti_once,
       [
           (call_script, "script_oim_get_distance_for_ranged_duel"), 
		   (assign, ":ranged_distance", reg0), 
		   (val_mul, ":ranged_distance", 100),
		   (set_fixed_point_multiplier, 100),
           (entry_point_get_position, pos1, 0),
           (init_position, pos2),
           (position_set_y, pos2, ":ranged_distance"),
           (position_transform_position_to_parent, pos3, pos1, pos2),
           (copy_position, pos1, pos3),
           (assign, ":end_cond", 10),
           (assign, ":shift_value", 0),
           (try_for_range, ":cur_i", 0, ":end_cond"),
             (store_sub, ":cur_instance", ":cur_i", ":shift_value"),
             (scene_prop_get_instance, ":target_object", "spr_gourd", ":cur_instance"),
             (copy_position, pos2, pos1),
             (init_position, pos0),
             (store_random_in_range, ":random_no", 0, 360),
             (position_rotate_z, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 50, 600),
             (position_move_x, pos2, ":random_no"),
             (store_random_in_range, ":random_no", 0, 360),
             (position_transform_position_to_local, pos3, pos1, pos2),
             (position_rotate_z, pos0, ":random_no"),
             (position_transform_position_to_parent, pos4, pos0, pos3),
             (position_transform_position_to_parent, pos2, pos1, pos4),
             (position_set_z_to_ground_level, pos2),
             (position_move_z, pos2, 150),
             (assign, ":valid", 1),
             (try_for_range, ":cur_instance_2", 0, 10),
               (eq, ":valid", 1),
               (neq, ":cur_instance", ":cur_instance_2"),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd", ":cur_instance_2"),
               (prop_instance_get_position, pos3, ":target_object_2"),
               (get_distance_between_positions, ":dist", pos2, pos3),
               (lt, ":dist", 100),
               (assign, ":valid", 0),
             (try_end),
             (try_begin),
               (eq, ":valid", 0),
               (val_add, ":end_cond", 1),
               (val_add, ":shift_value", 1),
             (else_try),
               (prop_instance_set_position, ":target_object", pos2),
               (prop_instance_animate_to_position, ":target_object", pos2, 1),
               (scene_prop_get_instance, ":target_object_2", "spr_gourd_spike", ":cur_instance"),
               (position_move_z, pos2, -150), #moving back to ground level
               (prop_instance_set_position, ":target_object_2", pos2),
               (prop_instance_animate_to_position, ":target_object_2", pos2, 1),
             (try_end),
           (try_end),
         ],
       []),		 
		 
		 
      (0, 0, 0,
       [
         (gt, "$g_last_destroyed_gourds", 0),
         (entry_point_get_position, pos1, 0),
         (position_move_y, pos1, 100, 0),
         (get_player_agent_no, ":player_agent"),
         (agent_get_position, pos2, ":player_agent"),
         (try_begin),
           (position_is_behind_position, pos2, pos1),
           (val_add, "$scene_num_total_gourds_destroyed", "$g_last_destroyed_gourds"),
         (else_try),
           (display_message, "@You must stay behind the line on the ground! Point is not counted."),
         (try_end),
         (assign, "$g_last_destroyed_gourds", 0),
         ],
       []),
    ],
  ),

  ("oim_tavern_rich_man_hunt", mtf_battle_mode|mtf_synch_inventory, charge,
    "You lead your men to battle.",
    [
	 (0,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
     (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (2,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
     (3,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	 
     (4,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),	 	 
     ],
    [
      
      common_inventory_not_available,

      (ti_tab_pressed, 0, 0, [(display_message,"@Cannot leave now.")], []),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),

      (0, 0, ti_once, [],
       [
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),

      (1, 4, ti_once, [(this_or_next|main_hero_fallen),(num_active_teams_le,1)],
       [
           (try_begin),
             (main_hero_fallen),
			 (assign, "$g_battle_result", -1),
             (jump_to_menu, "mnu_oim_rich_visitor_result"),
           (else_try),
             (jump_to_menu, "mnu_oim_rich_visitor_result"),
           (try_end),
           (finish_mission),
           ]),
    ],
  ),


  (
    "castle_default",0,-1,
    "Default town visit",
    [(0,mtef_scene_source|mtef_team_0,af_override_horse,0,1,pilgrim_disguise),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),(2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (6,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
	 (7,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (8,mtef_scene_source,af_override_horse,0,1,[]),
	 (9,mtef_visitor_source,af_override_horse,0,1,[]),
	 (10,mtef_scene_source,af_override_horse,0,1,[]),
	 (11,mtef_scene_source,af_override_horse,0,1,[]),
     (12,mtef_scene_source,af_override_horse,0,1,[]),
	 (13,mtef_scene_source,0,0,1,[]),
	 (14,mtef_scene_source,0,0,1,[]),
	 (15,mtef_scene_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),
	 (17,mtef_visitor_source,af_override_horse,0,1,[]),
	 (18,mtef_visitor_source,af_override_horse,0,1,[]),
	 (19,mtef_visitor_source,af_override_horse,0,1,[]),
	 (20,mtef_visitor_source,af_override_horse,0,1,[]),
	 (21,mtef_visitor_source,af_override_horse,0,1,[]),
	 (22,mtef_visitor_source,af_override_horse,0,1,[]),
	 (23,mtef_visitor_source,af_override_horse,0,1,[]),
	 (24,mtef_visitor_source,af_override_horse,0,1,[]),
     (25,mtef_visitor_source,af_override_horse,0,1,[]),
	 (26,mtef_visitor_source,af_override_horse,0,1,[]),
	 (27,mtef_visitor_source,af_override_horse,0,1,[]),
	 (28,mtef_visitor_source,af_override_horse,0,1,[]),
	 (29,mtef_visitor_source,af_override_horse,0,1,[]),
	 (30,mtef_visitor_source,af_override_horse,0,1,[]),
	 (31,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
    [
      
      (1, 0, ti_once, [], [
          (store_current_scene, ":cur_scene"),
          (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
          (try_begin),
            (eq, "$sneaked_into_town", 1),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
          (else_try),
            (eq, "$talk_context", tc_tavern_talk),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
          (else_try),
            (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
          (try_end),
        ]),
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_inventory_key_pressed, 0, 0, [(set_trigger_result,1)], []),
      (ti_tab_pressed, 0, 0, [(set_trigger_result,1)], []),
    ],
  ),


    (
    "oim_simle_fight_interior_alevtina",mtf_battle_mode|mtf_synch_inventory,-1,
    "Simple interrior fight",
    [
	 (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,oim_duel_equip_alevtina_hanum),
     (1,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (2,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (3,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (4,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (5,mtef_scene_source|mtef_team_0,af_override_horse,0,1,[]),
     (6,mtef_visitor_source,af_override_horse,0,1,[]),
     (7,mtef_visitor_source,af_override_horse,0,1,[]),
     
     (8,mtef_visitor_source,af_override_horse,0,1,[]),
     (9,mtef_visitor_source,af_override_horse,0,1,[]),(10,mtef_visitor_source,af_override_horse,0,1,[]),(11,mtef_visitor_source,af_override_horse,0,1,[]),(12,mtef_visitor_source,af_override_horse,0,1,[]),(13,mtef_visitor_source,0,0,1,[]),(14,mtef_visitor_source,0,0,1,[]),(15,mtef_visitor_source,0,0,1,[]),
     (16,mtef_visitor_source,af_override_horse,0,1,[]),(17,mtef_visitor_source,af_override_horse,0,1,[]),(18,mtef_visitor_source,af_override_horse,0,1,[]),(19,mtef_visitor_source,af_override_horse,0,1,[]),(20,mtef_visitor_source,af_override_horse,0,1,[]),(21,mtef_visitor_source,af_override_horse,0,1,[]),(22,mtef_visitor_source,af_override_horse,0,1,[]),(23,mtef_visitor_source,af_override_horse,0,1,[]),
     (24,mtef_visitor_source,af_override_horse,0,1,[]),(25,mtef_visitor_source,af_override_horse,0,1,[]),(26,mtef_visitor_source,af_override_horse,0,1,[]),(27,mtef_visitor_source,af_override_horse,0,1,[]),(28,mtef_visitor_source,af_override_horse,0,1,[]),(29,mtef_visitor_source,af_override_horse,0,1,[]),(30,mtef_visitor_source,af_override_horse,0,1,[]),(31,mtef_visitor_source,af_override_horse,0,1,[]),
     (32,mtef_visitor_source,af_override_horse,0,1,[]),(33,mtef_visitor_source,af_override_horse,0,1,[]),(34,mtef_visitor_source,af_override_horse,0,1,[]),(35,mtef_visitor_source,af_override_horse,0,1,[]),(36,mtef_visitor_source,af_override_horse,0,1,[]),(37,mtef_visitor_source,af_override_horse,0,1,[]),(38,mtef_visitor_source,af_override_horse,0,1,[]),(39,mtef_visitor_source,af_override_horse,0,1,[]),
     (40,mtef_visitor_source,af_override_horse,0,1,[]),(41,mtef_visitor_source,af_override_horse,0,1,[]),(42,mtef_visitor_source,af_override_horse,0,1,[]),(43,mtef_visitor_source,af_override_horse,0,1,[]),(44,mtef_visitor_source,af_override_horse,0,1,[]),(45,mtef_visitor_source,af_override_horse,0,1,[]),(46,mtef_visitor_source,af_override_horse,0,1,[]),(47,mtef_visitor_source,af_override_horse,0,1,[]),
     ],
	 [
           
      (ti_before_mission_start, 0, 0, [],
       [
         (call_script, "script_change_banners_and_chest"),
	 (mission_enable_talk),
        ]),
      
      (ti_tab_pressed, 0, 0, [(display_message, "@Cannot leave now.")], []),
           
      common_inventory_not_available,		

	(1, 0, ti_once, [
		#(ge, "$tutorial_4_state", 2), 
		(assign, ":not_alive", 0),
        (try_begin),
			(call_script, "script_cf_check_agent_count"),                       
			(assign, ":not_alive", 1),
		(else_try),
			(main_hero_fallen),
			(assign, ":not_alive", 1),
		(try_end),
        (eq, ":not_alive", 1),
    ],
    [
		(try_begin),
			(main_hero_fallen),
			(jump_to_menu, "$g_next_menu"),
			(assign, "$g_battle_result", -1),
			(finish_mission, 4),
        (else_try),
			(jump_to_menu, "$g_next_menu"),
			(finish_mission, 4),
	    (try_end),
    ]),
	

	]),  
  
	(
    "credit_fight",mtf_arena_fight,-1,
    "You must fight your way out!",
    [
      (0,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
      
      common_battle_mission_start,
      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),
      (ti_question_answered, 0, 0, [],
       [
			(store_trigger_param_1,":answer"),
			(eq,":answer",0),
			(party_set_slot, "$current_town", slot_ms_party_operation_time, 25),
			(call_script, "script_ms_remove_gold_if_become_as_prisoner"),
			(jump_to_menu,"mnu_captivity_start_castle_defeat"),
			(finish_mission,0),
		]),
      
      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
      (0, 3, 0,
       [
           (main_hero_fallen,0),
        ],
       [
		   (party_set_slot, "$current_town", slot_ms_party_operation_time, 25),
		   (call_script, "script_ms_remove_gold_if_become_as_prisoner"),
		   (jump_to_menu,"mnu_captivity_start_castle_defeat"),
		   (finish_mission,0)
	   ]),
      (5, 1, ti_once, [(num_active_teams_le,1),(neg|main_hero_fallen)],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),(party_set_slot, "$current_town", slot_ms_party_operation_time, 25),(finish_mission,1)]),
      (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),(party_set_slot, "$current_town", slot_ms_party_operation_time, 25),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [
	  (display_message,"str_cant_use_inventory_arena"),
	  ], []),
      
    ],
  ),

   (
    "lead_charge_ai_wagenburg_horsed",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (4,mtef_defenders|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_defenders|mtef_team_1,0,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_0,0,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_0,0,aif_start_alarmed,0,[]),
     ],
    [
      
		
	 (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),

         (assign, ":initial_courage_score", 5000),
                  
         (agent_get_troop_id, ":troop_id", ":agent_no"),
         (store_character_level, ":troop_level", ":troop_id"),
         (val_mul, ":troop_level", 35),
         (val_add, ":initial_courage_score", ":troop_level"), #average : 20 * 35 = 700
         
         (store_random_in_range, ":randomized_addition_courage", 0, 3000), #average : 1500
         (val_add, ":initial_courage_score", ":randomized_addition_courage"), 
                   
         (agent_get_party_id, ":agent_party", ":agent_no"),         
         (party_get_morale, ":cur_morale", ":agent_party"),
         
         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
         (val_mul, ":morale_effect_on_courage", 30), #this can effect morale with -2100..900
         (val_add, ":initial_courage_score", ":morale_effect_on_courage"), 
         
         #average = 5000 + 700 + 1500 = 7200; min : 5700, max : 8700
         #morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
         #min starting : 3600, max starting  : 9600, average starting : 7200
         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"), 
		 (agent_set_slot, ":agent_no", slot_agent_courage_score_fading_out, 0), 
         ]),
		 
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
		 
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
##          (str_store_troop_name, s6, ":dead_agent_troop_id"),
##          (assign, reg0, ":dead_agent_no"),
##          (assign, reg1, ":killer_agent_no"),
##          (assign, reg2, ":is_wounded"),
##          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),

        (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
         ]),	  
		 
      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20, 1),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

         (party_clear, "p_routed_enemies"),

         (assign, "$g_latest_order_1", 1), 
         (assign, "$g_latest_order_2", 1), 
         (assign, "$g_latest_order_3", 0), 
         (assign, "$g_latest_order_4", 3), 
		 (assign, "$g_latest_order_5", 3), 
         ]),

		 
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_place_player_banner_near_inventory"),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           (assign, "$g_defender_reinforcement_limit", 7),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [
                              
      #new (25.11.09) starts (sdsd = TODO : make a similar code to also helping ally encounters)
      #count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
      (assign, ":total_enemy_soldiers", reg0),
      
      #decrease number of agents already in battle area to find all number of reinforcement enemies
      (assign, ":enemy_soldiers_in_battle_area", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_party_id, ":agent_party", ":cur_agent"),
        (try_begin),
          (neq, ":agent_party", "p_main_party"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":enemy_soldiers_in_battle_area", 1),
        (try_end),
      (try_end),
      (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers", ":enemy_soldiers_in_battle_area"),

      (try_begin),
        (lt, ":total_enemy_reinforcements", 15),
        (ge, "$defender_reinforcement_stage", 2),
        (eq, "$defender_reinforcement_limit_increased", 0),
        (val_add, "$g_defender_reinforcement_limit", 1),                    
        (assign, "$defender_reinforcement_limit_increased", 1),
      (try_end),    
      #new (25.11.09) ends
      
      
      
      
      
      
      (lt,"$defender_reinforcement_stage","$g_defender_reinforcement_limit"),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,3,7),(assign, "$defender_reinforcement_limit_increased", 0),(val_add,"$defender_reinforcement_stage",1)]),
      
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",7),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,0,7),(val_add,"$attacker_reinforcement_stage",1)]),
      
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)]),

      common_battle_inventory,


      #AI Triggers
      (0, 0, ti_once, [
          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          ],
       [(call_script, "script_select_battle_tactic"),
        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        ]),
      
      (3, 0, 0, [
          (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
              ], []), #calculating and applying effect of people on others courage scores

      (3, 0, 0, [
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),          
            (store_mission_timer_a,":mission_time"),
            (ge,":mission_time",3),          
            (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
          (try_end),          
              ], []), #controlling courage score and if needed deciding to run away for each agent
      
      (2, 0, 0, [
          (store_mission_timer_a,":mission_time"),

          (ge,":mission_time",3),
          
          (call_script, "script_battle_tactic_apply"),
          ], []), #applying battle tactic

      common_battle_order_panel,
      common_battle_order_panel_tick,
	  
	  #oim code
     (1, 1, ti_once, [
		(eq, "$g_ai_wagenburg_is_on", 1),
	  ],
     [
      (set_show_messages, 0),
      (team_give_order, 1, grc_everyone, mordr_hold),
      (entry_point_get_position, pos1, 4),
		(team_set_order_position, 1, grc_everyone, pos1),
		(set_show_messages, 1),
     ]),	      

    ],
  ),
  
  (
    "lead_charge_ai_wagenburg",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (4,mtef_defenders|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_defenders|mtef_team_1,0,aif_start_alarmed,0,[]),
     (1,mtef_attackers|mtef_team_0,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     ],
    [
      	
	 (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),

         (assign, ":initial_courage_score", 5000),
                  
         (agent_get_troop_id, ":troop_id", ":agent_no"),
         (store_character_level, ":troop_level", ":troop_id"),
         (val_mul, ":troop_level", 35),
         (val_add, ":initial_courage_score", ":troop_level"), #average : 20 * 35 = 700
         
         (store_random_in_range, ":randomized_addition_courage", 0, 3000), #average : 1500
         (val_add, ":initial_courage_score", ":randomized_addition_courage"), 
                   
         (agent_get_party_id, ":agent_party", ":agent_no"),         
         (party_get_morale, ":cur_morale", ":agent_party"),
         
         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
         (val_mul, ":morale_effect_on_courage", 30), #this can effect morale with -2100..900
         (val_add, ":initial_courage_score", ":morale_effect_on_courage"), 
         
         #average = 5000 + 700 + 1500 = 7200; min : 5700, max : 8700
         #morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
         #min starting : 3600, max starting  : 9600, average starting : 7200
         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"), 
		 (agent_set_slot, ":agent_no", slot_agent_courage_score_fading_out, 0), 
         ]),

      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  #custom_oim_horse_dim_test, 
	  oim_on_horse_dismount,
		 
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),
		 
        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
##          (str_store_troop_name, s6, ":dead_agent_troop_id"),
##          (assign, reg0, ":dead_agent_no"),
##          (assign, reg1, ":killer_agent_no"),
##          (assign, reg2, ":is_wounded"),
##          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),
		 
        (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
         ]),	  

      common_battle_tab_press,

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20, 1),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

         (party_clear, "p_routed_enemies"),

         (assign, "$g_latest_order_1", 1), 
         (assign, "$g_latest_order_2", 1), 
         (assign, "$g_latest_order_3", 0), 
         (assign, "$g_latest_order_4", 3), 
		 (assign, "$g_latest_order_5", 3), 
         ]),

		 
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_place_player_banner_near_inventory"),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           (assign, "$g_defender_reinforcement_limit", 7),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [
                              
      #new (25.11.09) starts (sdsd = TODO : make a similar code to also helping ally encounters)
      #count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
      (assign, ":total_enemy_soldiers", reg0),
      
      #decrease number of agents already in battle area to find all number of reinforcement enemies
      (assign, ":enemy_soldiers_in_battle_area", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_party_id, ":agent_party", ":cur_agent"),
        (try_begin),
          (neq, ":agent_party", "p_main_party"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":enemy_soldiers_in_battle_area", 1),
        (try_end),
      (try_end),
      (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers", ":enemy_soldiers_in_battle_area"),

      (try_begin),
        (lt, ":total_enemy_reinforcements", 15),
        (ge, "$defender_reinforcement_stage", 2),
        (eq, "$defender_reinforcement_limit_increased", 0),
        (val_add, "$g_defender_reinforcement_limit", 1),                    
        (assign, "$defender_reinforcement_limit_increased", 1),
      (try_end),    
      #new (25.11.09) ends
      
      
      
      
      
      
      (lt,"$defender_reinforcement_stage","$g_defender_reinforcement_limit"),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,3,7),(assign, "$defender_reinforcement_limit_increased", 0),(val_add,"$defender_reinforcement_stage",1)]),
      
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",7),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,0,7),(val_add,"$attacker_reinforcement_stage",1)]),
      
      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)]),

      common_battle_inventory,


      #AI Triggers
      (0, 0, ti_once, [
          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          ],
       [(call_script, "script_select_battle_tactic"),
        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        ]),
      
      (3, 0, 0, [
          (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
              ], []), #calculating and applying effect of people on others courage scores

      (3, 0, 0, [
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),          
            (store_mission_timer_a,":mission_time"),
            (ge,":mission_time",3),          
            (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
          (try_end),          
              ], []), #controlling courage score and if needed deciding to run away for each agent
      
      (2, 0, 0, [
          (store_mission_timer_a,":mission_time"),

          (ge,":mission_time",3),
          
          (call_script, "script_battle_tactic_apply"),
          ], []), #applying battle tactic

      common_battle_order_panel,
      common_battle_order_panel_tick,
	  
	  #oim code
      (1, 1, ti_once, [
		(eq, "$g_ai_wagenburg_is_on", 1),
	  ],
        [
		  (set_show_messages, 0),
          (team_give_order, 1, grc_everyone, mordr_hold),
          (entry_point_get_position, pos1, 4),
		  (team_set_order_position, 1, grc_everyone, pos1),
		  (set_show_messages, 1),
         ]),	  

      (1, 1, ti_once, [
		(eq, "$g_ai_wagenburg_is_on", 1),
	  ],
        [
		  (set_show_messages, 0),
          (team_give_order, 1, grc_everyone, mordr_dismount),
		  (set_show_messages, 1),
         ]),     

    ],
  ),
  
  
	(
    "credit_fight_town",mtf_arena_fight,-1,
    "You must fight your way out!",
    [
      (0,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
	  (1,mtef_visitor_source|mtef_team_1,af_override_horse,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,af_override_horse,aif_start_alarmed,1,[]),
    ],
    [
      
      common_battle_mission_start,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  
	  
      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),
      (ti_question_answered, 0, 0, [],
       [
			(store_trigger_param_1,":answer"),
			(eq,":answer",0),
			(party_set_slot, "$current_town", slot_ms_party_operation_time, 25),
			(call_script, "script_ms_remove_gold_if_become_as_prisoner"),
			(jump_to_menu,"mnu_captivity_start_castle_defeat"),
			(finish_mission,0),
		]),
      
      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
      (0, 3, 0,
       [
           (main_hero_fallen,0),
        ],
       [
		   (call_script, "script_ms_remove_gold_if_become_as_prisoner"),
		   (party_set_slot, "$current_town", slot_ms_party_operation_time, 25),
		   (jump_to_menu,"mnu_captivity_start_castle_defeat"),
		   (finish_mission,0)
	   ]),
      (5, 1, ti_once, [(num_active_teams_le,1),(neg|main_hero_fallen)],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards"),(party_set_slot, "$current_town", slot_ms_party_operation_time, 25),(finish_mission,1)]),
      (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away"),(party_set_slot, "$current_town", slot_ms_party_operation_time, 25),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [
		
		(display_message,"str_cant_use_inventory_arena"),
		], []),
      
    ],
  ),
   
   (
    "shturm_podkup_horse",mtf_battle_mode|mtf_synch_inventory,-1,
    "Shturm podkupom na kone",
     [
     (0,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (4,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (5,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (6,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (7,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
	
	(0, 0, ti_once, [], [(call_script, "script_open_town_doors"),
                             
                             ]),
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

    ],
  ),  



  (
    "castle_attack_walls_2_ladder",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
	 (41,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  common_check_ladders_and_go_to,
	  common_check_to_ladders,
	  common_check_to_last_point,
	  common_check_last_point_to_free,
	  common_check_for_new_agents,
	  common_free_to_order,
	  custom_oim_replace_items_begin,

    ],
  ),
  
	(
    "castle_attack_walls_3_ladder",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
	 (41,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (42,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  common_check_ladders_and_go_to,
	  common_check_to_ladders,
	  common_check_to_last_point,
	  common_check_last_point_to_free,
	  common_check_for_new_agents,
	  common_free_to_order,
	  custom_oim_replace_items_begin,

    ],
  ),
  
  (
    "castle_attack_walls_4_ladder",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
	 (41,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (42,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (43,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  common_check_ladders_and_go_to,
	  common_check_to_ladders,
	  common_check_to_last_point,
	  common_check_last_point_to_free,
	  common_check_for_new_agents,
	  common_free_to_order,
	  custom_oim_replace_items_begin,

    ],
  ),
  
  (
    "castle_attack_walls_5_ladder",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
	 (41,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (42,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (43,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
	 (44,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  common_check_ladders_and_go_to,
	  common_check_to_ladders,
	  common_check_to_last_point,
	  common_check_last_point_to_free,
	  common_check_for_new_agents,
	  common_free_to_order,
	  custom_oim_replace_items_begin,

    ],
  ),  

	(
    "shturm_podkup",mtf_battle_mode|mtf_synch_inventory,-1,
    "Shturm podkupom peshkom",
     [
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0,mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),

     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (41,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     ],
    [
      
	
	(0, 0, ti_once, [], [(call_script, "script_open_town_doors"),
                             
                             ]),
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
	  custom_oim_replace_items_begin,
      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  

    ],
  ),

   (
    "sneak_caught_fight_t",mtf_arena_fight,-1,
    "You must fight your way outt!",
    [
      (0,mtef_visitor_source|mtef_team_0,af_override_all,aif_start_alarmed,1,pilgrim_disguise),
      (25,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (26,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (27,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (28,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (29,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (30,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (31,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
      (32,mtef_visitor_source|mtef_team_1,af_override_weapons,aif_start_alarmed,1,[itm_practice_staff]),
#      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
    ],
    [
      
      (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest")]),
      (ti_tab_pressed, 0, 0, [],
       [(question_box,"str_do_you_wish_to_surrender")]),
      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),(eq,":answer",0),(jump_to_menu,"mnu_captivity_start_castle_defeat"),(finish_mission,0),]),
      
      (1, 0, ti_once, [],
       [
         (play_sound,"snd_sneak_town_halt"),
         (call_script, "script_music_set_situation_with_culture", mtf_sit_fight),
         ]),
      (0, 3, 0,
       [
           (main_hero_fallen,0),
        ],
       [(jump_to_menu,"mnu_captivity_start_castle_defeat"),(finish_mission,0)]),
      (5, 1, ti_once, [(num_active_teams_le,1),(neg|main_hero_fallen)],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_dispersed_guards_t"),(finish_mission,1)]),
      (ti_on_leave_area, 0, ti_once, [],
       [(assign,"$auto_menu",-1),(jump_to_menu,"mnu_sneak_into_town_caught_ran_away_t"),(finish_mission,0)]),

      (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
	  
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  
      
    ],
  ),


  (
    "chenstohova_lead_charge",mtf_battle_mode|mtf_synch_inventory,charge,
    "You lead your men to battle.",
    [
     (1,mtef_defenders|mtef_team_0,0,aif_start_alarmed,12,[]),
     (0,mtef_defenders|mtef_team_0,0,aif_start_alarmed,0,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,12,[]),
     (4,mtef_attackers|mtef_team_1,0,aif_start_alarmed,0,[]),
     ],
    [
      
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_agent_reassign_team", ":agent_no"),

         (assign, ":initial_courage_score", 5500),
         (store_random_in_range, ":randomized_addition_courage", 0, 3000), #average : 1500
         (val_add, ":initial_courage_score", ":randomized_addition_courage"), 
                   
         (agent_get_party_id, ":agent_party", ":agent_no"),
         (ge, ":agent_party", 0),         
         (party_get_morale, ":cur_morale", ":agent_party"),
         
         (store_sub, ":morale_effect_on_courage", ":cur_morale", 70),
         (val_mul, ":morale_effect_on_courage", 30), #this can effect morale with -2100..900
         (val_add, ":initial_courage_score", ":morale_effect_on_courage"), 
         
         #average = 6000 + 1500 = 7500; min : 6000, max : 9000
         #morale effect = min : -2100(party morale is 0), average : 0(party morale is 70), max : 900(party morale is 100)
         #min starting : 3900, max starting  : 9900, average starting : 6000
         (agent_set_slot, ":agent_no", slot_agent_courage_score, ":initial_courage_score"), 
		 (agent_set_slot, ":agent_no", slot_agent_courage_score_fading_out, 0), 
         ]),

      common_battle_init_banner,
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  
		 
      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
        (store_trigger_param_1, ":dead_agent_no"),
        (store_trigger_param_2, ":killer_agent_no"),
        (store_trigger_param_3, ":is_wounded"),

        (try_begin),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_ally, ":dead_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (agent_get_troop_id, ":dead_agent_troop_id", ":dead_agent_no"),
          (str_store_troop_name, s6, ":dead_agent_troop_id"),
          (assign, reg0, ":dead_agent_no"),
          (assign, reg1, ":killer_agent_no"),
          (assign, reg2, ":is_wounded"),
          (agent_get_team, reg3, ":dead_agent_no"),          
          #(display_message, "@{!}dead agent no : {reg0} ; killer agent no : {reg1} ; is_wounded : {reg2} ; dead agent team : {reg3} ; {s6} is added"), 
          (party_add_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), #addition_to_p_total_enemy_casualties
          (eq, ":is_wounded", 1),
          (party_wound_members, "p_total_enemy_casualties", ":dead_agent_troop_id", 1), 
        (try_end),

        (call_script, "script_apply_death_effect_on_courage_scores", ":dead_agent_no", ":killer_agent_no"),
       ]),

      (ti_tab_pressed, 0, 0,
       [
         (try_begin), 
		    (eq,"$g_battle_won",1),
			(eq, "$g_battle_result", 1),
			(call_script, "script_count_mission_casualties_from_agents"),
			(finish_mission, 1),
		 (else_try), 	
			(display_message, "str_cannot_leave_now"),
		 (end_try), 	
         ], []),

      (ti_question_answered, 0, 0, [],
       [(store_trigger_param_1,":answer"),
        (eq,":answer",0),
        (assign, "$pin_player_fallen", 0),
        (try_begin),
          (store_mission_timer_a, ":elapsed_time"),
          (gt, ":elapsed_time", 20),
          (str_store_string, s5, "str_retreat"),
          (call_script, "script_simulate_retreat", 10, 20, 1),
        (try_end),
        (call_script, "script_count_mission_casualties_from_agents"),
        (finish_mission,0),]),

      (ti_before_mission_start, 0, 0, [],
       [
         (team_set_relation, 0, 2, 1),
         (team_set_relation, 1, 3, 1),
         (call_script, "script_place_player_banner_near_inventory_bms"),

         (party_clear, "p_routed_enemies"),

         (assign, "$g_latest_order_1", 1), 
         (assign, "$g_latest_order_2", 1), 
         (assign, "$g_latest_order_3", 0), 
         (assign, "$g_latest_order_4", 3), 
		 (assign, "$g_latest_order_5", 3), 
         ]),

      
      (0, 0, ti_once, [], [(assign,"$g_battle_won",0),
                           (assign,"$defender_reinforcement_stage",0),
                           (assign,"$attacker_reinforcement_stage",0),
                           (call_script, "script_place_player_banner_near_inventory"),
                           (call_script, "script_combat_music_set_situation_with_culture"),
                           (assign, "$g_defender_reinforcement_limit", 7),
                           ]),

      common_music_situation_update,
      common_battle_check_friendly_kills,

      (1, 0, 5, [
                              
      #new (25.11.09) starts (sdsd = TODO : make a similar code to also helping ally encounters)
      #count all total (not dead) enemy soldiers (in battle area + not currently placed in battle area)
      (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
      (assign, ":total_enemy_soldiers", reg0),
      
      #decrease number of agents already in battle area to find all number of reinforcement enemies
      (assign, ":enemy_soldiers_in_battle_area", 0),
      (try_for_agents,":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_get_party_id, ":agent_party", ":cur_agent"),
        (try_begin),
          (neq, ":agent_party", "p_main_party"),
          (neg|agent_is_ally, ":cur_agent"),
          (val_add, ":enemy_soldiers_in_battle_area", 1),
        (try_end),
      (try_end),
      (store_sub, ":total_enemy_reinforcements", ":total_enemy_soldiers", ":enemy_soldiers_in_battle_area"),

      (try_begin),
        (lt, ":total_enemy_reinforcements", 15),
        (ge, "$defender_reinforcement_stage", 2),
        (eq, "$defender_reinforcement_limit_increased", 0),
        (val_add, "$g_defender_reinforcement_limit", 1),                    
        (assign, "$defender_reinforcement_limit_increased", 1),
      (try_end),    
      #new (25.11.09) ends
      
      
      
      
      
      
      (lt,"$defender_reinforcement_stage","$g_defender_reinforcement_limit"),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_defenders", 0),
                 (lt,":num_defenders",6)],
           [(add_reinforcements_to_entry,0,7),(assign, "$defender_reinforcement_limit_increased", 0),(val_add,"$defender_reinforcement_stage",1)]),
      
      (1, 0, 5, [(lt,"$attacker_reinforcement_stage",7),
                 (store_mission_timer_a,":mission_time"),
                 (ge,":mission_time",10),
                 (store_normalized_team_count,":num_attackers", 1),
                 (lt,":num_attackers",6)],
           [(add_reinforcements_to_entry,3,7),(val_add,"$attacker_reinforcement_stage",1)]),

      common_battle_check_victory_condition,
      common_battle_victory_display,

      (1, 4, ti_once, [(main_hero_fallen)],
          [
              (assign, "$pin_player_fallen", 1),
              (str_store_string, s5, "str_retreat"),
              (call_script, "script_simulate_retreat", 10, 20, 1),
              (assign, "$g_battle_result", -1),
              (set_mission_result,-1),
              (call_script, "script_count_mission_casualties_from_agents"),
              (finish_mission,0)]),

      common_battle_inventory,


      #AI Triggers
      (0, 0, ti_once, [
          (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          ],
       [(call_script, "script_select_battle_tactic"),
        (call_script, "script_battle_tactic_init"),
        #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        ]),
      
      (3, 0, 0, [
          (call_script, "script_apply_effect_of_other_people_on_courage_scores"),
              ], []), #calculating and applying effect of people on others courage scores

      (3, 0, 0, [
          (try_for_agents, ":agent_no"),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),          
            (store_mission_timer_a,":mission_time"),
            (ge,":mission_time",3),          
            (call_script, "script_decide_run_away_or_not", ":agent_no", ":mission_time"),
          (try_end),          
              ], []), #controlling courage score and if needed deciding to run away for each agent

      (2, 0, 0, [
          (store_mission_timer_a,":mission_time"),

          (ge,":mission_time",3),
          
          (call_script, "script_battle_tactic_apply"),
          ], []), #applying battle tactic

      common_battle_order_panel,
      common_battle_order_panel_tick,

    ],
  ),  

    (
    "multiplayer_duel",mtf_battle_mode,-1, #duel mode
    "You lead your men to battle.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (5,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (8,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (15,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (16,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (17,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (18,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (19,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (20,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (21,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (22,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (23,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (24,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (25,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (26,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (27,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (28,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (29,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (30,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (31,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),

      (32,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (33,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (34,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (35,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (36,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (37,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (38,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (39,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (40,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (41,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (42,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (43,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (44,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (45,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (46,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (47,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (48,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (49,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (50,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (51,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (52,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (53,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (54,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (55,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),

      (56,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (57,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (58,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (59,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (60,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (61,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (62,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (63,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
     ],
    [
      
      multiplayer_server_check_polls,

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (call_script, "script_multiplayer_server_on_agent_spawn_common", ":agent_no"),
         ]),
      
      (ti_server_player_joined, 0, 0, [],
       [
         (store_trigger_param_1, ":player_no"),
         (call_script, "script_multiplayer_server_player_joined_common", ":player_no"),
         ]),

      (ti_before_mission_start, 0, 0, [],
       [
         (assign, "$g_multiplayer_game_type", multiplayer_game_type_duel),
         (call_script, "script_multiplayer_server_before_mission_start_common"),
         #make everyone see themselves as allies, no friendly fire
         (team_set_relation, 0, 0, 1),
         (team_set_relation, 0, 1, 1),
         (team_set_relation, 1, 1, 1),
         (mission_set_duel_mode, 1),
         (call_script, "script_multiplayer_init_mission_variables"),
         (call_script, "script_multiplayer_remove_destroy_mod_targets"),
         (call_script, "script_multiplayer_remove_headquarters_flags"), # close this line and open map in deathmatch mod and use all ladders firstly 
         ]),                                                            # to be able to edit maps without damaging any headquarters flags ext. 

      (ti_after_mission_start, 0, 0, [], 
       [
         (set_spawn_effector_scene_prop_kind, 0, -1), #during this mission, agents of "team 0" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (set_spawn_effector_scene_prop_kind, 1, -1), #during this mission, agents of "team 1" will try to spawn around scene props with kind equal to -1(no effector for this mod)
         (call_script, "script_initialize_all_scene_prop_slots"),
         (call_script, "script_multiplayer_move_moveable_objects_initial_positions"),
         (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
         ]),

      (ti_on_multiplayer_mission_end, 0, 0, [],
       [
         (call_script, "script_multiplayer_event_mission_end"),
         (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
         (start_presentation, "prsnt_multiplayer_stats_chart_deathmatch"),
         ]),

      (ti_on_agent_killed_or_wounded, 0, 0, [],
       [
         (store_trigger_param_1, ":dead_agent_no"), 
         (store_trigger_param_2, ":killer_agent_no"), 

         (call_script, "script_multiplayer_server_on_agent_killed_or_wounded_common", ":dead_agent_no", ":killer_agent_no"),

         (try_begin),
           (get_player_agent_no, ":player_agent"),
           (agent_is_active, ":player_agent"),
           (agent_slot_ge, ":player_agent", slot_agent_in_duel_with, 0),
           (try_begin),
             (eq, ":dead_agent_no", ":player_agent"),
             (display_message, "str_you_have_lost_a_duel"),
           (else_try),
             (agent_slot_eq, ":player_agent", slot_agent_in_duel_with, ":dead_agent_no"),
             (display_message, "str_you_have_won_a_duel"),
           (try_end),
         (try_end),
         (try_begin),
           (agent_slot_ge, ":dead_agent_no", slot_agent_in_duel_with, 0),
           (agent_get_slot, ":duelist_agent_no", ":dead_agent_no", slot_agent_in_duel_with),
           (agent_set_slot, ":dead_agent_no", slot_agent_in_duel_with, -1),
           (try_begin),
             (agent_is_active, ":duelist_agent_no"),
             (agent_set_slot, ":duelist_agent_no", slot_agent_in_duel_with, -1),
             (agent_clear_relations_with_agents, ":duelist_agent_no"),
             (try_begin),
               (agent_get_player_id, ":duelist_player_no", ":duelist_agent_no"),
               (neg|player_is_active, ":duelist_player_no"), #might be AI
               (agent_force_rethink, ":duelist_agent_no"),
             (try_end),
           (try_end),
         (try_end),
         ]),
      
      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         (get_max_players, ":num_players"),
         (try_for_range, ":player_no", 0, ":num_players"),
           (player_is_active, ":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

           (player_get_team_no, ":player_team", ":player_no"), #if player is currently spectator do not spawn his agent
           (lt, ":player_team", multi_team_spectator),

           (player_get_troop_id, ":player_troop", ":player_no"), #if troop is not selected do not spawn his agent
           (ge, ":player_troop", 0),

           (player_get_agent_id, ":player_agent", ":player_no"),
           (assign, ":spawn_new", 0),
           (try_begin),
             (player_get_slot, ":player_first_spawn", ":player_no", slot_player_first_spawn),
             (eq, ":player_first_spawn", 1),
             (assign, ":spawn_new", 1),
             (player_set_slot, ":player_no", slot_player_first_spawn, 0),
           (else_try),
             (try_begin),
               (lt, ":player_agent", 0),
               (assign, ":spawn_new", 1),
             (else_try),
               (neg|agent_is_alive, ":player_agent"),
               (agent_get_time_elapsed_since_removed, ":elapsed_time", ":player_agent"),
               (gt, ":elapsed_time", "$g_multiplayer_respawn_period"),
               (assign, ":spawn_new", 1),
             (try_end),             
           (try_end),
           (eq, ":spawn_new", 1),
           (call_script, "script_multiplayer_buy_agent_equipment", ":player_no"),

           (troop_get_inventory_slot, ":has_item", ":player_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),
         
           (call_script, "script_multiplayer_find_spawn_point", ":player_team", 0, ":is_horseman"), 
           (player_spawn_new_agent, ":player_no", reg0),
         (try_end),
         ]),

      (1, 0, 0, [ (multiplayer_is_server),
                  (this_or_next|gt,"$g_multiplayer_num_bots_team_1",0),
                  (gt,"$g_multiplayer_num_bots_team_2",0), # are there any bots?
                ], #do this in every new frame, but not at the same time
       [
         (store_mission_timer_a, ":mission_timer"),
         (ge, ":mission_timer", 2),
         (assign, ":team_1_count", 0),
         (assign, ":team_2_count", 0),
         (try_for_agents, ":cur_agent"),
           (agent_is_non_player, ":cur_agent"),
           (agent_is_human, ":cur_agent"),
           (assign, ":will_be_counted", 0),
           (try_begin),
             (agent_is_alive, ":cur_agent"),
             (assign, ":will_be_counted", 1), #alive so will be counted
           (else_try),
             (agent_get_time_elapsed_since_removed, ":elapsed_time", ":cur_agent"),
             (le, ":elapsed_time", "$g_multiplayer_respawn_period"),
             (assign, ":will_be_counted", 1), 
           (try_end),
           (eq, ":will_be_counted", 1),
           (agent_get_team, ":cur_team", ":cur_agent"),
           (try_begin),
             (eq, ":cur_team", 0),
             (val_add, ":team_1_count", 1),
           (else_try),
             (eq, ":cur_team", 1),
             (val_add, ":team_2_count", 1),
           (try_end),
         (try_end),
         (store_sub, "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_team_1", ":team_1_count"),
         (store_sub, "$g_multiplayer_num_bots_required_team_2", "$g_multiplayer_num_bots_team_2", ":team_2_count"),
         (val_max, "$g_multiplayer_num_bots_required_team_1", 0),
         (val_max, "$g_multiplayer_num_bots_required_team_2", 0),
         ]),

      (0, 0, 0, [],
       [
         (multiplayer_is_server),
         (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
         (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"),
         (try_begin),
           (gt, ":total_req", 0),
           (store_random_in_range, ":random_req", 0, ":total_req"),
           (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),
           (try_begin),
             (lt, ":random_req", 0),
             #add to team 1
             (assign, ":selected_team", 0),
             (val_sub, "$g_multiplayer_num_bots_required_team_1", 1),
           (else_try),
             #add to team 2
             (assign, ":selected_team", 1),
             (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
           (try_end),

           (team_get_faction, ":team_faction_no", ":selected_team"),
           (assign, ":available_troops_in_faction", 0),

           (try_for_range, ":troop_no", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
             (store_troop_faction, ":troop_faction", ":troop_no"),
             (eq, ":troop_faction", ":team_faction_no"),
             (val_add, ":available_troops_in_faction", 1),
           (try_end),

           (store_random_in_range, ":random_troop_index", 0, ":available_troops_in_faction"),
           (assign, ":end_cond", multiplayer_ai_troops_end),
           (try_for_range, ":troop_no", multiplayer_ai_troops_begin, ":end_cond"),
             (store_troop_faction, ":troop_faction", ":troop_no"),
             (eq, ":troop_faction", ":team_faction_no"),
             (val_sub, ":random_troop_index", 1),
             (lt, ":random_troop_index", 0),
             (assign, ":end_cond", 0),
             (assign, ":selected_troop", ":troop_no"),
           (try_end),
         
           (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
           (try_begin),
             (ge, ":has_item", 0),
             (assign, ":is_horseman", 1),
           (else_try),
             (assign, ":is_horseman", 0),
           (try_end),

           (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"), 
           (store_current_scene, ":cur_scene"),
           (modify_visitors_at_site, ":cur_scene"),
           (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", -1),
           (assign, "$g_multiplayer_ready_for_spawning_agent", 0),
         (try_end),
         ]),

      (1, 0, 0, [],
       [
         (multiplayer_is_server),
         #checking for restarting the map
         (assign, ":end_map", 0),
         (try_begin),
           (store_mission_timer_a, ":mission_timer"),
           (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
           (gt, ":mission_timer", ":game_max_seconds"),
           (assign, ":end_map", 1),
         (try_end),
         (try_begin),
           (eq, ":end_map", 1),
           (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
           (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 0),
           (call_script, "script_game_set_multiplayer_mission_end"),
         (try_end),
         ]),
        
      (ti_tab_pressed, 0, 0, [],
       [
         (try_begin),
           (eq, "$g_multiplayer_mission_end_screen", 0),
           (assign, "$g_multiplayer_stats_chart_opened_manually", 1),
           (start_presentation, "prsnt_multiplayer_stats_chart_deathmatch"),
         (try_end),
         ]),

      multiplayer_once_at_the_first_frame,
      
      (ti_escape_pressed, 0, 0, [],
       [
         (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart_deathmatch"),
         (eq, "$g_waiting_for_confirmation_to_terminate", 0),
         (start_presentation, "prsnt_multiplayer_escape_menu"),
         ]),

      (1, 0, 0, [],
       [
         (store_mission_timer_a, ":mission_timer"),
         (store_sub, ":duel_start_time", ":mission_timer", 3),
         (try_for_agents, ":cur_agent"),
           (agent_slot_ge, ":cur_agent", slot_agent_in_duel_with, 0),
           (agent_get_slot, ":duel_time", ":cur_agent", slot_agent_duel_start_time),
           (ge, ":duel_time", 0),
           (le, ":duel_time", ":duel_start_time"),
           (agent_set_slot, ":cur_agent", slot_agent_duel_start_time, -1),
           (agent_get_slot, ":opponent_agent", ":cur_agent", slot_agent_in_duel_with),
           (agent_is_active, ":opponent_agent"),
           (agent_add_relation_with_agent, ":cur_agent", ":opponent_agent", -1),
           (agent_force_rethink, ":cur_agent"),
         (try_end),
         ]),
      ],
  ),  
  
  
  (
    "oim_castle_attack_walls_2_ladder",mtf_battle_mode|mtf_synch_inventory,-1,
    "You attack the walls of the castle...",
    [
     (0, mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,12,[]),
     (0, mtef_attackers|mtef_team_1,af_override_horse,aif_start_alarmed,0,[]),
     (10,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (11,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
     (15,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,0,[]),
	 (41,mtef_defenders|mtef_team_0,af_override_horse,aif_start_alarmed,7,[]),
     (40,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (42,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (43,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (44,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,1,[]),
     (45,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,3,[]),
     (46,mtef_defenders|mtef_team_0|mtef_archers_first,af_override_horse,aif_start_alarmed,3,[]),
     ],
    [
      
      common_battle_mission_start,
      common_battle_tab_press,
      common_siege_question_answered,
      common_siege_init,
      common_music_situation_update,
      common_siege_ai_trigger_init,
      common_siege_ai_trigger_init_2,
      common_siege_ai_trigger_init_after_2_secs,
      common_siege_defender_reinforcement_check,
      common_siege_defender_reinforcement_archer_reposition,
      common_siege_attacker_reinforcement_check,
      common_siege_attacker_do_not_stall,
      common_battle_check_friendly_kills,
      common_battle_check_victory_condition,
      common_battle_victory_display,
      common_siege_refill_ammo,
      common_siege_check_defeat_condition,
      common_battle_order_panel,
      common_battle_order_panel_tick,
      common_inventory_not_available,
 	  custom_oim_replace_items_begin,
	  common_battle_init_banner,
	  oim_common_ladders_system_init,	  
	  oim_common_ladders_system_process, 
	  custom_oim_replace_items_nerf,
	  oim_on_horse_dismount,
	  oim_common_process_siege_attackers_no_stack,

    ],
  ),  
  
  #OiM new training mission template
  (
    "oim_tutorial_training_ground",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,0,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  
      (5,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (8,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	],
	[
          
	  (ti_before_mission_start, 0, 0, [], 
	   [
	    (call_script, "script_change_banners_and_chest"), 
		(assign, "$g_oim_training_stage", 0),
		
	    (team_set_relation, 0, 2, 1),
		(team_set_relation, 1, 3, 1),
	   ]),	
	   
	   
      common_inventory_not_available,
	  common_battle_mission_start,
      common_battle_order_panel,
      common_battle_order_panel_tick,

	  
     (ti_tab_pressed, 0, 0,
       [
         (display_message, "str_cannot_leave_now"),
         ], []),

      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
		 (try_begin), 
			(this_or_next|eq, ":troop_no", "trp_foot_gop"),
			(this_or_next|eq, ":troop_no", "trp_pahan_gop"),
			(             eq, ":troop_no", "trp_mounted_gop"),
			(agent_set_team, ":agent_no", 1),
		  (else_try), 
		    (agent_set_team, ":agent_no", 0),
		  (end_try), 
		  (val_add, "$g_troop_spawned", 1),
         ]),
	  	 
      (0, 0, 0, [],
       [  
                 (store_mission_timer_a_msec, ":mission_timer"),
		 (store_sub, ":time_diff", ":mission_timer", "$g_last_time"),
		 (get_player_agent_no, ":player_agent"),
		 (agent_is_active, ":player_agent"),
		 (agent_get_team, ":player_team", ":player_agent"), 
                 (try_for_agents, ":cur_agent"),
			(agent_is_active, ":cur_agent"), 
			(agent_is_alive, ":cur_agent"), 
			(agent_is_human, ":cur_agent"), 
                        (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
                        (eq, ":cur_agent_troop", "trp_oim_monfore_tutorial"),
                        (assign, ":monfore_agent", ":cur_agent"),
			(agent_set_hit_points, ":monfore_agent", 100),
                 (try_end),
		 #(agent_get_action_dir, ":action_dir_attacker", ":player_agent"),
		 (try_begin), 
			(eq, "$g_oim_training_stage", 0), 
			#(dialog_box, "str_oim_training_1_text", "str_oim_training_1_caption"), 
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 
			(eq, "$g_oim_training_stage", 1),
			(dialog_box, "str_oim_training_2_text", "str_oim_training_2_caption"), 
			(val_add, "$g_oim_training_stage", 1), 
			(add_visitors_to_current_scene, 1, "trp_oim_monfore_tutorial", 1),
		 #code first few words Monfore
		 (else_try),
			(eq, "$g_oim_training_stage", 2), 
			(agent_is_active, ":monfore_agent"), 
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try),
                        (eq, "$g_oim_training_stage", 3), 		 
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
                        (start_mission_conversation, "trp_oim_monfore_tutorial"),
			(agent_equip_item, ":player_agent", "itm_rusty_palash"),
			(agent_set_wielded_item, ":player_agent", "itm_rusty_palash"),
		 (else_try),
			(eq, "$g_oim_training_stage", 4), 
			(neg|conversation_screen_is_active),			
			(dialog_box, "str_oim_training_1_text", "str_oim_training_1_caption"), 
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try),
                        (eq, "$g_oim_training_stage", 5), 		 
                        (assign, "$g_tutorial_training_ground_melee_state", 1), #down
			(tutorial_message_set_size, 17, 17),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),
                        (tutorial_message, "str_tutorial_training_ground_attack_training_down"),
                        (store_sub, "$g_tutorial_mouse_dir", "$g_tutorial_training_ground_melee_state", 1),
                        (assign, "$g_tutorial_mouse_click", 0),
                        (start_presentation, "prsnt_tutorial_show_mouse_movement"),		
		 (else_try),
                        (eq, "$g_oim_training_stage", 6), 		 
                        (assign, "$g_tutorial_training_ground_melee_state", 4), #up
			(ge, ":time_diff", 250),
                        (tutorial_message, "str_tutorial_training_ground_attack_training_up"),
                        (store_sub, "$g_tutorial_mouse_dir", "$g_tutorial_training_ground_melee_state", 1),
                        (assign, "$g_tutorial_mouse_click", 0),
                        (start_presentation, "prsnt_tutorial_show_mouse_movement"),		
		 (else_try),
                        (eq, "$g_oim_training_stage", 7), 		 
                        (assign, "$g_tutorial_training_ground_melee_state", 2), #right
                        (tutorial_message, "str_tutorial_training_ground_attack_training_right"),
                        (store_sub, "$g_tutorial_mouse_dir", "$g_tutorial_training_ground_melee_state", 1),
                        (assign, "$g_tutorial_mouse_click", 0),
                        (start_presentation, "prsnt_tutorial_show_mouse_movement"),		
		 (else_try),
                        (eq, "$g_oim_training_stage", 8), 		 
                        (assign, "$g_tutorial_training_ground_melee_state", 3), #left
                        (tutorial_message, "str_tutorial_training_ground_attack_training_left"),
                        (store_sub, "$g_tutorial_mouse_dir", "$g_tutorial_training_ground_melee_state", 1),
                        (assign, "$g_tutorial_mouse_click", 0),
                        (start_presentation, "prsnt_tutorial_show_mouse_movement"),	
		 (else_try),
                        (ge, ":time_diff", 750),
			(eq, "$g_oim_training_stage", 9), 		 
			(dialog_box, "str_oim_training_10_text", "str_oim_training_10_caption"), 
			(val_add, "$g_oim_training_stage", 1), 
			(assign, "$g_last_time", ":mission_timer"),
                 (else_try), 
			(ge, ":time_diff", 10),
                        (eq, "$g_oim_training_stage", 10), 		 
			(dialog_box, "str_oim_training_11_text", "str_oim_training_11_caption"), 
			(val_add, "$g_oim_training_stage", 1), 
			(assign, "$g_last_time", ":mission_timer"),
                 (else_try), 
			(ge, ":time_diff", 250),
			(eq, "$g_oim_training_stage", 11), 		 
			(agent_is_active, ":monfore_agent"), 
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try),
			(eq, "$g_oim_training_stage", 12), 	
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
                        (start_mission_conversation, "trp_oim_monfore_tutorial"),
			(assign, "$g_last_time", ":mission_timer"),
                 (else_try), 
			(ge, ":time_diff", 250),
			(eq, "$g_oim_training_stage", 13), 		 
			(assign, "$g_troop_spawn_req", 3),
			(assign, "$g_troop_spawned", 0),
			(add_visitors_to_current_scene, 5, "trp_foot_gop", 3),
			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_hold),
			(team_give_order, 1, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			(val_add, "$g_oim_training_stage", 1), 
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try), 
			(eq, "$g_oim_training_stage", 14), 		 
			(ge, ":time_diff", 8000), #1
			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 
			(eq, "$g_oim_training_stage", 15), 	
			(eq, "$g_troop_spawn_req", "$g_troop_spawned"),
			(call_script, "script_get_alive_enemies_count", ":player_team"),
			(eq, reg0, 0), 
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 
			(val_add, "$g_oim_training_stage", 1), 
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try),
			(eq, "$g_oim_training_stage", 16), 	
			(ge, ":time_diff", 100), #2
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
                        (start_mission_conversation, "trp_oim_monfore_tutorial"),
		 (else_try), 	
			(eq, "$g_oim_training_stage", 17), 	
			(agent_equip_item, ":player_agent", "itm_pistol"),
			(agent_equip_item, ":player_agent", "itm_cartridges"),
			(agent_set_wielded_item, ":player_agent", "itm_pistol"),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 	
			(eq, "$g_oim_training_stage", 18), 		
			(neg|conversation_screen_is_active),			
			(dialog_box, "str_oim_training_3_text", "str_oim_training_3_caption"), 
			(val_add, "$g_oim_training_stage", 1), 			
		 (else_try), 	
			(eq, "$g_oim_training_stage", 19), 	
			(assign, "$g_troop_spawn_req", 5),
			(assign, "$g_troop_spawned", 0),
			(add_visitors_to_current_scene, 6, "trp_foot_gop", 5),
			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_hold),
			(team_give_order, 1, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			(assign, "$g_last_time", ":mission_timer"),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 			
			(eq, "$g_oim_training_stage", 20), 	
			(ge, ":time_diff", 16500), #2
			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 
			(eq, "$g_oim_training_stage", 21), 		 
			(eq, "$g_troop_spawn_req", "$g_troop_spawned"),
			(call_script, "script_get_alive_enemies_count", ":player_team"),
			(eq, reg0, 0), 
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1),
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 
			(val_add, "$g_oim_training_stage", 1), 
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try),
			(ge, ":time_diff", 700),
			(eq, "$g_oim_training_stage", 22), 	
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
                        (start_mission_conversation, "trp_oim_monfore_tutorial"),
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try),
			(ge, ":time_diff", 100),
			(neg|conversation_screen_is_active),			
			(eq, "$g_oim_training_stage", 23), 		 
			(call_script, "script_get_mission_agent_count_of_kind", "trp_foot_gop"),
			(eq, reg0, 0), 
			(entry_point_get_position, pos0, 20),
			(agent_get_team, ":team", ":monfore_agent"),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),
			##(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			##(agent_force_rethink, ":monfore_agent"),
			(val_add, "$g_oim_training_stage", 1), 
                        (entry_point_get_position, pos1, 20),
                        (set_spawn_position, pos1),
                        (spawn_horse, "itm_very_bad_horse"),
                        (entry_point_get_position, pos1, 21),
                        (set_spawn_position, pos1),
                        (spawn_horse, "itm_very_bad_horse"),
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try), 
			(eq, "$g_oim_training_stage", 24), 
			(ge, ":time_diff", 100),
			(tutorial_message, "str_oim_training_4_text"),
			(entry_point_get_position, pos0, 20),
			##(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			##(agent_force_rethink, ":monfore_agent"),
			##(entry_point_get_position, pos0, 20),	
			(agent_get_position, pos1, ":monfore_agent"),	
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 	
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 
			(eq, "$g_oim_training_stage", 25), 
			(set_show_messages, 0),
			(entry_point_get_position, pos0, 20),	
			(agent_get_position, pos1, ":monfore_agent"),	
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 	
			##(agent_clear_scripted_mode, ":monfore_agent"),	
			(agent_force_rethink, ":monfore_agent"),			
			(agent_get_team, 0, ":monfore_agent"), 
			(team_give_order, 0, grc_everyone, mordr_mount),
			(val_add, "$g_oim_training_stage", 1), 
			(set_show_messages, 1),
		 (else_try), 
			(eq, "$g_oim_training_stage", 26), 
			(agent_get_horse, ":horse", ":monfore_agent"),
			(agent_get_horse, ":horse_pl", ":player_agent"),
			(agent_is_active, ":horse"),
			(agent_is_active, ":horse_pl"),
		 	(val_add, "$g_oim_training_stage", 1), 
			(entry_point_get_position, pos0, 22),
			##(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			##(agent_force_rethink, ":monfore_agent"),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),

		 (else_try), 
			(eq, "$g_oim_training_stage", 27), 
			(entry_point_get_position, pos0, 22),	
			(agent_get_position, pos1, ":monfore_agent"),	
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 	
			#spawn monfore army and mounted bandits
			(add_visitors_to_current_scene, 7, "trp_foot_gop", 4),
			(add_visitors_to_current_scene, 8, "trp_foot_gop", 4),
			(add_visitors_to_current_scene, 9, "trp_foot_gop", 4),

			(add_visitors_to_current_scene, 10, "trp_pahan_gop", 2),
			(add_visitors_to_current_scene, 11, "trp_pahan_gop", 2),
			(add_visitors_to_current_scene, 12, "trp_pahan_gop", 2),
			(add_visitors_to_current_scene, 13, "trp_mounted_gop", 6),
			
			#spawn add forces
			(add_visitors_to_current_scene, 2, "trp_schwarzer_ritter", 1),
			(add_visitors_to_current_scene, 3, "trp_sved_lancers", 4),
			(add_visitors_to_current_scene, 4, "trp_nord_champion", 4),

			(agent_clear_scripted_mode, ":monfore_agent"),	
			(agent_force_rethink, ":monfore_agent"),			

			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_charge),
			(team_give_order, 1, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			
			
			#change message
			(tutorial_message, "str_oim_training_5_text"),
			(assign, "$g_last_time", ":mission_timer"),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try),
			(eq, "$g_oim_training_stage", 28), 
			(ge, ":time_diff", 500),
			(tutorial_message, -1),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try),
			(eq, "$g_oim_training_stage", 29), 
			(agent_is_active, ":player_agent"), 
			(call_script, "script_get_alive_enemies_count", ":player_team"),
			(eq, reg0, 0),
			(val_add, "$g_oim_training_stage", 1), 
		 (else_try), 
			(eq, "$g_oim_training_stage", 30), 	
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1),
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 
			(val_add, "$g_oim_training_stage", 1), 
			##(assign, "$g_last_time", ":mission_timer"),
		 (else_try),
			(eq, "$g_oim_training_stage", 31), 	
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
		    (start_mission_conversation, "trp_oim_monfore_tutorial"),
		 (else_try),
			(eq, "$g_oim_training_stage", 32), 	
			(assign, "$g_tutoral_mission_done", 1),
			(assign, "$g_battle_result", 1),
			(finish_mission),
		 (end_try), 
         ]),	

      (0, 0, 0, [],
       [
			(get_player_agent_no, ":player_agent"),
			(agent_is_active, ":player_agent"),
			(store_mission_timer_a_msec, ":mission_timer"),
                        (agent_get_attack_action, ":attack_action", ":player_agent"),
                        (eq, ":attack_action", 2), #release
			(agent_get_action_dir, ":action_dir", ":player_agent"),
			(try_begin), 
				(eq, "$g_oim_training_stage", 5), 
				(eq, ":action_dir", 0), #down
				(val_add, "$g_oim_training_stage", 1), 
				(assign, "$g_tutorial_mouse_click", -1), #stop presentation
			(else_try), 
				(eq, "$g_oim_training_stage", 6), 
				(eq, ":action_dir", 3), #up
				(val_add, "$g_oim_training_stage", 1), 
				(assign, "$g_tutorial_mouse_click", -1), #stop presentation
			(else_try), 
				(eq, "$g_oim_training_stage", 7), 
				(eq, ":action_dir", 1), #right
				(val_add, "$g_oim_training_stage", 1), 
				(assign, "$g_tutorial_mouse_click", -1), #stop presentation
			(else_try), 
				(eq, "$g_oim_training_stage", 8), 
				(eq, ":action_dir", 2), #left
				(val_add, "$g_oim_training_stage", 1), 
				(assign, "$g_tutorial_mouse_click", -1), #stop presentation
				(assign, "$g_last_time", ":mission_timer"),
				(tutorial_message, -1),
			(end_try), 
         ]),
		 
		 
		 (0.1, 0, 0, [
			(main_hero_fallen),
			(assign,"$g_battle_result",-1),
			(assign, "$g_tutoral_mission_done", 1),
		],
		[
			#(call_script, "script_custom_battle_end"),
			(finish_mission),
		 ]), 
		 #Add: 
		 #
		 #Control of time (timer)
		 #All tips
		 #Parring lessons
		 #Mika'il document about changes
		 #main hero skills
		 #
		(0, 0, 0, [],
		[
			(game_key_clicked, key_k),
			(assign, "$g_last_time", 9),
		])
 	],
	),  
	
  #tw new training mission template
  (
    "tw_tutorial_training_ground",mtf_arena_fight,-1,
    "You enter the training ground.",
    [
      (0,mtef_visitor_source|mtef_team_0,0,0,1,[]),
      (1,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (2,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (3,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
      (4,mtef_visitor_source|mtef_team_0,0,aif_start_alarmed,1,[]),
	  
      (5,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (6,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (7,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (8,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (9,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (10,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (11,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (12,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (13,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
      (14,mtef_visitor_source|mtef_team_1,0,aif_start_alarmed,1,[]),
	],
	[
          
	  (ti_before_mission_start, 0, 0, [], 
	   [
	    (call_script, "script_change_banners_and_chest"), 
		(assign, "$g_tw_training_stage", 0),
		(assign, "$g_tutorial_sound_1_played", 0),
		(assign, "$g_tutorial_sound_2_played", 0),
		(assign, "$g_tutorial_sound_3_played", 0),
		(assign, "$g_tutorial_sound_4_played", 0),
		(assign, "$g_tutorial_sound_5_played", 0),
		(assign, "$g_tutorial_sound_6_played", 0),
		(assign, "$g_tutorial_sound_7_played", 0),
		(assign, "$g_tutorial_sound_8_played", 0),
		(assign, "$g_tutorial_sound_9_played", 0),
		
	    (team_set_relation, 0, 2, 1),
		(team_set_relation, 1, 3, 1),
	   ]),	
	   
	   
      common_inventory_not_available,
	  common_battle_mission_start,
      common_battle_order_panel,
      common_battle_order_panel_tick,

	  (ti_tab_pressed, 0, 0, [],
	  [
		(question_box, "str_do_you_wish_to_leave_tutorial"),
        ]),
		
	(ti_question_answered, 0, 0, [],
	[
		(store_trigger_param_1, ":answer"),
        (eq, ":answer", 0),
		(assign, "$g_tutoral_mission_done", 1),
		(assign, "$g_battle_result", 1),
        (finish_mission),
		]),
		
      (ti_on_agent_spawn, 0, 0, [],
       [
         (store_trigger_param_1, ":agent_no"),
         (agent_get_troop_id, ":troop_no", ":agent_no"),
		 (try_begin), 
			(this_or_next|eq, ":troop_no", "trp_foot_gop"),
			(this_or_next|eq, ":troop_no", "trp_pahan_gop"),
			(eq, ":troop_no", "trp_mounted_gop"),
			(agent_set_team, ":agent_no", 1),
		  (else_try), 
			(agent_set_no_death_knock_down_only, ":agent_no", 1),
		    (agent_set_team, ":agent_no", 0),
		  (end_try), 
		  (val_add, "$g_troop_spawned", 1),
         ]),
		 
	(ti_on_agent_knocked_down, 0, 0, [],
       [    
			(store_trigger_param_1, ":cur_agent"),
		    (agent_is_active, ":cur_agent"), 
			(agent_is_alive, ":cur_agent"), 
			(agent_is_human, ":cur_agent"), 
            (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
			(try_begin), 
				(eq, ":cur_agent_troop", "trp_oim_monfore_tutorial"),
				(agent_set_hit_points, ":cur_agent", 100),
			(end_try), 	
			(try_begin), 
				(eq, ":cur_agent_troop", "trp_oim_shoha1_tutorial"),
				(agent_set_hit_points, ":cur_agent", 100),
			(end_try), 	
			(try_begin), 
				(eq, ":cur_agent_troop", "trp_oim_shoha2_tutorial"),
				(agent_set_hit_points, ":cur_agent", 100),
			(end_try),]),
		 
	  (0, 0, 0,
       [
         (call_script, "script_iterate_pointer_arrow"),
         ], []),
		
      (0, 0, 0, [],
       [
		 (mission_disable_talk),
         (store_mission_timer_a_msec, ":mission_timer"),
		 (store_sub, ":time_diff", ":mission_timer", "$g_last_time"),
		 (get_player_agent_no, ":player_agent"),
		 (agent_is_active, ":player_agent"),
		 (agent_get_team, ":player_team", ":player_agent"), 
         (try_for_agents, ":cur_agent"),
			(agent_is_active, ":cur_agent"), 
			(agent_is_alive, ":cur_agent"), 
			(agent_is_human, ":cur_agent"), 
            (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
			(try_begin), 
				(eq, ":cur_agent_troop", "trp_oim_monfore_tutorial"),
				(assign, ":monfore_agent", ":cur_agent"),
				(agent_set_hit_points, ":monfore_agent", 100),
			(end_try), 	
			(try_begin), 
				(eq, ":cur_agent_troop", "trp_oim_shoha1_tutorial"),
				(assign, ":ally1", ":cur_agent"),
				(agent_set_hit_points, ":ally1", 100),
			(end_try), 	
			(try_begin), 
				(eq, ":cur_agent_troop", "trp_oim_shoha2_tutorial"),
				(assign, ":ally2", ":cur_agent"),
				(agent_set_hit_points, ":ally2", 100),
			(end_try), 				
         (try_end),
		 (try_begin), 
			(eq, "$g_tw_training_stage", 0), 
			(assign, "$g_last_time", ":mission_timer"),
			(assign, "$g_pointer_arrow_height_adder", -1000),
			(agent_get_position, pos26, ":player_agent"), 
			
			(add_visitors_to_current_scene, 3, "trp_oim_monfore_tutorial", 1),
			(add_visitors_to_current_scene, 3, "trp_oim_shoha1_tutorial", 1),
			(add_visitors_to_current_scene, 3, "trp_oim_shoha2_tutorial", 1),
			
		    (add_visitors_to_current_scene, 10, "trp_foot_gop", 1),
			
			(assign, "$g_tw_training_stage", 100),
		(else_try), 
			(eq, "$g_tw_training_stage", 100), 
			(ge, ":time_diff", 120),
			
			(set_show_messages, 0),
			(entry_point_get_position, pos0, 2),
			(agent_get_team, ":team", ":monfore_agent"),
			(team_give_order, ":team", grc_everyone, mordr_charge),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),
			
			(entry_point_get_position, pos0, 1),
			(team_give_order, 1, grc_everyone, mordr_charge),
			(team_set_order_position, 1, grc_everyone, pos0),
			(team_give_order, 1, grc_everyone, mordr_hold),
			(team_set_order_position, 1, grc_everyone, pos0),
			(set_show_messages, 1),
			
			(assign, "$g_tw_training_stage", 1),
		 (else_try), 
			(eq, "$g_tw_training_stage", 1), 
			
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_16_text"),
			(ge, ":time_diff", 1000),
			(try_begin),
				(eq, "$g_tutorial_sound_1_played", 0),
				(play_sound, "snd_tutorial_narrator_1"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_1_played", 1),
			(try_end),
			
			(ge, ":time_diff", 3000),
			
			(agent_get_position, pos1, ":player_agent"),

                        (scene_prop_get_instance, ":tyn_id", "spr_oim_tyn_destructable", 0),                 
                        (prop_instance_get_position, pos29, ":tyn_id"),
			(get_distance_between_positions, ":dist",  pos29, pos1), 
			(le, ":dist", 400), #4 meters to fence.

			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_1_text"),
			(try_begin),
				(eq, "$g_tutorial_sound_2_played", 0),
				(try_begin),
					(store_sub, ":cut_limit", ":mission_timer", 16500),
					(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
					(stop_sound_channel, "$g_tutorial_last_sound_channel"),
				(try_end),
				(play_sound, "snd_tutorial_narrator_2"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_2_played", 1),
			(try_end),
			
			(entry_point_get_position, pos0, 4),
            (scene_prop_get_instance, ":pointer_instance", "spr_pointer_arrow", 0),
            (prop_instance_set_position, ":pointer_instance", pos0),
            (assign, "$g_pointer_arrow_height_adder", 300),
			   
			(assign, "$g_tw_training_stage", 2), 
			(agent_equip_item, ":player_agent", "itm_rusty_palash"),
			(agent_set_wielded_item, ":player_agent", "itm_rusty_palash"),
		 (else_try), 
			(eq, "$g_tw_training_stage", 2),
			(eq, "$g_fence_destroyed", 1),	
			(tutorial_message, -1),
			(assign, "$g_pointer_arrow_height_adder", -1000),
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_10_text"),
			(try_begin),
				(eq, "$g_tutorial_sound_3_played", 0),
				(try_begin),
					(store_sub, ":cut_limit", ":mission_timer", 11500),
					(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
					(stop_sound_channel, "$g_tutorial_last_sound_channel"),
				(try_end),
				(play_sound, "snd_tutorial_narrator_3"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_3_played", 1),
			(try_end),
			
			(ge, ":time_diff", 2500),
			(assign, "$g_tw_training_stage", 3), 
		 (else_try), 
			(eq, "$g_tw_training_stage", 3), 
			(try_begin), 
				(call_script, "script_get_alive_enemies_count", ":player_team"),
				(eq, reg0, 0), 
				(ge, ":time_diff", 3500),
				(tutorial_message, -1),
				(tutorial_message_set_size, 20, 20),
				(tutorial_message_set_position, 500, 650),
				(tutorial_message_set_center_justify, 0),
				(tutorial_message_set_background, 1),			
				(tutorial_message, "str_oim_training_17_text"),
				(try_begin),
					(eq, "$g_tutorial_sound_5_played", 0),
					(try_begin),
						(store_sub, ":cut_limit", ":mission_timer", 5500),
						(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
						(stop_sound_channel, "$g_tutorial_last_sound_channel"),
					(try_end),
					(play_sound, "snd_tutorial_narrator_5"),
					(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
					(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
					(assign, "$g_tutorial_sound_5_played", 1),
				(try_end),
			
				(agent_get_position, pos0, ":monfore_agent"),
				(scene_prop_get_instance, ":pointer_instance", "spr_pointer_arrow", 0),
				(prop_instance_set_position, ":pointer_instance", pos0),
				(assign, "$g_pointer_arrow_height_adder", 200),
			
				(assign, "$g_last_time", ":mission_timer"),
				(assign, "$g_tw_training_stage", 4), 
				(assign, "$g_tw_tutorial_displayed", -1),
			(else_try), 
				(entry_point_get_position, pos0, 1),
				(agent_get_position, pos1, ":player_agent"),
				(get_distance_between_positions, ":dist",  pos0, pos1), 
				(le, ":dist", 1000), 
				(tutorial_message, -1),
				(tutorial_message_set_size, 20, 20),
				(tutorial_message_set_position, 500, 650),
				(tutorial_message_set_center_justify, 0),
				(tutorial_message_set_background, 1),			
				(tutorial_message, "str_oim_training_21_text"),
				(try_begin),
					(eq, "$g_tutorial_sound_4_played", 0),
					(try_begin),
						(store_sub, ":cut_limit", ":mission_timer", 14500),
						(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
						(stop_sound_channel, "$g_tutorial_last_sound_channel"),
					(try_end),
					(play_sound, "snd_tutorial_narrator_4"),
					(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
					(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
					(assign, "$g_tutorial_sound_4_played", 1),
				(try_end),
				
				(try_for_agents, ":cur_agent"),
					(agent_is_active, ":cur_agent"), 
					(agent_is_alive, ":cur_agent"), 
					(agent_is_human, ":cur_agent"), 
					(agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
					(eq, ":cur_agent_troop", "trp_foot_gop"),
					(set_show_messages, 0),
					(team_give_order, 1, grc_everyone, mordr_charge),
					(set_show_messages, 1),
					(agent_force_rethink, ":cur_agent"),
				(try_end),
			(end_try), 		
		 (else_try), 
			(eq, "$g_tw_training_stage", 3), 
			(call_script, "script_get_alive_enemies_count", ":player_team"),
			(eq, reg0, 0), 
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try), 
			(eq, "$g_tw_training_stage", 4),	
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 750), 
			(assign, "$g_pointer_arrow_height_adder", -1000),
			(tutorial_message, -1),		
			(tutorial_message_set_size, 17, 17),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_14_text"),
			
			(add_visitors_to_current_scene, 5, "trp_foot_gop", 5),
			(assign, "$g_troop_spawn_req", 5),
			(assign, "$g_troop_spawned", 0),

			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_charge),
			(team_give_order, 1, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			(assign, "$g_last_time", ":mission_timer"),
			(assign, "$g_tw_training_stage", 5), 
		 (else_try), 
			(eq, "$g_tw_training_stage", 5),
			(eq, "$g_troop_spawn_req", "$g_troop_spawned"),
			(call_script, "script_get_alive_enemies_count", ":player_team"),
			(lt, reg0, "$g_troop_spawned"),
			(tutorial_message, -1),
			(eq, reg0, 0), 	
			(assign, "$g_last_time", ":mission_timer"),
			(assign, "$g_tw_training_stage", 45),
		 (else_try),
		    (eq, "$g_tw_training_stage", 45),
			(ge, ":time_diff", 3000),
			(agent_is_active, ":monfore_agent"), 
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 250), 
			(assign, "$g_last_time", ":mission_timer"),
			(assign, "$g_tw_training_stage", 6),
		 (else_try), 
			(eq, "$g_tw_training_stage", 6), 		
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
			(start_mission_conversation, "trp_oim_monfore_tutorial"),	
		(else_try), 
			(eq, "$g_tw_training_stage", 7), 
			(neg|conversation_screen_is_active),	
			(entry_point_get_position, pos0, 7),
			(scene_prop_get_instance, ":pointer_instance", "spr_pointer_arrow", 0),
			(prop_instance_set_position, ":pointer_instance", pos0),
			(assign, "$g_pointer_arrow_height_adder", 200),
			(set_show_messages, 0),
			(entry_point_get_position, pos0, 8),
			(team_give_order, 0, grc_everyone, mordr_charge),
			(team_set_order_position, 0, grc_everyone, pos0),
			(team_give_order, 0, grc_everyone, mordr_hold),
			(team_set_order_position, 0, grc_everyone, pos0),	
			(set_show_messages, 1),
			(assign, "$g_last_time", ":mission_timer"),
			(assign, "$g_tw_training_stage", 8),
		 (else_try), 
			(eq, "$g_tw_training_stage", 8), 
			(entry_point_get_position, pos0, 7),
			(agent_get_position, pos1, ":monfore_agent"),
			(agent_get_position, pos2, ":player_agent"),
			(get_distance_between_positions, ":dist1",  pos0, pos2),
			(get_distance_between_positions, ":dist2",  pos1, pos2),			
			(le, ":dist1", 500),
            (le, ":dist2", 700), 
			(agent_is_active, ":monfore_agent"), 
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1), 
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 300), 			
			(assign, "$g_tw_training_stage", 9),
		 (else_try), 
			(eq, "$g_tw_training_stage", 9), 
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
			(assign, "$g_last_time", ":mission_timer"),
			(start_mission_conversation, "trp_oim_monfore_tutorial"),	
		 (else_try), 
			(eq, "$g_tw_training_stage", 10),
			
			(ge, ":time_diff", 250),
			(neg|conversation_screen_is_active),		
			
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_11_text"),
			(try_begin),
				(eq, "$g_tutorial_sound_6_played", 0),
				(try_begin),
					(store_sub, ":cut_limit", ":mission_timer", 5500),
					(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
					(stop_sound_channel, "$g_tutorial_last_sound_channel"),
				(try_end),
				(play_sound, "snd_tutorial_narrator_6"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_6_played", 1),
			(try_end),
			
			(agent_equip_item, ":player_agent", "itm_pistol"),
			(agent_equip_item, ":player_agent", "itm_cartridges"),
			(agent_set_wielded_item, ":player_agent", "itm_pistol"),
			
			(assign, "$g_num_shots_fired", 0),
			(assign, "$g_tw_tutorial_mode", 1),
			
			(assign, "$g_tw_training_stage", 12),
		(else_try), 
			(eq, "$g_tw_training_stage", 12),
			(ge, "$g_num_shots_fired", 1),
			(neq, "$g_lock_destroyed", 1),
			
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_18_text"),
			
			(assign, "$g_tw_training_stage", 13),
		 (else_try), 
			(this_or_next|eq, "$g_tw_training_stage", 12),
			(eq, "$g_tw_training_stage", 13),
			(eq, "$g_lock_destroyed", 1),
			
			(assign, "$g_pointer_arrow_height_adder", -1000),
			(assign, "$g_tw_tutorial_mode", 0),
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_4_text"),
			(try_begin),
				(eq, "$g_tutorial_sound_7_played", 0),
				(try_begin),
					(store_sub, ":cut_limit", ":mission_timer", 23500),
					(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
					(stop_sound_channel, "$g_tutorial_last_sound_channel"),
				(try_end),
				(play_sound, "snd_tutorial_narrator_7"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_7_played", 1),
			(try_end),
			
			(entry_point_get_position, pos0, 20),
			(agent_get_team, ":team", ":monfore_agent"),
			(set_show_messages, 0),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(set_show_messages, 1),
			
			(entry_point_get_position, pos1, 31),	
			(set_spawn_position, pos1),
			(spawn_horse, "itm_sumpter_horse"),

			(entry_point_get_position, pos1, 32),	
			(set_spawn_position, pos1),
			(spawn_horse, "itm_sumpter_horse"),

			(entry_point_get_position, pos1, 33),	
			(set_spawn_position, pos1),
			(spawn_horse, "itm_sumpter_horse"),

			(entry_point_get_position, pos1, 34),	
			(set_spawn_position, pos1),
			(spawn_horse, "itm_sumpter_horse"),
		
			(assign, "$g_tw_training_stage", 14),
		 (else_try), 
			(eq, "$g_tw_training_stage", 14),
			(entry_point_get_position, pos0, 20),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1),
			(le, ":dist", 300),
			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_mount),
			(set_show_messages, 1),
			(assign, "$g_tw_training_stage", 15),
		 (else_try),
			(eq, "$g_tw_training_stage", 15),
			
			(agent_get_horse, ":horse", ":monfore_agent"),
			(agent_get_horse, ":horse_pl", ":player_agent"),
			(agent_get_horse, ":horse_1", ":ally1"),
			(agent_get_horse, ":horse_2", ":ally2"),
			(agent_is_active, ":horse_pl"),
			(agent_get_position, pos31, ":horse_pl"),
			(tutorial_message, -1),
			(agent_is_active, ":horse"),
			(agent_is_active, ":horse_1"),
			(agent_is_active, ":horse_2"),
			
			(entry_point_get_position, pos0, 21),
			(set_show_messages, 0),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),			
			(set_show_messages, 1),
			(assign, "$g_tw_training_stage", 16),
		 (else_try),
			(eq, "$g_tw_training_stage", 16), 
			
			(agent_get_horse, ":horse_pl", ":player_agent"),
			(agent_is_active, ":horse_pl"),
			(agent_get_position, pos32, ":horse_pl"),
			(get_distance_between_positions, ":dist",  pos31, pos32), 
			(ge, ":dist", 300), 
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_8_text"),
			(try_begin),
				(eq, "$g_tutorial_sound_8_played", 0),
				(try_begin),
					(store_sub, ":cut_limit", ":mission_timer", 8500),
					(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
					(stop_sound_channel, "$g_tutorial_last_sound_channel"),
				(try_end),
				(play_sound, "snd_tutorial_narrator_8"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_8_played", 1),
			(try_end),
			
			(assign, "$g_tw_training_stage", 17),
		(else_try),
			(eq, "$g_tw_training_stage", 17), 
			(entry_point_get_position, pos0, 21),	
			(agent_get_position, pos1, ":monfore_agent"),	
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 2000), 	
			(entry_point_get_position, pos0, 22),
			(set_show_messages, 0),
			(team_give_order, ":team", grc_everyone, mordr_charge),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),			
			(set_show_messages, 1),
			(assign, "$g_tw_training_stage", 18), 
		(else_try),
			(eq, "$g_tw_training_stage", 18), 
			(entry_point_get_position, pos0, 22),	
			(agent_get_position, pos1, ":monfore_agent"),	
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 2000),
			(entry_point_get_position, pos0, 11),
			(set_show_messages, 0),
			(team_give_order, ":team", grc_everyone, mordr_charge),
			(team_set_order_position, ":team", grc_everyone, pos0),
			(team_give_order, ":team", grc_everyone, mordr_hold),
			(team_set_order_position, ":team", grc_everyone, pos0),			
			(set_show_messages, 1),
			(assign, "$g_tw_training_stage", 19),
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try),
			(eq, "$g_tw_training_stage", 19), 
			(entry_point_get_position, pos0, 11),	
			(agent_get_position, pos1, ":monfore_agent"),	
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(le, ":dist", 2000),
			(tutorial_message_set_size, 20, 20),
			(tutorial_message_set_position, 500, 650),
			(tutorial_message_set_center_justify, 0),
			(tutorial_message_set_background, 1),			
			(tutorial_message, "str_oim_training_9_text"),
			(try_begin),
				(eq, "$g_tutorial_sound_9_played", 0),
				(try_begin),
					(store_sub, ":cut_limit", ":mission_timer", 20500),
					(gt, "$g_tutorial_last_sound_time", ":cut_limit"),
					(stop_sound_channel, "$g_tutorial_last_sound_channel"),
				(try_end),
				(play_sound, "snd_tutorial_narrator_9"),
				(store_last_sound_channel, "$g_tutorial_last_sound_channel"),
				(assign, "$g_tutorial_last_sound_time", ":mission_timer"),
				(assign, "$g_tutorial_sound_9_played", 1),
			(try_end),
			(this_or_next|le, ":dist", 500),
			(ge, ":time_diff", 10000),
			(add_visitors_to_current_scene, 12, "trp_mounted_gop", 8),
        
			(agent_clear_scripted_mode, ":monfore_agent"),	
			(agent_force_rethink, ":monfore_agent"),			
        
			(entry_point_get_position, pos0, 12),
			(set_show_messages, 0),
			(team_give_order, 0, grc_everyone, mordr_charge),
			(team_set_order_position, 0, grc_everyone, pos0),
			(team_give_order, 1, grc_everyone, mordr_charge),
			(set_show_messages, 1),
			(assign, "$g_tw_training_stage", 20), 
		 (else_try), 	
			(eq, "$g_tw_training_stage", 20), 
			(agent_is_active, ":player_agent"), 
			(call_script, "script_get_alive_enemies_count", ":player_team"),
			(eq, reg0, 0),
			(tutorial_message, -1),
			(assign, "$g_last_time", ":mission_timer"),
			(assign, "$g_tw_training_stage", 21),
			(assign, "$g_last_time", ":mission_timer"),
		 (else_try), 
			(eq, "$g_tw_training_stage", 21), 	
			(ge, ":time_diff", 1250),
			(agent_get_position, pos0, ":player_agent"),
			(agent_set_scripted_destination, ":monfore_agent", pos0, 1),
			(agent_force_rethink, ":monfore_agent"),
			(agent_get_position, pos0, ":player_agent"),
			(agent_get_position, pos1, ":monfore_agent"),
			(get_distance_between_positions, ":dist",  pos0, pos1), 
			(this_or_next|le, ":dist", 300),
			(ge, ":time_diff", 10000),
			(assign, "$g_tw_training_stage", 22),
		 (else_try),
			(eq, "$g_tw_training_stage", 22), 	
			(agent_clear_scripted_mode, ":monfore_agent"),
			(agent_force_rethink, ":monfore_agent"),
		    (start_mission_conversation, "trp_oim_monfore_tutorial"),
		 (else_try),
			(eq, "$g_tw_training_stage", 23), 	
			(assign, "$g_tutoral_mission_done", 1),
			(assign, "$g_battle_result", 1),
			(finish_mission),
		 (end_try),
         ]),	
		 
		 (0.1, 0, 0, [
			(main_hero_fallen),
			(assign,"$g_battle_result",-1),
			(assign, "$g_tutoral_mission_done", 1),
		],
		[
			(finish_mission),
		 ]), 
	],
	),  
	
	

]
