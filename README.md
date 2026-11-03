# Breaker Load Check

A Python tool that compares measured circuit currents (for example from a
clamp meter) against the breaker rating and reports which circuits are
overloaded.

## How it works

- Measured currents are stored in a list.
- A function splits the circuits into OK (current ≤ breaker rating) and
  OVERLOAD (current > breaker rating) and returns both lists.
- The report shows each circuit, the totals and the highest current measured.

## How to run

```
python breaker_load_check.py
```

## Example output

```
--- Breaker load check (breaker 16 A) ---
✅ Circuit #1: OK, 12.3 A
✅ Circuit #3: OK, 9.5 A
✅ Circuit #4: OK, 16.0 A
❌ Circuit #2: OVERLOAD, 17.8 A
❌ Circuit #5: OVERLOAD, 21.4 A
----------------------
✅ OK: 3
❌ OVERLOAD: 2
Highest current measured: 21.4 A

```

## Author

Michalis Malatras, Electrical engineer, learning Python for industrial automation.
