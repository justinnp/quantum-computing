from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator


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

    raise NotImplementedError(
            "`encoder` function in "
            + "`question1.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`decoder1` function in "
            + "`question1.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`decoder2` function in "
            + "`question1.py` needs to be implemented"
        )
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc
