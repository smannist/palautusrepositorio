from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("\nTop scorers by selected country:\n")

    for player in players:
        print(player)

    print("\n")

if __name__ == "__main__":
    main()
