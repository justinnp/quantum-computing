from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile

"""
In this question you need to implement the quantum oracles $U_f$ of Deutsch and Deutsch-Jozsa circuits based on the definition of the given functions.
"""

def deutsch_f1_oracle():
    """
    Implement the ORACLE of Deutsch algorithm for the following function:
    f_1(0) = 0, f_1(1) = 0
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f_1
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    # Assume superposition (H) is already applied on input qubits
    qc = QuantumCircuit(2)
    # Assume superposition negation (H) is already applied on qubit 0
    qc.i(0)
    qc.i(1)
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def deutsch_f2_oracle():
    """
    Implement the ORACLE of Deutsch algorithm for the following function:
    f_2(0) = 1, f_2(1) = 0
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f_2
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(2)
    qc.x(0)
    qc.cx(0, 1)
    qc.x(0)
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def deutsch_f3_oracle():
    """
    Implement the ORACLE of Deutsch algorithm for the following function:
    f_3(0) = 0, f_3(1) = 1
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f_3
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(2)
    qc.cx(0, 1)
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def deutsch_f4_oracle():
    """
    Implement the ORACLE of Deutsch algorithm for the following function:
    f_4(0) = 1, f_4(1) = 1
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of the ORACLE of Deutsch algorithm for function f_4
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    qc = QuantumCircuit(2)
    qc.x(1)

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def deutsch_jozsa_oracle():
    """
    Given g(x) where
        g(x) = 0 if x is even
        g(x) = 1 if x is odd
    Implement the ORACLE of Deutsch-Jozsa algorithm for function g(x)
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of the ORACLE of Deutsch-Jozsa algorithm circuit for g(x)
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
        "`deutsch_jozsa_oracle` function in "
        + "`question2.py` needs to be implemented"
    )

    ############################################################################
    # Student code end
    ############################################################################

    return qc

