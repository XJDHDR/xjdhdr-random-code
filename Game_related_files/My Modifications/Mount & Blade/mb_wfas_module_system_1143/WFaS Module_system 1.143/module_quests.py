from header_quests import *

####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################

quests = [
# Note : This is defined as the first governer quest in module_constants.py: 
 ("deliver_message", "Deliver a Message to {s13}", qf_random_quest,
  "{s9} asked you to take a message to {s13}. {s13} was at {s4} when you were given this quest."
  ),
 ("deliver_message_to_enemy_lord", "Deliver a Message to {s13}", qf_random_quest,
  "{s9} asked you to take a message to {s13} of {s15}. {s13} was at {s4} when you were given this quest."
  ),
 ("raise_troops", "Raise {reg1} {s14}", qf_random_quest,
  "{s9} asked you to raise {reg1} {s14} and bring them to him."
  ),
 ("escort_lady", "Escort {s13} to {s14}", qf_random_quest,
  "None"
  ),
## ("rescue_lady_under_siege", "Rescue {s3} from {s4}", qf_random_quest,
##  "{s1} asked you to rescue his {s7} {s3} from {s4} and return her back to him."
##  ),
## ("deliver_message_to_lover", "Deliver Message to {s3}", qf_random_quest,
##  "{s1} asked you to take a message to his lover {s3} at {s4}."
##  ),
## ("bring_prisoners_to_enemy", "Bring Prisoners to {s4}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3} as prisoners to the guards at {s4}."
##  ),
## ("bring_reinforcements_to_siege", "Bring Reinforcements to the Siege of {s5}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3} to {s4} at the siege of {s5}."
##  ),
## ("deliver_supply_to_center_under_siege", "Deliver Supplies to {s5}", qf_random_quest,
##  "TODO: Take {reg1} cartloads of supplies from constable {s3} and deliver them to constable {s4} at {s5}."
##  ),
 ("deal_with_bandits_at_lords_village", "Save the Village of {s15}", qf_random_quest,
  "{s13} asked you to deal with the bandits who have taken refuge in his village of {s15}, and then report back to him."
  ),
 ("collect_taxes", "Collect Taxes from {s3}", qf_random_quest,
  "{s9} asked you to collect taxes from {s3}. He offered to give you one-fifth of all the money you collect there."
  ),
 ("hunt_down_fugitive", "Hunt Down {s4}", qf_random_quest,
  "{s9} asked you to hunt down the fugitive named {s4}. He is currently believed to be at {s3}."
  ),
## ("capture_messenger", "Capture {s3}", qf_random_quest,
##  "{s1} asked you to capture a {s3} and bring him back."
##  ),
## ("bring_back_deserters", "Bring {reg1} {s3}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3}."
##  ),
 ("kill_local_merchant", "Assassinate Local Merchant at {s3}", qf_random_quest,
  "{s9} asked you to assassinate a local merchant at {s3}."
  ),
 ("bring_back_runaway_serfs", "Bring Back Runaway Serfs", qf_random_quest,
  "{s9} asked you to find the three groups of runaway serfs, and bring them back to {s2}. He said all three groups were fleeing in the direction of {s3}."
  ),
 ("follow_spy", "Follow the Spy to the Meeting", qf_random_quest,
  "{s11} asked you to follow the spy who will be leaving from {s12}. You must be careful not to be seen by the spy during his travel, or he may become suspicious and turn back. Once the spy meets with his accomplice, you are to ambush and capture them, and bring them both back to {s11}."
  ),
 ("capture_enemy_hero", "Capture a Lord from {s13}", qf_random_quest,
  "TODO: {s11} asked you to capture a lord from {s13}."
  ),
 ("lend_companion", "Lend Your Companion {s3} to {s9}", qf_random_quest,
  "{s9} asked you to lend your companion {s3} to him for a week."
  ),
 ("collect_debt", "Collect the debt that {s3} owes to {s9}", qf_random_quest,
  "{s9} asked you to collect the debt of {reg4} thaler that {s3} owes to him."
  ),
## ("capture_conspirators", "Capture Conspirators", qf_random_quest,
##  "TODO: {s1} asked you to capture all troops in {reg1} conspirator parties that plan to rebel against him and join {s3}."
##  ),
## ("defend_nobles_against_peasants", "Defend Nobles Against Peasants", qf_random_quest,
##  "TODO: {s1} asked you to defend {reg1} noble parties against peasants."
##  ),
 ("incriminate_loyal_commander", "Incriminate the Loyal Commander of {s13}, {s16}", qf_random_quest,
  "None"
  ),
 ("raid_caravan_to_start_war", "Raid {reg13} Caravans of {s13}", qf_random_quest,
  "None"
  ),
 ("meet_spy_in_enemy_town", "Meet Spy in {s13}", qf_random_quest,
  "None"
  ),
 ("capture_prisoners", "Bring {reg1} {s3} Prisoners", qf_random_quest,
  "{s9} wanted you to bring him {reg1} {s3} as prisoners."
  ),

## ("hunt_down_raiders", "Hunt Down Raiders",qf_random_quest,
##  "{s1} asked you to hunt down and punish the raiders that attacked a village near {s3} before they reach the safety of their base at {s4}."
##  ),

##################
# Enemy Kingdom Lord quests
##################
# Note : This is defined as the first enemy lord quest in module_constants.py:
 ("lend_surgeon", "Lend Your Surgeon {s3} to {s1}", qf_random_quest,
  "Lend your experienced surgeon {s3} to {s1}."
  ),

##################
# Kingdom Army quests
##################
# Note : This is defined as lord quests end in module_constants.py:
 ("follow_army", "Follow {s9}'s Army", qf_random_quest,
  "None"
  ),
 ("report_to_army", "Report to Marshall {s13}", qf_random_quest,
  "None"
  ),
# Note : This is defined as the first army quest in module_constants.py:
 ("deliver_cattle_to_army", "Deliver {reg3} Head of Cattle to {s13}", qf_random_quest,
  "The elder of the village of {s3} has asked you to bring them {reg5} head of cattle."
  ),
 ("join_siege_with_army", "Join the Siege of {s14}", qf_random_quest,
  "None"
  ),
 ("scout_waypoints", "Scout {s13}, {s14}, and {s15}", qf_random_quest, "None"
  ),


##################
# Kingdom Lady quests
##################
# Note : This is defined as the first kingdom lady quest in module_constants.py:
 ("rescue_lord_by_replace", "Rescue {s13} from {s14}", qf_random_quest,
  "None"
  ),
 ("deliver_message_to_prisoner_lord", "Deliver a Message to {s13} at {s14}", qf_random_quest,
  "None"
  ),
  ("duel_for_lady", "Challenge {s13} to a Trial of Arms", qf_random_quest,
  "None"
  ),

##################
# Mayor quests
##################
# Note : This is defined as the first mayor quest in module_constants.py: 
 ("move_cattle_herd", "Move Cattle Herd to {s13}", qf_random_quest,
  "The mayor of {s10} asked you to move a cattle herd to {s13}."
  ),
 ("escort_merchant_caravan", "Escort the Merchant Caravan to {s8}", qf_random_quest,
  "Escort the merchant caravan to the town of {s8}."
  ),
 ("deliver_wine", "Deliver {reg5} Units of {s6} to {s4}", qf_random_quest,
  "{s9} of {s3} asked you to deliver {reg5} units of {s6} to the tavern in {s4} within the next seven days."
  ),
 ("troublesome_bandits", "Hunt Down the Troublesome Bandits", qf_random_quest,
  "{s9} of {s4} asked you to hunt down the troublesome bandits in the vicinity of the town."
  ),
 ("kidnapped_girl", "Ransom the Girl from the Bandits", qf_random_quest,
  "The mayor of {s4} gave you {reg12} thaler to pay the ransom of a girl kidnapped by bandits. You are to meet the bandits near {s3} and pay them the ransom. After that, you are to return the girl to {s4}."
  ),
 ("persuade_lords_to_make_peace", "Ensure that Neither Lord Objects to Peace", qf_random_quest,
  "The Mayor of {s4} promised you {reg12} thaler if you can ensure that neither {s12} nor {s13} pose a threat to a peace settlement between {s15} and {s14}. In order to do this, you must either convince them, or make sure they fall captive and remain so until a peace agreement is complete."
  ),
 ("deal_with_looters", "Deal with the Looters", qf_random_quest,
  "The Mayor of {s4} has asked you to deal with several bands of looters around {s4}, and bring back any goods you recover."
  ),
 ("deal_with_night_bandits", "Deal with the Night Bandits", qf_random_quest,
  "TODO: The Mayor of {s14} has asked you to deal with night bandits at {s14}."
  ),

############
# Village Elder quests
############
# Note : This is defined as the first village elder quest in module_constants.py:
 ("deliver_grain", "Bring wheat to {s3}", qf_random_quest,
  "The elder of the village of {s3} has asked you to bring them {reg5} packs of wheat.."
  ), 
 ("deliver_cattle", "Cattle for {s3}", qf_random_quest,
  "The elder of the village of {s3} asked you to bring {reg5} heads of cattle."
  ), 
 ("train_peasants_against_bandits", "A Bit of Training", qf_random_quest,
  "None"
  ), 
# Deliver horses, Deliver food, Escort_Caravan, Hunt bandits, Ransom Merchant.
## ("capture_nobleman", "Capture Nobleman",qf_random_quest,
##  "{s1} wanted you to capture an enemy nobleman on his way from {s3} to {s4}. He said the nobleman would leave {s3} in {reg1} days."
##  ),

# Bandit quests: Capture rich merchant, capture banker, kill manhunters?..

# Note : This is defined as the last village elder quest in module_constants.py:
 ("eliminate_bandits_infesting_village", "Bandits in {s7}", qf_random_quest,
  "A villager from {s7} begged you to save their village from the bandits that have taken up residence there."
  ),


 # Tutorial quest
## ("destroy_dummies", "Destroy Dummies", qf_show_progression,
##  "Trainer ordered you to destroy 10 dummies in the training camp."
##     ),

 # Join Kingdom quest
  ("join_faction", "Oath of Homage to {s1}", qf_random_quest,
  "Find {s1} and give him your oath of homage."
  ),

 # Rebel against Kingdom quest
 ("rebel_against_kingdom", "Support a Claimant to the Throne", qf_random_quest,
  "None"
  ),   

 #OiM quests list

 ("talk_to_zamoshie_elder", "Talk to the Zamoshye Elder", 0, "Clermont mentioned that the elder of Zamoshye would pay you well for your services. Perhaps you might pay him a visit."),
 ("zamoshie_lower_taxes", "Peasant Taxes", 0, "Convince the warlord of Smolensk to lower the taxes of the Zamoshye peasants."),
 ("deal_with_zamoshie_bandits", "Zamoshye Bandits", 0, "Kill the Zamoshye bandits."),
 ("oim_bring_goods_zamoshie", "Bring Goods to Zamoshye", 0, "Deliver Salt to Ataman Naum Vasiliev in Zamoshye."),
 ("oim_trakay_icon", "Elusive Priest", 0, "Elusive Priest"),

 ("oim_bring_tatarin_to_sich", "To the Sich with a Prisoner", 0, "To the Sich with a Prisoner"),
 ("oim_bring_tatarin_to_perekop", "To Perekop", 0, "To Perekop"),
 ("oim_sem_samuraev", "The Splendid Seven", 0, "The Splendid Seven"), 
 
 ("oim_lendliz", "Help the Don Cossacks", 0, "Help the Don Cossacks"),  
 ("oim_lendliz2", "Help the Don Cossacks", 0, "Help the Don Cossacks"),  
 
 ("oim_monfor_shved", "Recruit Clermont", 0, "Recruit Clermont"),  
 
 ("oim_monfor_shved_army", "Royal Cortege", 0, "Royal Cortege"),  
  
 ("mest_i_zakon", "Law and Vengeance", 0, "Law and Vengeance"),  
 ("mest_i_zakon2", "The Rescued Village", 0, "Law and Vengeance"),  
 ("mest_i_zakon3", "Hmelnitski's Revenge", 0, "Law and Vengeance"),  
  
 ("oim_kidalovo_z_konyem", "Half a Kingdom for a Horse", 0, "Half a Kingdom for a Horse"),  
 
 ("oim_invest", "Hidden Cache", 0, "Hidden Cache"),  
 
 ("oim_trubeckoy_rekomendation", "Recommendation to Trubetskoy", 0, "Recommendation to Trubetskoy"),  
 
 ("oim_tzr_korsar", "Corsair of the Tsar", 0, "Corsair of the Tsar"),  
 
 ("oim_potop_main", "The Deluge", 0, "The Deluge"),  
 
 ("oim_potop_find_zagloba", "Colonel Zagloba", 0, "Colonel Zagloba"),  
 
 ("oim_potop_deliver_letter", "Bad News for the King", 0, "Bad News for the King"),  
 
 ("oim_potop_deliver_swedish_solders", "Raid the Swedish Rears", 0, "Raid the Swedish Rears"),  

 ("oim_potop_deliver_swedish_troops_reward", "Receive the Reward", 0, "Receive the Reward"),  
 
 ("oim_potop_defend_church", "Polish Relic", 0, "Polish Relic"),  

 ("oim_potop_defend_get_back_warshaw", "Warsaw", 0, "Warsaw"),  
 
 ("oim_potop_capture_swedish_lord", "Error of Protestant Ways", 0, "Error of Protestant Ways"),  
 
 ("oim_potop_shtirlic", "The New Khan", 0, "{!}Do not translate"),  
 
 ("oim_potop_alias", "Tatar Ally", 0, "Tatar Ally"),   
 
 ("oim_potop_return", "Return of a Hero", 0, "Return of a Hero"),   
 
 ("oim_potop_kmitic", "Damn Khovansky!", 0, "Damn Khovansky!"),   

 ("oim_potop_volodievskiy", "Kidnapped Bride", 0, "Horse Thief"),   

 ("oim_potop_kshetuskiy", "Horse Thief", 0, "Kidnapped Bride"),   
  
 ("oim_potop_marshal", "Knapsack with Marshal's Baton", 0, "Knapsack with Marshal's Baton"),   
 
 ("oim_potop_marshal_started", "Marshal Elections", 0, "Marshal Elections"),   
 
 ("oim_potop_mission_impossible", "Liberator Hero", 0, "Liberator Hero"),   
 
 ("oim_potop_capture_tszar", "Hunt for the Tsar", 0, "Hunt for the Tsar"),   
 
 ("oim_potop_king_elections_kings_node", "Zagloba's Rebellion", 0, "Zagloba's Rebellion"),   
 
 ("oim_potop_king_elections_zagloba", "Unused", 0, "Unused"),  

 ("oim_potop_last_qst", "Death in Ascension", 0, "Death in Ascension"),  
 
 ("oim_potop_zagloba_revoult", "Emperor Zagloba!", 0, "Emperor Zagloba!"),  
 
 ("oim_potop_invasion_info", "German Regiments", 0, "German Regiments"),  
 
 ("oim_potop_destroy_mercs", "German Regiments", 0, "German Regiments"),  
 
 ("oim_potop_dismiss_king", "Anti-Tsar Coalition", 0, "Anti-Tsar Coalition"),  
 
 ("oim_potop_execute_king", "King's Abdication", 0, "King's Abdication"),  
 
 ("oim_potop_final_qst", "The Final Border", 0, "The Final Border"),  
 
 ##############################################################################
 ##black getman quests part
 ##############################################################################
 
 ("oim_getman_defend_villages", "Defend the Villages", 0, "Defend the Villages"),  
 
 ("oim_getman_main", "Secret of the Black Mace", 0, "Secret of the Black Mace"),  
 
 ("oim_getman_kozaks_service", "Errands", 0, "Errands"),  
  
 ("oim_getman_za_radzivilla", "For Great Lithuania!", 0, "For Great Lithuania!"),  

 ("oim_getman_radzivill_rebelion", "Radziwill Rebellion", 0, "Radziwill Rebellion"),   
 
 ("oim_getman_radzivill_capture_city", "First Order", 0, "First Order"), 

 ("oim_getman_kiev_capture", "Seizure of Kiev", 0, "Seizure of Kiev"),   
 
 ("oim_getman_kiev_burgomistr", "Kiev Mayor's Report", 0, "Kiev Mayor's Report"),   
 
 ("oim_getman_kiev_burgomistr_gold", "Kiev Legend", 0, "Kiev Legend"),   
  
 ("oim_getman_ask_add_info", "The Intractable Radziwill", 0, "The Intractable Radziwill"),   
 
 ("oim_getman_capture_tatarin", "Tatar Mirza", 0, "Tatar Mirza"),   
 
 ("oim_getman_tampliers_archives", "The Templar Archive", 0, "The Templar Archive"),   

 ("oim_getman_nesviz_grobnica_radzivilov", "The Family Crypt", 0, "The Family Crypt"),    
 
 ("oim_getman_nesviz_legend", "Nesvizh Legend", 0, "Nesvizh Legend"),    
 
 ("oim_getman_tayna_knyaza", "The Secret of House Oleg", 0, "The Secret of House Oleg"),    
 
 ("oim_getman_borat_dlg", "Prince Boryatinsky", 0, "{!}Do not translate"),    
 
 ("oim_getman_voron_book", "Book of the Crow", 0, "{!}Do not translate"),     
 
 ("oim_getman_voron_translate", "Pafnuty", 0, "{!}Do not translate"),     
 
 ("oim_getman_kozak_legend", "Cossack Legends", 0, "{!}Do not translate"),     
 
 ("oim_getman_barabash", "Hetman Barabash", 0, "{!}Do not translate"),     
 
 ("oim_getman_nesvizh_pernach", "Nesvizh", 0, "{!}Do not translate"),     
 
 ("oim_getman_kill_radzivill", "Hetman Radziwill", 0, "{!}Do not translate"),     
 
 ("oim_getman_za_barabasha", "For Barabash!", 0, "{!}Do not translate"),      
 
 ("oim_getman_caravan", "Cart with a Letter", 0, "{!}Do not translate"),      
 
 ("oim_getman_za_hmelya", "For Hmel!", 0, "{!}Do not translate"),      
 
 ("oim_na_rech_pospolitu", "To Poland!", 0, "{!}Do not translate"),      
 
 ("oim_getman_hmel_reb", "Rebellion", 0, "{!}Do not translate"),      
 
 ("oim_getman_hmel_casus_beli", "The military incident", 0, "{!}Do not translate"),      
 
 ("oim_getman_hmel_greate_war", "War on Two Fronts", 0, "{!}Do not translate"),      

 ("oim_getman_korona_vitovta", "Vytautas' Crown", 0, "{!}Do not translate"),      
  
 ("oim_getman_last_qst", "From Sea to Sea", 0, "{!}Do not translate"),      

 ##barabash code
 ("oim_na_msk_tsarzd", "To Muscovite Tsardom!", 0, "{!}Do not translate"),      

 ("oim_getman_barabash_reb", "Rebellion!", 0, "{!}Do not translate"),      

 ("oim_getman_barabash_casus_beli", "The military incident", 0, "{!}Do not translate"), 
 
 ("oim_getman_barabash_greate_war", "A War on Two Fronts", 0, "{!}Do not translate"),      
 
 ##############################################################################
 ###### oim dmitriy 
 ############################################################################## 
 
 ("oim_dmitriy_main", "Tsar Secrets...", 0, "{!}Do not translate"),     
 
 ("dmitriy_loot_villages", "Ravage the Villages", 0, "{!}Do not translate"),     

 ("oim_dmitriy_gerasim", "Gerasim Evangelic", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_elena", "Eleanor", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_eleonora", "Bring Eleanor to Carl", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_eleonora_home", "Bring Eleanor to the Prince", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_deliver_letter_msk", "A Letter to the Tsar", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_deliver_letter_shwed", "A Letter to the Tsar", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_talk_to_voevoda", "Talk to the Warlord", 0, "{!}Do not translate"),     
 
 ("oim_dmitriy_tsar_prison", "The Tsar's Mercies", 0, "{!}Do not translate"),      
 
 ("oim_dmitriy_razin", "Stepan Razin", 0, "{!}Do not translate"),      
  
 ("biyars_specnaz", "Talks with Boyars", 0, "{!}Do not translate"),      
 
 ("oim_alevtina_hanum", "Alevtina-hanum", 0, "{!}Do not translate"),      
 
 ("oim_black_lord", "False Dmitry the Third", 0, "False Dmitry the Third"),      
 #oim_dmitriy_elections
 ("oim_dmitriy_elections", "Elections of the Tsar", 0, "Elections of the Tsar"),      
 
 #oim special code
 #oim_duel_wound
 ("oim_duel_wound", "Wounded in a Duel", 0, "Wounded in a Duel"),      

 ("oim_alcoholic", "Alcoholism", 0, "Alcoholism"),      

 #illness 
 ("oim_illness_1", "Fever", 0, "Fever"),
 ("oim_illness_2", "Gout", 0, "Gout"),
 ("oim_illness_3", "Dropsy", 0, "Dropsy"),
 ("oim_illness_4", "Dysentery", 0, "Dysentery"),
 ("oim_illness_5", "Scabies", 0, "Scabies"),
 
 ("oim_potop_capture_city", "Capture the City", 0, "{!}Do not translate"),
 
 ("oim_deliver_caravan", "Deliver Caravan", 0, "{!}Do not translate"),
 
 ("oim_trade_pantent", "Trade patent", 0, "{!}Do not translate"),

 ("oim_hunt_down_thieves", "Hunt Down Thieves", 0, "{!}Do not translate"), 

 ("oim_get_feast_supplies", "Supplies for a Feast", 0, "{!}Do not translate"),

 ("oim_invest_2", "Return Money", 0, "{!}Do not translate"),
    
 ("quests_end", "Mission Accomplished", 0, "{!}Do not translate"),

]