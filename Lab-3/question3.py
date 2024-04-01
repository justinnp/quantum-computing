from qiskit import QuantumCircuit, QuantumRegister, transpile
from qiskit_aer.backends.qasm_simulator import QasmSimulator
from qiskit.circuit import Gate, ControlledGate
from qiskit.circuit.library import CUGate
from qiskit.quantum_info import Statevector
import math
import numpy as np


def cx_ideal():
    """
    A noise-free cx gate implemented using a qiskit.circuit.Gate object
    Hint: use CUGate
    Args:
        None
    Return:
        studentGate: qiskit.circuit.Gate
    """
    studentGate = None
    ############################################################################
    # Student code begin
    ############################################################################

    studentGate = CUGate(np.pi, 0, np.pi, 0)
    
    ############################################################################
    # Student code end
    ############################################################################

    return studentGate


def cx_p95():
    """
    A noisy cx gate of p=0.95 according to the definition in the
    jupyter notebook implemented using a qiskit.circuit.Gate object
    Hint: use CUGate
    Args:
        None
    Return:
        studentGate: qiskit.circuit.Gate
    """
    studentGate = None
    ############################################################################
    # Student code begin
    ############################################################################
    p = 0.95
    theta = 2 * math.asin(math.sqrt(p))

    studentGate = CUGate(theta, 0,0, 0)
    
    ############################################################################
    # Student code end
    ############################################################################

    return studentGate


def cx_p70():
    """
    A noisy cx gate of p=0.70 according to the definition in the
    jupyter notebook implemented using a qiskit.circuit.Gate object
    Hint: use CUGate
    Args:
        None
    Return:
        studentGate: qiskit.circuit.Gate
    """
    studentGate = None
    ############################################################################
    # Student code begin
    ############################################################################

    p = 0.70
    theta = 2 * math.asin(math.sqrt(p))

    studentGate = CUGate(theta, 0,0, 0)
    
    ############################################################################
    # Student code end
    ############################################################################

    return studentGate


def q3c_edge_gates():
    """
    Implement the cx gates on each edge according to q3c device topology,
    each key denotes a bidirectional edge of the device
    Args:
        None
    Return:
        edge_gates: dict[str, qiskit.circuit.Gate]
    """
    edge_gates = {
        "01": None,
        "12": None,
        "23": None,
        "03": None,
    }
    ############################################################################
    # Student code begin
    ############################################################################

    edge_gates["01"] = CUGate(2 * math.asin(math.sqrt(0.99)), 0, 0, 0)
    edge_gates["12"] = CUGate(2 * math.asin(math.sqrt(0.90)), 0, 0, 0)
    edge_gates["23"] = CUGate(2 * math.asin(math.sqrt(0.80)), 0, 0, 0)
    edge_gates["03"] = CUGate(2 * math.asin(math.sqrt(0.75)), 0, 0, 0)

    ############################################################################
    # Student code end
    ############################################################################

    return edge_gates


def q3c_device_qubit_route_mapping():
    """
    The logical qubits (int) to physical qubits (int) mapping for qubit
    allocation
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################

    qubit_mapping = {
        0: 1,
        1: 0,
        2: 2,
        3: 3
    }

    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping


def q3c_device_compatible_physical_circuit():
    """
    Your implementation physical quantum circuit based on the logical circuit
    and device topology q3c_device_topology.png
    Args:
        None
    Return:
        qc: QuanutmCircuit
    """
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################
    edge_gates = q3c_edge_gates()
    qubit_mapping = q3c_device_qubit_route_mapping()
    qc = QuantumCircuit(4)
    qc.append(edge_gates["01"], [qubit_mapping[0], qubit_mapping[1]])
    qc.append(edge_gates["12"], [qubit_mapping[0], qubit_mapping[2]])
    # SWAP using noisy CNOTs
    qc.append(edge_gates["23"], [qubit_mapping[2], qubit_mapping[3]])
    qc.append(edge_gates["23"], [qubit_mapping[3], qubit_mapping[2]])
    qc.append(edge_gates["23"], [qubit_mapping[2], qubit_mapping[3]])
    # CNOT with newly swapped q3
    qc.append(edge_gates["12"], [qubit_mapping[0], qubit_mapping[2]])
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3c_device_qubit_read_mapping():
    """
    Your physical qubits (int) to logical qubits (int) mapping for information
    recovery
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################
    qubit_mapping = {
        0: 1,
        1: 0,
        2: 3,
        3: 2
    }
    
    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping


def q3d_edge_gates():
    """
    Implement the cx gates on each edge according to q3d device topology,
    each key denotes a bidirectional edge of the device
    Args:
        None
    Return:
        edge_gates: dict[str, qiskit.circuit.Gate]
    """
    edge_gates = {
        "01": None,
        "12": None,
        "13": None,
        "34": None,
    }
    ############################################################################
    # Student code begin
    ############################################################################

    edge_gates["01"] = CUGate(2 * math.asin(math.sqrt(0.850)), 0, 0, 0)
    edge_gates["12"] = CUGate(2 * math.asin(math.sqrt(0.825)), 0, 0, 0)
    edge_gates["13"] = CUGate(2 * math.asin(math.sqrt(0.975)), 0, 0, 0)
    edge_gates["34"] = CUGate(2 * math.asin(math.sqrt(0.990)), 0, 0, 0)

    ############################################################################
    # Student code end
    ############################################################################

    return edge_gates


def q3d_device_qubit_route_mapping():
    """
    The logical qubits (int) to physical qubits (int) mapping for qubit
    allocation
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################

    qubit_mapping = {
        0: 3,
        1: 4,
        2: 1,
        3: 0,
        4: None
    }

    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping


def q3d_device_compatible_physical_circuit():
    """
    Your implementation physical quantum circuit based on the logical circuit
    and device topology q3d_device_topology.png
    Args:
        None
    Return:
        qc: QuanutmCircuit
    """
    qc = None
    ############################################################################
    # Student code begin
    ############################################################################

    edge_gates = q3d_edge_gates()
    qubit_mapping = q3d_device_qubit_route_mapping()
    qc = QuantumCircuit(5)
    # CNOT 0 -> 1
    qc.append(edge_gates["34"], [qubit_mapping[0], qubit_mapping[1]])
    # CNOT 0 -> 2
    qc.append(edge_gates["13"], [qubit_mapping[0], qubit_mapping[2]])
    # SWAP 2 <-> 3
    qc.append(edge_gates["01"], [qubit_mapping[2], qubit_mapping[3]])
    qc.append(edge_gates["01"], [qubit_mapping[3], qubit_mapping[2]])
    qc.append(edge_gates["01"], [qubit_mapping[2], qubit_mapping[3]])
    # CNOT 0 -> swapped(3)
    qc.append(edge_gates["13"], [qubit_mapping[0], qubit_mapping[2]])
    
    ############################################################################
    # Student code end
    ############################################################################

    return qc


def q3d_device_qubit_read_mapping():
    """
    Your physical qubits (int) to logical qubits (int) mapping for information
    recovery
    Args:
        None
    Return:
        qubit_mapping: dict[int, int]
    """
    qubit_mapping = None
    ############################################################################
    # Student code begin
    ############################################################################
    qubit_mapping = {
        0: 3,
        1: 4,
        2: 0,
        3: 1,
        4: None
    }
    
    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping

