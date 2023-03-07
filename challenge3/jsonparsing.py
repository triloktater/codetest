import json

def jsonpars(obj, key):
    y = json.loads(obj)
    temp = key.split("/")
    try:
        for i in temp:
                y = y[i]
    except:
        return    
    return y
