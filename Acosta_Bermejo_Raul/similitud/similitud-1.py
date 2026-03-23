#
#
#
import os
import subprocess
import itertools

def get_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for f in filenames:
            files.append(os.path.join(root, f))
    return files

def compare_files(file1, file2):
    try:
        result = subprocess.run(
            ["ssdeep", "-s", file1, file2],
            capture_output=True,
            text=True
        )
        output = result.stdout.strip().split("\n")
        
        # La salida relevante está en la segunda línea
        if len(output) >= 2:
            parts = output[1].split(",")
            similarity = parts[0].strip()
            return int(similarity)
    except Exception as e:
        print(f"Error comparando {file1} y {file2}: {e}")
    
    return 0

def main(directory):
    files = get_files(directory)
    print(f"Total archivos: {len(files)}\n")

    for file1, file2 in itertools.combinations(files, 2):
        similarity = compare_files(file1, file2)
        print(f"{file1} <-> {file2} = {similarity}%")

if __name__ == "__main__":
    #folder = "/ruta/a/tu/carpeta"  # Cambia esto
    folder = "./ada-sdeep"  # Cambia esto
    main(folder)

