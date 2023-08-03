import numpy as np

def main():
    # Create the data matrix based on the provided table
    data = np.array([[279, 200, 479],
                     [81, 156, 237],
                     [132, 160, 292]])

    # Calculate the totals for each row and column
    row_totals = np.sum(data, axis=1)
    column_totals = np.sum(data, axis=0)
    total_responses = np.sum(data)

    # Calculate the percentages of the different categories
    game_percent = (data[0, 0] / total_responses) * 100
    commercials_percent = (data[1, 0] / total_responses) * 100
    wont_watch_percent = (data[2, 0] / total_responses) * 100

    male_percent = (column_totals[0] / total_responses) * 100
    female_percent = (column_totals[1] / total_responses) * 100

    # Print the results
    print("Results based on the provided table:")
    print("---------------------------------------------------------")
    print(f"Percentage of males who watch the game: {game_percent:.2f}%")
    print(f"Percentage of males who watch the commercials: {commercials_percent:.2f}%")
    print(f"Percentage of males who won't watch: {wont_watch_percent:.2f}%")
    print(f"Percentage of females who watch the game: {(data[0, 1] / total_responses) * 100:.2f}%")
    print(f"Percentage of females who watch the commercials: {(data[1, 1] / total_responses) * 100:.2f}%")
    print(f"Percentage of females who won't watch: {(data[2, 1] / total_responses) * 100:.2f}%")
    print("---------------------------------------------------------")
    print(f"Percentage of total respondents who are male: {male_percent:.2f}%")
    print(f"Percentage of total respondents who are female: {female_percent:.2f}%")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    main()
