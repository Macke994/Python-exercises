def describe_city(city, country="Sweden"):
    """Display information about a city in a country"""
    print(f"\n{city} is in {country}.")

describe_city("Stockholm")
describe_city("Luleå")
describe_city("London", country="England")