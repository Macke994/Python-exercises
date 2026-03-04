def city_country(city, country):
    """Return a city-country combo"""
    return f"{city.title()}, {country.title()}"

print(city_country("Tokyo", "Japan"))
print(city_country("Stockholm", "Sweden"))
print(city_country("London", "England"))
