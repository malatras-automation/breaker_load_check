"""
Breaker load check: compares measured circuit currents
against the breaker rating and reports which circuits are overloaded.
"""
# Constants
BREAKER = 16   # A

def check_loads(measured, breaker):
    """Split measured currents into OK and overloaded circuits."""
    ok_log = []
    over_log = []
    circuit_no = 1
    for current in measured:
        if current <= breaker:
            msg = f"Circuit #{circuit_no}: OK, {current} A"
            ok_log.append(msg)
        else:
            msg = f"Circuit #{circuit_no}: OVERLOAD, {current} A"
            over_log.append(msg)
        circuit_no += 1
    return ok_log, over_log


# Main program
measured = [12.3, 17.8, 9.5, 16.0, 21.4]
ok_log, over_log = check_loads(measured, BREAKER)

print(f"--- Breaker load check (breaker {BREAKER} A) ---")
for msg in ok_log:
    print(f"✅ {msg}")
for msg in over_log:
    print(f"❌ {msg}")

print("----------------------")
print(f"✅ OK: {len(ok_log)}")
print(f"❌ OVERLOAD: {len(over_log)}")
print(f"Highest current measured: {max(measured):.1f} A")
