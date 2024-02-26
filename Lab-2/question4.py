from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

"""
Simon's algorithm deals with the period finding problem which enables quantum advantage against classical algorithms towards solving large number factorization problems.
"""

def simon():
    """
    Implement the Simon's algorithm using the given oracle in the question.
    Args: 
        None
    Return:
        qc: QuantumCircuit of your implementation of Simon's algorithm
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    quantum_registers = QuantumRegister(8, 'q_reg')
    qc = QuantumCircuit(quantum_registers)

    # Start of Simon's Algorithm - Superposition
    for i in range(0, 4):
        qc.h(quantum_registers[i])

    # Apply barriers for visual purposes
    qc.barrier(quantum_registers[3])
    qc.barrier(quantum_registers[0])
    qc.barrier(quantum_registers[2])
    qc.barrier(quantum_registers[1])

    # Oracle function circuit implementation
    qc.cx(quantum_registers[0], quantum_registers[4])
    qc.cx(quantum_registers[1], quantum_registers[5])
    qc.barrier(quantum_registers[0])
    qc.barrier(quantum_registers[0])
    qc.cx(quantum_registers[2], quantum_registers[6])
    qc.barrier(quantum_registers[0])
    qc.barrier(quantum_registers[2])
    qc.cx(quantum_registers[3], quantum_registers[7])
    qc.barrier(quantum_registers[0])
    qc.cx(quantum_registers[1], quantum_registers[5])
    qc.barrier(quantum_registers[0])
    qc.barrier(quantum_registers[3])
    qc.barrier(quantum_registers[2])
    qc.cx(quantum_registers[1], quantum_registers[7])
    qc.barrier(quantum_registers[0])
    qc.barrier(quantum_registers[1])
    qc.barrier(quantum_registers[0])
    qc.barrier(quantum_registers[3])
    qc.barrier(quantum_registers[2])

    # End of Simon's Algorithm - Interference
    for i in range(0, 4):
        qc.h(quantum_registers[i])

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def calculate_period():
    """
    Calculate the period of the given oracle. (This can be hard coded!)
    Args:
        None
    Return:
        period: str of the period of the function 
    """

    period = "1010"
    ############################################################################
    # Student code begin
    ############################################################################

    # qc.measure(quantum_registers[:4], classical_registers[:4])
    # simulator = QasmSimulator()
    # cc = transpile(qc, simulator)
    # result = simulator.run(cc, shots=1024).result()
    # counts = result.get_counts(cc)
    # plot_histogram(counts)
    # then form system of linear equations from histogram results and determine likely characteristics of hidden string

    ############################################################################
    # Student code end
    ############################################################################

    return period