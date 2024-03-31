from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile, transpiler
from utils import get_benchmark_dict

workload_list = get_benchmark_dict("SWAP_Benchmarks")

def create_coupling_maps():
    """
    Generate each coupling map as shown above using transpiler.CouplingMap and store them in the dictionary provided using the given keys.

    Args: 
        None
    Return:
        output_dict: dict[str, qiskit.transpiler.CouplingMap]
    """

    coupling_maps = {}
    coupling_maps['GRID 5X5'] = None
    coupling_maps['GRID 5X4'] = None
    coupling_maps['GRID 7X3'] = None
    coupling_maps['RING 20'] = None
    ############################################################################
    # Student code begin
    ############################################################################
    
    raise NotImplementedError(
            "`create_coupling_maps` function in "
            + "`question2.py` needs to be implemented"
        )

    ############################################################################
    # Student code end
    ############################################################################

    return coupling_maps


def average_depth_change():
    """
    calculate the average change of circuit depth when transpiling the benchmark circuits for given coupling maps,
    using SABRE for routing and mapping. You need to return a dictionary with benchmark circuits' names as keys and
    change of circuit depth averaged over all coupling maps.
    
    You are expected to use the same names of circuits generated by `get_benchmark_dict`.
    
    Args: 
        None
    Return:
        output_dict: dict[str, float]
    """

    output_dict = {}
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`average_depth_change` function in "
            + "`question2.py` needs to be implemented"
        )
    
    ############################################################################
    # Student code end
    ############################################################################
    
    return output_dict


def average_nswap_change():
    """
    Calculate the average number of swaps inserted when transpiling the benchmark circuits for given coupling maps,
    using SABRE for routing and mapping. You need to return a dictionary with benchmark circuits' names as keys and
    number of swaps inserted averaged over all coupling maps.

    You are expected to use the same names of circuits generated by `get_benchmark_dict`.
    
    Args: 
        None
    Return:
        output_dict: dict[str, float]
    """

    output_dict = {}
    ############################################################################
    # Student code begin
    ############################################################################

    raise NotImplementedError(
            "`average_nswap_change` function in "
            + "`question2.py` needs to be implemented"
        )
    
    ############################################################################
    # Student code end
    ############################################################################

    return output_dict
