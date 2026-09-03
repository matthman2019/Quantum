from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
import numpy as np

desiredState = [1/np.sqrt(4)] * 4

qc = QuantumCircuit(2)
qc.initialize(desiredState, [0, 1])

qc.draw(output="mpl")
plt.show()

# Okay so here's my thought.
# We classically find all possible trees,
# find the desired superposition for their states,
# then start qaoa with that.

# I'm watching this video: https://www.youtube.com/watch?v=IhfptAC-2jA
# the number of trees possible is n^(n-2)... that would give our finding
# algorithm O(n^n) if we don't optimize it... thankfully
# there are algorithms developed to find all possible trees