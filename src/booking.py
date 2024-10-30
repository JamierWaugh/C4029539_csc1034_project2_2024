class Booking:

    def __init__(self, room, start, hours, title, contact):
        self.room = room
        self.start = start
        self.hours = hours
        self.title = title
        self.contact = contact

    def get_room(self):
        return self.room

    def get_start(self):
        return self.start

    def get_hours(self):
        return self.hours

    def get_title(self):
        return self.title

    def get_contact(self):
        return self.contact

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def overlaps_with(self, other):
        pass
