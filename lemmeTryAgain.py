import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)


qc.draw(output="mpl")

simulator = AerSimulator()

compiledCircuit = transpile(qc, simulator)

job = simulator.run(compiledCircuit, shots=1024)
result = job.result()

counts = result.get_counts()
print(counts)