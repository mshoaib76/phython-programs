dict={ "name ":"shoaib baloch",
       "marks ":93,
       "subjects ":["math","OOp","Discreate structure","DLD","programinh"],
         "CGPA":3.5
         }
#dictory is mutable , but dont copy allow in dict
dict["marks"]=95    # slicing in dictary is possible
dict["location"]="layyah"       #add key and value in dict form
print(dict)
nesteddict={
    "name":"shazaib khan",
    "class ":3,
     "Another Male":{      #nested dictory <------
        "location":"layyah",
        "cast ":"Baloch",
        "education":"4thclass"
     }
}
print(nesteddict["Another Male"]["location"])   #we can print nesteddict and in nesteddict of current value
print(nesteddict.keys())  # print to keys of nesteddict
print(len(dict))            #length of dict
print(len(nesteddict))
#dictory print only keys mean first value not assign value
print(list(dict.keys()))  #dictory can be print in list form
#dictory can print olny values mean seond assign value not key
print(dict.values())
#dictory can be print in touple form
print(nesteddict.items())
