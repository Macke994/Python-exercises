cities = [
{
    "City" : "Gällivare" ,
    "Country" : "Sweden" ,
    "Population" : "17214" ,
    "Fact" : "Hooja comes from this place."
},
{
    "City" : "Ayia napa" ,
    "Country" : "Cyprus" ,
    "Population" : "4716" ,
    "Fact" : "Is one of the most popular party places."
},
{
    "City" : "Tokyo" ,
    "Country" : "Japan" ,
    "Population" : "37 million" ,
    "Fact" : "Was once called Edo" 
}
]

for city in cities:
    print("\n---")
    for key, value in city.items():
        print(f"{key}: {value}")

