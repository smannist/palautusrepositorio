from statistics import Statistics, SortBy
from player_reader import PlayerReader

def main():
    stats = Statistics(PlayerReader())
    philadelphia_flyers_players = stats.team("PHI")

    print("\n")

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)
    print("\n")

    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)
    print("\n")

    print("Top point getters (without sort parameter):")
    for player in stats.top(10):
        print(player)
    print("\n")
    
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)
    print("\n")

    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)
    
    print("\n")

if __name__ == "__main__":
    main()
