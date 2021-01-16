class Item:
    def __init__(self, name, description, zone_description, moveable):
        self.name = name

        self.description = description
        self.zone_description = zone_description

        self.moveable = moveable

CIRCUIT_BOX = Item("CIRCUIT BOX", "Controls the flow of electricity in the 'Theater' area.", "There is a 'Circuit Box' on the wall in the corner of the room.", False)
CLIENT_LIST = Item("CLIENT LIST", "A list of the casino's most frequent visitors.", "A sheet of paper labelled 'Client List' is on the ground.", True)
COMPUTER = Item("COMPUTER", "Stores the casino's financial data.", "A bulky 'Computer' with a CRT monitor is sitting atop the accounting desk. It's humming quietly.", False)
DOOR_CODE = Item("DOOR CODE", "A sticky note with the words 'Door Code' and numbers '0451' written on it in green ink.", "A note labelled 'Door Code' is lying on the ground.", True)
KEYCARD = Item("KEYCARD", "Grants access to the 'Main Office'.", "A 'Keycard' is on the ground.", True)
LASER_TOOL = Item("LASER TOOL", "Can be used to disable 'Camera'.", "Your 'Laser Tool' is on the ground.", True)
LOCKER = Item("LOCKER", "The 'Manager' 'Locker'.", "Amongst the yellow lockers is one red 'Locker' labelled 'Manager'.", False)
LOCKER_KEY = Item("LOCKER KEY", "Grants access to the red 'Locker'.", "A 'Locker Key' is on the ground.", True)
RADIO = Item("RADIO", "Can be used to talk to police headquarters.", "Your 'Radio' is on the ground.", True)
ROLODEX = Item("ROLODEX", "A list of the manager's acquaintances.", "On the desk there is a 'Rolodex'.", False)
SCANNER = Item("SCANNER", "Can be used to match objects to criminals in the police database.", "Your 'Scanner' is on the ground.", True)
SIGNAL_SCRAMBLER = Item("SIGNAL SCRAMBLER", "Can be used to disable electrical equipment.", "Your 'Signal Scrambler' is on the ground.", True)
SPEAKER_SYSTEM = Item("SPEAKER SYSTEM", "Controls the speakers on the casino floor.", "In the corner you see an unsupervised 'Speaker System'.", False)
STAFF_LIST = Item("STAFF LIST", "A list of the casino's staff.", "A sheet of paper labelled 'Staff List' is on the ground.", True)
TRACKING_DEVICE = Item("TRACKING DEVICE", "Can be used to track moving targets.", "Your 'Tracking Device' is on the ground.", True)
WASHROOM_KEY = Item("WASHROOM KEY", "Grants access to one of the casino's two main washrooms.", "A key labelled 'Washroom Key' is on the ground.", True)