from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator

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

    raise NotImplementedError(
            "`qubit_preparation` function in "
            + "`Question1.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`qubit_encoding` function in "
            + "`Question1.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`qubit_decoding` function in "
            + "`Question1.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return restored_information
