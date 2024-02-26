from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi

"""
Implement Bernstein Vazirani (BV) algorithm with an oracle function $U_f$ of secrete key `0101010`. Your implementation should not contain any measurments.
"""

def bv_ideal():
    """
    Implement the BV circuit of secrete string "0101010"
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of ideal BV algorithm
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    secret_string = "0101010"
    # 7 qubits instantiated for 7 classical bits in secret string, with +1 qubit acting as the tmp qubit
    n = len(secret_string)
    qc = QuantumCircuit(n+1)

    # apply superposition (H) to all classically mapped qubits
    for i in range(n):
        qc.h(i)

    # apply X gate and superposition (H) to tmp qubit
    qc.x(n)
    qc.h(n)

    # apply CNOT controlled by qubit_i wherever a 1 is found
    for i, value in enumerate(secret_string):
        if value == '1':
            qc.cx(i, n)

    # negate superposition (H) for all qubits after oracle
    for i in range(n+1):
        qc.h(i)
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def bv_noisy():
    """
    Implement the BV circuit of secrete string "0101010"
    with simulated noise by replacing all H gates with U(pi/2, pi/16, pi) gates

    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of noisy BV algorithm
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    secret_string = "0101010"
    # 7 qubits instantiated for 7 classical bits in secret string, with +1 qubit acting as the tmp qubit
    n = len(secret_string)
    qc = QuantumCircuit(n+1)

    # apply superposition (H) to all classically mapped qubits
    for i in range(n):
        qc.u(pi / 2, pi / 16, pi, i)

    # apply X gate and superposition (H) to tmp qubit
    qc.x(n)
    qc.u(pi / 2, pi / 16, pi, n)

    # apply CNOT controlled by qubit_i wherever a 1 is found
    for i, value in enumerate(secret_string):
        if value == '1':
            qc.cx(i, n)

    # negate superposition (H) for all qubits after oracle
    for i in range(n+1):
        qc.u(pi / 2, pi / 16, pi, i)

    ############################################################################
    # Student code end
    ############################################################################

    return qc
