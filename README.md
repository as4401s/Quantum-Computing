# Quantum Computing

Runnable Python examples for the five-part WhiskerBrief course. Work out the prediction from the lesson, then run the matching example and compare. The five core examples use Python’s standard library. The final lesson also includes a local Qiskit lab.

| Lesson | Example | What to look for |
| --- | --- | --- |
| 1. What Is a Qubit? | [01_qubit.py](01_qubit.py) | Square the amplitudes to get 75% and 25%. Read the plus and minus states directly, then put a Hadamard before the readout. |
| 2. How Quantum Circuits Compute | [02_bell.py](02_bell.py) | Build a Bell state. Compare it with the shared-coin mixture in two bases and see what one reversed sign changes. |
| 3. How a Quantum Computer Is Built | [03_hardware.py](03_hardware.py) | Calculate a 5 GHz transition, pulse durations, and all four scores in the two-lamp annealing example. |
| 4. Why Quantum Computers Are So Hard to Build | [04_repetition.py](04_repetition.py) | Use two parity checks to correct a single flip and see what goes wrong when two bits flip. |
| 5. Program Your First Quantum Algorithm | [05_qiskit_lab.py](05_qiskit_lab.py) and [05_grover.py](05_grover.py) | Run the Hadamard and Bell circuits, check bit order, and build a search that amplifies one marked string. |

[WhiskerBrief on YouTube](https://www.youtube.com/channel/UCeu22q3sbIwPaPhLyiVY7AA). Direct course-video links will appear here when available.

## Run a lesson

From this directory:

```sh
python3 01_qubit.py
python3 02_bell.py
python3 03_hardware.py
python3 04_repetition.py
python3 05_grover.py --marked 10
```

A state vector stores **amplitudes** in basis order. The two-qubit examples use `00, 01, 10, 11`, with qubit zero on the right. Measurement probabilities are the squared magnitudes of the amplitudes. These small calculations model ideal gates and readouts. The thermal and repetition-code examples use the simplifying assumptions stated in the code.

## Run the final lesson’s Qiskit lab

Use a Python environment with Qiskit installed. The lesson was tested with Python 3.12.12 and Qiskit 2.6.1.

```sh
python -m pip install "qiskit==2.6.1"
python 05_qiskit_lab.py
python 05_grover.py --marked 10 --qiskit
python 05_grover.py --marked 01 --qiskit
```

The first lab prints the exact Hadamard probabilities, the sampled counts, a Bell circuit and its counts in two bases, and the output of a lone X on wire zero. With seed 7, the Hadamard run gave 517 zeros and 507 ones. The X-only run put the one on the right, giving `01` in every shot.

Each Grover command compares the flat 25% probabilities after marking with the output after diffusion. The ideal sampler returns the target in all 1,024 shots for these two-qubit examples. [Qiskit local sampler documentation](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler).
