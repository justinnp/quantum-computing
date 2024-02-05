from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator
from question1 import q1a, q1b, q1c

"""
Qiskit quantum circuits can be run on either real quantum computers, or simulators.
For example, the QasmSimulator:
    simulator = QasmSimulator()

In this question, you need to follow the instructions and run the circuits you have created in question 1,
and return the Counts (https://docs.quantum.ibm.com/api/qiskit/qiskit.result.Counts) of the simulation.

For measuring the qubits you can use measure_all() or measure(qreg,creg) methods.
    https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit#measure
    https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.QuantumCircuit#measure_all

An example has been provided to you for reference in q2_example.

"""

def q2_example():
    """
    An example of how to measure you quantum circuit.
    Args:
        None
    Return:
        qiskit.result.Counts
    """

    simulator = QasmSimulator()

    qr = QuantumRegister(1, 'q')
    qc = QuantumCircuit(qr)
    qc.h(0)

    qc.measure_all()
    cc = transpile(qc, simulator)

    # Execute the circuit on the qasm simulator
    job = simulator.run(cc, shots=1000)

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(cc)

    return counts


def quantum_simulator(circuit):
    """
    Transpiles and runs the Qasm simulator in 65536 shots
    Args: 
        circuit: qiskit.QuantumCircuit
    Return:
        counts: qiskit.result.count
    """
    simulator = QasmSimulator()
    cc = transpile(circuit, simulator)
    # Execute the circuit on the qasm simulator
    job = simulator.run(cc, shots=65536)
    # Grab results from the job
    result = job.result()
    counts = result.get_counts(cc)
    return counts

def q2a():
    """
    Instructions:
        - Use the quantum circuit defined in q1a
        - Measure all qubits using measure_all()
        - Compiled the circuit using QasmSimulator()
        - Run the compiled circuit on the simulator with 65536 shots
        - Return the qiskit.result.Counts
    Args: 
        None
    Return:
        counts: qiskit.result.Counts
    """
    
    counts = None
    ############################################################################
    # Student code begin
    ############################################################################
    q2a_circuit = q1a()
    q2a_circuit.measure_all()
    counts = quantum_simulator(q2a_circuit)

    ############################################################################
    # Student code end
    ############################################################################

    return counts


def q2b():
    """
    Instructions:
        - Use the quantum circuit defined in q1b
        - Measure the first three qubits using measure(qregs, cregs)
        - Compiled the circuit using QasmSimulator()
        - Run the compiled circuit on the simulator with 65536 shots
        - Return the qiskit.result.Counts
    Args: 
        None
    Return:
        counts: qiskit.result.Counts
    """
    
    counts = None
    ############################################################################
    # Student code begin
    ############################################################################

    q2b_circuit = q2b()
    q2b_circuit.measure_all()
    counts = quantum_simulator(q2b_circuit)

    ############################################################################
    # Student code end
    ############################################################################

    return counts


def q2c():
    """
    Instructions:
        - Use the quantum circuit defined in q1c
        - Measure the last three qubits using measure(qregs, cregs)
        - Compiled the circuit using QasmSimulator()
        - Run the compiled circuit on the simulator with 65536 shots
        - Return the qiskit.result.Counts
    Args: 
        None
    Return:
        counts: qiskit.result.Counts
    """
    
    counts = None
    ############################################################################
    # Student code begin
    ############################################################################

    q2c_circuit = q2c()
    q2c_circuit.measure_all()
    counts = quantum_simulator(q2c_circuit)

    ############################################################################
    # Student code end
    ############################################################################

    return counts
