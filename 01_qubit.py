"""Convert amplitudes to probabilities and compare two measurement bases."""

from math import sqrt

from quantum import hadamard, probabilities, show


state = [sqrt(3) / 2, 0.5j]
print("Born rule for √3/2 and i/2:", show(probabilities(state)))

plus = hadamard([1, 0], wire=0)
minus = [plus[0], -plus[1]]
for name, prepared in (("plus", plus), ("minus", minus)):
    print(f"{name}, direct: {show(probabilities(prepared))}")
    print(f"{name}, H then read: {show(probabilities(hadamard(prepared, wire=0)))}")
