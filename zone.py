from item import *

class Zone:
    def __init__(self, name, description, better_description, items):
        self.name = name

        self.description = description
        self.better_description = better_description

        self.items = items
        self.connections = {}

        self.destination_keyword = name.upper()

    def look(self):
        output = self.better_description

        for item in self.items:
            output += " " + item.zone_description

        return output