import requests

__all__ = ("Person")

class Person:

    def __init__(self, imageUrl: str):
        self.__headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        self.__url = imageUrl

    def getImage(self):
        try:
            picBytes = requests.get(self.__url, headers = self.__headers)
            if (picBytes.status_code != 200):
                print("status code {0}".format(picBytes.status_code))
                return None
            return picBytes.content
        except Exception as e:
            print(e)
            return None
