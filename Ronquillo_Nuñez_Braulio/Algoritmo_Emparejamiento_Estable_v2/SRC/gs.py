from array import array
import argparse
import json
import time


def build_rankings(receivers_prefs: list[list[int]]) -> list[array]:
    n = len(receivers_prefs)
    ranking = [array("I", [0]) * n for _ in range(n)]

    for receiver, prefs in enumerate(receivers_prefs):
        if len(prefs) != n:
            raise ValueError("Cada receptor debe tener exactamente N preferencias.")

        row = ranking[receiver]
        for pos, proposer in enumerate(prefs):
            row[proposer] = pos

    return ranking


def gale_shapley_idx(
    proposers_prefs: list[list[int]],
    receivers_prefs: list[list[int]],
) -> list[int]:
    """
    Devuelve match_p de tamaño N, donde match_p[p] = r.

    La estructura next_choice garantiza que cada proponente propone
    a cada receptor a lo sumo una vez, evitando ciclos repetidos.
    """
    n = len(proposers_prefs)
    if len(receivers_prefs) != n:
        raise ValueError("Los dos conjuntos deben tener el mismo tamaño.")

    ranking = build_rankings(receivers_prefs)
    next_choice = array("I", [0]) * n
    receiver_partner = array("i", [-1]) * n

    # El orden de atención no afecta la estabilidad; una pila simple
    # reduce sobrecarga frente a mantener estructuras más pesadas.
    free = list(range(n - 1, -1, -1))

    while free:
        proposer = free.pop()
        choice_idx = next_choice[proposer]

        if choice_idx >= n:
            continue

        receiver = proposers_prefs[proposer][choice_idx]
        next_choice[proposer] = choice_idx + 1

        current = receiver_partner[receiver]
        if current == -1:
            receiver_partner[receiver] = proposer
            continue

        if ranking[receiver][proposer] < ranking[receiver][current]:
            receiver_partner[receiver] = proposer
            free.append(current)
        else:
            free.append(proposer)

    match_p = array("i", [-1]) * n
    for receiver, proposer in enumerate(receiver_partner):
        if proposer != -1:
            match_p[proposer] = receiver

    return match_p.tolist()


def bench_file(path: str, warmup: int = 0) -> None:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    instances = data["instances"]

    for _ in range(max(0, warmup)):
        for inst in instances:
            gale_shapley_idx(inst["proposers"], inst["receivers"])

    print(f"{'Instancia':>9} {'N':>6} {'Tiempo (s)':>12} {'Tiempo (ms)':>12}")
    print("-" * 55)

    for idx, inst in enumerate(instances):
        n = inst["N"]

        t0 = time.perf_counter()
        gale_shapley_idx(inst["proposers"], inst["receivers"])
        t1 = time.perf_counter()

        secs = t1 - t0
        print(f"{idx:>9} {n:>6} {secs:>12.6f} {secs * 1000:>12.3f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        nargs="?",
        default="instancias.json",
        help="Archivo JSON con instancias (default: instancias.json)",
    )
    parser.add_argument(
        "--warmup",
        type=int,
        default=0,
        help="Repeticiones de warmup (default: 0)",
    )
    args = parser.parse_args()

    bench_file(args.file, warmup=args.warmup)


if __name__ == "__main__":
    main()
