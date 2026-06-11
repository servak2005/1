# Riemann Nuclear Resonance Laboratory

**Emergent Riemann-Zero Modulation in Nuclear Mean-Field Dynamics**

Сильні чисельні докази (до **9.5σ**) того, що спектри ядерних рівнів і енергія зв’язку модулюються уявними частинами нетривіальних нулів дзета-функції Рімана.

---

## Основні результати

- Виявлено чіткий **резонанс** при **ε ≈ 0.45**
- Максимальна значущість: **9.47σ** (феноменологічна модель)
- Самосогласований Skyrme-HF: **7.84σ**
- Мінімум повної енергії зв’язку при тому ж ε (виграш до **-2.99 MeV** у ²³⁸U)
- Ефект систематичний для різних ядер (U-238, Dy-162, Pb-208, 90Zr, 48Ca)

---

## Структура проєкту

```bash
Riemann-Nuclear-Resonance/
├── main.py                 # Основний скрипт
├── dashboard.py            # Інтерактивний Streamlit-дашборд
├── config.py
├── core/                   # Основні модулі
│   ├── hamiltonian.py
│   ├── riemann_perturbation.py
│   ├── spectrum_analyzer.py
│   ├── fourier_analyzer.py
│   └── skyrme_riemann.py
├── papers/
│   └── main_paper.tex      # Повна стаття
└── results/                # Результати розрахунків
