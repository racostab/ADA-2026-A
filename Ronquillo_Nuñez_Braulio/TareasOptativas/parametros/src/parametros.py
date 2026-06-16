# Author: Ronquillo Nunez Braulio
# Optional task: parameters and call stack

import sys


def format_frame(frame):
    params = [f"{name}={value}" for name, value in frame["params"]]
    if params:
        return f'{frame["name"]}(' + ", ".join(params) + ")"
    return f'{frame["name"]}()'


def simulate(max_size, operations):
    stack = []
    log = []

    for operation in operations:
        parts = operation.split()

        if not parts:
            continue

        command = parts[0]

        if command == "CALL":
            name = parts[1]
            param_count = int(parts[2])

            if len(stack) == max_size:
                log.append(f"overflow en {name}")
                continue

            params = []
            pos = 3
            for _ in range(param_count):
                params.append((parts[pos], parts[pos + 1]))
                pos += 2

            stack.append({"name": name, "params": params})
            log.append(f"call {name}: profundidad {len(stack)}")

        elif command == "SET":
            depth = int(parts[1])
            name = parts[2]
            value = parts[3]
            index = len(stack) - 1 - depth

            if index < 0 or index >= len(stack):
                log.append("set invalido")
                continue

            params = stack[index]["params"]
            changed = False
            for i, (param_name, _) in enumerate(params):
                if param_name == name:
                    params[i] = (param_name, value)
                    changed = True
                    break

            if changed:
                log.append(f"set {name}={value} en {stack[index]['name']}")
            else:
                log.append(f"parametro {name} no encontrado")

        elif command == "RETURN":
            if stack:
                frame = stack.pop()
                log.append(f"return {frame['name']}: profundidad {len(stack)}")
            else:
                log.append("return con pila vacia")

    return log, stack


def solve():
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]

    if len(lines) < 2:
        return

    max_size = int(lines[0])
    operation_count = int(lines[1])
    operations = lines[2 : 2 + operation_count]

    log, stack = simulate(max_size, operations)

    print("eventos:")
    for item in log:
        print(item)

    print("pila final:")
    if not stack:
        print("vacia")
    else:
        for depth, frame in enumerate(reversed(stack)):
            print(f"{depth}: {format_frame(frame)}")


if __name__ == "__main__":
    solve()
