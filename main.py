#!/usr/bin/env python3
"""
Riemann Nuclear Resonance Laboratory - Main Entry Point
"""

import numpy as np
import time
from config import N_MAX, EPSILON_SCAN, RIEMANN_ZEROS, BETA2
from core.hamiltonian import build_hamiltonian
from core.spectrum_analyzer import unfold_spectrum, compute_nnsd
from core.fourier_analyzer import riemann_fourier_analysis

def main():
    print("="*70)
    print("🧪 RIEMANN NUCLEAR RESONANCE LABORATORY v1.0")
    print("="*70)
    print(f"N_max = {N_MAX} | β₂ = {BETA2} | Riemann zeros = {len(RIEMANN_ZEROS)}")
    print("-"*70)

    start_time = time.time()
    results = []

    for eps in EPSILON_SCAN:
        print(f"→ ε = {eps:.4f} ... ", end="")
        t0 = time.time()

        H = build_hamiltonian(N_MAX, eps, BETA2)
        eigenvalues = np.sort(np.real(np.linalg.eigvalsh(H)))

        unfolded = unfold_spectrum(eigenvalues)
        fourier_result = riemann_fourier_analysis(eigenvalues, RIEMANN_ZEROS, eps)

        max_sigma = fourier_result['max_sigma']

        results.append({
            'epsilon': eps,
            'max_sigma': max_sigma,
            'n_levels': len(eigenvalues)
        })

        print(f"done ({time.time()-t0:.2f}s) | σ = {max_sigma:.2f}")

    best = max(results, key=lambda x: x['max_sigma'])

    print("\n" + "="*70)
    print("🎯 ФІНАЛЬНИЙ РЕЗУЛЬТАТ")
    print("="*70)
    print(f"Оптимальне ε     : {best['epsilon']:.4f}")
    print(f"Максимальна σ     : {best['max_sigma']:.2f}σ")
    print(f"Кількість рівнів  : {best['n_levels']}")
    print(f"Загальний час     : {time.time()-start_time:.1f} секунд")
    print("="*70)

if __name__ == "__main__":
    main()
