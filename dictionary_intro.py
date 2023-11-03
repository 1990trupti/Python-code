"""
Dictionary:
    *internally implemented as hash table and uses closed hashing a.k.a open addressing
    * Unlike other data types Dictionary holds a pair(KEY, VALUE) as a single element.
    *Dictionary is mutable
    *Key must be immutable(String, Number, Tuple) and no duplicates allowed.
    *Value can be of any type(Mutable or immutable) and duplicated are allowed.
    *elements are accessed using keys.
    *can be nested
    *insertion deletion is efficient and searching is not efficient compared to insertion/deletion.

Dict_methods:
copy(), clear(), fromkeys(), get(), items(), keys(), values(), pop(),
popitem(), setdefault(),update()

how to use/create:
    * new_dict = {}
    * new_dict = newDict = {key1:value1, key2:value2,.....,key n: value n}
    * newDict = dict() / This will create a blank dictionary.
    * newDict = dict({key1:value1,key2:value2,...,key n:value n}

e.g:
data = {'action':'list','state':'Finished','show_last':1,'target':ip}

my_preference = dict({'fruit':'pomegrante','bike':'honda','cuisine':'chinese'
                       'weather':'winter'})
"""
data = {}
#data = {} or data = dict()
data = {"fruit":"watermelon", "season":"summer",
        "weather":40}

# person = ["rakesh","shah", 45, 56, 5.7, 5.4, "black"]

person = {"name":"Rakesh", "Lastname":"Shah",
          "age":45, "weight":"56","height":5.7,
          "BMI":5.7,"fav_color":"black"}
print(person)

#____________________________
#pop method
person.pop("fav_color")
print(person)

#______________________________
#update method
print(person.update({"fav_color":"orange"}))
print(person)

print(person["weight"])
print(person["fav_color"])
print(person["Lastname"])


#_____________________________

indian_team = {
                "captain":"Rohit Sharma",
                "vc":"KL Rahul",
                "batsmen":["virat Kohli", "surya", "pujara"],
                "all_rounder":["axar patel", "ravindra jadeja"],
                "bowlers":{
                   "fast":["shami","siraj","bumrah"],
                   "spin":["kuldeep","cahal"]
                          },
                "coach":"rahul dravid"
             }


print(indian_team["captain"])
print(indian_team["vc"])
print(indian_team["batsmen"])
print(indian_team["all_rounder"])
print(indian_team["bowlers"])
print(indian_team["coach"])

weather_data = {
    "request":{
        "type":"City",
        "query":"Pune, India",
        "language":"en",
        "unit":"f"
    },
    "location":{
        "name":"Pune",
        "country":"India",
        "region":"Maharashtra",
        "lat":"18.533",
        "lon":"73.867",
        "timezone_id":"Asia/Kolkata",
        "localtime":"2023-02-28 08:52",
        "localtime_epoch": 1677574320,
        "utc_offset":"5.50"
    },
    "current":{
        "observation_time": "03:22 AM",
        "temperature": 77,
        "weather_code":113,
        "weather_icons":["http://"],
        "weather_descriptions":["sunny"],
        "wind_speed":2,
        "wind_degree":201,
        "wind_dir": "SSW",
        "pressure": 1017,
        "precip": 0,
        "humidity":19,
        "cloudcover": 4,
        "feelslike":75,
        "uv_index": 7,
        "visibility": 6,
        "is_day":"yes"
    }
}

 #__________________________________
 #keys - return a list of all the keys
 # syntax - dict_name.keys()

# print(indian_team.keys())
print(weather_data.keys())

#________________________________________
#values - returns a list of all the values

# print(indian_team.values())

#items- returns the list of items

print(indian_team.items())

#______________________________________________________
#reading data from dictionary
#get() - return the values of the given key if present,
#if key not present, returns the default value if specified,
# else will return NONE.
# syntax - .get("keyname", "optional_default_value")

# print(indian_team["captain"])
# print(indian_team.get("captain"))
#
# # print(indian_team["bat"])   #give error
# print(indian_team.get("bet"))   #will not give error and print none

#_________________________________________________
#update - upadte the dictionary with given dictionary
#syntax: dict_name.update(<new_dict>)

# new_team_members = {"physio":"Rajesh Jha","12th":"Iyer","cheerleader":["1","2","3","4"],"vc":"pant"}
# print(indian_team)
# indian_team.update(new_team_members)
# print(indian_team)


#__________________________________
#setdefault- returns the value of the key if present
#if not present returns the default value
#which is passed and updates the dictionary with new key and given value

# print(indian_team.setdefault("vc"))
# print(indian_team.setdefault("pysio","rajesh jha"))
# print(indian_team)

#______________________________________
#fromkeys - creates a dictionary from a sequence type

seasons =  ["summer","autum", "rainy","winter"]

# weather = dict.fromkeys(seasons, "sunny")
# print(weather)
# weather["winter"] ="cold"
# weather["rainy"] ="cloudy"
# weather["autum"] ="dry"
#
# print(weather)
# weather["winter"] ="cold"
# weather["winter"] ="cold"

#_______________________________________
# pop and popitem
#popitem - removes an item from dict
#pop - removes the given key value pair

# indian_team.popitem()
# print(indian_team)
#
# vice_captain = indian_team.pop("vc")
# print(vice_captain)
# print(indian_team)

#____________________________
# copy - return a copy of the dictionary
# print(indian_team)
# indian_team.copy()
# print(indian_team)


#clear - remove all items from dictionary
print(indian_team)
indian_team.clear()
print(indian_team)
