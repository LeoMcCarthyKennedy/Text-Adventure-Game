import string

from data import *
from casino_map import *
import item

EXPLORE_MODE = False

VERBS = [" MOVE ",
         " LOOK ",
         " EXAMINE ",
         " INVENTORY ",
         " TAKE ",
         " DROP ",
         " USE ",
         " TALK ",
         " ASK ",
         " WAIT ",
         " CHECK "]

def get_action():
    action = input(">").strip().upper().translate(str.maketrans("", "", string.punctuation))

    while "\t" in action or "  " in action:
        action = action.replace("\t", " ")
        action = action.replace("  ", " ")

    return " " + action

def update(data, action):
    data.freeze = False

    # no action was entered
    if len(action) == 0:
        data.error_code = 0
        return False

    verb = action.split()[0]

    # move
    if verb == VERBS[0].strip():    
        data.output = ""
        destination = action.replace(VERBS[0], "")

        for key in data.map.zones[data.player.current_zone].connections.keys():
            for connection in data.map.zones[data.player.current_zone].connections.get(key):
                if destination == connection:
                    if key == 10:
                        if not data.closet_unlocked:
                            data.output = "You need the 'Janitor' to unlock the door to the 'Janitorial Closet'."
                            return True

                    elif key == 14:
                        if not data.office_unlocked:
                            if item.KEYCARD in data.player.inventory:
                                data.office_unlocked = True
                                data.output += "The 'Main Office' door has been unlocked.\n\n"
                                data.player.inventory.remove(item.KEYCARD)

                            else:
                                data.output = "You need a 'Keycard' to unlock the 'Main Office' door."
                                return True

                    elif key == 22:
                        print("\nEnter passcode\n")
                        password = get_action()

                        if password == " 0451":
                            data.output += "ACCESS GRANTED\n"

                            if not data.vault_entered:
                                data.score += 1
                                data.output += "\nRadio: Amazing. Now we just need to track where this money will go.\n\n"

                            data.vault_entered = True

                        else:
                            data.output = "That is the wrong password."
                            return True

                    elif key == 24:
                        if not data.washroom_unlocked:
                            if item.WASHROOM_KEY in data.player.inventory:
                                data.washroom_unlocked
                                data.output += "The 'Washroom' door has been unlocked.\n\n"
                                data.player.inventory.remove(item.WASHROOM_KEY)
                                data.score += 2

                            else:
                                data.output = "You need a 'Washroom Key' to unlock the 'Washroom' door."
                                return True

                    data.player.current_zone = key
                    data.output += data.map.zones[data.player.current_zone].description
                    
                    if not data.closet_unlocked and data.player.current_zone == data.janitor_loop[(data.turn // 5) % 2]:
                        data.output += "\n\nA 'Janitor' is cleaning in the corner."

                    if data.player.current_zone == data.informant_loop[(data.turn // 5) % 2]:
                        data.output += "\n\nThe police 'Informant' is standing in the middle of the room."

                    return True

        data.error_code = 3
        data.error_fragment = destination
        return False

    # look
    elif verb == VERBS[1].strip():
        if len(action.split()) > 1:
            data.error_code = 2
            argument_count = len(action.split()) - 1

            if argument_count > 1:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            else:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            return False

        data.output = data.map.zones[data.player.current_zone].look()
        return True

    # examine
    elif verb == VERBS[2].strip():
        if len(action.split()) == 1:
            data.error_code = 2
            data.error_fragment = verb + " takes 1 argument. None were given."
            return False

        target_item = action.replace(VERBS[2], "")

        for possible_item in data.map.zones[data.player.current_zone].items:
            if target_item == possible_item.name:
                data.output = possible_item.description
                return True

        for possible_item in data.player.inventory:
            if target_item == possible_item.name:
                data.output = possible_item.description
                return True

        data.error_code = 4
        data.error_fragment = target_item
        return False

    # inventory
    elif verb == VERBS[3].strip():
        if len(action.split()) > 1:
            data.error_code = 2
            argument_count = len(action.split()) - 1

            if argument_count > 1:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            else:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            return False

        data.output = "Inventory:\n"

        for possible_item in data.player.inventory:
            data.output += "\n\t" + possible_item.name

        return True

    # take
    elif verb == VERBS[4].strip():
        if len(action.split()) == 1:
            data.error_code = 2
            data.error_fragment = verb + " takes 1 argument. None were given."
            return False

        target_item = action.replace(VERBS[4], "")

        for possible_item in data.map.zones[data.player.current_zone].items:
            if target_item == possible_item.name and possible_item.moveable:
                data.output = "You take the " + possible_item.name
                data.map.zones[data.player.current_zone].items.remove(possible_item)
                data.player.inventory.append(possible_item)   

                if target_item == "WASHROOM KEY" and not data.has_washroom_key:
                    data.has_washroom_key = True
                    data.score += 1

                elif target_item == "STAFF LIST" and not data.has_staff_list:
                    data.has_staff_list = True
                    data.score += 1

                elif target_item == "CLIENT LIST" and not data.has_client_list:
                    data.has_client_list = True
                    data.score += 1

                return True

        for possible_item in data.player.inventory:
            if target_item == possible_item.name:
                data.error_code = 6
                return False

        data.error_code = 5
        data.error_fragment = target_item
        return False

    # drop
    elif verb == VERBS[5].strip():
        if len(action.split()) == 1:
            data.error_code = 2
            data.error_fragment = verb + " takes 1 argument. None were given."
            return False

        target_item = action.replace(VERBS[5], "")

        for possible_item in data.player.inventory:
            if target_item == possible_item.name:
                if target_item == "RADIO":
                    data.output = "Radio: I don't think that's such a good idea."
                    return True

                elif target_item == "TRACKING DEVICE" and data.player.current_zone == 22:
                    data.device_planted = True
                    data.score += 1
                    data.output = "You place the TRACKING DEVICE deep within the money pile.\n\nRadio: Good work detective! We are so close!"
                    data.player.inventory.remove(possible_item)  
                    return True

                data.output = "You drop the " + possible_item.name
                data.player.inventory.remove(possible_item)   
                data.map.zones[data.player.current_zone].items.append(possible_item)
                return True

        data.error_code = 7
        data.error_fragment = target_item
        return False

    # use
    elif verb == VERBS[6].strip():
        if len(action.split()) == 1:
            data.error_code = 2
            data.error_fragment = verb + " takes 1 argument. None were given."
            return False

        target_item = action.replace(VERBS[6], "")

        for possible_item in data.player.inventory:
            if target_item == possible_item.name:
                if target_item == "RADIO":
                    data.output = "Radio: I'm not completely sure what you have already done but here are your objectives:\n\n" + data.OBJECTIVES
                    return True

                elif target_item == "LOCKER KEY" and data.player.current_zone == 19:
                    if not data.locker_unlocked:
                        data.locker_unlocked = True
                        data.output = "The locker has been unlocked. Inside the 'Locker' you find a note labelled 'Door Code'. It has been added to your 'Inventory'."
                        data.player.inventory.append(item.DOOR_CODE)
                        return True
                    
                    data.output = "The locker is already unlocked."
                    return True

                elif target_item == "LOCKER KEY":
                    data.output = "That item can't be used here."
                    return True

                elif target_item == "SCANNER" and data.player.current_zone == 16:
                    if not data.parking_lot_scanned:
                        data.output = "You scan the car license plates.\n\nRadio: Good work detective. According to the database some of those are stollen cars."
                        data.parking_lot_scanned = True
                        data.score += 1
                        return True

                    else:
                        data.output = "You have already scanned the car license plates."
                        return True

                elif target_item == "SCANNER" and data.player.current_zone == 22:
                    if not data.vault_scanned:
                        data.output = "You scan the serial numbers on the money.\n\nRadio: Good work detective. We're almost done."
                        data.vault_scanned = True
                        data.score += 1
                        return True

                    else:
                        data.output = "You have already scanned the serial numbers on the money."
                        return True

                elif target_item == "SCANNER":
                    data.output = "Nothing to scan here."
                    return True

                if target_item == "LASER TOOL" and data.player.current_zone == 3 and 3 in data.camera_rooms:
                    data.output = "You disable the room's 'Camera'."
                    data.camera_rooms.remove(3)
                    return True

                elif target_item == "LASER TOOL" and data.player.current_zone == 5 and 5 in data.camera_rooms:
                    data.output = "You disable the room's 'Camera'."
                    data.camera_rooms.remove(5)
                    return True
                
                elif target_item == "LASER TOOL" and data.player.current_zone == 11 and 11 in data.camera_rooms:
                    data.output = "You disable the room's 'Camera'."
                    data.camera_rooms.remove(11)
                    return True

                elif target_item == "LASER TOOL" and data.player.current_zone == 17 and 17 in data.camera_rooms:
                    data.output = "You disable the room's 'Camera'."
                    data.camera_rooms.remove(17)
                    return True

                elif target_item == "LASER TOOL":
                    data.output = "There are no cameras in this room to use it on."
                    return True

                elif target_item == "SIGNAL SCRAMBLER" and data.player.current_zone == 2:
                    data.player.inventory.remove(item.SIGNAL_SCRAMBLER)
                    data.output = "You fry the 'Circuit Box'. All the 'Theater' lights go out.\n\nRadio: Good work. My tracker is telling me that the 'Manager' must have seen the outage on his computer screen. He has left the building to get help. We won't have to worry about him anymore."
                    data.manager_gone = True
                    return True

                elif target_item == "SIGNAL SCRAMBLER" and data.player.current_zone == 3:
                    data.player.inventory.remove(item.SIGNAL_SCRAMLBER)
                    data.output = "You fry the 'Speaker System'. The speakers on the 'Casino Floor' get blown out.\n\nRadio: Good work. My tracker is telling me that the 'Manager' must have seen the outage on his computer screen. He has left the building to get help. We won't have to worry about him anymore."
                    data.manager_gone = True
                    return True

                elif target_item == "SIGNAL SCRAMBLER":
                    data.output = "There are no electronics in this room to use it on."
                    return True

        data.error_code = 8
        data.error_fragment = target_item
        return False

    # talk
    elif verb == VERBS[7].strip():
        if len(action.split()) == 1:
            data.error_code = 2
            data.error_fragment = verb + " takes 1 argument. None were given."
            return False

        person = action.split()[1]

        data.freeze = True

        if person == "WOMAN" and data.player.current_zone == 13:
            data.output = "\tWoman: Hello. How can I help you?"
            return True

        if person == "JANITOR" and data.player.current_zone == data.janitor_loop[(data.turn // 5) % 2]:
            data.output = "\tJanitor: Hey there lad. Don't mind me."
            return True

        if person == "INFORMANT" and data.player.current_zone == data.informant_loop[(data.turn // 5) % 2]:
            data.output = "\tInformant: There you are. I left a package for you in the 'Washroom' incase you didn't get it yet. Talk quick or you'll blow our cover."
            return True

        if person == "RADIO":
            data.output = "\tRadio: You are doing well. You have " + str(data.score) + " out of 10 objectives completed. Keep going."
            return True

        data.freeze = False

        data.error_code = 9
        data.error_fragment = person
        return False

    # ask
    elif verb == VERBS[8].strip():
        if len(action.split()) == 1:
            data.error_code = 2
            data.error_fragment = verb + " takes 2 argument. None were given."
            return False

        elif len(action.split()) == 2:
            data.error_code = 2
            data.error_fragment = verb + " takes 2 argument. 1 was given."
            return False

        person = action.split()[1]
        topic = action.replace(VERBS[8], "").replace(person + " ", "")

        data.freeze = True

        if person == "WOMAN" and data.player.current_zone == 13:
            if topic == "JANITOR":
                data.output = "\tWoman: You can usually find the 'Janitor' in the 'Kitchen' or the 'Restaurant'. That's where he cleans at this hour."
                return True

            elif topic == "WASHROOM KEY":
                data.output = "\tWoman: If you need a key to one of the washrooms the 'Janitor' will probably have it."
                return True

            elif topic == "LOCKER KEY":
                data.output = "\tWoman: I can't help you with that. I got a key for my own 'Locker' but I wouldn't give it away to anybody."
                return True

            elif topic == "MOB":
                data.output = "\tWoman: I beg your pardon."
                return True

            elif topic == "CASINO":
                data.output = "\tWoman: I've been working here since it opened a few years ago. The pay is decent."
                return True

            elif topic == "MANAGER":
                data.output = "\tWoman: Blair is the 'Manager' here. He is kind of uptight and rude. I try not to get in his way."
                return True

            elif topic == "SUPERVISOR":
                data.output = "\tWoman: I don't know the 'Supervisor' too well. He mostly supervises the 'Loading Dock' and the 'Monitoring Room'."
                return True

            elif topic == "MASK" or topic == "MASKED FIGURE" or topic == "MYSTERIOUS MASKED FIGURE":
                data.output = "\tWoman: Do you mean that creep walking around wearing that mask? Freaks me out. I don't see him very often. I think he is close with the 'Supervisor'."
                return True

            elif topic == "VAULT":
                data.output = "\tWoman: I've never been inside of it. Probably never will too."
                return True

            elif topic == "STAFF LIST":
                data.output = "\tWoman: I think we have a 'Staff List' in the 'Staff Room'. I don't see why you'd need it though."
                return True

            elif topic == "CLIENT LIST":
                data.output = "\tWoman: You'd probably find that in the 'Accounting Office'."
                return True

            else:
                data.output = "\tWoman: I'm not sure what you mean."
                return True

        if person == "JANITOR" and data.player.current_zone == data.janitor_loop[(data.turn // 5) % 2] and not data.closet_unlocked:
            if topic == "JANITOR":
                data.output = "\tJanitor: That's me."
                return True

            elif topic == "WASHROOM KEY":
                data.output = "\tJanitor: I forgot that I locked that 'Washroom'. The key is the 'Janitorial Closet'. I'll go and unlock it for you.\n\nThe 'Janitor' left to unlock the 'Janitorial Closet'."
                data.closet_unlocked = True
                data.janitor_found = True
                return True

            elif topic == "LOCKER KEY":
                data.output = "\tJanitor: I don't use my 'Locker' here."
                return True

            elif topic == "MANAGER":
                data.output = "\tJanitor: Blair is the 'Manager' here. He's kind of a jerk."
                return True

            elif topic == "SUPERVISOR":
                data.output = "\tJanitor: Weird guy. Don't get in his way."
                return True

            elif topic == "MASK" or topic == "MASKED FIGURE" or topic == "MYSTERIOUS MASKED FIGURE":
                data.output = "\tJanitor: That masked freak has been walking around here for the last few hours. I got to find a new job."
                return True

            elif topic == "STAFF LIST":
                data.output = "\tJanitor: Probably in the 'Staff Room'."
                return True

            elif topic == "CLIENT LIST":
                data.output = "\tJanitor: I got no idea where they keep that. Maybe try the 'Accounting Office'?"
                return True

            else:
                data.output = "\tJanitor: What?"
                return True

        if person == "INFORMANT" and data.player.current_zone == data.informant_loop[(data.turn // 5) % 2]:
            if topic == "JANITOR":
                data.output = "\tInformant: He's probably in the 'Kitchen' cleaning."
                return True

            elif topic == "WASHROOM KEY":
                data.output = "\tInformant: Last I checked it was in the 'Janitorial Closet'."
                return True

            elif topic == "LOCKER KEY":
                data.output = "\tInformant: The 'Manager' keeps it in the 'Main Office'."
                return True

            elif topic == "MANAGER":
                data.output = "\tInformant: You mean Blair? Not a fun guy."
                return True

            elif topic == "SUPERVISOR":
                data.output = "\tInformant: That guy scares me."
                return True

            elif topic == "MASK" or topic == "MASKED FIGURE" or topic == "MYSTERIOUS MASKED FIGURE":
                data.output = "\tInformant: The masked guy? I'm glad I spotted him when I did. I think he is onto us. Stay clear."
                return True

            elif topic == "STAFF LIST":
                data.output = "\tInformant: In the 'Staff Room' I think."
                return True

            elif topic == "CLIENT LIST":
                data.output = "\tInformant: Try the 'Accounting Office'. If not there then definitely the 'Main Office'."
                return True

            elif topic == "LASER TOOL":
                data.output = "\tInformant: That thing is super good at discretely taking out cameras."
                return True

            elif topic == "SCANNER":
                data.output = "\tInformant: You tried scanning the 'Parking Lot' with it yet?"
                return True

            elif topic == "TRACKING DEVICE":
                data.output = "\tInformant: You've got to leave that in the 'Vault' with all the money my friend."
                return True

            elif topic == "SIGNAL SCRAMBLER":
                data.output = "\tInformant: Use that on the 'Casino Floor' or 'Backstage'."
                return True

            else:
                data.output = "\tInformant: I don't understand."
                return True

        if person == "RADIO":
            if topic == "JANITOR":
                data.output = "\tRadio: I'm not sure where he is. Try asking someone there."
                return True

            elif topic == "WASHROOM KEY":
                data.output = "\tRadio: The 'Janitor' probably has it."
                return True

            elif topic == "LOCKER KEY":
                data.output = "\tRadio: No clue where that could be man."
                return True

            elif topic == "MANAGER":
                data.output = "\tRadio: I'm still tracking him. Give me a 'CHECK' if you need to know his location."
                return True

            elif topic == "SUPERVISOR":
                data.output = "\tRadio: I'm still tracking him. Give me a 'CHECK' if you need to know his location."
                return True

            elif topic == "MASK" or topic == "MASKED FIGURE" or topic == "MYSTERIOUS MASKED FIGURE":
                data.output = "\tRadio: I'm still tracking him. Give me a 'CHECK' if you need to know his location."
                return True

            elif topic == "STAFF LIST":
                data.output = "\tRadio: If we can get the 'Staff List' we can find connections to the mob."
                return True

            elif topic == "CLIENT LIST":
                data.output = "\tRadio: Useful information."
                return True

            elif topic == "LASER TOOL":
                data.output = "\tRadio: Use it in rooms with cameras and it will permanently wipe them out."
                return True

            elif topic == "SCANNER":
                data.output = "\tRadio: Use it in the 'Parking Lot' and the 'Vault' when you get the chance."
                return True

            elif topic == "TRACKING DEVICE":
                data.output = "\tRadio: Leave it in the 'Vault'."
                return True

            elif topic == "SIGNAL SCRAMBLER":
                data.output = "\tRadio: Nifty gadget. My information is telling me that you could probably use it in the 'Backstage' area or on the 'Casino Floor'."
                return True

            else:
                data.output = "\tRadio: I don't know what you mean."
                return True

        data.freeze = False

        data.error_code = 9
        data.error_fragment = person
        return False

    # wait
    elif verb == VERBS[9].strip():
        if len(action.split()) > 1:
            data.error_code = 2
            argument_count = len(action.split()) - 1

            if argument_count > 1:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            else:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            return False

        data.update_time(1)
        data.output = "You wait two minutes."
        return True

    # check
    elif verb == VERBS[10].strip():
        if len(action.split()) > 1:
            data.error_code = 2
            argument_count = len(action.split()) - 1

            if argument_count > 1:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            else:
                data.error_fragment = verb + " takes no arguments. " + str(argument_count) + " were given."

            return False

        data.output = "Radio: Here are the location's of the trackers I have:\n"
        data.output += "\n\t'Manager':       " + ("Left" if data.manager_gone else data.map.zones[data.manager_loop[(data.turn // 7) % 7]].name + "\t\tNext: " + data.map.zones[data.manager_loop[((data.turn + 2) // 7) % 7]].name)
        data.output += "\n\t'Supervisor':    " + data.map.zones[data.dock_supervisor_loop[(data.turn // 15 % 2)]].name + "\t\tNext: " + data.map.zones[data.dock_supervisor_loop[((data.turn + 2) // 15) % 2]].name
        data.output += "\n\t'Masked Figure': " + data.map.zones[data.mob_member_loop[(data.turn // 9) % 4]].name + "\t\tNext: " + data.map.zones[data.mob_member_loop[((data.turn + 2) // 9) % 4]].name
        return True

    # invalid verb
    else:
        data.error_code = 1
        data.error_fragment = verb
        return False

def death_check(data):
    if EXPLORE_MODE:
        return True

    if data.player.current_zone == 13 and data.score == 9:
        print("Amazing work! You have made it out of the Opal Garden Casino alive and with enough evidence to shut down the mob indefinitely!.\n\nFinal Score: " + str(data.score + 1))
        return False

    if data.turn >= 240:
        print("Your time has unfortunately run out. Your partner picks you up in a covert vehicle out front. Maybe next time.\n\nFinal Score: " + str(data.score))
        return False

    if data.player.current_zone == data.dock_supervisor_loop[(data.turn // 15 % 2)]:
        print("\nYou've run face first into the 'Supervisor'. He asks you to leave while pointing to a revolver in his waistband. You have been compromised.\n\nFinal Score: " + str(data.score))
        return False

    if data.player.current_zone in data.camera_rooms and data.dock_supervisor_loop[(data.turn // 15 % 2)] == 15:
        print("\nThe 'Supervisor' has seen you snooping around on one of the 'Cameras'. You have been compromised.\n\nFinal Score: " + str(data.score))
        return False

    if data.player.current_zone == data.mob_member_loop[(data.turn // 9) % 4]:
        print("\nYou've run face first into a 'Masked Figure'. Your disguise doesn't fool him. You have been compromised.\n\nFinal Score: " + str(data.score))
        return False
    
    if not data.manager_gone:
        if data.player.current_zone == data.manager_loop[(data.turn // 7) % 7]:
            print("\nYou've run face first into the 'Manager'. He insists your inspection is done and that it is time for you to leave. Mission failed.\n\nFinal Score: " + str(data.score))
            return False

    return True

def render(data):
    print()

    if not data.update:
        if data.error_code == 0:
            print("* No action was entered.")

        elif data.error_code == 1:
            print("* " + data.error_fragment + " is not a valid verb.")

        elif data.error_code == 2:
            print(data.error_fragment)

        elif data.error_code == 3:
            print("* Destination: " + data.error_fragment + " is invalid or not specific enough.")

        elif data.error_code == 4:
            print("* " + data.error_fragment + " cannot be examined.")

        elif data.error_code == 5:
            print("* " + data.error_fragment + " cannot be taken.")

        elif data.error_code == 6:
            print("* You already have that item.")

        elif data.error_code == 7:
            print("* " + data.error_fragment + " cannot be dropped.")

        elif data.error_code == 8:
            print("* " + data.error_fragment + " cannot be used.")

        elif data.error_code == 9:
            print("* " + data.error_fragment + " cannot be talked to.")

    else:
        print("Location: " + data.map.zones[data.player.current_zone].name)
        print("Time:     " + data.time)
        print("Score:    " + str(data.score))
        print("\n" + data.output)

    print()

def main():
    data = Data()

    print("""THE OPAL GARDEN CASINO

by: Leo McCarthy-Kennedy

    COMMANDS:

        MOVE (location or direction)    Moves the player to desired adjacent location

        LOOK                            Describes the current zone

        EXAMINE (item)                  Describes item

        INVENTORY                       Lists items in the player's inventory

        TAKE (item)                     Add item from the zone to the player's inventory

        DROP (item)                     Removes item from the player's inventory and places it in the player's current zone

        USE (item)                      Uses item

        TALK (person)                   Starts dialogue with person

        ASK (person) (topic)            Gains information on topic from person

        WAIT                            Makes two minutes pass in the game world

        CHECK                           Display current enemy positions

    MISSION:

        You are going undercover to investigate the Opal Garden Casino. It is believed that the casino is a front for a criminal 
        organization that is using the casino's resources to launder their money.

        You have been sent disguised as a health inspector who is there for a routine check. Because of your disguise the casino 
        has granted you access to almost all of their rooms.

        The administration has also provided you with a few gadgets to get the job done. You have been equipped with a police radio
        that allows you to talk to your man on the outside. More gadgets are waiting for you in one of the casino's washrooms. They 
        have been stashed by an informant on the inside.

        It's unfortunate that it was not realized sooner but one of the supervisors at the casino has had a few run-ins with you in 
        the past. Avoid him at all cost. If that wasn't bad enough, the informant tells us that a mysterious masked figure has been 
        patroling the casino all day. Definitely avoid him as well.

        Finally, you need to avoid the casino manager. Although he is not threatening, he knows something is up and will probably
        find a way to remove you from the premises.

        To help you avoid these dangers the administration has been tracking the movement of several casino employees by
        triangulating cellphone signals coming from inside.

        It is believed their behaviour is as follows:

            MANAGER:        Does a general patrol of the lower half of the casino. Changes room every 7 minutes.

            SUPERVISOR:     Alternates between the Monitoring Room and the Loading Dock every 15 minutes.

            MASKED FIGURE:  Patrols the Eastern Hallway. Changes room every 9 minutes.

        Also watch out for the cameras. Their location has not been able to be identified. If the Supervisor is in the Monitoring
        Room, make sure to stay out of rooms with cameras.

        Remember to use TALK RADIO, ASK RADIO (topic) and USE RADIO at any time to contact the outside.

        Good luck.
""", end="")

    while data.running:
        render(data)
        data.update = update(data, get_action())

        if data.update:
            if not data.freeze:
                data.update_time(1)

            data.running = death_check(data)

    print()

if __name__ == "__main__":
    main()
