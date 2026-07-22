# Extend Hello World to n qbit ghz state
# Step 1: Map problem to circuits
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt


def getQCForNQubitGHZState(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)

    return qc

n=100
qc = getQCForNQubitGHZState(n)

from qiskit.quantum_info import SparsePauliOp

operator_strings = ["Z" + "I"*i + "Z" + "I"*(n-2-i) for i in range(n-1)]
# print(operator_strings)
# print(len(operator_strings))

operators = [SparsePauliOp(operator_string) for operator_string in operator_strings]

# Step 2: Optimize problem for quantum execution

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

backend_name = "ibm_brisbane"
backend = QiskitRuntimeService().get_backend(backend_name)
pass_manager = generate_preset_pass_manager(optimization_level=1, backend=backend)