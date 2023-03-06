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


# some JSON:
obj =  '''{"employees":
    {
        "name": "Alice",
        "role": "dev",
        "nbr": 1
      },
    "firm":
    {
      "name": "Charlie's Waffle Emporium",
      "location": "CA"
    }
}'''

key = "firm/name"

print(jsonpars(obj, key))   