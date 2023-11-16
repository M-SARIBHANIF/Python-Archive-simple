Travel_log=[
    {
     "country":"France",
     "visits":12,
     "cities":["Paris","Litte","Dijon"],
    }
    ,
    {
     "country":"Germany",
     "visits":5,
     "cities":["Berlin","Hamburg","Stuttgard"],
    }
]
def add_new_country(country,no_visits,cities):
    new_entry = {}
    new_entry["country"] = country
    new_entry["visits"] = no_visits
    new_entry["cities"] = cities

    Travel_log.append(new_entry)

add_new_country("Russia",2,["Moscow","Saint Petersbu"])