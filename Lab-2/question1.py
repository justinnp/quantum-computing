from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator
import math

"""
For this question, implement the components of super dense coding in `question1.py` to transmit $n$ bits of classical binary information.
"""

def qubit_preparation(n):
    """
    Prepare enough qubits based on the length of the information to be sent.
    Args:
        n: int of length of classical_information
    Return:
        qc: QuantumCircuit of prepared qubits
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    # adds additional qubit when n is odd
    num_qubits = math.ceil(n / 2) * 2
    qc = QuantumCircuit(num_qubits, n)

    # qubit preparation by Charlie
    # to prepare encoding for SDC: +superposition(h) +entanglement (cx)
    for i in range(0, num_qubits, 2):
        qc.h(i)
        qc.cx(i, i + 1)  

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def qubit_encoding(prepared_qubits, classical_information):
    """
    Based on the Super Dense Coding principle, Alice can only use the first ceil(n/2) qubits of the prepared qubits.
    Args:
        prepared_qubits: QuantumCircuit of prepared qubits
        classical_information: str
    Return:
        qc: QuantumCircuit of encoded qubits
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    n = len(classical_information)

    # Classical preparation and encoding
    if n % 2 == 0:
        # create bit pair tuples for enumeration
        bit_pairs = zip(classical_information[0::2], classical_information[1::2])
        for i, (a, b) in enumerate(bit_pairs):
            # when a == 1, apply Z gate on q0
            # when b == 1, apply X gate on q0
            if a == '1':
                prepared_qubits.z(i)
            if b == '1':
                prepared_qubits.x(i)
        qc = prepared_qubits

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def qubit_decoding(encoded_qubits, n):
    """
    Bob restores the classical information using the encoded qubits 
    Args:
        encoded_qubits: QuantumCircuit of encoded qubits
        n: int of length of classical_information
    Return:
        restored_information: str of restored information
    """

    restored_information = ""
    ############################################################################
    # Student code begin
    ############################################################################

    # decoding employs reverse encoding gates: -entanglement (cx) -superposition (h)
    num_qubits = math.ceil(n / 2) * 2
    if n % 2 == 0:
        for i in range(0, num_qubits, 2):
            encoded_qubits.cx(i, i + 1)
            encoded_qubits.h(i)
    
        # measure encoded qubits
        for i in range(0, num_qubits, 2):
            encoded_qubits.measure(i, i)
            encoded_qubits.measure(i + 1, i + 1)

        # simulate to extract results
        simulator = QasmSimulator()
        cc = transpile(encoded_qubits, simulator)
        job = simulator.run(cc, shots=1)
        result = job.result()
        counts = result.get_counts(encoded_qubits)
        measurement = next(iter(counts))
        restored_information = measurement[::-1]

    ############################################################################
    # Student code end
    ############################################################################

    return restored_information
