from casino_map import *
from zone import *
from player import *

class Data:
    OBJECTIVES = "\t1.  Find the 'Janitor'.\n\t2.  Get the 'Washroom Key'.\n\t3.  Get your equipment.\n\t4.  Get the 'Staff List'.\n\t5.  'Scan' the 'Parking Lot'.\n\t6.  Get the 'Client List'.\n\t7.  Get into the 'Vault'.\n\t8.  'Scan' the 'Vault'.\n\t9.  'Drop' the 'Tracking Device' in the 'Vault'\n\t10. Return to the 'Lobby'."

    def __init__(self):
        self.running = True
        self.update = True

        self.output = ""

        # 0 no action was entered
        # 1 invalid verb
        # 2 ACTION takes no arguments
        # 3 destination argument is invalid or not specific enough
        # 4 item cannot be examined
        # 5 item cannot be taken
        # 6 you already have that item
        # 7 item cannot be dropped
        # 8 item can't be used
        self.error_code = 0
        self.error_fragment = ""

        self.map = CasinoMap()
        self.output = self.map.zones[LOBBY].description

        self.player = Player()

        self.closet_unlocked = False
        self.office_unlocked = False
        self.locker_unlocked = False
        self.washroom_unlocked = False

        self.janitor_found = False
        self.has_washroom_key = False
        self.has_staff_list = False
        self.parking_lot_scanned = False
        self.has_client_list = False
        self.vault_entered = False
        self.vault_scanned = False
        self.device_planted = False
        self.manager_gone = False

        self.manager_loop = [14, 6, 12, 20, 4, 3, 15]
        self.dock_supervisor_loop = [12, 15]
        self.mob_member_loop = [17, 7, 15, 7]
        self.camera_rooms = [3, 5, 11, 17]

        self.janitor_loop = [18, 11]
        self.informant_loop = [5, 2, 21]

        self.freeze = False

        self.score = 0

        self.turn = 0
        self.time = "6:00 PM"

    def update_time(self, amount):
        self.turn += amount
        self.time = str(6 + self.turn // 60) + ":{:02d} PM".format(self.turn % 60)
