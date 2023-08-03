def main():
    cities = {
        "New York": {
            "country": "United States",
            "population": "8.4 million",
            "fact": "New York City is known as the 'Big Apple'."
        },
        "London": {
            "country": "United Kingdom",
            "population": "8.9 million",
            "fact": "London is home to the famous Big Ben clock tower."
        },
        "Tokyo": {
            "country": "Japan",
            "population": "13.9 million",
            "fact": "Tokyo is the largest metropolitan area in the world."
        }
    }

    # Print the name of each city and all of the information stored about it
    for city, city_info in cities.items():
        print(f"\nCity: {city}")
        print(f"Country: {city_info['country']}")
        print(f"Population: {city_info['population']}")
        print(f"Fact: {city_info['fact']}")

if __name__ == "__main__":
    main()
