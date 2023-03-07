from jsonparsing import jsonpars


obj1 =  '''{"employees":
    {
        "name": "Alice",
        "role": "dev",
        "nbr": 1
      },
    "firm":
    {
      "name": "Charlie's Waffle Emporium",
      "location":  {
          "country": "INDIA",
          "state": "RJ"
      }
    }
}'''

key1 = "firm/location/state"

print(jsonpars(obj1, key1))


obj2 =  '''{
	"firstName": "John",
	"lastName": "Doe",
	"address": {
		"home": {
			"addressLines": {
				"1": "Flat 304",
				"2": "Crockemwell road"
			}
		}
	},
	"customerType": {
		"retail": {
			"channel": "Top100",
			"spending": "Top10"
		}
	}
}'''

key2 = "address/home/addressLines/2"

print(jsonpars(obj2, key2))  
