class Booking:

    def __init__(self, room, start, hours, title, contact):
        self.__room = room #Double underscore privatises attributes
        self.__start = start
        self.__hours = hours
        self.__title = title
        self.__contact = contact

    def get_room(self):
        return self.__room

    def get_start(self):
        return self.__start

    def get_hours(self):
        return self.__hours

    def get_title(self):
        return self.__title

    def get_contact(self):
        return self.__contact

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
