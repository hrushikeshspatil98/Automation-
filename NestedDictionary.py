#Nested Dictionaries
#A dictionary can also contain many dictionaries, this is called nested dictionaries.

nest_dict={
             "p1":{
                       "Name":"Akshay",
                       "Company":"NP AV"
                    },
             "p2":{
                       "Name":"Vrushi",
                       "Company":"Google"
                    },
             "p3":{
                       "Name":"Pooja",
                       "Company":"TCS"
                    },
             "p4":{
                       "Name":"Ankita",
                       "Company":"Wipro"
                    },
             "p5":{
                       "Name":"Sukanya",
                       "Company":"Apple"
                    },
             "p6":{
                       "Name":"Hrushi",
                       "Company":"TechM"
                    }
          }
print("nest_dict: ",nest_dict)

#To nest Six dictionaries that already exists as dictionaries
p1={ "Name":"Akshay","Company":"NP AV"}
p2={"Name":"Vrushi","Company":"Google" }
p3={ "Name":"Pooja","Company":"TCS" }
p4={ "Name":"Ankita", "Company":"Wipro" }
p5={ "Name":"Sukanya","Company":"Apple" }
p6={ "Name":"Hrushi","Company":"TechM" }

myP={
      "p1":p1,
      "p2":p2,
      "p3":p3,
      "p4":p4,
      "p5":p5,
      "p6":p6
     }

print("myP: ",myP)

"""Output:
nest_dict:  {'p1': {'Name': 'Akshay', 'Company': 'NP AV'}, 'p2': {'Name': 'Vrushi', 'Company': 'Google'}, 'p3': {'Name': 'Pooja', 'Company': 'TCS'}, 'p4': {'Name': 'Ankita', 'Company': 'Wipro'}, 'p5': {'Name': 'Sukanya', 'Company': 'Apple'}, 'p6': {'Name': 'Hrushi', 'Company': 'TechM'}}
myP:  {'p1': {'Name': 'Akshay', 'Company': 'NP AV'}, 'p2': {'Name': 'Vrushi', 'Company': 'Google'}, 'p3': {'Name': 'Pooja', 'Company': 'TCS'}, 'p4': {'Name': 'Ankita', 'Company': 'Wipro'}, 'p5': {'Name': 'Sukanya', 'Company': 'Apple'}, 'p6': {'Name': 'Hrushi', 'Company': 'TechM'}}
"""
