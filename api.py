from person_data import PersonData
import requests
import util

__all__ = ("Api")

class Api:

    __BASE_URL = "https://api.generated.photos/api/frontend/v1/images"

    def __init__(self, apiKey : str, personType : PersonData):
        self.__headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Authorization" : "API-Key {0}".format(apiKey)
        }
        self.personData = personType
        self.__apiKey = apiKey
        

    def getPeople(self, limit : int = 100):
        persons = []
        querry = self.personData.getQuerry()
        step = 0
        for i in range(101, 1, -1):
            if limit % i == 0:
                step = i
                break
        #print(f"step - {step}")
        url = f"{self.__BASE_URL}?order_by=latest&page=1&per_page={step}{querry}"
        for i in range(step, limit+1, step):
            print(url)
            try:
                resp = requests.get(url, headers = self.__headers)
                if resp.status_code != 200:
                    print("status code {0}".format(resp.status_code))
                    #print(resp.content)
                    return persons
                persons.extend(util.parseUrls(resp.content))
            except Exception as e:
                print(e)
                return persons
            url = f"{self.__BASE_URL}?order_by=latest&page={(i+step)//step}&per_page={step}{querry}"
        return persons