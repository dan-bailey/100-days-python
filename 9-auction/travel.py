# travel log dictionary/list mix example

travel_log = []

def add_new_country(country, visits, citylist):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = citylist
    travel_log.append(new_country)

add_new_country("Germany", 3, ["Berlin", "Aachen", "Hamburg", "Munich"])
add_new_country("France", 2, ["Paris", "Lyon", "Nice"])
add_new_country("Spain", 1, ["Barcelona"])
add_new_country("United States", 20, ["Los Angeles", "Las Vegas", "New York", "Seattle", "Minneapolis", "Philadelphia", "Boston", "Miami", "Fort Lauderdale", "Austin", "Houston", "Atlanta", "Raleigh-Durham", "Washington, DC"])
print(travel_log)