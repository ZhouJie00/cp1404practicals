import csv


def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon(filename)
    champion_wins = count_champion_wins(champions)

    display_champion_wins(champion_wins)

#read wimbledon data
def read_wimbledon(filename):
    champions = []
    countries = set()

    try:
        with open(filename, "r", encoding="utf-8-sig", errors="ignore") as in_file:
            reader = csv.reader(in_file)
            next(reader)  # Skip the header row

            for row in reader:
                champion = row[0]
                country = row[1]

                champions.append(champion)
                countries.add(country)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        champions, countries = [], set()

    except Exception as e:
        print(f"An error occurred: {e}")
        champions, countries = [], set()

    return champions, countries

#count champion wins
def count_champion_wins(champions):
    champion_wins = {}

    for champion in champions:
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1

    return champion_wins

#display champion wins
def display_champion_wins(champion_wins):
    print("Wimbledon Champions:")

    for champion, wins in champion_wins.items():
        print(f"{champion}: {wins} wins")



if __name__ == "__main__":
    main()
