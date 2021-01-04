from api import Api
from person_data import PersonData
from person import Person
import util

filters = util.load_person_filter()
settings = util.load_settings()

pType = PersonData(filters["SEX"], filters["AGE"], filters["ETHNICITY"], 
     filters["EMOUTION"], filters["FACE"], filters["HAIR"])
origin = Api(settings["API_KEY"], pType)
for item in origin.getPeople(50):
    p = Person(item)
    util.saveImage(p.getImage(), settings["OUTPUT_PATH"])
