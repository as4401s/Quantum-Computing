# Quantum Computing

Small, runnable Python examples for the five-part WhiskerBrief course. Work out the prediction from the lesson, then run the matching example and compare. All five examples run locally with Python 3 and its standard library.

| Lesson | Example | What to look for |
| --- | --- | --- |
| 1. What Is a Qubit? | [01_qubit.py](01_qubit.py) | Square the amplitudes to get 75% and 25%. Read the plus and minus states directly, then put a Hadamard before the readout. |
| 2. How Quantum Circuits Compute | [02_bell.py](02_bell.py) | Build a Bell state. Compare it with the shared-coin mixture in two bases and see what one reversed sign changes. |
| 3. How a Quantum Computer Is Built | [03_hardware.py](03_hardware.py) | Calculate a 5 GHz transition, pulse durations, and all four scores in the two-lamp annealing example. |
| 4. Why Quantum Computers Are So Hard to Build | [04_repetition.py](04_repetition.py) | Use two parity checks to correct a single flip and see what goes wrong when two bits flip. |
| 5. Program Your First Quantum Algorithm | [05_grover.py](05_grover.py) | Mark one string by phase, reflect the amplitudes about their mean, and check the final probabilities. |

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

To try the SDK version of the final example, install Qiskit in a Python environment of your choice. This example was tested with Qiskit 2.6.1. Then run `python3 05_grover.py --marked 01 --qiskit`. The circuit runs on a local state-vector sampler and prints its 1,024 shot counts. In the original example using `10`, the oracle alone leaves all four probabilities at 25%. The diffusion step raises `10` to 100% in the ideal calculation. [Qiskit’s local sampler documentation](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler).
