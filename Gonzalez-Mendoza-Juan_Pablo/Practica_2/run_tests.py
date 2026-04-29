import ollama
import json
import time
import os
import importlib.util
import sys
from datetime import datetime

client = ollama.Client(host='http://localhost:11434')

def load_cocktail_sort(path="cocktail_sort.py"):
    spec = importlib.util.spec_from_file_location("cocktail_sort", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def generate_test_cases():
    prompt = """
Genera casos de prueba para el algoritmo Cocktail Shaker Sort en formato JSON.
Devuelve SOLO un array JSON válido con exactamente 8 casos de prueba.
Cada caso debe tener:
- "name": nombre descriptivo del caso
- "input": lista de números a ordenar
- "expected": la lista correctamente ordenada

Incluye estos tipos de casos:
1. Lista vacía
2. Un solo elemento
3. Lista ya ordenada (5 elementos)
4. Lista en orden inverso (5 elementos)
5. Lista con duplicados
6. Lista con números negativos
7. Lista aleatoria pequeña (8 elementos)
8. Lista aleatoria grande (15 elementos)

Responde ÚNICAMENTE con el JSON, sin texto ni bloques markdown.
"""
    print("Generando casos de prueba con Ollama...")
    response = client.generate(
        model='mistral:latest',
        prompt=prompt,
        options={'temperature': 0.1}
    )

    raw = response.response.strip()
    if raw.startswith("```"):
        lines = raw.split("\n")
        raw = "\n".join(lines[1:-1]) if lines[-1] == "```" else "\n".join(lines[1:])

    return json.loads(raw)

def run_tests(module, test_cases):
    results = []
    for tc in test_cases:
        name     = tc["name"]
        inp      = tc["input"]
        expected = tc["expected"]

        arr_copy = inp.copy()
        start    = time.perf_counter()

        try:
            if hasattr(module, 'cocktail_shaker_sort_verbose'):
                result = module.cocktail_shaker_sort_verbose(arr_copy)
                sorted_arr  = result.get('sorted', arr_copy)
                comparisons = result.get('comparisons', 'N/A')
                swaps       = result.get('swaps', 'N/A')
                passes      = result.get('passes', 'N/A')
            else:
                sorted_arr  = module.cocktail_shaker_sort(arr_copy)
                comparisons = swaps = passes = 'N/A'

            elapsed = (time.perf_counter() - start) * 1000
            passed  = sorted_arr == expected

            results.append({
                "name":        name,
                "input":       inp,
                "expected":    expected,
                "got":         sorted_arr,
                "passed":      passed,
                "time_ms":     round(elapsed, 4),
                "comparisons": comparisons,
                "swaps":       swaps,
                "passes":      passes,
                "error":       None
            })

        except Exception as e:
            results.append({
                "name":        name,
                "input":       inp,
                "expected":    expected,
                "got":         None,
                "passed":      False,
                "time_ms":     0,
                "comparisons": 'N/A',
                "swaps":       'N/A',
                "passes":      'N/A',
                "error":       str(e)
            })

    return results

def save_results(results, path="test_results.json"):
    total  = len(results)
    passed = sum(1 for r in results if r["passed"])

    output = {
        "timestamp":  datetime.now().isoformat(),
        "model":      "mistral:latest",
        "summary": {
            "total":   total,
            "passed":  passed,
            "failed":  total - passed,
            "success_rate": f"{(passed/total*100):.1f}%"
        },
        "results": results
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return output

def print_summary(output):
    s = output["summary"]
    r = output["results"]

    print("\n" + "=" * 60)
    print(f"RESULTADOS — {output['timestamp']}")
    print("=" * 60)
    print(f"  Total:   {s['total']}")
    print(f"  Passed:  {s['passed']} ")
    print(f"  Failed:  {s['failed']} ")
    print(f"  Tasa:    {s['success_rate']}")
    print("=" * 60)

    for tc in r:
        status = "PASS" if tc["passed"] else "FAIL"
        print(f"\n{status}  {tc['name']}")
        print(f"  Input:    {tc['input']}")
        if not tc["passed"]:
            print(f"  Expected: {tc['expected']}")
            print(f"  Got:      {tc['got']}")
        if tc["error"]:
            print(f"  Error:    {tc['error']}")
        if tc["comparisons"] != 'N/A':
            print(f"  Stats:    comparaciones={tc['comparisons']}  "
                  f"swaps={tc['swaps']}  pasadas={tc['passes']}")
        print(f"  Tiempo:   {tc['time_ms']} ms")

    print("\n" + "=" * 60)
    print(f"Resultados guardados en: {os.path.abspath('test_results.json')}")


if __name__ == "__main__":
    if not os.path.exists("cocktail_sort.py"):
        print("ERROR: No se encontró cocktail_sort.py")
        print("Ejecuta primero: python generate_cocktail_sort.py")
        sys.exit(1)

    module     = load_cocktail_sort()
    test_cases = generate_test_cases()
    results    = run_tests(module, test_cases)
    output     = save_results(results)
    print_summary(output)
