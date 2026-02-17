#Agrego una prueba
def greet(name: str) -> str:
    return f"Hola, {name}!"

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser no negativo")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    import sys
    if len(sys.argv) < 3:
        print("Uso: python prueba.py [factorial|prime|greet] argumento")
        return
    cmd = sys.argv[1].lower()
    arg = sys.argv[2]
    try:
        if cmd == "factorial":
            n = int(arg)
            print(factorial(n))
        elif cmd == "prime":
            n = int(arg)
            print(is_prime(n))
        elif cmd == "greet":
            print(greet(arg))
        else:
            print("Comando desconocido.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

