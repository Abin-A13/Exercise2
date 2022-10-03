from enum import Enum

class GenreType(Enum):
    FANTASY = "FANTASY"
    LITERARY = "LITERARY"
    MYSTREY  =  "MYSTREY"
    NON_FICTION = "NON_FICTION"
    SCIENCE_FICTION = "SCIENCE_FICTION"
    THRILLER = "THRILLER"
    EDUCTION = "Eduction"

    @classmethod
    def choices(genres):
        return tuple((item.name, item.value) for item in genres)


class UserType(Enum):
    ADMIN = "ADMIN"
    SELLER= "SELLER"
    BUYER  =  "BUYER"

    @classmethod
    def choices(user):
        return tuple((item.name, item.value) for item in user)