from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

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
    qc = QuantumCircuit(2)
    # apply H to both qubits to get superposition across 00, 01, 10, 11 w/ 25% probability for each
    qc.h(0)
    qc.h(1)

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
    q_register = QuantumRegister(3, 'q')
    qc = QuantumCircuit(q_register)
    # amplitudes derived as cos(theta/2) = 1/2, sin(theta/2) = sqrt(3)/2
    # apply Ry gate with 2pi/3 rotation
    qc.ry((2 * pi) / 3, q_register[0])
    qc.cx(q_register[0], q_register[2])
    qc.x(q_register[1])
    qc.cx(q_register[0], q_register[1])

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
    q_register = QuantumRegister(2, 'q')
    qc = QuantumCircuit(q_register)
    # apply H for superposition
    qc.h(q_register[0])
    # apply CNOT for entanglement and
    qc.cx(q_register[0], q_register[1])
    # flip second qubit
    qc.x(q_register[1])
    # phase shift on second qubit for negative sign
    qc.z(q_register[1])

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
