from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator


def encoder():
    """
    Your implementation of bit-flip QEC encoder that works for both 1 bit-flip error and 2 bit-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = QuantumCircuit(3)
    ############################################################################
    # Student code begin
    ############################################################################

    qc.cx(0, 1)
    qc.cx(0, 2)
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc

def decoder1():
    """
    Your implementation of bit-flip QEC decoder that works for 1 bit-flip error
    Args:
        None
    Return:
        QuantumCircuit
    """
    
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(5,2)
    # Error Detection
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(1, 4)
    qc.cx(2, 4)
    # Classical measurement on ancilla
    qc.measure(3, 1)
    qc.measure(4, 0)
    # Correction (flip if ancilla classical 0 is 1 and 1 is 0)
    # if b'01' then apply X to third qubit
    qc.x(2).c_if(qc.cregs[0], 1)
    # if b'10' then apply X to qubit 0
    qc.x(0).c_if(qc.cregs[0], 2)
    # if b'11' then apply X to second qubit
    qc.x(1).c_if(qc.cregs[0], 3)
    # Decode
    qc.cx(0, 2)
    qc.cx(0, 1)
    ############################################################################
    # Student code end
    ############################################################################
    return qc

def decoder2():
    """
    Your implementation of bit-flip QEC decoder that works for 2 bit-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    return qc
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc
