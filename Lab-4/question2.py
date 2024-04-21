from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator


def encoder():
    """
    Your implementation of phase-flip QEC encoder that works for both 1 bit-flip error and 2 bit-flip errors
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
    for i in range(3):
        qc.h(i)
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc

def decoder1():
    """
    Your implementation of phase-flip QEC decoder that works for 1 phase-flip error
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    qc = QuantumCircuit(5, 2)
    # Detection - basic circuit layout
    for i in range(3):
        qc.h(i)
    qc.cx(0, 3) # X1
    qc.cx(1, 3) # X2
    qc.cx(1, 4) # X2
    qc.cx(2, 4) # X3
    for i in range(3):
        qc.h(i)
    # Measurement - little endian format
    qc.measure(3, 1) # holds s1 = X1 x X2
    qc.measure(4, 0) # holds s2 = X2 x X3
    # Correction
    # if binary '10' then error location is at qubit 0, apply Z gate
    qc.z(0).c_if(qc.cregs[0], 2)
    # if binary '11' then error location is at qubit 1
    qc.z(1).c_if(qc.cregs[0], 3)
    # if binary '01' then error location is at qubit 2
    qc.z(2).c_if(qc.cregs[0], 1)
    # Decode
    for i in range(3):
        qc.h(i)
    qc.cx(0, 2)
    qc.cx(0, 1)
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc

def decoder2():
    """
    Your implementation of phase-flip QEC decoder that works for 2 phase-flip errors
    Args:
        None
    Return:
        QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(5, 2)
    # Detection - basic circuit layout
    for i in range(3):
        qc.h(i)
    qc.cx(0, 3) # X1
    qc.cx(1, 3) # X2
    qc.cx(1, 4) # X2
    qc.cx(2, 4) # X3
    for i in range(3):
        qc.h(i)
    # Measurement - little endian format
    qc.measure(3, 1) # holds s1 = X1 x X2
    qc.measure(4, 0) # holds s2 = X2 x X3

    # Correction - inverse of 1-bit QEC
    # if binary '10' then error location at qubit 1 and 2, apply Z
    qc.z(1).c_if(qc.cregs[0], 2)
    qc.z(2).c_if(qc.cregs[0], 2)
    # if binary '11' then error location at qubit 0 and 2
    qc.z(0).c_if(qc.cregs[0], 3)
    qc.z(2).c_if(qc.cregs[0], 3)
    # if binary '01' then error location at qubit 0 and 1
    qc.z(0).c_if(qc.cregs[0], 1)
    qc.z(1).c_if(qc.cregs[0], 1)
     # Decode
    for i in range(3):
        qc.h(i)
    qc.cx(0, 2)
    qc.cx(0, 1)
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc
