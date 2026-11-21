"""Run the four local Qiskit examples from the final course lesson."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector


def sampled_counts(circuit: QuantumCircuit, shots: int = 1024) -> dict[str, int]:
    measured = circuit.copy()
    measured.measure_all()
    sampler = StatevectorSampler(seed=7)
    job = sampler.run([measured], shots=shots)
    result = job.result()[0]
    return result.data.meas.get_counts()


def main() -> None:
    single = QuantumCircuit(1)
    single.h(0)
    exact = Statevector.from_instruction(single).probabilities()
    print("Hadamard exact probabilities:", exact.round(3).tolist())
    print("Hadamard counts:", sampled_counts(single))

    bell = QuantumCircuit(2)
    bell.h(0)
    bell.cx(0, 1)
    print("\nBell circuit:\n", bell.draw(output="text"), sep="")
    print("Bell direct counts:", sampled_counts(bell))

    changed_basis = bell.copy()
    changed_basis.h(0)
    changed_basis.h(1)
    print("Bell with H on both wires:", sampled_counts(changed_basis))

    bit_order = QuantumCircuit(2)
    bit_order.x(0)
    print("X on q0 alone:", sampled_counts(bit_order))


if __name__ == "__main__":
    main()
