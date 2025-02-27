import arcade
class Room:
    def __int__(self):
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():
    room_list = []
    # The first room
    first_room = Room()
    first_room.description = "La primera sala"
    first_room.north = 1
    first_room.south = 5
    first_room.east = 4
    first_room.west = 3
    room_list.append(first_room)

main()


