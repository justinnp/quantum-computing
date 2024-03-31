from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, transpiler
from utils import get_benchmark_dict
import os
workload_list = get_benchmark_dict("SWAP_Benchmarks")

def q1a():
    '''
    In ./SWAP_Benchmarks, we have five quantum benchmark circuits in ".qasm" format.
    Decompose the benchmark circuits using qiskit transpile function with basis gates set [cx,u],
    and return a dictionary of benchmark circuits' names as keys and transpiled circuits as values.

    You are expected to use the same names of circuits generated by get_benchmark_dict.
    
    Args: 
        None
    Return:
        output_dict
    '''

    output_dict = {}
    ############################################################################
    # Student code begin
    ############################################################################
    q1a_basis_gates = ['cx', 'u']
    for benchmark_circuit in workload_list.keys():
        circuit = workload_list[benchmark_circuit]
        transpiled = transpile(circuit, basis_gates=q1a_basis_gates)
        output_dict[benchmark_circuit] = transpiled
    ############################################################################
    # Student code end
    ############################################################################

    return output_dict


def q1b():
    '''
    In ./SWAP_Benchmarks, we have five quantum benchmark circuits in ".qasm" format.
    Decompose the benchmark circuits using qiskit transpile function with basis gates set [cx,rx,ry,rz],
    and return a dictionary of benchmark circuits' names as keys and transpiled circuits as values.

    You are expected to use the same names of circuits generated by get_benchmark_dict.
    
    Args: 
        None
    Return:
        output_dict
    '''

    output_dict = {}
    ############################################################################
    # Student code begin
    ############################################################################
    q1b_basis_gates = ['cx','rx','ry','rz']
    for benchmark_circuit in workload_list.keys():
        circuit = workload_list[benchmark_circuit]
        transpiled = transpile(circuit, basis_gates=q1b_basis_gates)
        output_dict[benchmark_circuit] = transpiled
    ############################################################################
    # Student code end
    ############################################################################
    
    return output_dict