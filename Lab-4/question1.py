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
    # Error Detection - basic circuit layout
    qc.cx(0, 3) # Z1
    qc.cx(1, 3) # Z2
    qc.cx(1, 4) # Z2
    qc.cx(2, 4) # Z3
    # Classical measurement on ancilla - measured in little endian format
    # qubit 3 holds s1 = Z1 x Z2
    qc.measure(3, 1)
    # qubit 4 holds s2 = Z2 x Z3 
    qc.measure(4, 0)
    # Correction
    # if binary '01' [MSB = 0(+1) LSB = 1(-1)] then apply X to qubit 2
    qc.x(2).c_if(qc.cregs[0], 1)
    # if b'10' then apply X to qubit 0
    qc.x(0).c_if(qc.cregs[0], 2)
    # if b'11' then apply X to qubit 1
    qc.x(1).c_if(qc.cregs[0], 3)
    # Decode - reversal of encoder
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

    qc = QuantumCircuit(5,2)
    # Error Detection - basic circuit layout
    qc.cx(0, 3) # Z1
    qc.cx(1, 3) # Z2
    qc.cx(1, 4) # Z2
    qc.cx(2, 4) # Z3
    # Classical measurement on ancilla - measured in little endian format
    # qubit 3 holds s1 = Z1 x Z2
    qc.measure(3, 1)
    # qubit 4 holds s2 = Z2 x Z3 
    qc.measure(4, 0)

    # Correction - invert 1-bit correction logic to implement 2-bit QEC knowing exactly 2 errors exist
    # under 1-bit QEC, if binary '01' [MSB = 0(+1) LSB = 1(-1)] then apply X to qubit 2
    # under 2-bit QEC, qubit 2 is correct, apply X to qubit 0 and 1
    qc.x(0).c_if(qc.cregs[0], 1)
    qc.x(1).c_if(qc.cregs[0], 1)
    # 1-bit QEC, if b'10' then apply X to qubit 0
    # 2-bit QEC, X on qubit 1 and 2
    qc.x(1).c_if(qc.cregs[0], 2)
    qc.x(2).c_if(qc.cregs[0], 2)
    # 1-bit QEC, if b'11' then apply X to qubit 1
    # 2-bit QEC, X on qubit 0 and 2
    qc.x(0).c_if(qc.cregs[0], 3)
    qc.x(2).c_if(qc.cregs[0], 3)
    # Decode
    qc.cx(0, 2)
    qc.cx(0, 1)
    ############################################################################
    # Student code end
    ############################################################################

    return qc
