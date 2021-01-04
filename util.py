import hashlib
import json
import config

def getHash(pic : bytes):
    h = hashlib.new("md5")
    h.update(pic)
    return h.hexdigest()

def load_settings():
    return config.settings

def load_person_filter():
    return config.persons_filter

def saveImage(pic : bytes, path : str = "", fileName : str = None):
    if fileName == None: fileName = getHash(pic)
    with open(path+fileName+".jpg",'wb') as file:
        file.write(pic)
        file.close()

def parseUrls(jsonStr : str):
    new = json.loads(jsonStr)['images']
    result = []
    for item in new:
        result.append(item["thumb_url"])
    return result