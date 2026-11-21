"""Mark one of four strings and amplify it, with an optional Qiskit run."""

from argparse import ArgumentParser

from quantum import probabilities, show


def invert_about_mean(amplitudes):
    """Reflect each amplitude about the mean of this state vector."""
    average = sum(amplitudes) / len(amplitudes)
    return [2 * average - amplitude for amplitude in amplitudes]


def run_qiskit(marked):
    from qiskit import QuantumCircuit
    from qiskit.primitives import StatevectorSampler
    from qiskit.quantum_info import Statevector

    circuit = QuantumCircuit(2)
    circuit.h([0, 1])

    # Move the marked string to 11 before CZ, then restore its address.
    zero_wires = [wire for wire, bit in enumerate(reversed(marked)) if bit == "0"]
    for wire in zero_wires:
        circuit.x(wire)
    circuit.cz(0, 1)
    for wire in zero_wires:
        circuit.x(wire)
    oracle_state = Statevector.from_instruction(circuit)

    # This gate sequence implements inversion about the mean up to a common sign.
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])
    circuit.h([0, 1])
    amplified = Statevector.from_instruction(circuit)
    print("\nQiskit oracle probabilities:", show(oracle_state.probabilities_dict()))
    print("Qiskit amplified probabilities:", show(amplified.probabilities_dict()))

    measured = circuit.copy()
    measured.measure_all()
    sampler = StatevectorSampler(seed=7)
    result = sampler.run([measured], shots=1024).result()[0]
    print("Qiskit local shot counts:", result.data.meas.get_counts())


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--marked", choices=["00", "01", "10", "11"], default="10")
    parser.add_argument("--qiskit", action="store_true", help="Also run the Qiskit circuit")
    args = parser.parse_args()

    prepared = [0.5] * 4
    marked_state = prepared.copy()
    marked_state[int(args.marked, 2)] *= -1
    amplified = invert_about_mean(marked_state)
    print("Initial amplitudes:", prepared)
    print("After the oracle:", marked_state)
    print("Oracle probabilities:", show(probabilities(marked_state)))
    print("After diffusion:", amplified)
    print("Final probabilities:", show(probabilities(amplified)))
    if args.qiskit:
        run_qiskit(args.marked)


if __name__ == "__main__":
    main()
