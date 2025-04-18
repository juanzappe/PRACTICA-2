rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]

estadisticas = {}

for i, ronda in enumerate(rounds, 1):
    print(f"\nRonda {i}")
    puntajes_ronda = {}
    for jugador, datos in ronda.items():
        kills = datos['kills']
        assists = datos['assists']
        deaths = 1 if datos['deaths'] else 0
        puntos = kills * 3 + assists * 1 - deaths * 1

        if jugador not in estadisticas:
            estadisticas[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'puntos': 0}

        estadisticas[jugador]['kills'] += kills
        estadisticas[jugador]['assists'] += assists
        estadisticas[jugador]['deaths'] += deaths
        estadisticas[jugador]['puntos'] += puntos
        puntajes_ronda[jugador] = puntos

    # Determinar MVP
    mvp = max(puntajes_ronda, key=puntajes_ronda.get)
    estadisticas[mvp]['mvp'] += 1
    print(f"MVP de la ronda: {mvp} con {puntajes_ronda[mvp]} puntos")

    print(f"{'Jugador':<10} {'Kills':<6} {'Asist.':<7} {'Muertes':<8} {'MVPs':<5} {'Puntos':<7}")
    for jugador, datos in estadisticas.items():
        print(f"{jugador:<10} {datos['kills']:<6} {datos['assists']:<7} {datos['deaths']:<8} {datos['mvp']:<5} {datos['puntos']:<7}")

# Ranking final
print("\n🏆 Ranking Final")
print(f"{'Jugador':<10} {'Kills':<6} {'Asist.':<7} {'Muertes':<8} {'MVPs':<5} {'Puntos':<7}")
for jugador, datos in sorted(estadisticas.items(), key=lambda x: x[1]['puntos'], reverse=True):
    print(f"{jugador:<10} {datos['kills']:<6} {datos['assists']:<7} {datos['deaths']:<8} {datos['mvp']:<5} {datos['puntos']:<7}")
