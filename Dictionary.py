#dictionary

candy = {                    #variabel som får datatypen dictionary 
    "name": "refresher",
    "type": "chewy",
    "color": "white",
    "Shape": ["round", "squareded"]
}

#"nyckel / key" : "värde"

candies = [] # lista 

candies.append(
        {
              "name": "sourSphere",
              "type": "sour",
              "color": "yellow"
        }
     )

candies = [
       {
            "name": "sourSphere",
            "type": "sour",
            "color": "yellow"
       },
        {
             "name": "nocco-tabelts",
              "type": "sweer",
              "color": "blue"
       }
]

print(candies[0])