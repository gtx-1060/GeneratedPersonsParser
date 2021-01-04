import enum

__all__ = ("PersonData")

class PersonData:

    class Age(enum.Enum):
        UNDEFINED = -1
        INFANT = 0
        CHILD = 1
        YOUNG = 2
        ADULT = 3
        MIDDLE_AGED = 4

    class Sex(enum.Enum):
        UNDEFINED = -1
        MALE = 0
        FEMALE = 1

    class Ethnicity(enum.Enum):
        UNDEFINED = -1
        WHITE = 0
        BLACK = 1
        LATINO = 2
        ASIAN = 3

    class Face(enum.Enum):
        UNDEFINED = -1
        NEUTRAL = 0
        BEAUTIFIED = 1

    class Emoution(enum.Enum):
        UNDEFINED = -1
        NEUTRAL = 0
        JOY = 1

    class Hair(enum.Enum):
        UNDEFINED = -1
        BROWN = 0
        BLACK = 1
        BLOND = 2
        GRAY = 3


    def __init__(self, sex : int, age: int, ethnicity : int = Ethnicity.UNDEFINED, emoution : int = Emoution.UNDEFINED, face: int = Face.UNDEFINED, hair : int = Hair.UNDEFINED):
        self.__sex = sex
        self.__age = age
        self.__ethnicity = ethnicity
        self.__emoution = emoution
        self.__face = face
        self.__hair =hair
        #self.__url imgUrl

    def getQuerry(self):
        querry = ""
        if (self.__sex == PersonData.Sex.MALE): querry+="&gender=male"
        elif (self.__sex == PersonData.Sex.FEMALE): querry+="&gender=female"
        if (self.__age == PersonData.Age.ADULT): querry+="&age=adult"
        elif (self.__age == PersonData.Age.YOUNG): querry+="&age=young-adult"
        elif (self.__age == PersonData.Age.MIDDLE_AGED): querry+="&age=middle-aged"
        elif (self.__age == PersonData.Age.INFANT): querry+="&age=infant"
        elif (self.__age == PersonData.Age.CHILD): querry+="&age=child"
        if (self.__ethnicity == PersonData.Ethnicity.WHITE): querry+="&ethnicity=white"
        elif (self.__ethnicity == PersonData.Ethnicity.ASIAN): querry+="&ethnicity=asian"
        elif (self.__ethnicity == PersonData.Ethnicity.BLACK): querry+="&ethnicity=black"
        elif (self.__ethnicity == PersonData.Ethnicity.LATINO): querry+="&ethnicity=latin"
        if (self.__emoution == PersonData.Emoution.NEUTRAL): querry+="&emoution=neutral"
        elif (self.__emoution == PersonData.Emoution.JOY): querry+="&emoution=joy"
        if (self.__face == PersonData.Face.NEUTRAL): querry+="&face=natural"
        elif (self.__face == PersonData.Face.BEAUTIFIED): querry+="&face=beautified"
        if (self.__hair == PersonData.Hair.BLACK): querry+="&hair=black"
        elif (self.__hair == PersonData.Hair.BLOND): querry+="&hair=blond"
        elif (self.__hair == PersonData.Hair.BROWN): querry+="&hair=brown"
        elif (self.__hair == PersonData.Hair.GRAY): querry+="&hair=gray"
        return querry

    