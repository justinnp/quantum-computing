from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

"""
In this question you need to construct the exact quantum circutis for each part according to the figures provided.
For each part, follow the instructions and return a QuantumCircuit object.
You may want to refer to https://docs.quantum.ibm.com/build/circuit-construction to learn how to build quantum circuits.
"""


def q1a():
    """
    Construct the quantum circuit shown in ./Figures/Q1A.png
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    qc = QuantumCircuit(3)
    # H gate at q0
    qc.h(0)
    # CNOT with q0 as control and q1 as target
    qc.cx(0,1)
    qc.cx(1,2)

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q1b():
    """
    Construct the quantum circuit shown in ./Figures/Q1B.png
    Args: 
        None
    Return:
        qc: your QuantumCircuit object
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    q_register = QuantumRegister(6, 'qreg')
    # instantiate classical register with 3 bits
    c_register = ClassicalRegister(3, 'creg')
    qc = QuantumCircuit(q_register, c_register)
    # apply H gate to each qubit
    for i in range(0,6):
        qc.h(q_register[i])
    qc.cx(0,2)
    qc.cx(1,3)
    qc.cx(2,4)
    # barrier for visual separation bw CNOT and H
    qc.barrier()
    qc.h(q_register[0])
    qc.h(q_register[2])
    qc.h(q_register[4])

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q1c():
    """
    Construct the quantum circuit shown in ./Figures/Q1C.png
    Args: 
        None
    Return:
        qcirc: your QuantumCircuit object
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    q_register = QuantumRegister(6, 'qreg')
    # instantiate classical register with 3 bits
    c_register = ClassicalRegister(3, 'creg')
    qc = QuantumCircuit(q_register, c_register)
    # H gates
    qc.h(q_register[0])
    qc.h(q_register[1])
    qc.h(q_register[5])
    # U gates
    for i in range(5,0,-1):
        # control starts at 0 to 4
        ix = 5 - i
        # target of q5
        qc.cu(0, 0, pi / (2**i), 0, q_register[ix], q_register[5])
    # SWAPs
    qc.swap(q_register[0], q_register[5])
    qc.barrier()
    qc.swap(q_register[1], q_register[4])
    qc.barrier()
    qc.swap(q_register[2], q_register[3])
    # q_circuit_1c.draw(output="mpl", plot_barriers=False)

    ############################################################################
    # Student code end
    ############################################################################

    return qc
