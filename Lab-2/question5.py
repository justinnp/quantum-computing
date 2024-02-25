from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

"""
Grover's algorithm can be used to amplify the probability of a target state by a rotation oracle and an inversion oracle.
In this question, you need to complete the Grover's circuit using the given oracles, find the target state,
and also find the probability of the target state after running Grover's circuit.
"""

def grover(n: int):
    """
    This function output Grover's algorithm circuit for a specific target. 
    Implement the circuit for applying
        Rotation phase + Inversion around the mean
    n times, where n is a nonnegative integer.
    Args: 
        n: integer of the number of times to apply (rotation + inversion)
    Return:
        qc: QuantumCircuit of your implementation of Grover's algorithm of n repetition
    """
    
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`grover` function in "
            + "`question5.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def target_state():
    """
    What is the target state found by the Grover's circuit? (This can be hard coded!)
    Args:
        None
    Return:
        s: str of the target state
    """

    s = ""
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`target_state` function in "
            + "`question5.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return s


def post_processing(grover_qc):
    """
    Args:
        grover_qc: QuantumCircuit returned by your grover function with input n
    Return:
        prob: float of the probability of finding the target state by running Grover's algorithm of n repetition
    """

    prob = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`post_processing` function in "
            + "`question5.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return prob