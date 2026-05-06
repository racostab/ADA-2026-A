import time
# import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    # 15 test cases
    test_cases = [
        [5, 3, 8, 1, 6, 4, 7, 2],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2] * 20,  # list of 2s
        [1, 3, 2, 5, 4],
        [7, 1, 9, 3, 5, 8, 2, 6, 4],
        [10, 20, 5, 15, 30, 25, 35],
        [100, 50, 150, 25, 75, 125, 175],
        [4, 2, 6, 1, 3, 5, 7],
        [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15],
        [99, 88, 77, 66, 55, 44, 33, 22, 11],
        [1, 1, 2, 2, 3, 3],
        [5, 5, 5, 5, 5]
    ]
    
    times = []
    sizes = []
    with open('Downloads\\resultados.txt', 'w') as f:
        for i, numbers in enumerate(test_cases, 1):
            arr = numbers.copy()
            start = time.time()
            heapSort(arr)
            end = time.time()
            elapsed = end - start
            times.append(elapsed)
            sizes.append(len(numbers))
            result = ' '.join(map(str, arr))
            line = f"Test {i}: {result}\n"
            print(line.strip())
            f.write(line)
    
    # Plot
    # plt.plot(sizes, times, marker='o')
    # plt.xlabel('Tamaño de la lista')
    # plt.ylabel('Tiempo (segundos)')
    # plt.title('Tiempo de ejecución de Heapsort')
    # plt.grid(True)
    # plt.savefig('C:\\Users\\Lupita_Guerra\\Downloads\\Figure_1.png')
    # # plt.show()  # Commented out for terminal execution
    pass