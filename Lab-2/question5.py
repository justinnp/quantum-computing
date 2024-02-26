from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator
import math

"""
Grover's algorithm can be used to amplify the probability of a target state by a rotation oracle and an inversion oracle.
In this question, you need to complete the Grover's circuit using the given oracles, find the target state,
and also find the probability of the target state after running Grover's circuit.
"""

def grover(n: int):
    """
    This function output Grover's algorithm circuit for a specific target. 
    Implement the circuit for applying
        Rotation phase + Inversion around the mean
    n times, where n is a nonnegative integer.
    Args: 
        n: integer of the number of times to apply (rotation + inversion)
    Return:
        qc: QuantumCircuit of your implementation of Grover's algorithm of n repetition
    """
    
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(3, 3)
    
    # super position for all qubits in the base Grover's circuit
    for i in range(3):
        qc.h(i)

    for i in range(n):
        # Rotation Operator Oracle
        qc.x(0)
        qc.h(2)
        qc.ccx(0, 1, 2)
        qc.x(0)
        qc.h(2)

        # Inversion Operator
        qc.h(0)
        qc.h(1)
        qc.h(2)
        qc.x(0)
        qc.x(1)
        qc.x(2)
        qc.barrier(2)
        qc.barrier(0)
        qc.barrier(1)
        qc.h(2)
        qc.ccx(0, 1, 2)
        qc.h(2)
        qc.barrier(0)
        qc.barrier(1)
        qc.barrier(2)
        qc.barrier(1)
        qc.barrier(0)
        qc.x(0)
        qc.x(1)
        qc.x(2)
        qc.h(0)
        qc.h(1)
        qc.h(2)

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def target_state():
    """
    What is the target state found by the Grover's circuit? (This can be hard coded!)
    Args:
        None
    Return:
        s: str of the target state
    """

    s = ""
    ############################################################################
    # Student code begin
    ############################################################################

    # measure, take max of counts for target state
    # g_qc.measure(q_r, c_r)
    # simulator = QasmSimulator()
    # cc = transpile(g_qc, simulator)
    # result = simulator.run(cc, shots=1024).result()
    # counts = result.get_counts(g_qc)
    # plot_histogram(counts)
    # target_state = max(counts, key=counts.get)

    s = "110"

    ############################################################################
    # Student code end
    ############################################################################

    return s


def post_processing(grover_qc):
    """
    Args:
        grover_qc: QuantumCircuit returned by your grover function with input n
    Return:
        prob: float of the probability of finding the target state by running Grover's algorithm of n repetition
    """

    prob = None
    ############################################################################
    # Student code begin
    ############################################################################
    for i in range(3):
        grover_qc.measure(i, i)
    simulator = QasmSimulator()
    cc = transpile(grover_qc, simulator)
    result = simulator.run(cc, shots=1024).result()
    counts = result.get_counts(grover_qc)
    target = "110"
    if target in counts:
        prob = counts[target] / sum(counts.values())

    ############################################################################
    # Student code end
    ############################################################################

    return prob