#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jpgm
"""

import random
import os
from typing import Dict, List, Tuple

class DatasetGenerator:
    def __init__(self, seed: int = 42):
        random.seed(seed)
        os.makedirs("datasets", exist_ok=True)
    
    def generate_names(self, n: int, prefix: str) -> List[str]:
        """Genera nombres de participantes"""
        return [f"{prefix}{i+1}" for i in range(n)]
    
    def generate_preferences(self, n: int, names: List[str]) -> Dict[str, List[str]]:
        """Genera preferencias aleatorias"""
        prefs = {}
        for name in names:
            pref_list = names.copy()
            random.shuffle(pref_list)
            prefs[name] = pref_list
        return prefs
    
    def generate_dataset(self, n: int, seed: int = None) -> Tuple[List[str], List[str], Dict, Dict]:
        """Genera un dataset completo"""
        if seed is not None:
            random.seed(seed)
        
        men_names = self.generate_names(n, 'h')
        women_names = self.generate_names(n, 'w')
        men_prefs = self.generate_preferences(n, women_names)
        women_prefs = self.generate_preferences(n, men_names)
        
        return men_names, women_names, men_prefs, women_prefs
    
    def save_to_txt(self, n: int, men_names: List[str], women_names: List[str],
                   men_prefs: Dict, women_prefs: Dict, mode: str = 'm',
                   filename: str = None) -> str:
        if filename is None:
            filename = f"dataset_n{n}_mode{mode}.txt"
        
        filepath = os.path.join("datasets", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # Línea 1: n
            f.write(f"{n}\n")
            # Línea 2: mode
            f.write(f"{mode}\n")
            
            # Men preferences
            for man in men_names:
                f.write(f"{man} {' '.join(men_prefs[man])}\n")
            
            # Women preferences
            for woman in women_names:
                f.write(f"{woman} {' '.join(women_prefs[woman])}\n")
        
        return filepath
    
    def generate_multiple_datasets(self, n_values: List[int]) -> Dict:
        """Genera múltiples datasets para diferentes n"""
        datasets = {}
        
        for n in n_values:
            men_names, women_names, men_prefs, women_prefs = self.generate_dataset(n)
            
            # Guardar para mode 'm'
            file_m = self.save_to_txt(n, men_names, women_names, men_prefs, women_prefs, 'm',
                                     f"dataset_n{n}_mode_m.txt")
            # Guardar para mode 'w'
            file_w = self.save_to_txt(n, men_names, women_names, men_prefs, women_prefs, 'w',
                                     f"dataset_n{n}_mode_w.txt")
            
            datasets[n] = {
                'men_names': men_names,
                'women_names': women_names,
                'men_prefs': men_prefs,
                'women_prefs': women_prefs,
                'file_m': file_m,
                'file_w': file_w
            }
        
        print(f" datasets generados en ./datasets/")
        return datasets

# Ejemplo de uso
if __name__ == "__main__":
    generator = DatasetGenerator(seed=42)
    n_values = [10, 50, 100, 200, 500]
    datasets = generator.generate_multiple_datasets(n_values)
