def team_lineup(*args):
    players_by_country = {}
    for player, country in args:
        if country not in players_by_country:
            players_by_country[country] = []
        players_by_country[country].append(player)
    sorted_players = dict(sorted(players_by_country.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''
    for c, ps in sorted_players.items():
        result += f"{c}:\n"
        for p in ps:
            result+= (f"  -{p}\n")
    return result

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


