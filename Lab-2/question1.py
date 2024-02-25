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

    # register qubits and classical bits
    num_qubits = math.ceil(n / 2) * 2
    quantum_registers = QuantumRegister(num_qubits, 'q_reg')
    qc = QuantumCircuit(quantum_registers)

    # qubit preparation by Charlie
    # to prepare encoding for SDC: +superposition(h) +entanglement (cx)
    for i in range(0, num_qubits, 2):
        qc.h(quantum_registers[i])
        qc.cx(quantum_registers[i], quantum_registers[i + 1])    

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

    # add classical bits to prepared quantum circuit
    n = len(classical_information)
    
    # TODO evaluate classical string of even length separately from odd lengthed

    # Classical preparation and encoding
    for i in range(0, n, 2):
        bit_pair = classical_information[i:i + 2]
        # Alice can only use the first ceil(n/2) qubits of the prepared qubits
        encoding_qubit = prepared_qubits.qubits[i // 2]
        # when a == 1, apply Z gate on q0
        # when b == 1, apply X gate on q0
        if bit_pair == '01':
            prepared_qubits.x(encoding_qubit)
        if bit_pair == '10':
            prepared_qubits.z(encoding_qubit)
        elif bit_pair == '11':
            prepared_qubits.x(encoding_qubit)
            prepared_qubits.z(encoding_qubit)
        # else bit_pair == 00 do nothing, send qubit as is
    
    # circuit construction, adding classical registers
    qc = prepared_qubits
    classical_registers = ClassicalRegister(n, "c_reg")
    qc.add_register(classical_registers)

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
    for i in range(0, num_qubits, 2):
        qubits = encoded_qubits.qubits
        encoded_qubits.cx(qubits[i], qubits[i + 1])
        encoded_qubits.h(qubits[i])
    
    # measure encoded qubits
    for i in range(0, num_qubits, 2):
        encoded_qubits.measure([i, i + 1], [i, i + 1])

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
