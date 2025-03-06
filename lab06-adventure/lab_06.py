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
    first_room.description = "The central room. You can go all directions"
    first_room.north = 1
    first_room.south = 4
    first_room.east = 3
    first_room.west = 2
    room_list.append(first_room)

    # The second room
    room = Room()
    room.description = "The north room. Here you can only go back to the south"
    room.north = None
    room.south = 0
    room.east = None
    room.west = None
    room_list.append(room)

    # The third room
    room = Room()
    room.description = "The west room. Here you can only go back to the east"
    room.north = None
    room.south = None
    room.east = 0
    room.west = None
    room_list.append(room)

    # The fourth room
    room = Room()
    room.description = "The east room. Here you can only go back to the west"
    room.north = None
    room.south = None
    room.east = None
    room.west = 0
    room_list.append(room)

    # The fifth room
    room = Room()
    room.description = "The south room. Here you can only go back to the north"
    room.north = 0
    room.south = None
    room.east = None
    room.west = None
    room_list.append(room)

    current_room = 0
    done = False
    while not done:
        print(" ")
        print(room_list[current_room].description)
        decision = input("Where do you want to go: ")
        if decision.lower() == "n" or decision.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go there")
            else:
                current_room = next_room

        elif decision.lower() == "w" or decision.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go there")
            else:
                current_room= next_room

        elif decision.lower() == "e" or decision.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go there")
            else:
                current_room= next_room

        elif decision.lower() == "s" or decision.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go there")
            else:
                current_room= next_room

        elif decision.lower() == "q" or decision.lower() == "quit":
            print("You done it! You quit this stupid game!")
            done = True


main()


