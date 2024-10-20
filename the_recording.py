import os

class man_ply:
    def __init__(self,
                 ply_number,
                 ply_name,
                 ply_health,
                 ply_sanity,
                 ply_str,
                 ply_agl,
                 ply_observation,
                 ply_lore,
                 ply_influence,
                 ply_will):
        self.ply_number = ply_number
        self.ply_name = ply_name
        self.ply_health = ply_health
        self.ply_sanity = ply_sanity
        self.ply_str = ply_str
        self.ply_agl = ply_agl
        self.ply_observation = ply_observation
        self.ply_lore = ply_lore
        self.ply_influence = ply_influence
        self.ply_will = ply_will
        
class man_mon:
    def __init__(self,
                 m_type,
                 m_tag,
                 m_name,
                 m_hp,
                 m_blood,
                 m_aware,
                 m_horror,
                 m_diff,
                 m_pos):
        self.m_type = m_type
        self.m_tag = m_tag
        self.m_name = m_name
        self.m_hp = m_hp
        self.m_blood = m_blood
        self.m_aware = m_aware
        self.m_horror = m_horror
        self.m_diff = m_diff
        self.m_pos = m_pos

class man_mythos:
    def __init__(self, 
                 myth_tag, 
                 myth_diff, 
                 myth_title, 
                 myth_effect, 
                 myth_complete):
        self.myth_tag = myth_tag
        self.myth_diff = myth_diff
        self.myth_title = myth_title
        self.myth_effect = myth_effect
        self.myth_complete = myth_complete
    
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


#Global variables? In 2024? Getoutta here. Also running out of time. Fix after the game
#global mon_list
mon_list = []
#global mythos_list
mythos_list = []
#global tile_list
tile_list = []
#global active_monsters
active_monsters = []
#global all mplayers
ply_list = []
#global active players
active_players = []
#global interactions 
interact_token = []
#global search 
search_token = []

def globalLoader():
    print("in Global Loader")
    loadPly()
    loadMon()
    loadMyth()
    loadInteractions()
    loadSearch()
    loadTile()
    

def mainMenu():
    print("Welcome to the DM screen YA DORK")
    print("1) Display Monsters, Tiles, and all that Jazz")
    print("2) Manage Monsters")
    print("3) Manage Map")
    print("4) Manage Itmes")
    print("5) Manage Players")
    print("9) Load Data")
    print("0) Save and Exit")

    verC = int(input("Please select what you want?: "))

    if(verC == 1):
        clear = lambda: os.system('clear')
        clear()
        displayMenu()
    elif(verC == 2):
        clear = lambda: os.system('clear')
        clear()
        monsterManager()

    elif(verC == 3):
        clear = lambda: os.system('clear')
        clear()
        mapSelector()
        
    elif(verC == 4):
        print("TBD")
        mainMenu()

    elif (verC == 0):
        exit()  
    else:
        exit()

def displayMenu():
    verC = 0
    continue_menu = 0
    print("1: Check Monsters")
    print("2: Check Mythos List")
    print("3: Check Tiles List")
    print("0: Return to Main Menu")

    verC = int(input("Please select what you want?: "))
     
    if (verC == 1):
        showMon()
    elif(verC == 2):
        showMyth()
    elif(verC == 3):
        showTile()
    elif(verC == 0):
        mainMenu()

    continue_menu = int(input("1) Back to Display or 2) Return to Main Menu: "))
    if(continue_menu == 2):
        mainMenu()
    else:
        displayMenu()

def loadInteractions():
    for x in range(0,12):
         interact_token.append(man_interaction("Tag: " + str(x),
                               "Difficulty: " + str(x), 
                               "Sucesses: " + str(x),
                               "Effect: " + str(x),
                               "Complete: " + str(x)))   

def loadSearch():
    for x in range(0,16):
        search_token.append(man_search("Tag: " + str(x),
                               "Difficulty: " + str(x), 
                               "Item: " + str(x),
                               "Effect: " + str(x),
                               "Complete: " + str(x))) 
  
def loadPly():
    for x in range (0,30):
        ply_list.append(man_ply("Player Number: " + str(x),
                               "Character Name: " + str(x), 
                               "Health: " + str(x),
                               "Sanity: " + str(x),
                               "Strength: " + str(x),
                               "Agility: " + str(x),
                               "Observation: " + str(x),
                               "Lore: " + str(x),
                               "Influence: " + str(x),                               
                               "Will: " + str(x))) 
    
def loadMon():
    for x in range (0,5):
        mon_list.append(man_mon("Type: " + str(x),
                               "Tag: " + str(x), 
                               "Monster Name: " + str(x),
                               "Monster HP: " + str(x),
                               "Blood Token Value: " + str(x),
                               "Monster Awareness: " + str(x),
                               "Monster Horror: " + str(x),
                               "Monster Difficulty: " + str(x),
                               "Monster Position: " +str(x)))

def showMon():
    for i in range(0,len(mon_list)):
        print("               ")
        print("Monster Number: " + str(i+1))
        print(mon_list[i].m_type)
        print(mon_list[i].m_tag)
        print(mon_list[i].m_name)
        print(mon_list[i].m_hp)
        print(mon_list[i].m_blood)
        print(mon_list[i].m_aware)
        print(mon_list[i].m_horror)
        print(mon_list[i].m_diff)
        print(mon_list[i].m_pos)
        print("               ")

def loadMyth():
    for x in range (0,1):
        mythos_list.append(man_mythos("Tag: " + str(x), 
            "Mythos Difficulty: " + str(x),
            "Mythos Title: " + str(x),
            "Mythos Effect: " + str(x),
            "Mythos Complete: " + str(x)))

def showMyth():
    for i in range(0,len(mythos_list)):
        print("               ")
        print("Mythos Number: " + str(i+1))
        print(mythos_list[i].myth_tag)
        print(mythos_list[i].myth_diff)
        print(mythos_list[i].myth_title)
        print(mythos_list[i].myth_effect)
        print(mythos_list[i].myth_complete)
        print("               ")

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
                                  [mon_list[0],mon_list[1],mon_list[2]], #Are Monsters Present
                                  [ply_list[0], ply_list[1],ply_list[2]], #Are 1 Plyers Present?
                                  [x,x,x,x], #Tile to the North? #Tile to the South? #Tile to the East #Tile to the West
                                  [interact_token[0],interact_token[1]], #Are 1 Plyers Present?
                                  [search_token[0], search_token[2],search_token[3],search_token[4]], #Are 1 Plyers Present?
                               ))

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

def monsterManager():
    mon_list[0].m_name = "Monster Name: "+ str(9999999)
    mainMenu()
    
def mapSelector():
    optionSel = 0
    
    for x in range (0, len(tile_list)):
        print(f"{tile_list[x].tile_name}" + " " + f"{x+1}")
        
    tileSel = int(input("Which tile are we working with? (1-21): "))
    tileSel -= 1
    clear = lambda: os.system('clear')
    clear()
    mapManager(tileSel)   
        
def mapManager(tileSel):
    
    showTile(tileSel)
    print("1) Start/Increase Fire")
    print("2) Put Out Fire")
    print("3) Interactions")
    print("4) Explore")
    print("5) Pick a different Tile")
    print("0) Return to Main Menu")
    
    optionSel = int(input("Select: "))
    
    if (optionSel == 1):
        clear = lambda: os.system('clear')
        clear()
        tileFire(tileSel)
    elif(optionSel == 2):
        clear = lambda: os.system('clear')
        clear()
        putTileOut(tileSel)
    elif(optionSel == 3):
        exit()
    elif(optionSel == 4):
        exit()
    elif(optionSel == 5):
        clear = lambda: os.system('clear')
        clear()
        mapSelector()
    elif(optionSel == 0):
        mainMenu()
               
def tileFire(tileSel):
    if(tile_list[tileSel].tile_fire_tracker < tile_list[tileSel].tile_max_fire):
        tile_list[tileSel].tile_fire_tracker += 1
    
    if(tile_list[tileSel].tile_fire_tracker >= tile_list[tileSel].tile_max_fire):
        tile_list[tileSel].tile_on_fire = True
    
    mapManager(tileSel)

def putTileOut(tileSel):
    
    if(tile_list[tileSel].tile_fire_tracker == 0 and tile_list[tileSel].tile_on_fire == True):
        tile_list[tileSel].tile_on_fire = False
    else:
        tile_list[tileSel].tile_fire_tracker -= 1
     
    mapManager(tileSel)
def tileInteraction(x):
    print

    
    
    
    
   
  
          
   
    


    
    
  


            
               

            
                        


    

    
    
    
    
    
    

    

globalLoader()
mainMenu()
