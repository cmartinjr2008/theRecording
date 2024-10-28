import os
from random import randrange
from re import L
from turtle import clearscreen
import pandas as pd

turn = 0
sealOne = False
sealTwo = False
sealThee = False
mon_list = []
mythos_list = []
item_list = []
tile_list = []
active_monsters = []  
ply_list = []
active_players = []
interact_token = []
search_token = []

class man_ply:
    def __init__(self,
                 ply_number,
                 ply_invest_number,
                 ply_name,
                 ply_title,
                 ply_max_health,
                 ply_health,
                 ply_injured,
                 ply_max_sanity,
                 ply_sanity,
                 ply_insane,
                 ply_str,
                 ply_agl,
                 ply_observation,
                 ply_lore,
                 ply_influence,
                 ply_will,
                 ply_ability,
                 ply_items,
                 ply_pos)
                 ply_attack_melee, 
                 ply_attack_unarmed,
                 ply_attack_range
                 ply_spells:
        self.ply_number = ply_number
        self.ply_invest_number = ply_invest_number
        self.ply_name = ply_name
        self.ply_title = ply_title
        self.ply_max_health = ply_max_health
        self.ply_health = ply_health
        self.ply_injured = ply_injured
        self.ply_max_sanity = ply_max_sanity
        self.ply_sanity = ply_sanity
        self.ply_insane = ply_insane
        self.ply_str = ply_str
        self.ply_agl = ply_agl
        self.ply_observation = ply_observation
        self.ply_lore = ply_lore
        self.ply_influence = ply_influence
        self.ply_will = ply_will
        self.ply_ability = ply_ability
        self.ply_items = ply_items
        self.ply_pos = ply_pos
        self.ply_attack_melee = ply_attack_melee
        self.ply_attack_unarmed = ply_attack_unarmed
        self.ply_attack_range = ply_attack_range
        self.ply_spells = ply_spells)

    def loadPly():
        for x in range (0,30):
            ply_list.append(man_ply(x, #Player Number
                                    x, #Investigator Number
                                    str(x), #Character Name
                                    str(x), #Character Title
                                    x, #Max Health
                                    x, #Health
                                    False,#injured
                                    x, #Max Sanity
                                    x, #Sanity
                                    False, #Insane
                                    x, #Strength
                                    x, #Agility
                                    x, #Observation
                                    x, #Lore
                                    x, #Influence                               
                                    x, #Will
                                    x, #Ability
                                    [], #Items
                                    x,#Tile Position
                                    [], #melee
                                    [], #unarmed
                                    [], #ranged
                                    [])) #Spells

    def plyMenu():
        optionSel = 0
        plySel = 0
        if(len(active_players) != 0):
            print("Active Players")
            print("_______________")
            for x in range (0, len(active_players)):
                print(f"Player " + str(x+1))
                print(f"Investigator: {active_players[x].ply_name}")
                print("_______________")
                print("\n")
        else:
            print("Please Setup Players!")
        print("1) Manage Players")
        print("2) Setup Players")
        print("3) Return to Main Menu")
        print("__________________\n")
        optionSel = int(input("What are you looking to do?: "))
        if(optionSel == 1):
            plySel = int(input("Which Player?: "))
            plySel -= 1
            clearScreen()
            man_mon.plyManager()
    
        elif(optionSel == 2):
            man_ply.plySetup()

        elif(optionSel == 3):
            clearScreen()
            mainMenu()

    def plySetup():
        numOfPlayers = 0
        numOfPlayers = int(input("How Many Players? (1-4): "))
        clearScreen()
        man_ply.investDisplay()
        man_ply.selectInvestigator(numOfPlayers)

    def investDisplay():
        for i in range (0, len(ply_list)):
            print("---------------------------")
            print(f"Investigator Number: {ply_list[i].ply_invest_number}")
            print(f"Investigator Name: {ply_list[i].ply_name}")
            print("---------------------------")

    def selectInvestigator(numOfPlayers):
        investSelect = 0
        for i in range (0,numOfPlayers):
            investSelect = int(input(f"Player " + str((i+1)) + " select your Investigator: "))
            print(investSelect)
            active_players.append(ply_list[investSelect])
        clearScreen()
        man_ply.plyMenu()

    def plyManager(plySel):
        optionSel = 0
        print("Player Manager")
        print("---------------")
        man_ply.showPly() 
        print("1) Move Player")
        print("2) Attack/Spell Check")
        print("3) Health & Sanity Check")
        print("4) Stats Check")
        print("5) Manage Items")
        print("9) Return to Player Menu")
        print("0) Return to Main Menu")
        print("__________________\n")

        optionSel = int(input("What are you looking to do?: "))   
    
        if(optionSel == 1):
            active_players[plySel].m_tile = man_ply.plyMove(plySel)
        elif(optionSel == 2):
            clearScreen()
            man_ply.plyAttacks(plySel)
        elif(optionSel == 3):
            clearScreen()
            man_ply.plyHealthAndSan(plySel)
        elif(optionSel == 4):
            clearScreen()
            man_ply.plyStats(plySel)
        elif(optionSel == 5):
            print("TBD")
            plyManager(plySel)
        elif(optionSel == 9):
            clearScreen()
            man_ply.plyMenu()
            
        elif(optionSel == 0):
            clearScreen()
            mainMenu()

    def plyMove(plySel):
        man_tile.showFullMap()
        currentTile = active_players[plySel].m_tile
        tileSelection = 0
        print("__________________\n")
        tileSelection = int(input("What room are you moving to?: "))
        print(currentTile)

        tile_list[tileSelection].tile_players.append(active_players[0])

        for i in reversed(range(tile_list.tile_players + 1)):
            if(tile_list[active_players[plySel].mon_pos].tile_players[i].mon_tag == active_monsters[plySel].mon_tag):
                del tile_list[active_players[plySel].mon_pos].tile_players[i]

        return man_ply.plyManager(plySel)

    def plyAttack(plySel):
        plyChoice = 0
        print("1) Melee Attack")
        print("2) Unarmed Attack")
        print("3) Range Attack")
        print("4) Spell Attack")
        print("0) Return to Player Menu")
        plyChoice = int(input("Please Select an attack: "))
        
        if(plyChoice == 1):
           
    def plyHealthAndSan(plySel):
        plyChoice = 0
        print("---------------------------")
        print(f"Player {ply_list[plySel].ply_invest_number}")
        print(f"Investigator Name: {ply_list[plySel].ply_name}")
        print(f"Investigator Health: {ply_list[plySel].ply_health}")
        if(active_players[plySel].ply_injured == True):
            print("!!!!!!INJURED!!!!!!")
        print(f"Investigator Sanity: {ply_list[plySel].ply_sanity}")
        if(active_players[plySel].ply_insane == True):
            print("!!!!!!!INSANE!!!!!!")
        print("---------------------------")
        print("1) Increase Health")
        print("2) Decrease Health")
        print("3) Increase Sanity")
        print("4) Decrease Sanity")
        print("0) Return to Player Menu")

        plyChoice = int(input("Please enter your choice: "))

        if(plyChoice == 1):
            if(active_players[plySel].ply_health >= active_players[plySel].ply_max_health):
                print("Already At Max Health!")
                plyChoice = int(input("Please another choice: "))
            else:
                active_players[plySel].ply_health += 1
                clearScreen()
                man_ply.plyHealthAndSan(plySel)

        if(plyChoice == 2):
            if(active_players[plySel].ply_health == 0 and active_players[plySel].ply_injured == False):
                print("Player is Injured!!")
                active_players[plySel].ply_injured = True
                active_players[plySel].ply_health = active_players[plySel].ply_max_health

            if(active_players[plySel].ply_health == 0 and active_players[plySel].ply_injured == True):
                print("!!Game Over!!")

        if(plyChoice == 3):
            if(active_players[plySel].ply_sanity >= active_players[plySel].ply_max_sanity):
                print("Already At Max Sanity!")
                plyChoice = int(input("Please another choice: "))
            else:
                active_players[plySel].ply_sanity += 1
                clearScreen()
                man_ply.plyHealthAndSan(plySel)
        
        if(plyChoice == 4):
            if(active_players[plySel].ply_sanity == 0 and active_players[plySel].ply_insane == False):
                print("Player is Injured!!")
                active_players[plySel].ply_insane = True
                active_players[plySel].ply_sanity = active_players[plySel].ply_max_sanity

            if(active_players[plySel].ply_sanity == 0 and active_players[plySel].ply_insane == True):
                print("!!Game Over!!")

        if(plyChoice == 0):
            clearScreen()
            man_ply.plyManager(plySel)

    def plyStats(plySel):
        plyChoice = 0
        abilityChoice = 0
        print("---------------------------")
        print(f"Player {ply_list[plySel].ply_invest_number}")
        print(f"Investigator Name: {ply_list[plySel].ply_name}")
        print(f"Investigator Strength: {ply_list[plySel].ply_health}")
        print(f"Investigator Agility: {ply_list[plySel].ply_sanity}")
        print(f"Investigator Observation: {ply_list[plySel].ply_sanity}")
        print(f"Investigator Lore: {ply_list[plySel].ply_sanity}")
        print(f"Investigator Influence: {ply_list[plySel].ply_sanity}")
        print(f"Investigator Will: {ply_list[plySel].ply_sanity}")
        print("---------------------------")

        print("1) Increase a Stat")
        print("2) Decrease a Stat")
        print("0) Return to Player Menu")
        plyChoice = int(input("Please enter your choice: "))

        if(plyChoice == 1):
            clearScreen()
            print("1) Strength")
            print("2) Agility")
            print("3) Observation")
            print("4) Lore")
            print("5) Influence")
            print("6) Will")     
            print("0) Cancel")
            abilityChoice = int(input("Please Select an Abiliy to Increase: "))
            
            if(abilityChoice == 1):
                active_players[plysel].ply_str += 1
            elif(abilityChoice == 2):
                active_players[plysel].ply_agl += 1
            elif(abilityChoice == 3):
                active_players[plysel].ply_observation += 1
            elif(abilityChoice == 4):
                active_players[plysel].ply_lore += 1
            elif(abilityChoice == 5):
                active_players[plysel].ply_influence += 1               
            elif(abilityChoice == 6):
                active_players[plysel].ply_agl += 1
            elif(abilityChoice == 0):
                clearscreen
                man_ply.plyStats(plySel)

        if(plyChoice == 2):
            clearScreen()
            print("1) Strength")
            print("1) Agility")
            print("1) Observation")
            print("1) Lore")
            print("1) Influence")
            print("1) Will")
            print("0) Cancel")
            abilityChoice = int(input("Please Select an Abiliy to Decrease: "))
            
            if(abilityChoice == 1):
                active_players[plysel].ply_str -= 1
            elif(abilityChoice == 2):
                active_players[plysel].ply_agl -= 1
            elif(abilityChoice == 3):
                active_players[plysel].ply_observation -= 1
            elif(abilityChoice == 4):
                active_players[plysel].ply_lore -= 1
            elif(abilityChoice == 5):
                active_players[plysel].ply_influence -= 1               
            elif(abilityChoice == 6):
                active_players[plysel].ply_agl -= 1
            elif(abilityChoice == 0):
                clearscreen
                man_ply.plyStats(plySel)
           
        if(plyChoice == 0):
            clearScreen()
            man_ply.plyManager(plySel)

    def plyItems(plySel):
        print("TBD")
        man_ply.plyManager(plySel)
        
    def plyAttacks(plySel):
        attackChoice = 0
        print("1) Melee Attack")
        print("2) Unarmed Attack")
        print("3) Ranged Attack")
        print("4) Spell Attack")
        print("0) Return to Player Menu")
        attackChoice = int(input("Please an Attack Type: "))
        
        if(attackChoice == 1):
            man_ply.plyMelee(plySel)
        elif(attackChoice == 2):
            man_ply.plyUnarmed(plySel)
        elif(attackChoice == 3):
            man_ply.plyRanged(plySel)
        elif(attackChoice == 4):
            man_ply.plySpell(plySel)
        elif(attackChoice == 0):
            clearscreen()
            man_ply.plyManager(plySel)

    def plyMelee(plySel):
        sucessChoice = 0
        attackNum = 0
        monSel = 0
        monsterDmg = 0
        
        attackNum = randrange(0,len(active_players[plysel].ply_attack_melee))
        print(active_players[plysel].ply_attack_melee[attackNum])
        print("\n")
        

        print("Did the attack land?: ")
        print("\n")
        sucessChoice = int(input("1) Yes    2)No  :  "))
        
        if(sucessChoice = 1):
            print("Active Monsters")
            print("_______________")
                for x in range (0, len(active_monsters)):
                    print(f"{active_monsters[x].m_name}" + " " + f"{x+1}")
            print("_______________")
            monSel = int(input("Targeting which monster?: "))
            print("_______________")
                monsterDmg = int(input("How much damage is monster taking?: " ))
                active_monsters[monSel].m_hp -= monsterDmg
                man_mon.monHealthCheck(monSel)
            clearscreen()
            man_ply.plyAttacks(plySel)
        elif(sucessChoice = 2):
            clearscreen()
            man_ply.plyAttacks(plySel)            
              
    def plyUnarmed(plySel):
        sucessChoice = 0
        attackNum = 0
        monSel = 0
        monsterDmg = 0
        
        attackNum = randrange(0,len(active_players[plysel].ply_attack_unarmed))
        print(active_players[plysel].ply_attack_unarmed[attackNum])
        print("\n")
        

        print("Did the attack land?: ")
        print("\n")
        sucessChoice = int(input("1) Yes    2)No  :  "))
        
        if(sucessChoice = 1):
            print("Active Monsters")
            print("_______________")
                for x in range (0, len(active_monsters)):
                    print(f"{active_monsters[x].m_name}" + " " + f"{x+1}")
            print("_______________")
            monSel = int(input("Targeting which monster?: "))
            print("_______________")
                monsterDmg = int(input("How much damage is monster taking?: " ))
                active_monsters[monSel].m_hp -= monsterDmg
                man_mon.monHealthCheck(monSel)
            clearscreen()
            man_ply.plyAttacks(plySel)
        elif(sucessChoice = 2):
            clearscreen()
            man_ply.plyAttacks(plySel)            

    def plyRanged(plySel):
        sucessChoice = 0
        attackNum = 0
        monSel = 0
        monsterDmg = 0
        
        attackNum = randrange(0,len(active_players[plysel].ply_attack_range))
        print(active_players[plysel].ply_attack_range[attackNum])
        print("\n")
        

        print("Did the attack land?: ")
        print("\n")
        sucessChoice = int(input("1) Yes    2)No  :  "))
        
        if(sucessChoice = 1):
            print("Active Monsters")
            print("_______________")
                for x in range (0, len(active_monsters)):
                    print(f"{active_monsters[x].m_name}" + " " + f"{x+1}")
            print("_______________")
            monSel = int(input("Targeting which monster?: "))
            print("_______________")
                monsterDmg = int(input("How much damage is monster taking?: " ))
                active_monsters[monSel].m_hp -= monsterDmg
                man_mon.monHealthCheck(monSel)
            clearscreen()
            man_ply.plyAttacks(plySel)
        elif(sucessChoice = 2):
            clearscreen()
            man_ply.plyAttacks(plySel)
            
    def plySpell(plySel):
        sucessChoice = 0
        attackNum = 0
        monSel = 0
        monsterDmg = 0
        
        attackNum = randrange(0,len(active_players[plysel].ply_spells))
        print(active_players[plysel].ply_spells[attackNum])
        print("\n")
        

        print("Did the attack land?: ")
        print("\n")
        sucessChoice = int(input("1) Yes    2)No  :  "))
        
        if(sucessChoice = 1):
            print("Active Monsters")
            print("_______________")
                for x in range (0, len(active_monsters)):
                    print(f"{active_monsters[x].m_name}" + " " + f"{x+1}")
            print("_______________")
            monSel = int(input("Targeting which monster?: "))
            print("_______________")
                monsterDmg = int(input("How much damage is monster taking?: " ))
                active_monsters[monSel].m_hp -= monsterDmg
                man_mon.monHealthCheck(monSel)
            clearscreen()
            man_ply.plyAttacks(plySel)
        elif(sucessChoice = 2):
            clearscreen()
            man_ply.plyAttacks(plySel)


class man_mon:
    
    def __init__(self,
                 m_tag, #tag == monster number (1 - whatever)
                 m_name,
                 m_hp,
                 m_blood,
                 m_aware,
                 m_horror,
                 m_diff,
                 m_fight_check,
                 m_horror_check,
                 m_sneak_check,
                 m_tile,
                 m_pos):
        self.m_tag = m_tag
        self.m_name = m_name
        self.m_hp = m_hp
        self.m_blood = m_blood
        self.m_aware = m_aware
        self.m_horror = m_horror
        self.m_diff = m_diff
        self.m_fight_check = m_fight_check
        self.m_horror_check = m_horror_check
        self.m_sneak_check = m_sneak_check
        self.m_tile = m_tile
        self.m_pos = m_pos
        
    def loadMon():
        for x in range (0,5):
            mon_list.append(man_mon(str(x),#Monster Tag
                                   str(x),#monster Name
                                   x,#Monster HP
                                   x,#Monster BTV
                                   x,#Monster Awareness
                                   x,#Monster Horror
                                   x,#Monster Difficulty
                                   ["Attack Check 1","Attack Check 2","Attack Check 3","Attack Check 4"],#Monster Fight Checks
                                   ["Horror Check 1","Horror Check 2","Horror Check 3"],#Monster Horror Checks
                                   ["Sneak Check 1","Sneak Check 2"],#Monster Sneak Checks
                                   x,#Monster Tile Location
                                   x)) #Active Monster Location
    
    def loadattacks():
        print()
    def loadHorror():
        print()

    def showMon(x):
     print("               ")
     print(f"Monster Number: {x+1}")
     print(f"Monster Name: {active_monsters[x].m_name}")
     print(f"Monster Difficulty: {active_monsters[x].m_diff}")
     print(f"Blood Token Value?: {active_monsters[x].m_blood}")
     print(f"HP: {active_monsters[x].m_hp}")
     print(f"Awareness?: {active_monsters[x].m_aware}")
     print(f"Horror: {active_monsters[x].m_horror}")
     print(f"Monster Location: {active_monsters[x].m_tile}")
     print("               ")

    def monMenu():
        optionSel = 0
        monsterSel = 0
        print("Active Monsters")
        print("_______________")
        for x in range (0, len(active_monsters)):
            print(f"{active_monsters[x].m_name}" + " " + f"{x+1}")
        print("_______________")

        print("1) Manage Monsters")
        print("2) Spawn Monster")
        print("3) Return to Main Menu")
        print("__________________\n")


        optionSel = int(input("What are you looking to do?: "))

        if(optionSel == 1):
            monsterSel = int(input("Which Monster?: "))
            monsterSel -= 1
            clearScreen()
            man_mon.monsterManager(monsterSel)
    
        elif(optionSel == 2):
            man_mon.monsterSpawnMenu()

        elif(optionSel == 3):
            clearScreen()
            mainMenu()

    def monsterManager(monSel):
        optionSel = 0
        print("Monster Manager")
        print("---------------")
        man_mon.showMon(monSel) 
        print("1) Move Monster")
        print("2) Attack Check")
        print("3) Horror Check")
        print("4) Sneak Check")
        print("9) Return to Monster Menu")
        print("0) Return to Main Menu")
        print("__________________\n")

        optionSel = int(input("What are you looking to do?: "))   
    
        if(optionSel == 1):
            active_monsters[monSel].m_tile = man_mon.monMove(monSel)
        elif(optionSel == 2):
            clearScreen()
            man_mon.monAttack(monSel)
        elif(optionSel == 3):
            clearScreen()
            man_mon.monHorror(monSel)
        elif(optionSel == 4):
            clearScreen()
            man_mon.monSneak(monSel)
        elif(optionSel == 0):
            clearScreen()
            mainMenu()

    def monMove(monSel):
        man_tile.showFullMap()
        currentTile = active_monsters[monSel].m_tile
        tileSelection = 0
        print("__________________\n")
        tileSelection = int(input("What room are you moving to?: "))
        print(currentTile)

        #Remove monster from its current position
        tile_list[tileSelection].tile_monsters.append(active_monsters[0])

        for i in reversed(range(tile_list.tile_monsters + 1)):
            if(tile_list[active_monsters[monSel].mon_pos].tile_monsters[i].mon_tag == active_monsters[monSel].mon_tag):
                del tile_list[active_monsters[monSel].mon_pos].tile_monsters[i]

        return man_mon.monsterManager(monSel)

    def monAttack(monSel):
        attackNum = randrange(0,len(active_monsters[monSel].m_fight_check))
        print(attackNum)
        print(active_monsters[monSel].m_fight_check[attackNum])
        input("Press Any Key to Continue")
        clearScreen()
        man_mon.monsterManager(monSel)

    def monHorror(monSel):
        horrorNum = randrange(0,len(active_monsters[monSel].m_horror_check))
        print(horrorNum)
        print(active_monsters[monSel].m_horror_check[horrorNum])
        input("Press Enter Key to Continue")
        clearScreen()
        man_mon.monsterManager(monSel)

    def monSneak(monSel):
        sneakNum = randrange(0,len(active_monsters[monSel].m_sneak_check))
        print(sneakNum)
        print(active_monsters[monSel].m_sneak_check[sneakNum])
        input("Press Any Key to Continue")
        clearScreen()
        man_mon.monsterManager(monSel)

    def monDamage(monSel):

    def monsterSpawnMenu():
        optionSel = 0 
        print("1) Spawn Normal Monster")
        print("2) Spawn Special Monster")
    
        optionSel = int(input("Please Select: "))
        if(optionSel == 1):
            clearScreen()
            man_mon.spawnNormal()
        elif(optionSel == 2):
            clearScreen()
            man_mon.spawnSpecial()

    def spawnNormal():
        monsterNumber = randrange(0,len(mon_list))
        monsterLocation = randrange(0,20)

        print(len(active_monsters))

        active_monsters.append(mon_list[monsterNumber])
        active_monsters[len(active_monsters) - 1].m_tile = monsterLocation
        print(monsterLocation)
        tile_list[monsterLocation].tile_monsters.append(active_monsters[0])

        clearScreen()
        man_mon.monMenu()

    def spawnSpecial():
        monsterNumber = randrange(0,len(mon_list))
        monsterLocation = randrange(0,20)

        print(len(active_monsters))

        active_monsters.append(mon_list[monsterNumber])
        active_monsters[len(active_monsters) - 1].m_tile = monsterLocation
        print(monsterLocation)
        tile_list[monsterLocation].tile_monsters.append(active_monsters[0])

        clearScreen()
        man_mon.monMenu()
       
    def monHealthCheck(monsterSelect):
        if(active_monsters[monSel].m_hp <= 0):
            print("Monster is dead! Collect those Blood Tokens!")
            del (active_monsters[monSel])
        clearscreen()
        man_ply.plyAttacks(monsterSelect)
        

class man_item:
    def __init__(self, i_number,
                       i_type,
                       i_desc):
        self.i_number = i_number
        self.i_type = i_type
        self.i_desc = i_desc

class man_mythos:
    def __init__(self, 
                 myth_tag, 
                 myth_effect):
        self.myth_tag = myth_tag
        self.myth_effect = myth_effect
        
    def loadMyth():
        for x in range (0,30):
            mythos_list.append(man_mythos(str(x),
                                          str(x)))
            
    def showMyth():
        for i in range(0,len(mythos_list)):
            print("               ")
            print("Mythos Number: " + str(i+1))
            print(mythos_list[i].myth_tag)
            print(mythos_list[i].myth_effect)
            print("               ")
            
    def readMythos():
        mythSelect = 0
        mythSelect = randrange(0,len(mythos_list))
        print(mythos_list[mythSelect].myth_effect)
        del(mythos_list[mythSelect])
                
class man_tile:
    def __init__(self, 
                 tile_name, 
                 tile_priority, 
                 tile_reveal, 
                 tile_lost, 
                 tile_on_fire,
                 tile_max_fire, 
                 tile_fire_tracker,
                 tile_dark, 
                 tile_monsters,
                 tile_players,
                 tile_position,
                 tile_interaction,
                 tile_search):
           
           self.tile_name = tile_name
           self.tile_priority = tile_priority
           self.tile_reveal = tile_reveal
           self.tile_lost = tile_lost
           self.tile_on_fire = tile_on_fire
           self.tile_max_fire = tile_max_fire
           self.tile_fire_tracker = tile_fire_tracker
           self.tile_dark = tile_dark           
           self.tile_monsters = tile_monsters
           self.tile_players = tile_players
           self.tile_position = tile_position
           self.tile_interaction = tile_interaction
           self.tile_search = tile_search

    def mapMenu():
        optionSel = 0
        man_tile.showFullMap()
        tileSel = int(input("Which tile are we working with? (1-21): "))
        tileSel -= 1
        clearScreen()
        man_tile.mapManager(tileSel)  

    def loadTile():
        for x in range (0,21):
            tile_list.append(man_tile(
                                      str(x),#Tile Name
                                      str(x), #Tile Priority 
                                      False, #Is Tile Revealed
                                      False, #Is Tile Lost in Time and Space
                                      False, #Is Tile on Fire?
                                      x,#Max Fire Allowed
                                      0,#Current Fire Tokens
                                      False, #Is the Tile Dark?                                 
                                      [], #Are Monsters Present
                                      [], #Are Plyers Present?
                                      [x,x,x,x], #Tile to the North? #Tile to the South? #Tile to the East #Tile to the West
                                      [], #Are Interactions Present?
                                      [], #Are Search Tokens Present?
                                       ))

    def showFullMap():
        for x in range (0, len(tile_list)):
            print(f"{tile_list[x].tile_name}" + " " + f"{x+1}")

    def mapManager(tileSel):
        man_tile.showTile(tileSel)
        print("1) Start/Increase Fire")
        print("2) Put Out Fire")
        print("3) Interactions")
        print("4) Explore")
        print("5) Pick a different Tile")
        print("0) Return to Main Menu")
    
        optionSel = int(input("Select: "))
    
        if (optionSel == 1):
            clearScreen()
            man_tile.tileFire(tileSel)
        elif(optionSel == 2):
            clearScreen()
            man_tile.putTileOut(tileSel)
        elif(optionSel == 3):
            exit()
        elif(optionSel == 4):
            exit()
        elif(optionSel == 5):
            clearScreen()
            man_tile.mapMenu()
        elif(optionSel == 0):
            clearScreen()
            mainMenu()

    def tileFire(tileSel):
        if(tile_list[tileSel].tile_fire_tracker < tile_list[tileSel].tile_max_fire):
            tile_list[tileSel].tile_fire_tracker += 1
    
        if(tile_list[tileSel].tile_fire_tracker >= tile_list[tileSel].tile_max_fire):
            tile_list[tileSel].tile_on_fire = True
        
        man_tile.mapManager(tileSel)

    def putTileOut(tileSel):
    
        if(tile_list[tileSel].tile_fire_tracker == 0 and tile_list[tileSel].tile_on_fire == True):
            tile_list[tileSel].tile_on_fire = False
        else:
            tile_list[tileSel].tile_fire_tracker -= 1
     
        man_tile.mapManager(tileSel)

    def tileInteraction(tileSel):
        print

    def showTile(x):
     print("               ")
     print(f"Tile Number: {x+1}")
     print(f"Tile Name: {tile_list[x].tile_name}")
     print(f"Tile Priority: {tile_list[x].tile_priority}")
     print(f"Revealed?: {tile_list[x].tile_reveal}")
     print(f"Lost in Time and Space?: {tile_list[x].tile_lost}")
     print(f"On Fire?: {tile_list[x].tile_on_fire}")
     print(f"Fire Tracker: {tile_list[x].tile_fire_tracker}")
     print(f"Maximum Fire: {tile_list[x].tile_max_fire}")
     print(f"Dark?: {tile_list[x].tile_dark}")
 
     if (tile_list[x].tile_monsters != None):
        for i in range(len(tile_list[x].tile_monsters)):
            print(f"Monster!: {tile_list[x].tile_monsters[i].m_name}")
    
     for i in range(len(tile_list[x].tile_players)):
        print(f"Player!: {tile_list[x].tile_players[i].ply_name}")
   
     for i in range(len(tile_list[x].tile_position)):
         if(i == 0 and tile_list[x].tile_position[i] != None):
             print(f"North: {tile_list[x].tile_position[i]}")
         
         elif(i == 1 and tile_list[x].tile_position[i] != None):
             print(f"South: {tile_list[x].tile_position[i]}")
         
         elif(i == 2 and tile_list[x].tile_position[i] != None):
             print(f"East: {tile_list[x].tile_position[i]}")
         
         elif(i == 3 and tile_list[x].tile_position[i] != None):
             print(f"West: {tile_list[x].tile_position[i]}")
         
     for i in range(len(tile_list[x].tile_interaction)):
        print(f"!: {tile_list[x].tile_interaction[i].inter_tag}")
 
     for i in range(len(tile_list[x].tile_search)):
        print(f"?: {tile_list[x].tile_search[i].search_tag}")
     print("               ")
     
    def tileLostInTime():
        global lostCheck
        for i in range (0, len(tile_list)):
                if (tile_list[i].tile_lost == True):
                    tile_list[i].tile_lost = False
                    print(f"{tile_list[lostCheck].tile_name} is no longer lost in time and space")

        
        lostCheck = randrange(0,len(tile_list))
        print(f"{tile_list[lostCheck].tile_name} is now lost in time and space")
        tile_list[lostCheck].tile_lost = True
        
        if(sealOne == True):
            lostCheck = 0
            lostCheck = randrange(0,len(tile_list))
            print(f"{tile_list[lostCheck].tile_name} is now lost in time and space")
            tile_list[lostCheck].tile_lost = True

        if(sealTwo == True):
            lostCheck = 0
            lostCheck = randrange(0,len(tile_list))
            print(f"{tile_list[lostCheck].tile_name} is now lost in time and space")
            tile_list[lostCheck].tile_lost = True
            
    def tileFireManage():
        for i in range(0,len(tile_list)):
            if (tile_list[i].tile_on_fire == True):
                tile_list[i].tile_fire_tracker += 1
                if(tile_list[i].tile_fire_tracker >= tile_list[i].tile_max_fire):
                    for x in range(0,3):
                        direction = 0 
                        if(tile_list[i].tile_position[x] != 0):
                            direction = tile_list[i].tile_position[x]
                        
                        if(tile_list[direction].tile_on_fire != True):
                            print(f"{tile_list[direction].tile_on_fire} is now on fire!")
                            tile_list[direction].tile_on_fire = True
                              
class man_interaction:
    def __init__(self, 
                 inter_tag,
                 inter_diff,
                 inter_successes,
                 inter_effect,
                 inter_complete):
        self.inter_tag = inter_tag
        self.inter_diff = inter_diff
        self.inter_sucesses = inter_successes
        self.inter_effect = inter_effect
        self.inter_complete = inter_complete

    def loadInteractions():
        for x in range(0,12):
             interact_token.append(man_interaction("Tag: " + str(x),
                                   "Difficulty: " + str(x), 
                                   "Sucesses: " + str(x),
                                   "Effect: " + str(x),
                                   "Complete: " + str(x)))
             
class man_search:
    def __init__(self,
                 search_tag, 
                 search_diff,
                 search_item,
                 search_effect,
                 search_complete):
        self.search_tag = search_tag
        self.search_diff = search_diff
        self.search_item = search_item
        self.search_effect = search_effect
        self.search_compelte = search_complete

    def loadSearch():
        for x in range(0,16):
            search_token.append(man_search("Tag: " + str(x),
                                   "Difficulty: " + str(x), 
                                   "Item: " + str(x),
                                   "Effect: " + str(x),
                                   "Complete: " + str(x)))

def globalLoader():
    man_ply.loadPly()
    man_mon.loadMon()
    man_mythos.loadMyth()
    man_interaction.loadInteractions()
    man_search.loadSearch()
    man_tile.loadTile()

def mainMenu():
    turndisplay()
    print("1) Manage Monsters")
    print("2) Manage Players")
    print("3) Manage Map")
    print("4) Manage Items")
    print("5) Manage Mythos")
    print("6) End a Turn")
    print("9) Load Data")
    print("0) Save and Exit")

    verC = int(input("Please select what you want?: "))

    if(verC == 1):
        clearScreen()
        man_mon.monMenu()
    elif(verC == 2):
        clearScreen()
        man_ply.plyMenu()
    elif(verC == 3):
        clearScreen()
        man_tile.mapMenu()
    elif(verC == 6):
        clearScreen()
        endTurn()
    elif(verC == 4):
        print("TBD")
        mainMenu()

    elif (verC == 0):
        clearScreen()
        exit()  

    else:
        clearScreen()    
        exit() 

def clearScreen():
    clear = lambda: os.system('clear')
    clear()
 
def turndisplay():
    print("*****************************")
    print(f"It is turn {turn}")
    print("*****************************")
    
def endTurn():
    global turn
    endCon = " "
    sealCheck()
    man_tile.tileLostInTime()
    
    endCom = input("")
    clearScreen()
    man_tile.tileFireManage()
    
    endCom = input("")
    clearScreen()
    man_mythos.readMythos()
    
    endCom = input("")
    
    turn += 1
    clearScreen()
    mainMenu()
    
def sealCheck():
    global sealOne
    global sealTwo
    global sealThee
    dmChoice = 0    
     
    if(sealOne == False and sealTwo == False and sealThee == False):
        dmChoice = 0
        print("Has the First Seal been broken?")
        dmChoice = int(input("1) Yes    2)  No : "))
        if(dmChoice == 1):
            sealOne = True
        dmChoice = 0
        clearScreen()

    if (sealOne == True and sealTwo == False and sealThee == False):
        dmChoice = 0
        print("Has the Second Seal been broken?")
        dmChoice = int(input("1) Yes    2)  No : "))
        
        if(dmChoice == 1):
            sealTwo = True
            
        clearScreen()

    if (sealOne == True and sealTwo == True and sealThee == False):
        print("Has the Third Seal been broken?")
        dmChoice = int(input("1) Yes    2)  No : "))
        
        if(dmChoice == 1):
            sealThee = True
            print("!!!!!!!GAME OVER!!!!!!!!!")
            exit()
            
globalLoader()
clearScreen()
mainMenu()
