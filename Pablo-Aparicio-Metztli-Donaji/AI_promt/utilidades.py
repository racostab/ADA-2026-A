import re

def limpiar_codigo(codigo):
    if codigo is None:
        return ""
    codigo = codigo.strip()
    bloque = re.search(
        r"```(?:python)?\s*(.*?)```",
        codigo,
        re.DOTALL | re.IGNORECASE
    )
    if bloque:
        return bloque.group(1).strip()

    return codigo


def guardar_codigo(codigo, archivo):
    with open(
        archivo,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(codigo)


def revisar_orden(salida):
    try:
        nums = list(
            map(
                int,
                salida.strip().split(",")
            )
        )
        return nums == sorted(nums)
    except:
        return False