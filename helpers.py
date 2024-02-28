from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator

def output_quantum_state(quantum_circuit):
    simulator = QasmSimulator()
    quantum_circuit.measure_all()
    cc = transpile(quantum_circuit, simulator)
    job = simulator.run(cc, shots=1)
    return job.result().get_counts(cc).keys()
