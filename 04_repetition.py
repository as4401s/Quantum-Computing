"""Calculate the bit-flip syndrome and failure rate of the toy repetition code."""

from math import isclose


def syndrome(bits):
    """Compare the 1st/2nd and 2nd/3rd bits."""
    first, middle, last = bits
    return first ^ middle, middle ^ last


def correct_single_flip(bits):
    """Decode under the assumption that at most one bit flipped."""
    location = {(1, 0): 0, (1, 1): 1, (0, 1): 2}.get(syndrome(bits))
    corrected = list(bits)
    if location is not None:
        corrected[location] ^= 1
    return tuple(corrected)


for observed in ((0, 1, 0), (1, 0, 1)):
    print(f"Received {observed} → checks {syndrome(observed)} → {correct_single_flip(observed)}")

# Independent flips, with perfect syndrome checks and correction.
p = 0.10
failure = 3 * p**2 * (1 - p) + p**3
assert isclose(failure, 0.028)
print(f"Failure probability: {failure:.1%}")
