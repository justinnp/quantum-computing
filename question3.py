from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

"""
In this question, you need to design quantum circuits to generate the given quantum states in Dirac's notations.
For each part, return a QuantumCircuit object that corresponds to the given state $\ket{\psi}$.
The Dirac's notations should be understood in Qiskit little-endian ordering.
You may not use the `initialize` instruction.
You can only use the following gates: `h, x, y, z, s, t, cx, ccx, u, cu, rx, ry, rz`
"""

def q3a():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{00} + \frac{1}{2}\ket{01} + \frac{1}{2}\ket{10} + \frac{1}{2}\ket{11}$$
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    '''

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`q3a` function in "
            + "`question3.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3b():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{010} + \frac{\sqrt{3}}{2}\ket{101}$$
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    '''

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`q3b` function in "
            + "`question3.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3c():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{\sqrt{2}}\ket{01} - \frac{1}{\sqrt{2}}\ket{10}$$
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    '''

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`q3c` function in "
            + "`question3.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3d():
    '''
    Construct the quantum circuit to generate
        $$\ket{\psi}= \frac{1}{2}\ket{0001} + \frac{i}{2}\ket{0010} - \frac{1}{2}\ket{0100} - \frac{i}{2}\ket{1000}$$
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    '''

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`q3d` function in "
            + "`question3.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc
