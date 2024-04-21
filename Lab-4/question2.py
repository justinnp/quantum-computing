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
    # detection
    for i in range(3):
        qc.h(i)

    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(1, 4)
    qc.cx(2, 4)

    for i in range(3):
        qc.h(i)

    qc.measure(3, 0)
    qc.measure(4, 1)

    # correction
    qc.z(0).c_if(qc.cregs[0], 1)
    qc.z(1).c_if(qc.cregs[0], 2)
    qc.z(2).c_if(qc.cregs[0], 3)

    # decode
    for i in range(3):
        qc.h(i)
    qc.cx(0, 1)
    qc.cx(0, 2)
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

    raise NotImplementedError(
            "`decoder2` function in "
            + "`question2.py` needs to be implemented"
        )
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc
