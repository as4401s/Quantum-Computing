"""Build a Bell pair and compare it with the shared-coin preparation."""

from quantum import controlled_x, hadamard, probabilities, show


def change_basis(state):
    return hadamard(hadamard(state, wire=0), wire=1)


zero_zero = [1, 0, 0, 0]
one_one = [0, 0, 0, 1]
bell = controlled_x(hadamard(zero_zero, wire=0), control=0, target=1)
minus_bell = [bell[0], 0, 0, -bell[3]]

# The coin picks one whole preparation per trial, so average probabilities.
for name, transform in (("direct", lambda state: state), ("H on both", change_basis)):
    heads = probabilities(transform(zero_zero))
    tails = probabilities(transform(one_one))
    mixture = {bits: (heads[bits] + tails[bits]) / 2 for bits in heads}
    print(f"Bell plus, {name}: {show(probabilities(transform(bell)))}")
    print(f"Shared coin, {name}: {show(mixture)}")
    print(f"Bell minus, {name}: {show(probabilities(transform(minus_bell)))}")
