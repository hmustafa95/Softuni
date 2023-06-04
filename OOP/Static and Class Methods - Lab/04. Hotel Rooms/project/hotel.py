from room import Room


class Hotel:
    def __init__(self, name: str, guests: int = 0):
        self.name = name
        self.guests = guests
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = next(filter(lambda r: r.number == room_number, self.rooms))

        Room.take_room(room, people)

    def free_room(self, room_number: int):
        room = next(filter(lambda r: r.number == room_number, self.rooms))

        Room.free_room(room)

    def status(self):
        self.guests = sum([x.guests for x in self.rooms])
        free_rooms = [x.number for x in self.rooms if x.is_taken == False]
        taken_rooms = [x.number for x in self.rooms if x.is_taken == True]
        return f"Hotel {self.name} has {self.guests} total guests\n" + \
               f"Free rooms: {', '.join(map(str, free_rooms))}\n" + \
               f"Taken rooms: {', '.join(map(str, taken_rooms))}"
