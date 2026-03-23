def gale_shapley(proposers_preferences, receivers_preferences):
    # Inicialización
    free = list(proposers_preferences.keys())
    engaged = {}
    proposals_count = {p: 0 for p in proposers_preferences}

    # Ranking para comparar preferencias rápido
    ranking = {
        r: {person: i for i, person in enumerate(prefs)}
        for r, prefs in receivers_preferences.items()
    }

    while free:
        p = free[0]

        # siguiente persona a quien propone
        r = proposers_preferences[p][proposals_count[p]]
        proposals_count[p] += 1

        if r not in engaged:
            engaged[r] = p
            free.pop(0)
        else:
            current = engaged[r]

            # comparar preferencias del receptor
            if ranking[r][p] < ranking[r][current]:
                engaged[r] = p
                free.pop(0)
                free.append(current)
            else:
                # sigue libre y propondrá otra vez
                free.append(free.pop(0))

    return engaged


# -------------------------
# Lectura de entrada
# -------------------------
first_line = input().split()
N = int(first_line[0])
first = first_line[1]

men_preferences = {}
women_preferences = {}

# preferencias hombres
for _ in range(N):
    data = input().split()
    men_preferences[data[0]] = data[1:]

# preferencias mujeres
for _ in range(N):
    data = input().split()
    women_preferences[data[0]] = data[1:]


# -------------------------
# Ejecutar algoritmo
# -------------------------
if first == 'm':  # hombres proponen
    engaged = gale_shapley(men_preferences, women_preferences)

    # convertir a hombre -> mujer
    matches = {man: woman for woman, man in engaged.items()}

    # salida ordenada por hombres
    for man in sorted(men_preferences.keys()):
        print(man, matches[man])

else:  # mujeres proponen
    engaged = gale_shapley(women_preferences, men_preferences)

    # convertir a mujer -> hombre
    matches = {woman: man for man, woman in engaged.items()}

    # salida ordenada por mujeres (quien propone)
    for woman in sorted(women_preferences.keys()):
        print(woman, matches[woman])