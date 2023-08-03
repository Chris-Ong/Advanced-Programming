def main():
    # Creating a dictionary containing film details
    film_details = {
        "Title": "Inception",
        "Director": "Christopher Nolan",
        "Release Year": 2010,
        "Genre": "Science Fiction",
        "Duration": 148,
        "IMDb Rating": 8.8
    }

    # Displaying the film details using a loop
    print("Film Details:")
    for key, value in film_details.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
