from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator


def encoder(x: int=0, y: int=0, n=4):
    """
    An encoder to convert two n-bit nonnegative integers (uint) x and y to a 2n-qubit QuantumCircuit.
    This encoder will be used by autograder.
    """
    assert x >= 0 and x < 2**n and isinstance(n,int), f"Your input x must be an integer in the range [0,{(2**n)-1}]."
    assert y >= 0 and y < 2**n and isinstance(n,int), f"Your input y must be an integer in the range [0,{(2**n)-1}]."

    qc = QuantumCircuit(n*2)
    
    for i in range(n):
        if x >= 2**(n-i-1):
            qc.x(n-i-1)
            x -= 2**(n-i-1)

    for i in range(n):
        if y >= 2**(n-i-1):
            qc.x(2*n-i-1)
            y -= 2**(n-i-1)
    
    return qc
    

def decoder(qc: QuantumCircuit, n=4):
    """
    A decoder to convert a QuantumCircuit to an n-bit nonnegative integer from the simulation histogram
    by measuring the first n qubits in the quantum circuit.
    The result should be deterministic on a noise-free machine, hence shot=1 is used for simulation.
    This decoder will be used by autograder.
    """
    assert n >= 1
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits >= n

    n_qubits = qc.num_qubits
    n_clbits = max(n, qc.num_clbits)

    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_clbits)
    qc_base = QuantumCircuit(qr, cr)
    qc = qc_base.compose(qc)

    simulator = QasmSimulator()
    qc.measure(list(range(n)), list(range(n)))
    cc = transpile(qc, simulator)
    job = simulator.run(cc, shots=1)
    result = list(job.result().get_counts(cc).keys())[0]

    z = 0
    for i in range(n):
        z += int(result[i])*2**(n-i-1)

    return z


def quantum_and():
    """
    An N-qubit quantum circuit which calculates the AND result of input1 on [q0] and input2 on [q1],
    The output will be measured on [q0].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=1) and decoder(n=1).
    N must be either 2 or 3.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`quantum_and` function in "
            + "`question4.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def quantum_or():
    """
    An N-qubit quantum circuit which calculates the OR result of input1 on [q0] and input2 on [q1],
    The output will be measured on [q0].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=1) and decoder(n=1).
    N must be either 2 or 3.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`quantum_or` function in "
            + "`question4.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc

def quantum_xor():
    """
    An N-qubit quantum circuit which calculates the XOR result of input1 on [q0] and input2 on [q1],
    The output will be measured on [q0].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=1) and decoder(n=1).
    N must be either 2 or 3.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`quantum_xor` function in "
            + "`question4.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def quantum_adder():
    """
    An N-qubit quantum circuit which adds input1 on [q0,q1,q2,q3] and input2 on [q4,q5,q6,q7],
    The output will be measured on [q0,q1,q2,q3].
    You need to decide the amount of additional qubits needed to implement the function.
    The function must be compatible with the provided encoder(n=4) and decoder(n=4).
    N must satisfy the following constraint: 8 <= N <= 16.
    Args: 
        None
    Return:
        qc: Your QuantumCircuit
    """

    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`quantum_adder` function in "
            + "`question4.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return qc


def encoder_signed(x: int=0, y: int=0, n=4):
    """
    An encoder to convert two n-bit integers x and y to a 2n-qubit QuantumCircuit.
    This encoder will be used by autograder.
    Args:
        x: int of input 1
        y: int of input 2
        n: int of input size
    Return:
        qc: your QuantumCircuit
    """
    assert x >= -2**(n-1) and x < 2**(n-1) and isinstance(n,int), f"Your input x must be an integer in the range [{-2**(n-1)},{2**(n-1)-1}]."
    assert y >= -2**(n-1) and y < 2**(n-1) and isinstance(n,int), f"Your input y must be an integer in the range [{-2**(n-1)},{2**(n-1)-1}]."

    qc = QuantumCircuit(n*2)
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`encoder_signed` function in "
            + "`question4.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################    
    
    return qc
    

def decoder_signed(qc: QuantumCircuit, n=4):
    """
    A decoder to convert a QuantumCircuit to an n-bit integer from the simulation histogram
    by measuring the first n qubits in the quantum circuit.
    The result should be deterministic on a noise-free machine, hence shot=1 is used for simulation.
    Args:
        qc: QuantumCircuit
        n: int of input size
    Return:
        z: int of your decode result
    """
    assert n >= 1
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits >= n

    n_qubits = qc.num_qubits
    n_clbits = max(n, qc.num_clbits)

    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_clbits)
    qc_base = QuantumCircuit(qr, cr)
    qc = qc_base.compose(qc)

    simulator = QasmSimulator()
    qc.measure(list(range(n)), list(range(n)))
    cc = transpile(qc, simulator)
    job = simulator.run(cc, shots=1)
    result = list(job.result().get_counts(cc).keys())[0]

    z = 0
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`decoder` function in "
            + "`question4.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################    
    
    return z


def test_your_implementation(x: int, y: int, n: int, quantum_calculation_circuit: QuantumCircuit=None, encoder_func=encoder, decoder_func=decoder):
    """
    Args:
        x: int of input uint x
        y: int of input uint y
        n: int of input size
        quantum_logic_circuit: QuantumCircuit of optional input of your quantum operation circuit function
    return:
        output: int of calculation result
    """
    assert isinstance(x, int)
    assert isinstance(y, int)
    assert isinstance(n, int) and n>=1
    assert quantum_calculation_circuit is None or isinstance(quantum_calculation_circuit, QuantumCircuit)

    if quantum_calculation_circuit is not None:
        n_qubits = max(2*n, len(quantum_calculation_circuit.qubits))
        n_clbits = max(n, len(quantum_calculation_circuit.clbits))
    else:
        n_qubits = 2*n
        n_clbits = n
    
    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_clbits)
    qc = QuantumCircuit(qr, cr)

    qc = qc.compose(encoder_func(x, y, n))
    if quantum_calculation_circuit is not None:
        qc = qc.compose(quantum_calculation_circuit)
    return decoder_func(qc, n)
