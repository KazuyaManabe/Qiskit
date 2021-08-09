#%%
from qiskit import *
from qiskit.tools.visualization import circuit_drawer#36page

# %%31page
q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q,c)
qc.x(q[0])#36page
qc.x(q[0])#36page
qc.measure(q,c)

r = execute(qc, Aer.get_backend('qasm_simulator'), shots=100).result()
print(r.get_counts())
circuit_drawer(qc)
