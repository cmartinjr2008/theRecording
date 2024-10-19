import os

class man_mon:
    def __init__(self,m_type,m_tag,m_name,m_hp,m_blood,m_aware,m_horror,m_diff,m_pos):
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
    def __init__(self, myth_tag, myth_diff, myth_title, myth_effect, myth_complete):
        self.myth_tag = myth_tag
        self.myth_diff = myth_diff
        self.myth_title = myth_title
        self.myth_effect = myth_effect
        self.myth_complete = myth_complete

class man_tile:
    def __init__(self, tile_name, tile_priority, tile_visual, tile_reveal, tile_lost, tile_on_fire, tile_max_fire, tile_fire_tracker, tile_dark, tile_adjecent):
           self.tile_name = tile_name
           self.tile_priority = tile_priority
           self.tile_visual = tile_visual
           self.tile_reveal = tile_reveal
           self.tile_lost = tile_lost
           self.tile_on_fire = tile_on_fire
           self.tile_max_fire = tile_max_fire
           self.tile_fire_tracker = tile_fire_tracker
           self.tile_dark = tile_dark
           self.tile_adjecent = tile_adjecent
#Global variables? In 2024? Getoutta here. Also running out of time. Fix after the game
#global mon_list
mon_list = []
#global mythos_list
mythos_list = []
#global tile_list
tile_list = []
#global active_monsters
active_monsters = []

def globalLoader():
    print("in Global Loader")
    loadMon()
    loadMyth()
    loadTile()

def mainMenu():
    print("Welcome to the DM screen YA DORK")
    print("1) Display Monsters, Tiles, and all that Jazz")
    print("2) Manage Monsters")
    print("3) Manage Tiles")
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
        print("TBD")
        mainMenu()
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
    
def loadMon():
    for x in range (0,1):
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
    for x in range (0,1):
        tile_list.append(man_tile("Tile Name: " + str(x),
                               "Tile Priority: " + str(x), 
                               "Tile Vis: " + str(x),
                               "Tile Revealed?:" + str(x),
                               "Tile Lost in Time and Space: " + str(x),
                               "Tile On Fire?: " + str(x),
                               "Max Fire Allowed: " + str(x),
                               "Fire Tracker: " + str(x),
                               "Dark?: " + str(x),
                               "Adjacent Rooms: " +str(x)))

def showTile():    
    for i in range(0,len(tile_list)):
        print("               ")
        print("Tile Number: " + str(i+1))
        print(tile_list[i].tile_name)
        print(tile_list[i].tile_priority)
        print(tile_list[i].tile_visual)
        print(tile_list[i].tile_reveal)
        print(tile_list[i].tile_lost)
        print(tile_list[i].tile_on_fire)
        print(tile_list[i].tile_max_fire)
        print(tile_list[i].tile_fire_tracker)
        print(tile_list[i].tile_dark)
        print(tile_list[i].tile_adjecent)
        print("               ")

def monsterManager():
    mon_list[0].m_name = "Monster Name: "+ str(9999999)
    mainMenu()

globalLoader()
mainMenu()


