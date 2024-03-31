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

    raise NotImplementedError(
            "`cx_ideal` function in "
            + "`question3.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`cx_p95` function in "
            + "`question3.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`cx_p70` function in "
            + "`question3.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`q3c_edge_gates` function in "
            + "`question3.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`q3c_device_qubit_route_mapping` function in "
            + "`question3.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`q3c_device_compatible_physical_circuit` function in "
            + "`question3.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`q3c_device_qubit_read_mapping` function in "
            + "`question3.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`q3d_edge_gates` function in "
            + "`question3.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`q3d_device_qubit_route_mapping` function in "
            + "`question3.py` needs to be implemented"
        )

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

    raise NotImplementedError(
            "`q3d_device_compatible_physical_circuit` function in "
            + "`question3.py` needs to be implemented"
        )
    
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

    raise NotImplementedError(
            "`q3d_device_qubit_read_mapping` function in "
            + "`question3.py` needs to be implemented"
        )
    
    ############################################################################
    # Student code end
    ############################################################################

    return qubit_mapping

