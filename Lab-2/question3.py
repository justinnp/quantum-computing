from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

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

    raise NotImplementedError(
            "`bv_ideal` function in "
            + "`Question3.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`bv_noisy` function in "
            + "`Question3.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc
