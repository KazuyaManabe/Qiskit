#%%
from qiskit import *

# %%26page
q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q,c)
qc.measure(q,c)

r = execute(qc, Aer.get_backend('qasm_simulator'), shots=100).result()
print(r.get_counts())

#%%
