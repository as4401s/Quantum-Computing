"""Small state-vector operations used by the course examples."""

from math import sqrt


def hadamard(state, wire):
    """Mix the amplitudes that differ only on the chosen wire."""
    step = 1 << wire
    normalizer = sqrt(2)
    updated = list(state)
    for zero_index in range(len(state)):
        if zero_index & step:
            continue
        one_index = zero_index | step
        a, b = state[zero_index], state[one_index]
        updated[zero_index] = (a + b) / normalizer
        updated[one_index] = (a - b) / normalizer
    return updated


def controlled_x(state, control, target):
    """Flip the target bit of each basis address with control set to one."""
    updated = [0j] * len(state)
    for address, amplitude in enumerate(state):
        output = address
        if address & (1 << control):
            output ^= 1 << target
        updated[output] = amplitude
    return updated


def probabilities(state):
    """Apply the Born rule to each amplitude in display order."""
    width = (len(state) - 1).bit_length()
    return {f"{i:0{width}b}": abs(a) ** 2 for i, a in enumerate(state)}


def show(distribution):
    return "  ".join(f"{bits}: {value:.1%}" for bits, value in distribution.items())
