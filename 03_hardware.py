"""Reproduce the energy, pulse and annealing calculations from Video 3."""

from itertools import product
from math import exp


# SI constants. One electronvolt has this many joules.
PLANCK = 6.62607015e-34
BOLTZMANN = 1.380649e-23
JOULES_PER_ELECTRONVOLT = 1.602176634e-19

carrier_hz = 5e9
gap_joules = PLANCK * carrier_hz
gap_micro_ev = gap_joules / JOULES_PER_ELECTRONVOLT * 1e6
temperature_k = 0.020
thermal_ratio = exp(-gap_joules / (BOLTZMANN * temperature_k))
rotation_turns_per_second = 10e6

print(f"Transition energy: {gap_micro_ev:.2f} μeV")
print(f"Ideal excited/ground population ratio at 20 mK: {thermal_ratio:.2g}")
print(f"Half-turn duration: {0.5 / rotation_turns_per_second * 1e9:g} ns")
print(f"Quarter-turn duration: {0.25 / rotation_turns_per_second * 1e9:g} ns")

print("\nEnergy penalty for choosing exactly one lamp:")
for x1, x2 in product((0, 1), repeat=2):
    energy = (x1 + x2 - 1) ** 2
    print(f"{x1}{x2}: {energy}")
