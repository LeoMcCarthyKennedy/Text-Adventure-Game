from zone import Zone
import item

NORTH = ["NORTH", "N"]
SOUTH = ["SOUTH", "S"]
EAST = ["EAST", "E"]
WEST = ["WEST", "W"]

ACCOUNTING_OFFICE = 0
ALLEY = 1
BACKSTAGE = 2
CASINO_FLOOR = 3
CLUB_ROOM = 4
GREEN_ROOM = 5
HALLWAY_A = 6
HALLWAY_B = 7
HALLWAY_C = 8
HIGH_ROLLER_ROOM = 9
JANITORIAL_CLOSET = 10
KITCHEN = 11
LOADING_DOCK = 12
LOBBY = 13
MAIN_OFFICE = 14
MONITORING_ROOM = 15
PARKING_LOT = 16
PRIVATE_ROOM = 17
RESTAURANT = 18
STAFF_ROOM = 19
STORAGE_ROOM = 20
THEATER = 21
VAULT = 22
WASHROOM_A = 23
WASHROOM_B = 24

class CasinoMap:
    def __init__(self):
        self.zones = [Zone("Accounting Office", "You are in the 'Accounting Office'. A dim fluorescent light illuminates the room. Papers are scattered across the desk and floor. A quiet hum fills the air.\n\nTo the 'North' is the 'Monitoring Room'.\nTo the 'South' is the 'Vault'.", "The room reeks of cigarettes.", [item.COMPUTER, item.CLIENT_LIST]),
                      Zone("Alley", "You are in the 'Alley'. The concrete ground is wet and covered with mud. Garbage is littered everywhere.\n\nTo the 'North' is the 'Parking Lot'.\nTo the 'West' is a 'Hallway'.", "You'd think someone would at least pick up the garbage.", []),
                      Zone("Backstage", "You are 'Backstage'. Costumes and props are scattered across the furniture. You can faintly hear the sound of cars passing by outside.\n\nTo the 'South' is the 'Theater'.\nTo the 'East' is the 'Green Room'.", "You wonder how often the casino puts on a show. Some of these costumes look like they haven't been cleaned in ages.", [item.CIRCUIT_BOX]),
                      Zone("Casino Floor", "You are on the 'Casino Floor'. It seems unusually quiet for a Friday night. Empty slot machines line the walls. You notice a few people playing cards. The 'Casino Floor' seems to be a hub for most of the casino's other rooms.\n\nTo the north is the 'Restaurant' and a 'Hallway'.\nTo the south is the 'Storage Room', the 'Janitorial Closet' and the 'Club Room'.\nTo the east is the 'Monitoring Room', the 'Private Room' and a 'Washroom'.\nTo the west is the 'Lobby' and the 'Staff Room'.", "The carpet is in dire need of a cleaning. You notice a security camera on the ceiling in the corner.", [item.SPEAKER_SYSTEM]),
                      Zone("Club Room", "You are in the 'Club Room'. On the wall is a bulletin board with a few posters attached. A table in the center of the room is scarcely covered in cards. It seems as if a game was recently played in here.\n\nTo the 'North' is the 'Casino Floor'.\nTo the 'West' is the 'Storage Room'.", "You notice an illustration of a figure in a yellow mask on one of the posters. You recognize this as one of the local mob outfits. They like dressing up. They seem to use it as some sort of a scare tactic.", []),
                      Zone("Green Room", "You are in the 'Green Room'. A few couches line the walls. In the center of the room is a coffee table with some empty glasses on it.\n\nTo the 'East' is the 'Parking Lot'.\nTo the 'West' is 'Backstage'.", "You wonder how often this room gets cleaned. Compared to the rest of the casino it is pretty cozy. You notice a security camera on the ceiling in the corner.", [item.KEYCARD]),
                      Zone("Hallway", "You are in a 'Hallway'.\n\nTo the north is the 'Storage Room' and the 'Main Office'.\nTo the 'West' is the 'Loading Dock'.", "The corridor is fairly barren.", []),
                      Zone("Hallway", "You are in a 'Hallway'.\n\nTo the 'East' is the 'Alley'.\nTo the west is the 'Private Room' and the 'Monitoring Room'.", "The corridor is fairly barren.", []),
                      Zone("Hallway", "You are in a 'Hallway'.\n\nTo the 'North' is the 'Theater'.\nTo the 'South' is the 'Casino Floor'.\nTo the 'East' is the 'High Roller Room'.", "The corridor is fairly barren.", []),
                      Zone("High Roller Room", "You are in the 'High Roller Room'. Surprisingly there are no players. The room has five card tables and three slot machines. Plastic plants fill the empty space.\n\nTo the 'North' is a 'Washroom'.\nTo the 'West' is a 'Hallway'.", "The carpet around the 'Washroom' entrance is stained. An out of order sign hangs from the 'Washroom' door. This casino is so filthy and void of people that they must be doing criminal activity of some kind. How else could they stay open?", []),
                      Zone("Janitorial Closet", "You are in the 'Janitorial Closet'. The closet is small and cramped. The smell of bleach pierces your nose.\n\nTo the 'North' is the 'Casino Floor'.", "So far the closet is the cleanest room in the casino. Although, it is cluttered with random cleaning supplies.", [item.WASHROOM_KEY]),
                      Zone("Kitchen", "You are in the 'Kitchen'. The chef is nowhere to be found. Dirty dishes are piled in the sink. How come the casino restaurant is closed on a Friday night?\n\nTo the 'North' is the 'Restaurant'.\nTo the 'South' is the 'Staff Room'.", "The floor is wet and slippery. A opaque window above the sink allows a glimpse into the outside world. You see a road far in the distance. Headlights of passing cars dissapear as they enter a tunnel. You notice a security camera on the ceiling in the corner.", []),
                      Zone("Loading Dock", "You are in the 'Loading Dock'. A few trucks are parked inside. Cardboard boxes fill the room. A small lightbulb is hanging from the ceiling.\n\nTo the west is the 'Storage Room' and a 'Hallway'.", "For such a rundown casino you are surprised they even have a 'Loading Dock'. What could they possibly need it for?", []),
                      Zone("Lobby", "You are in the 'Lobby'. The room reeks of cigarette smoke. You see a 'Woman' shrouded in fake plastic plants sitting at the front desk. She watches as you enter.\n\nTo the 'North' is the 'Staff Room'.\nTo the 'East' is the 'Casino Floor'.", "The 'Woman' has bags under her eyes. You would too if you worked in a place like this. She takes a drag from her cigarette.", []),
                      Zone("Main Office", "You are in the 'Main Office'. The manager's desk is in the center. It is decorated with various trinkets. A stack of papers is placed neatly on the corner of the desk.\n\nTo the 'North' is the 'Monitoring Room'.\nTo the 'South' is a 'Hallway'.", "The manager seems to keep himself busy.", [item.ROLODEX, item.LOCKER_KEY]),
                      Zone("Monitoring Room", "You are in the 'Monitoring Room'. The wall is covered in computer screens. Each screen is displaying a camera feed from a location in the casino.\n\nTo the south is the 'Accounting Office' and the 'Main Office'.\nTo the 'East' is a 'Hallway'.\nTo the 'West' is the 'Casino Floor'.", "You recognize some of the rooms on the screens. You can see feeds from the 'Private Room', the 'Casino Floor', the 'Kitchen' and the 'Green Room'.", []),
                      Zone("Parking Lot", "You are in the 'Parking Lot'. There are only a few cars. Most of them are old and rusted. You notice one exceptionally clean car parked in the corner.\n\nTo the 'South' is the 'Alley'.\nTo the 'West' is the 'Green Room'.", "A rat is gnawing on a slice of pizza in the corner.", []),
                      Zone("Private Room", "You are in the 'Private Room'. Compared to the rest of the casino this room is exceptionally fancy. A box of cigars is lying on the card table at the center of the room. The walls are covered in a dark green wallpaper.", "A yellow mask is lying on the card table. You notice a security camera on the ceiling in the corner.", []),
                      Zone("Restaurant", "You are in the 'Restaurant'. The room is filled with round dinner tables covered in checkered tablecloth. The north wall is covered in windows. You can see the ocean from here.\n\nTo the south is the 'Kitchen' and the 'Casino Floor'.", "You faintly hear the sounds of waves in distance. The room has a calming atmosphere.", []),
                      Zone("Staff Room", "You are in the 'Staff Room'. A small table is at the center of the room. The west wall is covered in yellow lockers. A few dirty uniforms are hanging on a coatrack in the corner.\n\nTo the 'North' is the 'Kitchen'.\nTo the 'South' is the 'Lobby'.\nTo the 'East' is the 'Casino Floor'.", "For a seemingly empty casino you are surprised at the number of staff lockers.", [item.STAFF_LIST, item.LOCKER]),
                      Zone("Storage Room", "You are in the 'Storage Room'. The room is cluttered with boxes. You barely make your way around without squeezing through a tight gap. There are cobwebs in the corners.\n\nTo the 'North' is the 'Casino Floor'.\nTo the 'South' is a 'Hallway'.\nTo the 'East' is the 'Club Room'.\nTo the 'West' is the 'Loading Dock'.", "A few decommissioned slot machines are lying against the wall.", []),
                      Zone("Theater", "You are in the 'Theater'. The room is large and echoey. If the casino was less rundown you could imagine some good shows being performed here.\n\nTo the 'North' is 'Backstage'.\nTo the 'South' is a 'Hallway'.", "You see an old projector hanging from the ceiling at the back. At one point this place must've shown movies.", []),
                      Zone("Vault", "You are in the 'Vault'. Piles of cash and gold bars fill the room. You are tempted to take some but you must remember why you're here. Your mission is almost over.\n\nTo the 'North' is the 'Accounting Office'.", "There is so much money you can't imagine how one could even spend it all. You better do your business and leave before someone catches you.", []),
                      Zone("Washroom", "You are in a 'Washroom'. Nothing is out of the ordinary. It's clear that the room isn't cleaned very often.\n\nTo the 'West' is the 'Casino Floor'.", "Nothing to see really.", []),
                      Zone("Washroom", "You are in a 'Washroom'. The floor is relatively dry but slippery under one of the stalls. You hear the sound of trickling water. A toilet is overflowing in one of the stalls.\n\nTo the 'South' is the 'High Roller Room'.", "This is the 'Washroom' where the 'Informant' stashed your package.", [item.SCANNER, item.TRACKING_DEVICE, item.LASER_TOOL, item.SIGNAL_SCRAMBLER])]

        self.zones[ACCOUNTING_OFFICE].connections = {MONITORING_ROOM: NORTH + [self.zones[MONITORING_ROOM].destination_keyword],
                                                     VAULT: SOUTH + [self.zones[VAULT].destination_keyword]}
        self.zones[ALLEY].connections = {HALLWAY_B: WEST + [self.zones[HALLWAY_B].destination_keyword],
                                         PARKING_LOT: NORTH + [self.zones[PARKING_LOT].destination_keyword]}
        self.zones[BACKSTAGE].connections = {GREEN_ROOM: EAST + [self.zones[GREEN_ROOM].destination_keyword],
                                             THEATER: SOUTH + [self.zones[THEATER].destination_keyword]}
        self.zones[CASINO_FLOOR].connections = {CLUB_ROOM: [self.zones[CLUB_ROOM].destination_keyword],
                                                HALLWAY_C: [self.zones[HALLWAY_C].destination_keyword],
                                                JANITORIAL_CLOSET: [self.zones[JANITORIAL_CLOSET].destination_keyword],
                                                LOBBY: [self.zones[LOBBY].destination_keyword],
                                                MONITORING_ROOM: [self.zones[MONITORING_ROOM].destination_keyword],
                                                PRIVATE_ROOM: [self.zones[PRIVATE_ROOM].destination_keyword],
                                                RESTAURANT: [self.zones[RESTAURANT].destination_keyword],
                                                STAFF_ROOM: [self.zones[STAFF_ROOM].destination_keyword],
                                                STORAGE_ROOM: [self.zones[STORAGE_ROOM].destination_keyword],
                                                WASHROOM_A: [self.zones[WASHROOM_A].destination_keyword]}
        self.zones[CLUB_ROOM].connections = {CASINO_FLOOR: NORTH + [self.zones[CASINO_FLOOR].destination_keyword],
                                             STORAGE_ROOM: WEST + [self.zones[STORAGE_ROOM].destination_keyword]}
        self.zones[GREEN_ROOM].connections = {BACKSTAGE: WEST + [self.zones[BACKSTAGE].destination_keyword],
                                              PARKING_LOT: EAST + [self.zones[PARKING_LOT].destination_keyword]}
        self.zones[HALLWAY_A].connections = {LOADING_DOCK: WEST + [self.zones[LOADING_DOCK].destination_keyword],
                                             MAIN_OFFICE: [self.zones[MAIN_OFFICE].destination_keyword],
                                             STORAGE_ROOM: [self.zones[STORAGE_ROOM].destination_keyword]}
        self.zones[HALLWAY_B].connections = {ALLEY: EAST + [self.zones[ALLEY].destination_keyword],
                                             MONITORING_ROOM: [self.zones[MONITORING_ROOM].destination_keyword],
                                             PRIVATE_ROOM: [self.zones[PRIVATE_ROOM].destination_keyword]}
        self.zones[HALLWAY_C].connections = {CASINO_FLOOR: SOUTH + [self.zones[CASINO_FLOOR].destination_keyword],
                                             HIGH_ROLLER_ROOM: EAST + [self.zones[HIGH_ROLLER_ROOM].destination_keyword],
                                             THEATER: NORTH + [self.zones[THEATER].destination_keyword]}
        self.zones[HIGH_ROLLER_ROOM].connections = {HALLWAY_C: WEST + [self.zones[HALLWAY_C].destination_keyword],
                                                    WASHROOM_B: NORTH + [self.zones[WASHROOM_B].destination_keyword]}
        self.zones[JANITORIAL_CLOSET].connections = {CASINO_FLOOR: NORTH + [self.zones[CASINO_FLOOR].destination_keyword]}
        self.zones[KITCHEN].connections = {RESTAURANT: NORTH + [self.zones[RESTAURANT].destination_keyword],
                                           STAFF_ROOM: SOUTH + [self.zones[STAFF_ROOM].destination_keyword]}
        self.zones[LOADING_DOCK].connections = {HALLWAY_A: [self.zones[HALLWAY_A].destination_keyword],
                                                STORAGE_ROOM: [self.zones[STORAGE_ROOM].destination_keyword]}
        self.zones[LOBBY].connections = {CASINO_FLOOR: EAST + [self.zones[CASINO_FLOOR].destination_keyword],
                                         STAFF_ROOM: NORTH + [self.zones[STAFF_ROOM].destination_keyword]}
        self.zones[MAIN_OFFICE].connections = {MONITORING_ROOM: NORTH + [self.zones[MONITORING_ROOM].destination_keyword],
                                               HALLWAY_A: SOUTH + [self.zones[HALLWAY_B].destination_keyword]}
        self.zones[MONITORING_ROOM].connections = {ACCOUNTING_OFFICE: [self.zones[ACCOUNTING_OFFICE].destination_keyword],
                                                  CASINO_FLOOR: WEST + [self.zones[CASINO_FLOOR].destination_keyword],
                                                  HALLWAY_B: EAST + [self.zones[HALLWAY_B].destination_keyword],
                                                  MAIN_OFFICE: [self.zones[MAIN_OFFICE].destination_keyword]}
        self.zones[PARKING_LOT].connections = {ALLEY: SOUTH + [self.zones[ALLEY].destination_keyword],
                                               GREEN_ROOM: WEST + [self.zones[GREEN_ROOM].destination_keyword]}
        self.zones[PRIVATE_ROOM].connections = {CASINO_FLOOR: WEST + [self.zones[CASINO_FLOOR].destination_keyword],
                                                HALLWAY_B: EAST + [self.zones[HALLWAY_B].destination_keyword]}
        self.zones[RESTAURANT].connections = {CASINO_FLOOR: [self.zones[CASINO_FLOOR].destination_keyword],
                                              KITCHEN: [self.zones[KITCHEN].destination_keyword]}     
        self.zones[STAFF_ROOM].connections = {CASINO_FLOOR: EAST + [self.zones[CASINO_FLOOR].destination_keyword],
                                              KITCHEN: NORTH + [self.zones[KITCHEN].destination_keyword],
                                              LOBBY: SOUTH + [self.zones[LOBBY].destination_keyword]}
        self.zones[STORAGE_ROOM].connections = {CASINO_FLOOR: NORTH + [self.zones[CASINO_FLOOR].destination_keyword],
                                                CLUB_ROOM: EAST + [self.zones[CLUB_ROOM].destination_keyword],
                                                HALLWAY_A: SOUTH + [self.zones[HALLWAY_A].destination_keyword],
                                                LOADING_DOCK: WEST + [self.zones[LOADING_DOCK].destination_keyword]}
        self.zones[THEATER].connections = {BACKSTAGE: NORTH + [self.zones[BACKSTAGE].destination_keyword],
                                           HALLWAY_C: SOUTH + [self.zones[HALLWAY_C].destination_keyword]}
        self.zones[VAULT].connections = {ACCOUNTING_OFFICE: NORTH + [self.zones[ACCOUNTING_OFFICE].destination_keyword]}
        self.zones[WASHROOM_A].connections = {CASINO_FLOOR: WEST + [self.zones[CASINO_FLOOR].destination_keyword]}
        self.zones[WASHROOM_B].connections = {HIGH_ROLLER_ROOM: SOUTH + [self.zones[HIGH_ROLLER_ROOM].destination_keyword]}