class room:
    def __init__(self,doors,fans,lights,beds):
        self.doors = doors
        self.fans = fans
        self.lights = lights
        self.beds = beds
    def get_doors(self,):
        return self.doors
    def get_fans(self,):
        return self.lights
    def get_lights(self,):
        return self.lights
    def get_beds(self,):
        return self.beds
    
def get_room(one_room : room):
    return one_room.get_lights(),one_room.get_beds(),one_room.get_doors(),one_room.get_fans()

    